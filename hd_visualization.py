import plotly.graph_objects as go
from hd_bodygraph import CENTERS, CHANNELS, GATE_TO_CENTER

CENTER_POSITIONS = {
    'Head': (250, 60),
    'Ajna': (250, 140),
    'Throat': (250, 230),
    'G': (250, 340),
    'Heart': (160, 320),
    'Sacral': (250, 450),
    'Spleen': (130, 400),
    'Solar Plexus': (370, 400),
    'Root': (250, 550)
}

CENTER_SHAPES = {
    'Head': 'triangle',
    'Ajna': 'triangle',
    'Throat': 'square',
    'G': 'diamond',
    'Heart': 'triangle',
    'Sacral': 'square',
    'Spleen': 'triangle',
    'Solar Plexus': 'triangle',
    'Root': 'square'
}

CHANNEL_PATHS = {
    '1-8': [('G', 'Throat')],
    '2-14': [('G', 'Sacral')],
    '3-60': [('Sacral', 'Root')],
    '4-63': [('Ajna', 'Head')],
    '5-15': [('Sacral', 'G')],
    '6-59': [('Solar Plexus', 'Sacral')],
    '7-31': [('G', 'Throat')],
    '9-52': [('Sacral', 'Root')],
    '10-20': [('G', 'Throat')],
    '10-34': [('G', 'Sacral')],
    '10-57': [('G', 'Spleen')],
    '11-56': [('Ajna', 'Throat')],
    '12-22': [('Throat', 'Solar Plexus')],
    '13-33': [('G', 'Throat')],
    '16-48': [('Throat', 'Spleen')],
    '17-62': [('Ajna', 'Throat')],
    '18-58': [('Spleen', 'Root')],
    '19-49': [('Root', 'Solar Plexus')],
    '20-34': [('Throat', 'Sacral')],
    '20-57': [('Throat', 'Spleen')],
    '21-45': [('Heart', 'Throat')],
    '23-43': [('Throat', 'Ajna')],
    '24-61': [('Ajna', 'Head')],
    '25-51': [('G', 'Heart')],
    '26-44': [('Heart', 'Spleen')],
    '27-50': [('Sacral', 'Spleen')],
    '28-38': [('Spleen', 'Root')],
    '29-46': [('Sacral', 'G')],
    '30-41': [('Solar Plexus', 'Root')],
    '32-54': [('Spleen', 'Root')],
    '34-57': [('Sacral', 'Spleen')],
    '35-36': [('Throat', 'Solar Plexus')],
    '37-40': [('Solar Plexus', 'Heart')],
    '39-55': [('Root', 'Solar Plexus')],
    '42-53': [('Sacral', 'Root')],
    '47-64': [('Ajna', 'Head')],
}

def create_bodygraph(analysis, show_transit=False, transit_gates=None):
    fig = go.Figure()
    
    fig.update_layout(
        showlegend=False,
        xaxis=dict(
            showgrid=False,
            zeroline=False,
            showticklabels=False,
            range=[0, 500],
            fixedrange=True
        ),
        yaxis=dict(
            showgrid=False,
            zeroline=False,
            showticklabels=False,
            range=[620, 0],
            scaleanchor="x",
            scaleratio=1,
            fixedrange=True
        ),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=20, r=20, t=20, b=20),
        height=650,
        width=500
    )
    
    defined_centers = set(analysis.get('defined_centers', []))
    defined_channels = analysis.get('defined_channels', [])
    
    for channel_key in CHANNELS.keys():
        if channel_key in CHANNEL_PATHS:
            paths = CHANNEL_PATHS[channel_key]
            for center1, center2 in paths:
                x0, y0 = CENTER_POSITIONS[center1]
                x1, y1 = CENTER_POSITIONS[center2]
                
                is_defined = channel_key in defined_channels
                
                fig.add_trace(go.Scatter(
                    x=[x0, x1],
                    y=[y0, y1],
                    mode='lines',
                    line=dict(
                        color='#e74c3c' if is_defined else '#cccccc',
                        width=8 if is_defined else 3
                    ),
                    hoverinfo='text',
                    hovertext=f"Channel {channel_key}: {CHANNELS[channel_key]['name']}" if is_defined else f"Channel {channel_key}",
                ))
    
    for center_name, pos in CENTER_POSITIONS.items():
        is_defined = center_name in defined_centers
        
        shape = CENTER_SHAPES[center_name]
        size = 50
        
        if shape == 'triangle':
            if center_name in ['Head', 'Heart']:
                x_points = [pos[0], pos[0] - 30, pos[0] + 30, pos[0]]
                y_points = [pos[1] - 25, pos[1] + 25, pos[1] + 25, pos[1] - 25]
            else:
                x_points = [pos[0], pos[0] - 30, pos[0] + 30, pos[0]]
                y_points = [pos[1] + 25, pos[1] - 25, pos[1] - 25, pos[1] + 25]
            
            fig.add_trace(go.Scatter(
                x=x_points,
                y=y_points,
                fill='toself',
                fillcolor='#f39c12' if is_defined else '#ffffff',
                line=dict(color='#2c3e50', width=2),
                mode='lines',
                hoverinfo='text',
                hovertext=f"{center_name} Center {'(Defined)' if is_defined else '(Open)'}",
            ))
        elif shape == 'square':
            x_points = [pos[0] - 30, pos[0] + 30, pos[0] + 30, pos[0] - 30, pos[0] - 30]
            y_points = [pos[1] - 25, pos[1] - 25, pos[1] + 25, pos[1] + 25, pos[1] - 25]
            
            fig.add_trace(go.Scatter(
                x=x_points,
                y=y_points,
                fill='toself',
                fillcolor='#e74c3c' if is_defined else '#ffffff',
                line=dict(color='#2c3e50', width=2),
                mode='lines',
                hoverinfo='text',
                hovertext=f"{center_name} Center {'(Defined)' if is_defined else '(Open)'}",
            ))
        elif shape == 'diamond':
            x_points = [pos[0], pos[0] + 35, pos[0], pos[0] - 35, pos[0]]
            y_points = [pos[1] - 30, pos[1], pos[1] + 30, pos[1], pos[1] - 30]
            
            fig.add_trace(go.Scatter(
                x=x_points,
                y=y_points,
                fill='toself',
                fillcolor='#f1c40f' if is_defined else '#ffffff',
                line=dict(color='#2c3e50', width=2),
                mode='lines',
                hoverinfo='text',
                hovertext=f"{center_name} Center {'(Defined)' if is_defined else '(Open)'}",
            ))
        
        fig.add_trace(go.Scatter(
            x=[pos[0]],
            y=[pos[1]],
            mode='text',
            text=[center_name],
            textposition='middle center',
            textfont=dict(size=10, color='#2c3e50', family='Arial Black'),
            hoverinfo='skip'
        ))
    
    return fig

def create_gate_table(gates_dict, title="Gates"):
    rows = []
    for planet, data in gates_dict.items():
        rows.append({
            'Planet': planet,
            'Gate': data['gate'],
            'Line': data['line'],
            'Gate.Line': f"{data['gate']}.{data['line']}",
            'Longitude': f"{data['longitude']:.2f}°"
        })
    return rows

def create_transit_comparison(natal_analysis, transit_gates):
    natal_gates = set(natal_analysis.get('all_gates', []))
    transit_gate_nums = set()
    
    for planet, data in transit_gates.items():
        transit_gate_nums.add(data['gate'])
    
    activating_gates = transit_gate_nums & natal_gates
    new_gates = transit_gate_nums - natal_gates
    
    return {
        'activating': list(activating_gates),
        'new': list(new_gates),
        'all_transit': list(transit_gate_nums)
    }
