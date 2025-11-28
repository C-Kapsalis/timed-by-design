CENTERS = {
    'Head': {
        'gates': [64, 61, 63],
        'position': (250, 50),
        'color': '#f0e68c',
        'type': 'pressure'
    },
    'Ajna': {
        'gates': [47, 24, 4, 17, 43, 11],
        'position': (250, 130),
        'color': '#98fb98',
        'type': 'awareness'
    },
    'Throat': {
        'gates': [62, 23, 56, 35, 12, 45, 33, 8, 31, 20, 16],
        'position': (250, 220),
        'color': '#dda0dd',
        'type': 'manifestation'
    },
    'G': {
        'gates': [7, 1, 13, 25, 46, 2, 15, 10],
        'position': (250, 320),
        'color': '#ffff00',
        'type': 'identity'
    },
    'Heart': {
        'gates': [21, 40, 26, 51],
        'position': (170, 340),
        'color': '#ff6347',
        'type': 'motor'
    },
    'Sacral': {
        'gates': [5, 14, 29, 59, 9, 3, 42, 27, 34],
        'position': (250, 430),
        'color': '#ff4500',
        'type': 'motor'
    },
    'Spleen': {
        'gates': [48, 57, 44, 50, 32, 28, 18],
        'position': (140, 430),
        'color': '#8b4513',
        'type': 'awareness'
    },
    'Solar Plexus': {
        'gates': [6, 37, 22, 36, 30, 55, 49],
        'position': (360, 430),
        'color': '#8b4513',
        'type': 'motor/awareness'
    },
    'Root': {
        'gates': [58, 38, 54, 53, 60, 52, 19, 39, 41],
        'position': (250, 540),
        'color': '#8b4513',
        'type': 'pressure/motor'
    }
}

CHANNELS = {
    '1-8': {'gates': [1, 8], 'centers': ['G', 'Throat'], 'name': 'Inspiration'},
    '2-14': {'gates': [2, 14], 'centers': ['G', 'Sacral'], 'name': 'The Beat'},
    '3-60': {'gates': [3, 60], 'centers': ['Sacral', 'Root'], 'name': 'Mutation'},
    '4-63': {'gates': [4, 63], 'centers': ['Ajna', 'Head'], 'name': 'Logic'},
    '5-15': {'gates': [5, 15], 'centers': ['Sacral', 'G'], 'name': 'Rhythm'},
    '6-59': {'gates': [6, 59], 'centers': ['Solar Plexus', 'Sacral'], 'name': 'Intimacy'},
    '7-31': {'gates': [7, 31], 'centers': ['G', 'Throat'], 'name': 'Alpha'},
    '9-52': {'gates': [9, 52], 'centers': ['Sacral', 'Root'], 'name': 'Concentration'},
    '10-20': {'gates': [10, 20], 'centers': ['G', 'Throat'], 'name': 'Awakening'},
    '10-34': {'gates': [10, 34], 'centers': ['G', 'Sacral'], 'name': 'Exploration'},
    '10-57': {'gates': [10, 57], 'centers': ['G', 'Spleen'], 'name': 'Perfected Form'},
    '11-56': {'gates': [11, 56], 'centers': ['Ajna', 'Throat'], 'name': 'Curiosity'},
    '12-22': {'gates': [12, 22], 'centers': ['Throat', 'Solar Plexus'], 'name': 'Openness'},
    '13-33': {'gates': [13, 33], 'centers': ['G', 'Throat'], 'name': 'Prodigal'},
    '16-48': {'gates': [16, 48], 'centers': ['Throat', 'Spleen'], 'name': 'Wavelength'},
    '17-62': {'gates': [17, 62], 'centers': ['Ajna', 'Throat'], 'name': 'Acceptance'},
    '18-58': {'gates': [18, 58], 'centers': ['Spleen', 'Root'], 'name': 'Judgment'},
    '19-49': {'gates': [19, 49], 'centers': ['Root', 'Solar Plexus'], 'name': 'Synthesis'},
    '20-34': {'gates': [20, 34], 'centers': ['Throat', 'Sacral'], 'name': 'Charisma'},
    '20-57': {'gates': [20, 57], 'centers': ['Throat', 'Spleen'], 'name': 'Brain Wave'},
    '21-45': {'gates': [21, 45], 'centers': ['Heart', 'Throat'], 'name': 'Money'},
    '23-43': {'gates': [23, 43], 'centers': ['Throat', 'Ajna'], 'name': 'Structuring'},
    '24-61': {'gates': [24, 61], 'centers': ['Ajna', 'Head'], 'name': 'Awareness'},
    '25-51': {'gates': [25, 51], 'centers': ['G', 'Heart'], 'name': 'Initiation'},
    '26-44': {'gates': [26, 44], 'centers': ['Heart', 'Spleen'], 'name': 'Surrender'},
    '27-50': {'gates': [27, 50], 'centers': ['Sacral', 'Spleen'], 'name': 'Preservation'},
    '28-38': {'gates': [28, 38], 'centers': ['Spleen', 'Root'], 'name': 'Struggle'},
    '29-46': {'gates': [29, 46], 'centers': ['Sacral', 'G'], 'name': 'Discovery'},
    '30-41': {'gates': [30, 41], 'centers': ['Solar Plexus', 'Root'], 'name': 'Recognition'},
    '32-54': {'gates': [32, 54], 'centers': ['Spleen', 'Root'], 'name': 'Transformation'},
    '34-57': {'gates': [34, 57], 'centers': ['Sacral', 'Spleen'], 'name': 'Power'},
    '35-36': {'gates': [35, 36], 'centers': ['Throat', 'Solar Plexus'], 'name': 'Transitoriness'},
    '37-40': {'gates': [37, 40], 'centers': ['Solar Plexus', 'Heart'], 'name': 'Community'},
    '39-55': {'gates': [39, 55], 'centers': ['Root', 'Solar Plexus'], 'name': 'Emoting'},
    '42-53': {'gates': [42, 53], 'centers': ['Sacral', 'Root'], 'name': 'Maturation'},
    '47-64': {'gates': [47, 64], 'centers': ['Ajna', 'Head'], 'name': 'Abstraction'},
}

GATE_TO_CENTER = {}
for center_name, center_data in CENTERS.items():
    for gate in center_data['gates']:
        GATE_TO_CENTER[gate] = center_name

def find_channel_for_gates(gate1, gate2):
    key1 = f"{min(gate1, gate2)}-{max(gate1, gate2)}"
    if key1 in CHANNELS:
        return key1
    return None

def get_defined_channels(active_gates):
    defined_channels = []
    gate_numbers = set(active_gates)
    
    for channel_key, channel_data in CHANNELS.items():
        gate1, gate2 = channel_data['gates']
        if gate1 in gate_numbers and gate2 in gate_numbers:
            defined_channels.append(channel_key)
    
    return defined_channels

def get_defined_centers(defined_channels):
    defined_centers = set()
    for channel_key in defined_channels:
        if channel_key in CHANNELS:
            for center in CHANNELS[channel_key]['centers']:
                defined_centers.add(center)
    return defined_centers

def calculate_type(defined_centers, defined_channels):
    has_sacral = 'Sacral' in defined_centers
    has_throat = 'Throat' in defined_centers
    
    motor_centers = {'Sacral', 'Heart', 'Solar Plexus', 'Root'}
    has_motor = bool(defined_centers & motor_centers)
    
    throat_connected_to_motor = False
    if has_throat:
        for channel_key in defined_channels:
            channel = CHANNELS[channel_key]
            if 'Throat' in channel['centers']:
                other_center = [c for c in channel['centers'] if c != 'Throat'][0]
                if other_center in motor_centers:
                    throat_connected_to_motor = True
                    break
                for sub_channel_key in defined_channels:
                    sub_channel = CHANNELS[sub_channel_key]
                    if other_center in sub_channel['centers']:
                        sub_other = [c for c in sub_channel['centers'] if c != other_center][0]
                        if sub_other in motor_centers:
                            throat_connected_to_motor = True
                            break
    
    if has_sacral:
        if throat_connected_to_motor:
            return "Manifesting Generator"
        return "Generator"
    elif throat_connected_to_motor:
        return "Manifestor"
    elif len(defined_centers) > 0:
        return "Projector"
    else:
        return "Reflector"

def calculate_authority(hd_type, defined_centers):
    if hd_type == "Reflector":
        return "Lunar"
    
    if 'Solar Plexus' in defined_centers:
        return "Emotional"
    if 'Sacral' in defined_centers:
        return "Sacral"
    if 'Spleen' in defined_centers:
        return "Splenic"
    if 'Heart' in defined_centers:
        return "Ego"
    if 'G' in defined_centers:
        return "Self-Projected"
    if 'Ajna' in defined_centers or 'Head' in defined_centers:
        return "Mental (Outer Authority)"
    
    return "None (Outer Authority)"

def calculate_definition(defined_centers, defined_channels):
    if len(defined_centers) == 0:
        return "No Definition"
    
    if len(defined_centers) == 1:
        return "Single Definition"
    
    groups = []
    remaining_centers = set(defined_centers)
    
    while remaining_centers:
        current_center = remaining_centers.pop()
        current_group = {current_center}
        
        changed = True
        while changed:
            changed = False
            for channel_key in defined_channels:
                channel = CHANNELS[channel_key]
                centers_in_channel = set(channel['centers'])
                if centers_in_channel & current_group:
                    new_centers = centers_in_channel - current_group
                    if new_centers & remaining_centers:
                        current_group.update(new_centers)
                        remaining_centers -= new_centers
                        changed = True
        
        groups.append(current_group)
    
    if len(groups) == 1:
        return "Single Definition"
    elif len(groups) == 2:
        return "Split Definition"
    elif len(groups) == 3:
        return "Triple Split"
    else:
        return "Quadruple Split"

def calculate_incarnation_cross(personality_gates, design_gates):
    p_sun = personality_gates.get('Sun', {}).get('gate', 0)
    p_earth = personality_gates.get('Earth', {}).get('gate', 0)
    d_sun = design_gates.get('Sun', {}).get('gate', 0)
    d_earth = design_gates.get('Earth', {}).get('gate', 0)
    
    return {
        'personality_sun': p_sun,
        'personality_earth': p_earth,
        'design_sun': d_sun,
        'design_earth': d_earth,
        'cross': f"{p_sun}/{p_earth} | {d_sun}/{d_earth}"
    }

def analyze_chart(natal_chart):
    personality_gates = natal_chart['personality']['gates']
    design_gates = natal_chart['design']['gates']
    
    all_gates = set()
    for planet_data in personality_gates.values():
        all_gates.add(planet_data['gate'])
    for planet_data in design_gates.values():
        all_gates.add(planet_data['gate'])
    
    defined_channels = get_defined_channels(all_gates)
    defined_centers = get_defined_centers(defined_channels)
    
    hd_type = calculate_type(defined_centers, defined_channels)
    authority = calculate_authority(hd_type, defined_centers)
    definition = calculate_definition(defined_centers, defined_channels)
    
    p_sun_line = personality_gates.get('Sun', {}).get('line', 1)
    d_sun_line = design_gates.get('Sun', {}).get('line', 1)
    profile = f"{p_sun_line}/{d_sun_line}"
    
    cross = calculate_incarnation_cross(personality_gates, design_gates)
    
    return {
        'type': hd_type,
        'authority': authority,
        'definition': definition,
        'profile': profile,
        'incarnation_cross': cross,
        'defined_channels': defined_channels,
        'defined_centers': list(defined_centers),
        'all_gates': list(all_gates),
        'personality_gates': personality_gates,
        'design_gates': design_gates
    }

STRATEGY = {
    "Generator": "Wait to Respond",
    "Manifesting Generator": "Wait to Respond, then Inform",
    "Manifestor": "Inform before Acting",
    "Projector": "Wait for the Invitation",
    "Reflector": "Wait a Lunar Cycle"
}

NOT_SELF_THEME = {
    "Generator": "Frustration",
    "Manifesting Generator": "Frustration and Anger",
    "Manifestor": "Anger",
    "Projector": "Bitterness",
    "Reflector": "Disappointment"
}

SIGNATURE = {
    "Generator": "Satisfaction",
    "Manifesting Generator": "Satisfaction",
    "Manifestor": "Peace",
    "Projector": "Success",
    "Reflector": "Surprise"
}
