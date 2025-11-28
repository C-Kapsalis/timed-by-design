#!/usr/bin/env python3
"""
Generate ephemeris data tables from JPL Horizons API for embedding in Swift.
This fetches geocentric ecliptic longitudes for all planets at regular intervals.
Output is Swift code with embedded lookup tables.
"""

import requests
import json
import sys
from datetime import datetime, timedelta
import time

# JPL Horizons API endpoint
API_URL = "https://ssd.jpl.nasa.gov/api/horizons.api"

# Planet IDs in Horizons
PLANETS = {
    "Sun": "10",
    "Moon": "301", 
    "Mercury": "199",
    "Venus": "299",
    "Mars": "499",
    "Jupiter": "599",
    "Saturn": "699",
    "Uranus": "799",
    "Neptune": "899",
    "Pluto": "999"
}

# For Human Design we also need nodes
# True North Node is computed differently

def fetch_ephemeris(body_id, start_date, stop_date, step="1d"):
    """
    Fetch geocentric ecliptic longitude from JPL Horizons.
    Returns list of (julian_date, longitude) tuples.
    """
    # Request observer ephemeris with ecliptic longitude
    # QUANTITIES: 31 = Observer ecliptic longitude & latitude
    params = {
        "format": "text",
        "COMMAND": f"'{body_id}'",
        "OBJ_DATA": "NO",
        "MAKE_EPHEM": "YES",
        "EPHEM_TYPE": "OBSERVER",
        "CENTER": "500@399",  # Geocentric
        "START_TIME": f"'{start_date}'",
        "STOP_TIME": f"'{stop_date}'",
        "STEP_SIZE": f"'{step}'",
        "QUANTITIES": "'31'",  # Ecliptic longitude and latitude
        "CAL_FORMAT": "JD",
        "ANG_FORMAT": "DEG"
    }
    
    # Build URL
    url = API_URL + "?"
    url += "&".join([f"{k}={v}" for k, v in params.items()])
    
    print(f"Fetching {body_id}...", file=sys.stderr)
    
    response = requests.get(url, timeout=120)
    
    if response.status_code != 200:
        print(f"Error: {response.status_code}", file=sys.stderr)
        print(response.text, file=sys.stderr)
        return []
    
    # Parse the response
    text = response.text
    
    # Find data between $$SOE and $$EOE markers
    start_marker = "$$SOE"
    end_marker = "$$EOE"
    
    start_idx = text.find(start_marker)
    end_idx = text.find(end_marker)
    
    if start_idx == -1 or end_idx == -1:
        print(f"Could not find data markers in response", file=sys.stderr)
        print(text[:2000], file=sys.stderr)
        return []
    
    data_section = text[start_idx + len(start_marker):end_idx].strip()
    
    results = []
    for line in data_section.split('\n'):
        line = line.strip()
        if not line:
            continue
        
        # Parse the line - format depends on quantities requested
        # For quantity 31: JD, ObsEcLon, ObsEcLat
        parts = line.split()
        if len(parts) >= 2:
            try:
                jd = float(parts[0])
                ecl_lon = float(parts[1])
                results.append((jd, ecl_lon))
            except ValueError:
                continue
    
    return results


def generate_swift_table(planet_name, data):
    """Generate Swift code for a planet's ephemeris table."""
    
    if not data:
        return f"    // No data for {planet_name}\n"
    
    # Sample every N days for reasonable table size
    # For planets, every 5 days is sufficient (interpolation handles the rest)
    # For Moon, need every day due to fast motion
    
    sample_rate = 1 if planet_name == "Moon" else 5
    sampled_data = data[::sample_rate]
    
    lines = []
    lines.append(f"    // {planet_name}: {len(sampled_data)} data points, every {sample_rate} day(s)")
    lines.append(f"    static let {planet_name.lower()}Data: [(jd: Double, lon: Double)] = [")
    
    for i, (jd, lon) in enumerate(sampled_data):
        comma = "," if i < len(sampled_data) - 1 else ""
        lines.append(f"        ({jd}, {lon:.6f}){comma}")
    
    lines.append("    ]")
    lines.append("")
    
    return "\n".join(lines)


def main():
    # Date range: 1920 to 2060 (140 years)
    start_year = 1920
    end_year = 2060
    
    # Fetch data for each planet
    all_data = {}
    
    for planet_name, body_id in PLANETS.items():
        # Fetch in chunks to avoid timeout
        chunk_years = 20
        planet_data = []
        
        for year in range(start_year, end_year, chunk_years):
            chunk_end = min(year + chunk_years, end_year)
            start_date = f"{year}-01-01"
            stop_date = f"{chunk_end}-01-01"
            
            chunk_data = fetch_ephemeris(body_id, start_date, stop_date)
            planet_data.extend(chunk_data)
            
            # Rate limiting
            time.sleep(1)
        
        all_data[planet_name] = planet_data
        print(f"Got {len(planet_data)} points for {planet_name}", file=sys.stderr)
    
    # Generate Swift file
    print("// JPLEphemerisData.swift")
    print("// Auto-generated from JPL Horizons API")
    print("// Data range: 1920-2060")
    print("// DO NOT EDIT - regenerate using generate_ephemeris.py")
    print("")
    print("import Foundation")
    print("")
    print("/// Pre-computed ephemeris data from JPL Horizons")
    print("/// Provides geocentric ecliptic longitudes for all planets")
    print("struct JPLEphemerisData {")
    print("")
    
    for planet_name in PLANETS.keys():
        swift_code = generate_swift_table(planet_name, all_data.get(planet_name, []))
        print(swift_code)
    
    # Generate interpolation function
    print("""
    /// Interpolate longitude for a given Julian Date
    static func interpolate(data: [(jd: Double, lon: Double)], jd: Double) -> Double {
        guard !data.isEmpty else { return 0 }
        
        // Binary search for bracketing points
        var low = 0
        var high = data.count - 1
        
        // Handle edge cases
        if jd <= data[low].jd { return data[low].lon }
        if jd >= data[high].jd { return data[high].lon }
        
        while high - low > 1 {
            let mid = (low + high) / 2
            if data[mid].jd <= jd {
                low = mid
            } else {
                high = mid
            }
        }
        
        // Linear interpolation with angle wrap handling
        let jd1 = data[low].jd
        let jd2 = data[high].jd
        var lon1 = data[low].lon
        var lon2 = data[high].lon
        
        // Handle angle wrap-around (e.g., 359° to 1°)
        if lon2 - lon1 > 180 {
            lon1 += 360
        } else if lon1 - lon2 > 180 {
            lon2 += 360
        }
        
        let t = (jd - jd1) / (jd2 - jd1)
        var result = lon1 + t * (lon2 - lon1)
        
        // Normalize to 0-360
        while result < 0 { result += 360 }
        while result >= 360 { result -= 360 }
        
        return result
    }
    
    /// Get longitude for a planet at a given Julian Date
    static func longitude(planet: Planet, jd: Double) -> Double {
        switch planet {
        case .sun: return interpolate(data: sunData, jd: jd)
        case .moon: return interpolate(data: moonData, jd: jd)
        case .mercury: return interpolate(data: mercuryData, jd: jd)
        case .venus: return interpolate(data: venusData, jd: jd)
        case .mars: return interpolate(data: marsData, jd: jd)
        case .jupiter: return interpolate(data: jupiterData, jd: jd)
        case .saturn: return interpolate(data: saturnData, jd: jd)
        case .uranus: return interpolate(data: uranusData, jd: jd)
        case .neptune: return interpolate(data: neptuneData, jd: jd)
        case .pluto: return interpolate(data: plutoData, jd: jd)
        case .northNode: return calculateNorthNode(jd: jd)
        case .southNode: return calculateSouthNode(jd: jd)
        case .earth: return (longitude(planet: .sun, jd: jd) + 180).truncatingRemainder(dividingBy: 360)
        }
    }
    
    /// Calculate True North Node (Mean Node approximation)
    static func calculateNorthNode(jd: Double) -> Double {
        let T = (jd - 2451545.0) / 36525.0
        // Mean longitude of ascending node
        var omega = 125.04452 - 1934.136261 * T + 0.0020708 * T * T + T * T * T / 450000.0
        // Normalize to 0-360
        omega = omega.truncatingRemainder(dividingBy: 360)
        if omega < 0 { omega += 360 }
        return omega
    }
    
    /// Calculate South Node (opposite of North Node)
    static func calculateSouthNode(jd: Double) -> Double {
        return (calculateNorthNode(jd: jd) + 180).truncatingRemainder(dividingBy: 360)
    }
}
""")
    
    print("}")


if __name__ == "__main__":
    main()
