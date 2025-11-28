"""
Human Design Calculations using Flatlib (Pure Python Alternative)
Use this if pyswisseph won't compile on your system.

To use: rename this file to hd_calculations.py
"""

from datetime import datetime, timedelta
import pytz
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder

# Try to import flatlib, fall back to basic calculations if not available
try:
    from flatlib.datetime import Datetime
    from flatlib.geopos import GeoPos
    from flatlib.chart import Chart
    from flatlib import const
    FLATLIB_AVAILABLE = True
except ImportError:
    FLATLIB_AVAILABLE = False
    print("Warning: flatlib not installed. Using basic calculations.")

# Gate boundaries (same as before)
GATE_BOUNDARIES = [
    (0.0, 3.875, 25), (3.875, 9.5, 17), (9.5, 15.125, 21), (15.125, 20.75, 51),
    (20.75, 26.375, 42), (26.375, 32.0, 3), (32.0, 37.625, 27), (37.625, 43.25, 24),
    (43.25, 48.875, 2), (48.875, 54.5, 23), (54.5, 60.125, 8), (60.125, 65.75, 20),
    (65.75, 71.375, 16), (71.375, 77.0, 35), (77.0, 82.625, 45), (82.625, 88.25, 12),
    (88.25, 93.875, 15), (93.875, 99.5, 52), (99.5, 105.125, 39), (105.125, 110.75, 53),
    (110.75, 116.375, 62), (116.375, 122.0, 56), (122.0, 127.625, 31), (127.625, 133.25, 33),
    (133.25, 138.875, 7), (138.875, 144.5, 4), (144.5, 150.125, 29), (150.125, 155.75, 59),
    (155.75, 161.375, 40), (161.375, 167.0, 64), (167.0, 172.625, 47), (172.625, 178.25, 6),
    (178.25, 183.875, 46), (183.875, 189.5, 18), (189.5, 195.125, 48), (195.125, 200.75, 57),
    (200.75, 206.375, 32), (206.375, 212.0, 50), (212.0, 217.625, 28), (217.625, 223.25, 44),
    (223.25, 228.875, 1), (228.875, 234.5, 43), (234.5, 240.125, 14), (240.125, 245.75, 34),
    (245.75, 251.375, 9), (251.375, 257.0, 5), (257.0, 262.625, 26), (262.625, 268.25, 11),
    (268.25, 273.875, 10), (273.875, 279.5, 58), (279.5, 285.125, 38), (285.125, 290.75, 54),
    (290.75, 296.375, 61), (296.375, 302.0, 60), (302.0, 307.625, 41), (307.625, 313.25, 19),
    (313.25, 318.875, 13), (318.875, 324.5, 49), (324.5, 330.125, 30), (330.125, 335.75, 55),
    (335.75, 341.375, 37), (341.375, 347.0, 63), (347.0, 352.625, 22), (352.625, 358.25, 36),
    (358.25, 360.0, 25),
]

def get_gate_from_longitude(longitude):
    """Convert longitude to gate and line."""
    longitude = longitude % 360
    for start, end, gate in GATE_BOUNDARIES:
        if start <= longitude < end:
            gate_size = end - start
            position_in_gate = longitude - start
            line = int((position_in_gate / gate_size) * 6) + 1
            return gate, min(line, 6)
    if longitude >= 358.25:
        position_in_gate = longitude - 358.25
        gate_size = 360.0 - 358.25 + 3.875
        line = int((position_in_gate / gate_size) * 6) + 1
        return 25, min(line, 6)
    return 25, 1

def normalize_angle(angle):
    """Normalize angle to 0-360 range."""
    while angle < 0:
        angle += 360
    while angle >= 360:
        angle -= 360
    return angle


# ============ FLATLIB IMPLEMENTATION ============

def get_planetary_positions_flatlib(dt, timezone_str='UTC'):
    """Get planetary positions using flatlib."""
    if not FLATLIB_AVAILABLE:
        return get_planetary_positions_basic(dt, timezone_str)
    
    # Convert to UTC
    if dt.tzinfo is None:
        tz = pytz.timezone(timezone_str)
        dt = tz.localize(dt)
    utc_dt = dt.astimezone(pytz.UTC)
    
    # Create flatlib datetime
    date_str = utc_dt.strftime('%Y/%m/%d')
    time_str = utc_dt.strftime('%H:%M:%S')
    
    # Create chart (using generic location - longitude doesn't affect planetary positions much)
    fl_date = Datetime(date_str, time_str, '+00:00')
    pos = GeoPos('0n00', '0e00')  # Equator, prime meridian
    
    chart = Chart(fl_date, pos)
    
    positions = {}
    
    # Get positions for each planet
    planet_map = {
        'Sun': const.SUN,
        'Moon': const.MOON,
        'Mercury': const.MERCURY,
        'Venus': const.VENUS,
        'Mars': const.MARS,
        'Jupiter': const.JUPITER,
        'Saturn': const.SATURN,
        'Uranus': const.URANUS,
        'Neptune': const.NEPTUNE,
        'Pluto': const.PLUTO,
        'North Node': const.NORTH_NODE,
    }
    
    for name, planet_const in planet_map.items():
        obj = chart.get(planet_const)
        positions[name] = obj.lon
    
    # Calculate Earth (opposite of Sun)
    positions['Earth'] = normalize_angle(positions['Sun'] + 180)
    
    # Calculate South Node (opposite of North Node)
    positions['South Node'] = normalize_angle(positions['North Node'] + 180)
    
    return positions


# ============ BASIC CALCULATION FALLBACK ============

import math

def julian_day(year, month, day, hour=0):
    """Calculate Julian Day Number."""
    if month <= 2:
        year -= 1
        month += 12
    A = int(year / 100)
    B = 2 - A + int(A / 4)
    JD = int(365.25 * (year + 4716)) + int(30.6001 * (month + 1)) + day + hour/24 + B - 1524.5
    return JD

def sun_longitude_basic(jd):
    """Calculate Sun's ecliptic longitude (simplified)."""
    T = (jd - 2451545.0) / 36525.0
    
    # Mean longitude
    L0 = 280.46646 + 36000.76983 * T + 0.0003032 * T**2
    
    # Mean anomaly
    M = 357.52911 + 35999.05029 * T - 0.0001537 * T**2
    M_rad = math.radians(M)
    
    # Equation of center
    C = (1.914602 - 0.004817 * T - 0.000014 * T**2) * math.sin(M_rad)
    C += (0.019993 - 0.000101 * T) * math.sin(2 * M_rad)
    C += 0.000289 * math.sin(3 * M_rad)
    
    # True longitude
    longitude = L0 + C
    
    return normalize_angle(longitude)

def moon_longitude_basic(jd):
    """Calculate Moon's ecliptic longitude (simplified)."""
    T = (jd - 2451545.0) / 36525.0
    
    # Mean longitude
    L = 218.3164477 + 481267.88123421 * T
    
    # Mean anomaly of Moon
    M = 134.9633964 + 477198.8675055 * T
    
    # Mean anomaly of Sun
    Ms = 357.5291092 + 35999.0502909 * T
    
    # Mean elongation
    D = 297.8501921 + 445267.1114034 * T
    
    # Argument of latitude
    F = 93.2720950 + 483202.0175233 * T
    
    # Convert to radians
    M_rad = math.radians(M)
    Ms_rad = math.radians(Ms)
    D_rad = math.radians(D)
    F_rad = math.radians(F)
    
    # Main perturbations
    longitude = L
    longitude += 6.288774 * math.sin(M_rad)
    longitude += 1.274027 * math.sin(2*D_rad - M_rad)
    longitude += 0.658314 * math.sin(2*D_rad)
    longitude += 0.213618 * math.sin(2*M_rad)
    longitude -= 0.185116 * math.sin(Ms_rad)
    longitude -= 0.114332 * math.sin(2*F_rad)
    
    return normalize_angle(longitude)

def get_planetary_positions_basic(dt, timezone_str='UTC'):
    """Basic planetary position calculations (less accurate but no dependencies)."""
    # Convert to UTC
    if dt.tzinfo is None:
        tz = pytz.timezone(timezone_str)
        dt = tz.localize(dt)
    utc_dt = dt.astimezone(pytz.UTC)
    
    # Calculate Julian Day
    jd = julian_day(
        utc_dt.year, utc_dt.month, utc_dt.day,
        utc_dt.hour + utc_dt.minute/60 + utc_dt.second/3600
    )
    
    T = (jd - 2451545.0) / 36525.0
    
    positions = {}
    
    # Sun
    positions['Sun'] = sun_longitude_basic(jd)
    positions['Earth'] = normalize_angle(positions['Sun'] + 180)
    
    # Moon
    positions['Moon'] = moon_longitude_basic(jd)
    
    # Mercury (simplified)
    L = 252.2509 + 149472.6746 * T
    positions['Mercury'] = normalize_angle(L + 23.4 * math.sin(math.radians(L)))
    
    # Venus (simplified)
    L = 181.9798 + 58517.8157 * T
    positions['Venus'] = normalize_angle(L + 0.7758 * math.sin(math.radians(L)))
    
    # Mars (simplified)
    L = 355.4330 + 19140.2993 * T
    positions['Mars'] = normalize_angle(L + 10.691 * math.sin(math.radians(L)))
    
    # Jupiter (simplified)
    L = 34.3515 + 3034.9057 * T
    positions['Jupiter'] = normalize_angle(L + 5.555 * math.sin(math.radians(L)))
    
    # Saturn (simplified)
    L = 50.0774 + 1222.1138 * T
    positions['Saturn'] = normalize_angle(L + 6.39 * math.sin(math.radians(L)))
    
    # Uranus (simplified)
    L = 314.055 + 428.4669 * T
    positions['Uranus'] = normalize_angle(L + 5.52 * math.sin(math.radians(L)))
    
    # Neptune (simplified)
    L = 304.349 + 218.4862 * T
    positions['Neptune'] = normalize_angle(L + 0.8883 * math.sin(math.radians(L)))
    
    # Pluto (very simplified)
    L = 238.929 + 145.1781 * T
    positions['Pluto'] = normalize_angle(L + 14.882 * math.sin(math.radians(L)))
    
    # North Node (mean)
    omega = 125.0445 - 1934.1363 * T
    positions['North Node'] = normalize_angle(omega)
    positions['South Node'] = normalize_angle(omega + 180)
    
    return positions


# ============ MAIN FUNCTIONS ============

def calculate_design_date(birth_dt, timezone_str='UTC'):
    """Calculate the design date (88 solar degrees before birth)."""
    # Convert to UTC
    if birth_dt.tzinfo is None:
        tz = pytz.timezone(timezone_str)
        birth_dt = tz.localize(birth_dt)
    utc_birth = birth_dt.astimezone(pytz.UTC)
    
    # Get birth sun position
    if FLATLIB_AVAILABLE:
        birth_positions = get_planetary_positions_flatlib(utc_birth, 'UTC')
    else:
        birth_positions = get_planetary_positions_basic(utc_birth, 'UTC')
    
    birth_sun = birth_positions['Sun']
    target_sun = normalize_angle(birth_sun - 88)
    
    # Binary search for design date (approximately 88 days before)
    days_back = 88
    design_dt = utc_birth - timedelta(days=days_back)
    
    # Refine with binary search
    low_days = 70
    high_days = 100
    
    for _ in range(50):  # 50 iterations for precision
        mid_days = (low_days + high_days) / 2
        test_dt = utc_birth - timedelta(days=mid_days)
        
        if FLATLIB_AVAILABLE:
            test_positions = get_planetary_positions_flatlib(test_dt, 'UTC')
        else:
            test_positions = get_planetary_positions_basic(test_dt, 'UTC')
        
        test_sun = test_positions['Sun']
        
        # Calculate angular difference
        diff = target_sun - test_sun
        if diff > 180:
            diff -= 360
        elif diff < -180:
            diff += 360
        
        if abs(diff) < 0.001:  # Close enough
            design_dt = test_dt
            break
        
        if diff > 0:
            high_days = mid_days
        else:
            low_days = mid_days
        
        design_dt = test_dt
    
    return design_dt

def calculate_gates(positions):
    """Convert planetary positions to gates."""
    gates = {}
    for planet, longitude in positions.items():
        gate, line = get_gate_from_longitude(longitude)
        gates[planet] = {
            'gate': gate,
            'line': line,
            'longitude': longitude
        }
    return gates

def calculate_natal_chart(birth_datetime, timezone_str='UTC'):
    """Calculate complete natal chart."""
    # Get personality positions (at birth)
    if FLATLIB_AVAILABLE:
        personality_positions = get_planetary_positions_flatlib(birth_datetime, timezone_str)
    else:
        personality_positions = get_planetary_positions_basic(birth_datetime, timezone_str)
    
    # Get design date
    design_dt = calculate_design_date(birth_datetime, timezone_str)
    
    # Get design positions
    if FLATLIB_AVAILABLE:
        design_positions = get_planetary_positions_flatlib(design_dt, 'UTC')
    else:
        design_positions = get_planetary_positions_basic(design_dt, 'UTC')
    
    # Convert to gates
    personality_gates = calculate_gates(personality_positions)
    design_gates = calculate_gates(design_positions)
    
    return {
        'birth_datetime': birth_datetime,
        'design_datetime': design_dt,
        'personality': {
            'positions': personality_positions,
            'gates': personality_gates
        },
        'design': {
            'positions': design_positions,
            'gates': design_gates
        }
    }

def calculate_transit_chart(transit_datetime=None, timezone_str='UTC'):
    """Calculate transit chart."""
    if transit_datetime is None:
        tz = pytz.timezone(timezone_str)
        transit_datetime = datetime.now(tz)
    elif transit_datetime.tzinfo is None:
        tz = pytz.timezone(timezone_str)
        transit_datetime = tz.localize(transit_datetime)
    
    if FLATLIB_AVAILABLE:
        positions = get_planetary_positions_flatlib(transit_datetime, timezone_str)
    else:
        positions = get_planetary_positions_basic(transit_datetime, timezone_str)
    
    gates = calculate_gates(positions)
    
    return {
        'datetime': transit_datetime,
        'positions': positions,
        'gates': gates
    }


# ============ GEOCODING ============

COMMON_LOCATIONS = {
    "agrinio": {"lat": 38.6216, "lon": 21.4083, "tz": "Europe/Athens", "address": "Agrinio, Greece"},
    "agrinio, greece": {"lat": 38.6216, "lon": 21.4083, "tz": "Europe/Athens", "address": "Agrinio, Greece"},
    "athens": {"lat": 37.9838, "lon": 23.7275, "tz": "Europe/Athens", "address": "Athens, Greece"},
    "athens, greece": {"lat": 37.9838, "lon": 23.7275, "tz": "Europe/Athens", "address": "Athens, Greece"},
    "new york": {"lat": 40.7128, "lon": -74.0060, "tz": "America/New_York", "address": "New York, USA"},
    "new york, usa": {"lat": 40.7128, "lon": -74.0060, "tz": "America/New_York", "address": "New York, USA"},
    "london": {"lat": 51.5074, "lon": -0.1278, "tz": "Europe/London", "address": "London, UK"},
    "london, uk": {"lat": 51.5074, "lon": -0.1278, "tz": "Europe/London", "address": "London, UK"},
    "los angeles": {"lat": 34.0522, "lon": -118.2437, "tz": "America/Los_Angeles", "address": "Los Angeles, USA"},
    "paris": {"lat": 48.8566, "lon": 2.3522, "tz": "Europe/Paris", "address": "Paris, France"},
    "berlin": {"lat": 52.5200, "lon": 13.4050, "tz": "Europe/Berlin", "address": "Berlin, Germany"},
    "tokyo": {"lat": 35.6762, "lon": 139.6503, "tz": "Asia/Tokyo", "address": "Tokyo, Japan"},
    "sydney": {"lat": -33.8688, "lon": 151.2093, "tz": "Australia/Sydney", "address": "Sydney, Australia"},
}

def geocode_location(location_str):
    """Geocode a location string."""
    import time
    try:
        geolocator = Nominatim(
            user_agent="HumanDesignCalculator/1.0",
            timeout=10
        )
        time.sleep(1)
        location = geolocator.geocode(location_str, language='en')
        if location:
            tf = TimezoneFinder()
            timezone_str = tf.timezone_at(lat=location.latitude, lng=location.longitude)
            return {
                'latitude': location.latitude,
                'longitude': location.longitude,
                'address': location.address,
                'timezone': timezone_str or 'UTC'
            }
    except Exception as e:
        print(f"Geocoding error: {e}")
    return None

def geocode_location_with_fallback(location_str):
    """Try common locations first, then API."""
    location_lower = location_str.lower().strip()
    if location_lower in COMMON_LOCATIONS:
        loc = COMMON_LOCATIONS[location_lower]
        return {
            'latitude': loc['lat'],
            'longitude': loc['lon'],
            'address': loc['address'],
            'timezone': loc['tz']
        }
    return geocode_location(location_str)


# ============ PROFILE NAMES ============

PROFILE_NAMES = {
    "1/3": "Investigator/Martyr",
    "1/4": "Investigator/Opportunist",
    "2/4": "Hermit/Opportunist",
    "2/5": "Hermit/Heretic",
    "3/5": "Martyr/Heretic",
    "3/6": "Martyr/Role Model",
    "4/6": "Opportunist/Role Model",
    "4/1": "Opportunist/Investigator",
    "5/1": "Heretic/Investigator",
    "5/2": "Heretic/Hermit",
    "6/2": "Role Model/Hermit",
    "6/3": "Role Model/Martyr"
}

def get_profile_name(profile):
    return PROFILE_NAMES.get(profile, "Unknown Profile")


# Test if run directly
if __name__ == "__main__":
    print(f"Flatlib available: {FLATLIB_AVAILABLE}")
    
    # Test with April 18, 2001, 12:30 PM, Agrinio
    test_dt = datetime(2001, 4, 18, 12, 30)
    chart = calculate_natal_chart(test_dt, 'Europe/Athens')
    
    print("\nPersonality Gates:")
    for planet, data in chart['personality']['gates'].items():
        print(f"  {planet}: Gate {data['gate']}.{data['line']} ({data['longitude']:.2f}°)")
    
    print("\nDesign Gates:")
    for planet, data in chart['design']['gates'].items():
        print(f"  {planet}: Gate {data['gate']}.{data['line']} ({data['longitude']:.2f}°)")
