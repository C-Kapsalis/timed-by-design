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

# Page configuration
st.set_page_config(
    page_title="Human Design Calculator",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for beautiful styling - Light, minimal theme
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Base styling - light theme */
    .stApp {
        background-color: #ffffff;
    }
    
    .main-header {
        font-family: 'Inter', sans-serif;
        font-size: 2.5rem;
        font-weight: 700;
        text-align: center;
        margin-bottom: 0.5rem;
        color: #1a1a1a;
    }
    
    .sub-header {
        font-family: 'Inter', sans-serif;
        font-size: 1.1rem;
        text-align: center;
        color: #666666;
        margin-bottom: 2rem;
    }
    
    .type-card {
        padding: 1.2rem;
        border-radius: 8px;
        text-align: center;
        color: white;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    }
    
    .insight-box {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
        border-left: 3px solid #1a1a1a;
    }
    
    .gate-tag {
        background: #f0f0f0;
        color: #1a1a1a;
        padding: 0.2rem 0.5rem;
        border-radius: 4px;
        margin: 0.1rem;
        display: inline-block;
        font-size: 0.85rem;
        font-weight: 500;
    }
    
    .gate-list {
        background: #f8f9fa;
        padding: 0.8rem 1rem;
        border-radius: 6px;
        margin: 0.5rem 0;
    }
    
    .practice-box {
        background: #f0fdf4;
        border: 1px solid #86efac;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
        color: #166534;
    }
    
    .warning-box {
        background: #fef3c7;
        border: 1px solid #fcd34d;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
        color: #92400e;
    }
    
    .info-box {
        background: #eff6ff;
        border: 1px solid #93c5fd;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
        color: #1e40af;
    }
    
    .center-defined {
        background-color: #1a1a1a;
        color: white;
        padding: 0.4rem 0.8rem;
        border-radius: 4px;
        margin: 0.2rem;
        display: inline-block;
        font-size: 0.85rem;
    }
    
    .center-open {
        background-color: #f0f0f0;
        color: #666;
        padding: 0.4rem 0.8rem;
        border-radius: 4px;
        margin: 0.2rem;
        display: inline-block;
        font-size: 0.85rem;
        border: 1px solid #e0e0e0;
    }
    
    /* Compact spacing */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    
    /* Clean expanders */
    .streamlit-expanderHeader {
        font-size: 0.9rem;
        font-weight: 500;
    }
    
    /* Sidebar styling */
    section[data-testid="stSidebar"] {
        background-color: #f8f9fa;
    }
    
    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 0.5rem;
    }
    
    .stTabs [data-baseweb="tab"] {
        padding: 0.5rem 1rem;
        font-size: 0.9rem;
    }
    
    /* Dataframe styling */
    .dataframe {
        font-size: 0.85rem;
    }
    
    /* Hide excessive padding */
    .element-container {
        margin-bottom: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="main-header">Human Design Calculator</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Discover your energetic blueprint</div>', unsafe_allow_html=True)

# Sidebar for navigation
with st.sidebar:
    st.markdown("### 🧭 Navigation")
    page = st.radio(
        "Choose a section:",
        ["📊 Calculate Chart", "🌙 Daily Transits"],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    st.markdown("### 💡 Quick Tips")
    st.info("""
    **For accurate results:**
    - Use your exact birth time
    - Include city AND country
    - Birth time affects your Profile and many gates
    """)

# Main content based on navigation
if page == "📊 Calculate Chart":
    st.subheader("Enter Your Birth Information")
    
    col1, col2 = st.columns(2)
    
    with col1:
        birth_date = st.date_input(
            "📅 Birth Date",
            value=date(1990, 1, 1),
            min_value=date(1900, 1, 1),
            max_value=date.today(),
            help="Select your date of birth"
        )
        
        birth_time = st.time_input(
            "⏰ Birth Time",
            value=time(12, 0),
            help="Your exact birth time is crucial for accurate calculations"
        )
        
        time_known = st.checkbox("I know my exact birth time", value=True)
        if not time_known:
            st.warning("⚠️ Without exact birth time, your Profile and some gates may be inaccurate. Consider using 12:00 noon as a starting point.")
    
    with col2:
        location_input = st.text_input(
            "📍 Birth Location",
            placeholder="e.g., New York, USA or London, UK",
            help="Enter city and country for accurate timezone"
        )
        
        location_data = None
        
        if location_input:
            with st.spinner("🔍 Looking up location..."):
                location_data = geocode_location_with_fallback(location_input)
                if location_data:
                    st.success(f"✅ {location_data['address']}")
                    st.caption(f"🌍 Timezone: {location_data['timezone']}")
                else:
                    st.warning("⚠️ Location not found via lookup. Please select timezone manually below.")
        
        # Manual timezone fallback
        if not location_data or st.checkbox("Select timezone manually", value=(location_input and not location_data)):
            common_timezones = [
                'UTC',
                'America/New_York', 'America/Chicago', 'America/Denver', 'America/Los_Angeles',
                'America/Toronto', 'America/Mexico_City', 'America/Sao_Paulo',
                'Europe/London', 'Europe/Paris', 'Europe/Berlin', 'Europe/Rome', 'Europe/Madrid',
                'Europe/Athens', 'Europe/Moscow',
                'Asia/Dubai', 'Asia/Kolkata', 'Asia/Singapore', 'Asia/Tokyo', 'Asia/Seoul', 'Asia/Shanghai',
                'Australia/Sydney', 'Australia/Melbourne',
                'Pacific/Auckland',
                'Africa/Cairo', 'Africa/Johannesburg'
            ]
            
            # Default to Europe/Athens for Greek locations
            default_idx = 0
            if location_input and 'greece' in location_input.lower():
                default_idx = common_timezones.index('Europe/Athens') if 'Europe/Athens' in common_timezones else 0
            
            manual_tz = st.selectbox(
                "Select your birth timezone",
                options=common_timezones,
                index=default_idx,
                help="Select the timezone where you were born"
            )
            
            location_data = {
                'latitude': 0,
                'longitude': 0,
                'address': location_input or 'Manual Entry',
                'timezone': manual_tz
            }
    
    st.markdown("---")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        calculate_btn = st.button("✨ Calculate My Human Design", type="primary", use_container_width=True)
    
    if calculate_btn and location_data:
        birth_datetime = datetime.combine(birth_date, birth_time)
        timezone_str = location_data.get('timezone', 'UTC')
        
        with st.spinner("🔮 Calculating your unique Human Design chart..."):
            try:
                natal_chart = calculate_natal_chart(birth_datetime, timezone_str)
                analysis = analyze_chart(natal_chart)
                
                st.session_state['natal_chart'] = natal_chart
                st.session_state['analysis'] = analysis
                st.session_state['birth_info'] = {
                    'date': birth_date,
                    'time': birth_time,
                    'location': location_data['address'],
                    'timezone': timezone_str
                }
            except Exception as e:
                st.error(f"Error calculating chart: {str(e)}")
    
    elif calculate_btn and not location_data:
        st.error("❌ Please enter a valid birth location to continue.")
    
    # Display results
    if 'analysis' in st.session_state:
        analysis = st.session_state['analysis']
        natal_chart = st.session_state['natal_chart']
        birth_info = st.session_state.get('birth_info', {})
        
        st.markdown("---")
        st.markdown("## 🌟 Your Human Design Chart")
        
        # Birth info summary
        if birth_info:
            st.caption(f"📅 {birth_info.get('date')} at {birth_info.get('time')} | 📍 {birth_info.get('location')}")
        
        # Main type cards
        col1, col2, col3, col4 = st.columns(4)
        
        type_colors = {
            "Generator": "#22c55e",
            "Manifesting Generator": "#f97316",
            "Manifestor": "#8b5cf6",
            "Projector": "#3b82f6",
            "Reflector": "#6b7280"
        }
        
        hd_type = analysis['type']
        
        with col1:
            st.markdown(f"""
            <div class="type-card" style="background: {type_colors.get(hd_type, '#333')};">
                <p style="margin: 0; opacity: 0.9; font-size: 0.8rem;">Type</p>
                <p style="margin: 0.3rem 0; font-size: 1.3rem; font-weight: 600;">{hd_type}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class="type-card" style="background: #1f2937;">
                <p style="margin: 0; opacity: 0.9; font-size: 0.8rem;">Profile</p>
                <p style="margin: 0.3rem 0; font-size: 1.3rem; font-weight: 600;">{analysis['profile']}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown(f"""
            <div class="type-card" style="background: #dc2626;">
                <p style="margin: 0; opacity: 0.9; font-size: 0.8rem;">Authority</p>
                <p style="margin: 0.3rem 0; font-size: 1.3rem; font-weight: 600;">{analysis['authority']}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col4:
            st.markdown(f"""
            <div class="type-card" style="background: #0891b2;">
                <p style="margin: 0; opacity: 0.9; font-size: 0.8rem;">Definition</p>
                <p style="margin: 0.3rem 0; font-size: 1.3rem; font-weight: 600;">{analysis['definition']}</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Strategy, Signature, Not-Self
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("🎯 Strategy", STRATEGY.get(hd_type, "Unknown"))
        with col2:
            st.metric("✨ Signature", SIGNATURE.get(hd_type, "Unknown"))
        with col3:
            st.metric("⚠️ Not-Self Theme", NOT_SELF_THEME.get(hd_type, "Unknown"))
        
        # Tabs for detailed information
        tab1, tab2, tab3, tab4 = st.tabs([
            "🎨 Bodygraph", 
            "💫 Type & Authority", 
            "🔮 Gates & Channels", 
            "📝 Daily Practice"
        ])
        
        with tab1:
            col1, col2 = st.columns([1, 1])
            
            with col1:
                st.markdown("### Your Bodygraph")
                fig = create_bodygraph(analysis)
                st.plotly_chart(fig, use_container_width=True)
            
            with col2:
                st.markdown("### Chart Overview")
                
                # Incarnation Cross
                cross = analysis['incarnation_cross']
                st.markdown(f"**🎭 Incarnation Cross:** {cross['cross']}")
                st.caption("Your life purpose theme - unfolds naturally as you live your design")
                
                st.markdown("---")
                
                # Defined Centers
                st.markdown("**Defined Centers (Colored):**")
                if analysis['defined_centers']:
                    for center in analysis['defined_centers']:
                        st.markdown(f'<span class="center-defined">{center}</span>', unsafe_allow_html=True)
                else:
                    st.write("None (Reflector)")
                
                st.markdown("<br>", unsafe_allow_html=True)
                
                # Open Centers
                all_centers = ['Head', 'Ajna', 'Throat', 'G', 'Heart', 'Sacral', 'Spleen', 'Solar Plexus', 'Root']
                open_centers = [c for c in all_centers if c not in analysis['defined_centers']]
                st.markdown("**Open Centers (White):**")
                for center in open_centers:
                    st.markdown(f'<span class="center-open">{center}</span>', unsafe_allow_html=True)
                
                st.markdown("---")
                
                # Defined Channels
                st.markdown("**Defined Channels:**")
                if analysis['defined_channels']:
                    for channel in analysis['defined_channels']:
                        channel_name = CHANNELS.get(channel, {}).get('name', '')
                        st.write(f"• **{channel}** - {channel_name}")
                else:
                    st.write("None")
        
        with tab2:
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("### 🌟 Your Type")
                type_insights = get_type_insights(hd_type)
                
                st.markdown(f"**What it means to be a {hd_type}:**")
                st.write(type_insights['description'])
                
                st.markdown("**Your Strengths:**")
                for strength in type_insights['strengths']:
                    st.write(f"✅ {strength}")
                
                st.markdown("**Growth Areas:**")
                for challenge in type_insights['challenges']:
                    st.write(f"🌱 {challenge}")
                
                st.markdown('<div class="practice-box">', unsafe_allow_html=True)
                st.markdown("**💡 Key Practice:**")
                st.write(type_insights['key_practice'])
                st.markdown('</div>', unsafe_allow_html=True)
            
            with col2:
                st.markdown("### 🧭 Your Authority")
                auth_insights = get_authority_insights(analysis['authority'])
                
                st.write(auth_insights['description'])
                
                st.markdown("**How to Use Your Authority:**")
                for tip in auth_insights['how_to_use']:
                    st.write(f"• {tip}")
                
                st.markdown('<div class="warning-box">', unsafe_allow_html=True)
                st.markdown("**⚠️ Watch Out For:**")
                st.write(auth_insights['warning'])
                st.markdown('</div>', unsafe_allow_html=True)
            
            st.markdown("---")
            
            # Profile insights
            st.markdown("### 👤 Your Profile")
            profile_insights = get_profile_insights(analysis['profile'])
            
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"**{analysis['profile']} - {get_profile_name(analysis['profile'])}**")
                st.write(profile_insights['description'])
            
            with col2:
                st.markdown("**Life Theme:**")
                st.write(profile_insights['life_theme'])
                st.markdown("**Learning Style:**")
                st.write(profile_insights['learning_style'])
        
        with tab3:
            st.markdown("### 🔮 Planetary Activations")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("#### 🟣 Personality (Conscious)")
                st.caption("What you're aware of - your conscious self")
                personality_gates = analysis['personality_gates']
                p_data = create_gate_table(personality_gates)
                st.dataframe(
                    pd.DataFrame(p_data)[['Planet', 'Gate.Line', 'Longitude']],
                    hide_index=True,
                    use_container_width=True
                )
            
            with col2:
                st.markdown("#### 🔴 Design (Unconscious)")
                st.caption("What others see - your body's wisdom")
                design_gates = analysis['design_gates']
                d_data = create_gate_table(design_gates)
                st.dataframe(
                    pd.DataFrame(d_data)[['Planet', 'Gate.Line', 'Longitude']],
                    hide_index=True,
                    use_container_width=True
                )
            
            st.markdown("---")
            
            # Channel insights
            if analysis['defined_channels']:
                st.markdown("### 🌈 Your Defined Channels")
                
                for channel in analysis['defined_channels']:
                    channel_info = CHANNELS.get(channel, {})
                    channel_insights = get_channel_insights(channel)
                    
                    with st.expander(f"**{channel}** - {channel_info.get('name', 'Unknown')}", expanded=False):
                        st.write(channel_insights['description'])
                        st.markdown("**Gift:**")
                        st.write(f"✨ {channel_insights['gift']}")
                        st.markdown("**Shadow:**")
                        st.write(f"🌑 {channel_insights['shadow']}")
            
            st.markdown("---")
            
            # Gate insights for key gates (Sun/Earth)
            st.markdown("### ☀️ Key Gate Insights")
            
            sun_gate = analysis['personality_gates'].get('Sun', {}).get('gate')
            earth_gate = analysis['personality_gates'].get('Earth', {}).get('gate')
            
            col1, col2 = st.columns(2)
            
            with col1:
                if sun_gate:
                    gate_info = get_gate_insights(sun_gate)
                    st.markdown(f"**Gate {sun_gate} - {gate_info['name']}** (Personality Sun)")
                    st.write(gate_info['description'])
                    st.caption(f"Theme: {gate_info['theme']}")
            
            with col2:
                if earth_gate:
                    gate_info = get_gate_insights(earth_gate)
                    st.markdown(f"**Gate {earth_gate} - {gate_info['name']}** (Personality Earth)")
                    st.write(gate_info['description'])
                    st.caption(f"Theme: {gate_info['theme']}")
        
        with tab4:
            st.markdown("### 📝 Today's Practice Based on Current Transits")
            
            # Calculate current transits
            from datetime import datetime
            current_transit = calculate_transit_chart(datetime.now(), 'UTC')
            transit_gates = current_transit['gates']
            
            # Get natal gates
            natal_gates = set(analysis.get('all_gates', []))
            transit_gate_nums = set(data['gate'] for data in transit_gates.values())
            
            # Find activating and new gates
            activating_gates = transit_gate_nums & natal_gates
            new_gates = transit_gate_nums - natal_gates
            
            # Get today's Sun gate for theme
            sun_transit = transit_gates.get('Sun', {})
            today_sun_gate = sun_transit.get('gate', 1)
            today_sun_line = sun_transit.get('line', 1)
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("### ☀️ Today's Energy Theme")
                today_gate_info = get_gate_insights(today_sun_gate)
                st.markdown(f"**Gate {today_sun_gate}.{today_sun_line} - {today_gate_info['name']}**")
                st.write(today_gate_info['description'])
                
                st.markdown("---")
                
                st.markdown("### 🔥 Transits Activating Your Chart")
                if activating_gates:
                    st.success(f"These gates are being amplified today: **{', '.join(map(str, sorted(activating_gates)))}**")
                    
                    # Show insights for key activating gates
                    for gate_num in list(activating_gates)[:3]:  # Show top 3
                        gate_info = get_gate_insights(gate_num)
                        with st.expander(f"Gate {gate_num} - {gate_info['name']}"):
                            st.write(gate_info['description'])
                            st.caption(f"Theme: {gate_info['theme']}")
                else:
                    st.info("No direct gate activations today - a day for reflection.")
            
            with col2:
                st.markdown("### 🌟 New Energies Available Today")
                if new_gates:
                    st.info(f"These gates are transiting but not in your chart: **{', '.join(map(str, sorted(new_gates)))}**")
                    st.caption("You may feel these energies from others or the collective field.")
                    
                    # Show insights for a couple new gates
                    for gate_num in list(new_gates)[:2]:
                        gate_info = get_gate_insights(gate_num)
                        with st.expander(f"Gate {gate_num} - {gate_info['name']} (Transit)"):
                            st.write(gate_info['description'])
                else:
                    st.success("All transit gates are in your chart - you're in your element!")
                
                st.markdown("---")
                
                # Moon gate for emotional theme
                moon_transit = transit_gates.get('Moon', {})
                moon_gate = moon_transit.get('gate', 1)
                moon_info = get_gate_insights(moon_gate)
                st.markdown("### 🌙 Emotional Undercurrent")
                st.markdown(f"**Gate {moon_gate} - {moon_info['name']}**")
                st.write(f"The Moon in Gate {moon_gate} colors today's emotional landscape with themes of {moon_info['theme'].lower()}.")
            
            st.markdown("---")
            
            # Personalized daily practice based on type + transits
            st.markdown("### 🧘 Your Personalized Practice for Today")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("#### 🌅 Morning Intention")
                morning_practice = get_transit_morning_practice(hd_type, today_sun_gate, activating_gates)
                st.markdown(f'<div class="practice-box">{morning_practice}</div>', unsafe_allow_html=True)
                
                st.markdown("#### 🎯 Today's Focus")
                focus = get_transit_focus(hd_type, analysis['authority'], today_sun_gate)
                st.info(focus)
            
            with col2:
                st.markdown("#### ⚠️ Watch Out For")
                not_self = get_not_self_guidance(hd_type)
                warning = get_transit_warning(hd_type, new_gates, not_self)
                st.markdown(f'<div class="warning-box">{warning}</div>', unsafe_allow_html=True)
                
                st.markdown("#### 🌙 Evening Question")
                evening_q = get_transit_evening_question(hd_type, analysis['authority'], activating_gates)
                st.success(evening_q)

elif page == "🌙 Daily Transits":
    st.markdown("## Today's Transit Reading")
    
    # Simple time controls in one line
    col1, col2, col3 = st.columns([2, 2, 1])
    with col1:
        transit_date = st.date_input("Date", value=date.today(), key="transit_date", label_visibility="collapsed")
    with col2:
        transit_tz = st.selectbox("Timezone", options=['UTC', 'America/New_York', 'America/Los_Angeles', 'Europe/London', 'Europe/Athens', 'Europe/Paris', 'Asia/Tokyo'], index=0, label_visibility="collapsed")
    
    # Auto-calculate
    transit_datetime = datetime.combine(transit_date, datetime.now().time())
    transit = calculate_transit_chart(transit_datetime, transit_tz)
    
    # Get transit gates
    sun_data = transit['gates'].get('Sun', {})
    sun_gate = sun_data.get('gate', 1)
    sun_info = get_gate_insights(sun_gate)
    
    moon_data = transit['gates'].get('Moon', {})
    moon_gate = moon_data.get('gate', 1)
    moon_info = get_gate_insights(moon_gate)
    
    # Today's theme - compact
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"### ☀️ Sun: Gate {sun_gate} - {sun_info['name']}")
        st.caption(f"{sun_info['description']}")
    with col2:
        st.markdown(f"### 🌙 Moon: Gate {moon_gate} - {moon_info['name']}")
        st.caption(f"{moon_info['description']}")
    
    st.markdown("---")
    
    # If user has chart - show personalized reading
    if 'analysis' in st.session_state:
        analysis = st.session_state['analysis']
        hd_type = analysis['type']
        natal_gates = set(analysis.get('all_gates', []))
        transit_gate_nums = set(data['gate'] for data in transit['gates'].values())
        
        activating = sorted(transit_gate_nums & natal_gates)
        new_gates = sorted(transit_gate_nums - natal_gates)
        
        # Compact two-column layout
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 🔥 Your Gates Activated")
            if activating:
                # Show as compact list with inline descriptions
                for gate in activating:
                    info = get_gate_insights(gate)
                    st.markdown(f"**{gate}** · {info['name']} — *{info['theme']}*")
            else:
                st.caption("No direct activations today")
        
        with col2:
            st.markdown("### 🌐 Collective Field")
            if new_gates:
                # Show as compact list with inline descriptions
                for gate in new_gates:
                    info = get_gate_insights(gate)
                    st.markdown(f"**{gate}** · {info['name']} — *{info['theme']}*")
            else:
                st.caption("All transits are in your chart!")
        
        st.markdown("---")
        
        # Type-specific guidance - very compact
        st.markdown(f"### 📋 Today's Practice for {hd_type}s")
        
        col1, col2 = st.columns(2)
        
        with col1:
            morning = get_transit_morning_practice(hd_type, sun_gate, activating)
            st.markdown(f'<div class="practice-box"><strong>Morning:</strong> {morning}</div>', unsafe_allow_html=True)
        
        with col2:
            not_self = get_not_self_guidance(hd_type)
            warning = get_transit_warning(hd_type, new_gates, not_self)
            st.markdown(f'<div class="warning-box"><strong>Watch for:</strong> {warning}</div>', unsafe_allow_html=True)
        
        # Evening question - single line
        evening = get_transit_evening_question(hd_type, analysis['authority'], activating)
        st.markdown(f'<div class="info-box"><strong>Evening reflection:</strong> {evening}</div>', unsafe_allow_html=True)
        
    else:
        st.markdown('<div class="info-box">💡 Calculate your chart first to see personalized transit insights.</div>', unsafe_allow_html=True)
    
    # Collapsible full transit table
    with st.expander("📊 All Planetary Positions"):
        transit_data = create_gate_table(transit['gates'])
        st.dataframe(
            pd.DataFrame(transit_data)[['Planet', 'Gate.Line', 'Longitude']],
            hide_index=True,
            use_container_width=True,
            height=200
        )

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #9ca3af; padding: 1rem; font-size: 0.8rem;">
    Human Design Calculator · Built with Swiss Ephemeris
</div>
""", unsafe_allow_html=True)
