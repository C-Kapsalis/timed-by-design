"""
Human Design Calculator - Streamlit App
A comprehensive tool to calculate and interpret your Human Design chart
"""

import streamlit as st
from datetime import datetime, date, time
import pytz
import pandas as pd

from hd_calculations import (
    calculate_natal_chart,
    calculate_transit_chart,
    geocode_location_with_fallback,
    get_profile_name
)
from hd_bodygraph import (
    analyze_chart,
    STRATEGY,
    NOT_SELF_THEME,
    SIGNATURE,
    CHANNELS
)
from hd_visualization import create_bodygraph, create_gate_table
from hd_insights import (
    get_type_insights,
    get_authority_insights,
    get_profile_insights,
    get_definition_insights,
    get_center_insights,
    get_channel_insights,
    get_gate_insights,
    get_not_self_guidance,
    get_daily_practice,
    get_transit_morning_practice,
    get_transit_focus,
    get_transit_warning,
    get_transit_evening_question
)

# Page configuration - NO SIDEBAR
st.set_page_config(
    page_title="Human Design Calculator",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide sidebar completely
st.markdown("""
<style>
    [data-testid="stSidebar"] {display: none;}
    [data-testid="collapsedControl"] {display: none;}
</style>
""", unsafe_allow_html=True)

# Custom CSS - Light, minimal, readable
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    .stApp {
        background-color: #ffffff;
    }
    
    .main-header {
        font-family: 'Inter', sans-serif;
        font-size: 2.2rem;
        font-weight: 700;
        text-align: center;
        margin-bottom: 0.3rem;
        color: #1a1a1a;
    }
    
    .sub-header {
        font-family: 'Inter', sans-serif;
        font-size: 1rem;
        text-align: center;
        color: #666666;
        margin-bottom: 1.5rem;
    }
    
    .type-card {
        padding: 1rem;
        border-radius: 8px;
        text-align: center;
        color: white;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    
    .type-card p {
        color: white !important;
    }
    
    .summary-row {
        display: flex;
        justify-content: center;
        gap: 2rem;
        margin: 1rem 0;
        flex-wrap: wrap;
    }
    
    .summary-item {
        text-align: center;
    }
    
    .summary-label {
        font-size: 0.75rem;
        color: #888;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    
    .summary-value {
        font-size: 1.1rem;
        font-weight: 600;
        color: #1a1a1a;
    }
    
    .practice-box {
        background: #f0fdf4;
        border: 1px solid #bbf7d0;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
        color: #166534;
    }
    
    .warning-box {
        background: #fffbeb;
        border: 1px solid #fde68a;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
        color: #92400e;
    }
    
    .info-box {
        background: #eff6ff;
        border: 1px solid #bfdbfe;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
        color: #1e40af;
    }
    
    .gate-item {
        background: #f8f9fa;
        border: 1px solid #e5e7eb;
        padding: 0.5rem 0.75rem;
        border-radius: 6px;
        margin: 0.25rem 0;
        color: #374151;
        cursor: pointer;
    }
    
    .gate-item:hover {
        background: #f3f4f6;
    }
    
    .gate-number {
        font-weight: 600;
        color: #1a1a1a;
    }
    
    .gate-name {
        color: #4b5563;
    }
    
    .gate-theme {
        font-style: italic;
        color: #6b7280;
        font-size: 0.9em;
    }
    
    .section-title {
        font-size: 1.1rem;
        font-weight: 600;
        color: #1a1a1a;
        margin-bottom: 0.75rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .transit-header {
        background: #f9fafb;
        padding: 1rem;
        border-radius: 8px;
        margin-bottom: 1rem;
        border: 1px solid #e5e7eb;
    }
    
    .transit-planet {
        font-size: 1.25rem;
        font-weight: 600;
        color: #1a1a1a;
    }
    
    .transit-desc {
        color: #4b5563;
        font-size: 0.9rem;
        margin-top: 0.25rem;
    }
    
    /* Fix tab text colors */
    .stTabs [data-baseweb="tab"] {
        color: #1a1a1a;
    }
    
    .stTabs [aria-selected="true"] {
        color: #1a1a1a;
        font-weight: 600;
    }
    
    /* Expander styling */
    .streamlit-expanderHeader {
        font-size: 0.95rem;
        color: #374151;
    }
    
    /* Make sure all text is readable */
    p, li, span {
        color: #374151;
    }
    
    h1, h2, h3, h4, h5, h6 {
        color: #1a1a1a;
    }
    
    /* Compact layout */
    .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
        max-width: 1200px;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="main-header">Human Design Calculator</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Discover your energetic blueprint</div>', unsafe_allow_html=True)

# Initialize session state
if 'chart_calculated' not in st.session_state:
    st.session_state.chart_calculated = False

# Birth Data Input Section
if not st.session_state.chart_calculated:
    # Show input form prominently
    st.markdown("### Enter Your Birth Details")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        birth_date = st.date_input(
            "Birth Date",
            value=date(1990, 1, 1),
            min_value=date(1900, 1, 1),
            max_value=date.today()
        )
    
    with col2:
        birth_time = st.time_input(
            "Birth Time",
            value=time(12, 0)
        )
    
    with col3:
        location_input = st.text_input(
            "Birth Location",
            placeholder="City, Country"
        )
    
    # Location lookup
    location_data = None
    if location_input:
        location_data = geocode_location_with_fallback(location_input)
        if location_data:
            st.caption(f"✓ {location_data['address']} ({location_data['timezone']})")
        else:
            st.caption("Location not found - select timezone manually")
    
    # Manual timezone if needed
    if not location_data:
        manual_tz = st.selectbox(
            "Select Timezone",
            options=['Europe/Athens', 'America/New_York', 'America/Los_Angeles', 'Europe/London', 
                     'Europe/Paris', 'Europe/Berlin', 'Asia/Tokyo', 'Australia/Sydney', 'UTC'],
            index=0
        )
        location_data = {'timezone': manual_tz, 'address': location_input or 'Manual'}
    
    # Calculate button
    if st.button("✨ Calculate My Chart", type="primary", use_container_width=True):
        if location_data:
            birth_datetime = datetime.combine(birth_date, birth_time)
            
            with st.spinner("Calculating your chart..."):
                chart = calculate_natal_chart(birth_datetime, location_data['timezone'])
                analysis = analyze_chart(chart)
                
                st.session_state['chart'] = chart
                st.session_state['analysis'] = analysis
                st.session_state['birth_info'] = {
                    'date': birth_date,
                    'time': birth_time,
                    'location': location_data['address'],
                    'timezone': location_data['timezone']
                }
                st.session_state.chart_calculated = True
                st.rerun()
        else:
            st.error("Please enter a location or select a timezone")

else:
    # Chart is calculated - show results
    analysis = st.session_state['analysis']
    chart = st.session_state['chart']
    birth_info = st.session_state['birth_info']
    hd_type = analysis['type']
    
    # Compact summary header
    col1, col2, col3, col4 = st.columns(4)
    
    type_colors = {
        "Generator": "#22c55e",
        "Manifesting Generator": "#f97316",
        "Manifestor": "#8b5cf6",
        "Projector": "#3b82f6",
        "Reflector": "#6b7280"
    }
    
    with col1:
        st.markdown(f"""
        <div class="type-card" style="background: {type_colors.get(hd_type, '#333')};">
            <p style="margin: 0; opacity: 0.9; font-size: 0.75rem;">TYPE</p>
            <p style="margin: 0.2rem 0; font-size: 1.2rem; font-weight: 600;">{hd_type}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="type-card" style="background: #374151;">
            <p style="margin: 0; opacity: 0.9; font-size: 0.75rem;">PROFILE</p>
            <p style="margin: 0.2rem 0; font-size: 1.2rem; font-weight: 600;">{analysis['profile']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="type-card" style="background: #dc2626;">
            <p style="margin: 0; opacity: 0.9; font-size: 0.75rem;">AUTHORITY</p>
            <p style="margin: 0.2rem 0; font-size: 1.2rem; font-weight: 600;">{analysis['authority']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div class="type-card" style="background: #0891b2;">
            <p style="margin: 0; opacity: 0.9; font-size: 0.75rem;">DEFINITION</p>
            <p style="margin: 0.2rem 0; font-size: 1.2rem; font-weight: 600;">{analysis['definition']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Strategy/Signature/Not-Self row
    st.markdown(f"""
    <div class="summary-row">
        <div class="summary-item">
            <div class="summary-label">Strategy</div>
            <div class="summary-value">{STRATEGY.get(hd_type, 'Unknown')}</div>
        </div>
        <div class="summary-item">
            <div class="summary-label">Signature</div>
            <div class="summary-value">{SIGNATURE.get(hd_type, 'Unknown')}</div>
        </div>
        <div class="summary-item">
            <div class="summary-label">Not-Self</div>
            <div class="summary-value">{NOT_SELF_THEME.get(hd_type, 'Unknown')}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Button to recalculate
    if st.button("↻ Enter Different Birth Data", type="secondary"):
        st.session_state.chart_calculated = False
        st.rerun()
    
    st.markdown("---")
    
    # TABS - Starting with Daily Practice
    tab1, tab2, tab3, tab4 = st.tabs([
        "📅 Daily Practice", 
        "🎨 Bodygraph", 
        "💫 Type & Authority", 
        "🔮 Gates & Channels"
    ])
    
    # ============ TAB 1: DAILY PRACTICE (Transit-aware) ============
    with tab1:
        # Calculate current transits
        current_transit = calculate_transit_chart(datetime.now(), 'UTC')
        transit_gates = current_transit['gates']
        
        # Get transit data
        sun_data = transit_gates.get('Sun', {})
        sun_gate = sun_data.get('gate', 1)
        sun_line = sun_data.get('line', 1)
        sun_info = get_gate_insights(sun_gate)
        
        moon_data = transit_gates.get('Moon', {})
        moon_gate = moon_data.get('gate', 1)
        moon_info = get_gate_insights(moon_gate)
        
        # Get natal vs transit comparison
        natal_gates = set(analysis.get('all_gates', []))
        transit_gate_nums = set(data['gate'] for data in transit_gates.values())
        activating = sorted(transit_gate_nums & natal_gates)
        new_gates = sorted(transit_gate_nums - natal_gates)
        
        # Today's cosmic weather
        st.markdown("### ☀️ Today's Energy")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"""
            <div class="transit-header">
                <div class="transit-planet">☀️ Sun in Gate {sun_gate} — {sun_info['name']}</div>
                <div class="transit-desc">{sun_info['description']}</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class="transit-header">
                <div class="transit-planet">🌙 Moon in Gate {moon_gate} — {moon_info['name']}</div>
                <div class="transit-desc">{moon_info['description']}</div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Gates comparison
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown('<div class="section-title">🔥 Your Gates Being Activated</div>', unsafe_allow_html=True)
            if activating:
                for gate in activating:
                    info = get_gate_insights(gate)
                    with st.expander(f"**{gate}** · {info['name']} — *{info['theme']}*"):
                        st.write(info['description'])
            else:
                st.caption("No direct activations today — a quieter day for reflection.")
        
        with col2:
            st.markdown('<div class="section-title">🌐 Collective Field Today</div>', unsafe_allow_html=True)
            if new_gates:
                for gate in new_gates:
                    info = get_gate_insights(gate)
                    with st.expander(f"**{gate}** · {info['name']} — *{info['theme']}*"):
                        st.write(info['description'])
            else:
                st.caption("All transit gates are in your chart — you're in sync!")
        
        st.markdown("---")
        
        # Personalized practice
        st.markdown(f"### 🧘 Your Practice for Today")
        
        col1, col2 = st.columns(2)
        
        with col1:
            morning = get_transit_morning_practice(hd_type, sun_gate, activating)
            st.markdown(f'<div class="practice-box"><strong>☀️ Morning Intention</strong><br>{morning}</div>', unsafe_allow_html=True)
            
            focus = get_transit_focus(hd_type, analysis['authority'], sun_gate)
            st.markdown(f'<div class="info-box"><strong>🎯 Today\'s Focus</strong><br>{focus}</div>', unsafe_allow_html=True)
        
        with col2:
            not_self = get_not_self_guidance(hd_type)
            warning = get_transit_warning(hd_type, new_gates, not_self)
            st.markdown(f'<div class="warning-box"><strong>⚠️ Watch Out For</strong><br>{warning}</div>', unsafe_allow_html=True)
            
            evening = get_transit_evening_question(hd_type, analysis['authority'], activating)
            st.markdown(f'<div class="practice-box"><strong>🌙 Evening Question</strong><br>{evening}</div>', unsafe_allow_html=True)
        
        # Full transit positions (collapsed)
        with st.expander("📊 All Planetary Positions"):
            transit_data = create_gate_table(transit_gates)
            st.dataframe(
                pd.DataFrame(transit_data)[['Planet', 'Gate.Line', 'Longitude']],
                hide_index=True,
                use_container_width=True
            )
    
    # ============ TAB 2: BODYGRAPH ============
    with tab2:
        col1, col2 = st.columns([2, 1])
        
        with col1:
            fig = create_bodygraph(analysis)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.markdown("### Incarnation Cross")
            cross = analysis.get('incarnation_cross', {})
            st.write(f"**{cross.get('name', 'Unknown')}**")
            st.caption(f"Sun: {cross.get('sun', 'N/A')} | Earth: {cross.get('earth', 'N/A')}")
            
            st.markdown("### Defined Centers")
            for center in analysis['defined_centers']:
                st.markdown(f'<span style="background:#1a1a1a;color:white;padding:4px 8px;border-radius:4px;margin:2px;display:inline-block;font-size:0.85rem;">{center}</span>', unsafe_allow_html=True)
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            st.markdown("### Open Centers")
            all_centers = ['Head', 'Ajna', 'Throat', 'G', 'Heart', 'Sacral', 'Spleen', 'Solar Plexus', 'Root']
            open_centers = [c for c in all_centers if c not in analysis['defined_centers']]
            for center in open_centers:
                st.markdown(f'<span style="background:#f3f4f6;color:#6b7280;padding:4px 8px;border-radius:4px;margin:2px;display:inline-block;font-size:0.85rem;border:1px solid #e5e7eb;">{center}</span>', unsafe_allow_html=True)
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            st.markdown("### Defined Channels")
            if analysis['defined_channels']:
                for channel in analysis['defined_channels']:
                    channel_name = CHANNELS.get(channel, {}).get('name', '')
                    st.caption(f"**{channel}** — {channel_name}")
            else:
                st.caption("None")
    
    # ============ TAB 3: TYPE & AUTHORITY ============
    with tab3:
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### About Your Type")
            type_insights = get_type_insights(hd_type)
            st.write(type_insights['description'])
            
            st.markdown("**Strengths:**")
            for s in type_insights['strengths'][:4]:
                st.write(f"• {s}")
            
            st.markdown("**Growth Areas:**")
            for c in type_insights['challenges'][:3]:
                st.write(f"• {c}")
        
        with col2:
            st.markdown("### Your Authority")
            auth_insights = get_authority_insights(analysis['authority'])
            st.write(auth_insights['description'])
            
            st.markdown("**How to Use It:**")
            for tip in auth_insights['how_to_use'][:4]:
                st.write(f"• {tip}")
        
        st.markdown("---")
        
        st.markdown("### Your Profile")
        profile_insights = get_profile_insights(analysis['profile'])
        col1, col2 = st.columns(2)
        with col1:
            st.write(f"**{analysis['profile']}** — {get_profile_name(analysis['profile'])}")
            st.write(profile_insights['description'])
        with col2:
            st.markdown("**Life Theme:**")
            st.write(profile_insights['life_theme'])
    
    # ============ TAB 4: GATES & CHANNELS ============
    with tab4:
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### Personality Gates (Conscious)")
            st.caption("What you're aware of")
            personality_gates = analysis['personality_gates']
            for planet, data in personality_gates.items():
                gate = data['gate']
                line = data['line']
                info = get_gate_insights(gate)
                with st.expander(f"**{planet}**: Gate {gate}.{line} — {info['name']}"):
                    st.write(info['description'])
                    st.caption(f"Theme: {info['theme']}")
        
        with col2:
            st.markdown("### Design Gates (Unconscious)")
            st.caption("What others see in you")
            design_gates = analysis['design_gates']
            for planet, data in design_gates.items():
                gate = data['gate']
                line = data['line']
                info = get_gate_insights(gate)
                with st.expander(f"**{planet}**: Gate {gate}.{line} — {info['name']}"):
                    st.write(info['description'])
                    st.caption(f"Theme: {info['theme']}")
        
        # Channel insights
        if analysis['defined_channels']:
            st.markdown("---")
            st.markdown("### Your Channels")
            for channel in analysis['defined_channels']:
                channel_info = get_channel_insights(channel)
                with st.expander(f"**Channel {channel}** — {channel_info['name']}"):
                    st.write(channel_info['description'])
                    st.markdown("**Gift:**")
                    st.write(channel_info['gift'])

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #9ca3af; padding: 0.5rem; font-size: 0.8rem;">
    Human Design Calculator · Built with Swiss Ephemeris
</div>
""", unsafe_allow_html=True)
