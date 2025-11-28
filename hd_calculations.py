import swisseph as swe
from datetime import datetime, timedelta
import pytz
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder

swe.set_ephe_path(None)

PLANETS = {
    'Sun': swe.SUN,
    'Moon': swe.MOON,
    'North Node': swe.TRUE_NODE,
    'Mercury': swe.MERCURY,
    'Venus': swe.VENUS,
    'Mars': swe.MARS,
    'Jupiter': swe.JUPITER,
    'Saturn': swe.SATURN,
    'Uranus': swe.URANUS,
    'Neptune': swe.NEPTUNE,
    'Pluto': swe.PLUTO
}

GATE_BOUNDARIES = [
    (0.0, 3.875, 25),
    (3.875, 9.5, 17),
    (9.5, 15.125, 21),
    (15.125, 20.75, 51),
    (20.75, 26.375, 42),
    (26.375, 32.0, 3),
    (32.0, 37.625, 27),
    (37.625, 43.25, 24),
    (43.25, 48.875, 2),
    (48.875, 54.5, 23),
    (54.5, 60.125, 8),
    (60.125, 65.75, 20),
    (65.75, 71.375, 16),
    (71.375, 77.0, 35),
    (77.0, 82.625, 45),
    (82.625, 88.25, 12),
    (88.25, 93.875, 15),
    (93.875, 99.5, 52),
    (99.5, 105.125, 39),
    (105.125, 110.75, 53),
    (110.75, 116.375, 62),
    (116.375, 122.0, 56),
    (122.0, 127.625, 31),
    (127.625, 133.25, 33),
    (133.25, 138.875, 7),
    (138.875, 144.5, 4),
    (144.5, 150.125, 29),
    (150.125, 155.75, 59),
    (155.75, 161.375, 40),
    (161.375, 167.0, 64),
    (167.0, 172.625, 47),
    (172.625, 178.25, 6),
    (178.25, 183.875, 46),
    (183.875, 189.5, 18),
    (189.5, 195.125, 48),
    (195.125, 200.75, 57),
    (200.75, 206.375, 32),
    (206.375, 212.0, 50),
    (212.0, 217.625, 28),
    (217.625, 223.25, 44),
    (223.25, 228.875, 1),
    (228.875, 234.5, 43),
    (234.5, 240.125, 14),
    (240.125, 245.75, 34),
    (245.75, 251.375, 9),
    (251.375, 257.0, 5),
    (257.0, 262.625, 26),
    (262.625, 268.25, 11),
    (268.25, 273.875, 10),
    (273.875, 279.5, 58),
    (279.5, 285.125, 38),
    (285.125, 290.75, 54),
    (290.75, 296.375, 61),
    (296.375, 302.0, 60),
    (302.0, 307.625, 41),
    (307.625, 313.25, 19),
    (313.25, 318.875, 13),
    (318.875, 324.5, 49),
    (324.5, 330.125, 30),
    (330.125, 335.75, 55),
    (335.75, 341.375, 37),
    (341.375, 347.0, 63),
    (347.0, 352.625, 22),
    (352.625, 358.25, 36),
    (358.25, 360.0, 25),
]

def get_gate_from_longitude(longitude):
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

def datetime_to_julian(dt, timezone_str='UTC'):
    if dt.tzinfo is None:
        tz = pytz.timezone(timezone_str)
        dt = tz.localize(dt)
    utc_dt = dt.astimezone(pytz.UTC)
    hour_decimal = utc_dt.hour + utc_dt.minute / 60.0 + utc_dt.second / 3600.0
    jd = swe.julday(utc_dt.year, utc_dt.month, utc_dt.day, hour_decimal)
    return jd

def get_planet_position(jd, planet_id):
    result, flag = swe.calc_ut(jd, planet_id)
    return result[0]

def normalize_angle(angle):
    while angle < 0:
        angle += 360
    while angle >= 360:
        angle -= 360
    return angle

def angle_difference(target, current):
    diff = target - current
    while diff > 180:
        diff -= 360
    while diff < -180:
        diff += 360
    return diff

def calculate_design_date(birth_jd):
    birth_sun_pos = get_planet_position(birth_jd, swe.SUN)
    target_pos = normalize_angle(birth_sun_pos - 88)
    
    jd_low = birth_jd - 100
    jd_high = birth_jd - 70
    
    low_sun = get_planet_position(jd_low, swe.SUN)
    high_sun = get_planet_position(jd_high, swe.SUN)
    
    low_diff = angle_difference(target_pos, low_sun)
    high_diff = angle_difference(target_pos, high_sun)
    
    if low_diff * high_diff > 0:
        jd_low = birth_jd - 120
        jd_high = birth_jd - 60
    
    for _ in range(100):
        jd_mid = (jd_low + jd_high) / 2
        mid_sun = get_planet_position(jd_mid, swe.SUN)
        mid_diff = angle_difference(target_pos, mid_sun)
        
        if abs(mid_diff) < 0.0001:
            return jd_mid
        
        low_diff = angle_difference(target_pos, get_planet_position(jd_low, swe.SUN))
        
        if low_diff * mid_diff < 0:
            jd_high = jd_mid
        else:
            jd_low = jd_mid
    
    return jd_mid

def calculate_planetary_positions(jd):
    positions = {}
    
    for planet_name, planet_id in PLANETS.items():
        positions[planet_name] = get_planet_position(jd, planet_id)
    
    sun_pos = positions['Sun']
    positions['Earth'] = normalize_angle(sun_pos + 180)
    
    north_node_pos = positions['North Node']
    positions['South Node'] = normalize_angle(north_node_pos + 180)
    
    return positions

def calculate_gates(positions):
    gates = {}
    for planet, longitude in positions.items():
        gate, line = get_gate_from_longitude(longitude)
        gates[planet] = {
            'gate': gate,
            'line': line,
            'longitude': longitude
        }
    return gates

def geocode_location(location_str):
    """
    Geocode a location string to get coordinates and timezone.
    Uses Nominatim with proper headers and retry logic.
    """
    import time
    
    try:
        # Use a more specific user agent to avoid blocks
        geolocator = Nominatim(
            user_agent="HumanDesignCalculator/1.0 (Educational Project)",
            timeout=10
        )
        
        # Add a small delay to respect rate limits
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
        else:
            # Try with just the city name if full string fails
            if ',' in location_str:
                city = location_str.split(',')[0].strip()
                time.sleep(1)
                location = geolocator.geocode(city, language='en')
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


# Common locations lookup table for faster results
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
    "toronto": {"lat": 43.6532, "lon": -79.3832, "tz": "America/Toronto", "address": "Toronto, Canada"},
    "chicago": {"lat": 41.8781, "lon": -87.6298, "tz": "America/Chicago", "address": "Chicago, USA"},
    "miami": {"lat": 25.7617, "lon": -80.1918, "tz": "America/New_York", "address": "Miami, USA"},
    "san francisco": {"lat": 37.7749, "lon": -122.4194, "tz": "America/Los_Angeles", "address": "San Francisco, USA"},
    "seattle": {"lat": 47.6062, "lon": -122.3321, "tz": "America/Los_Angeles", "address": "Seattle, USA"},
    "boston": {"lat": 42.3601, "lon": -71.0589, "tz": "America/New_York", "address": "Boston, USA"},
    "denver": {"lat": 39.7392, "lon": -104.9903, "tz": "America/Denver", "address": "Denver, USA"},
    "phoenix": {"lat": 33.4484, "lon": -112.0740, "tz": "America/Phoenix", "address": "Phoenix, USA"},
    "amsterdam": {"lat": 52.3676, "lon": 4.9041, "tz": "Europe/Amsterdam", "address": "Amsterdam, Netherlands"},
    "rome": {"lat": 41.9028, "lon": 12.4964, "tz": "Europe/Rome", "address": "Rome, Italy"},
    "madrid": {"lat": 40.4168, "lon": -3.7038, "tz": "Europe/Madrid", "address": "Madrid, Spain"},
    "barcelona": {"lat": 41.3851, "lon": 2.1734, "tz": "Europe/Madrid", "address": "Barcelona, Spain"},
    "munich": {"lat": 48.1351, "lon": 11.5820, "tz": "Europe/Berlin", "address": "Munich, Germany"},
    "vienna": {"lat": 48.2082, "lon": 16.3738, "tz": "Europe/Vienna", "address": "Vienna, Austria"},
    "zurich": {"lat": 47.3769, "lon": 8.5417, "tz": "Europe/Zurich", "address": "Zurich, Switzerland"},
    "moscow": {"lat": 55.7558, "lon": 37.6173, "tz": "Europe/Moscow", "address": "Moscow, Russia"},
    "dubai": {"lat": 25.2048, "lon": 55.2708, "tz": "Asia/Dubai", "address": "Dubai, UAE"},
    "singapore": {"lat": 1.3521, "lon": 103.8198, "tz": "Asia/Singapore", "address": "Singapore"},
    "hong kong": {"lat": 22.3193, "lon": 114.1694, "tz": "Asia/Hong_Kong", "address": "Hong Kong"},
    "seoul": {"lat": 37.5665, "lon": 126.9780, "tz": "Asia/Seoul", "address": "Seoul, South Korea"},
    "mumbai": {"lat": 19.0760, "lon": 72.8777, "tz": "Asia/Kolkata", "address": "Mumbai, India"},
    "delhi": {"lat": 28.7041, "lon": 77.1025, "tz": "Asia/Kolkata", "address": "Delhi, India"},
    "melbourne": {"lat": -37.8136, "lon": 144.9631, "tz": "Australia/Melbourne", "address": "Melbourne, Australia"},
    "auckland": {"lat": -36.8509, "lon": 174.7645, "tz": "Pacific/Auckland", "address": "Auckland, New Zealand"},
    "cape town": {"lat": -33.9249, "lon": 18.4241, "tz": "Africa/Johannesburg", "address": "Cape Town, South Africa"},
    "cairo": {"lat": 30.0444, "lon": 31.2357, "tz": "Africa/Cairo", "address": "Cairo, Egypt"},
    "mexico city": {"lat": 19.4326, "lon": -99.1332, "tz": "America/Mexico_City", "address": "Mexico City, Mexico"},
    "sao paulo": {"lat": -23.5505, "lon": -46.6333, "tz": "America/Sao_Paulo", "address": "São Paulo, Brazil"},
    "buenos aires": {"lat": -34.6037, "lon": -58.3816, "tz": "America/Argentina/Buenos_Aires", "address": "Buenos Aires, Argentina"},
}


def geocode_location_with_fallback(location_str):
    """
    Try common locations first, then fall back to geocoding API.
    """
    # Check common locations first (instant, no API call)
    location_lower = location_str.lower().strip()
    if location_lower in COMMON_LOCATIONS:
        loc = COMMON_LOCATIONS[location_lower]
        return {
            'latitude': loc['lat'],
            'longitude': loc['lon'],
            'address': loc['address'],
            'timezone': loc['tz']
        }
    
    # Try geocoding API
    return geocode_location(location_str)

def calculate_natal_chart(birth_datetime, timezone_str='UTC'):
    jd_birth = datetime_to_julian(birth_datetime, timezone_str)
    jd_design = calculate_design_date(jd_birth)
    
    personality_positions = calculate_planetary_positions(jd_birth)
    design_positions = calculate_planetary_positions(jd_design)
    
    personality_gates = calculate_gates(personality_positions)
    design_gates = calculate_gates(design_positions)
    
    return {
        'birth_jd': jd_birth,
        'design_jd': jd_design,
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
    if transit_datetime is None:
        tz = pytz.timezone(timezone_str)
        transit_datetime = datetime.now(tz)
    elif transit_datetime.tzinfo is None:
        tz = pytz.timezone(timezone_str)
        transit_datetime = tz.localize(transit_datetime)
    
    jd_transit = datetime_to_julian(transit_datetime, timezone_str)
    transit_positions = calculate_planetary_positions(jd_transit)
    transit_gates = calculate_gates(transit_positions)
    
    return {
        'transit_jd': jd_transit,
        'datetime': transit_datetime,
        'positions': transit_positions,
        'gates': transit_gates
    }

def get_profile(personality_sun_line, design_sun_line):
    return f"{personality_sun_line}/{design_sun_line}"

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