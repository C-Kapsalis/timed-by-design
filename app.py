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
    get_daily_practice
)

# Page configuration
st.set_page_config(
    page_title="Human Design Calculator",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for beautiful styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    .main-header {
        font-family: 'Inter', sans-serif;
        font-size: 2.8rem;
        font-weight: 700;
        text-align: center;
        margin-bottom: 0.5rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .sub-header {
        font-family: 'Inter', sans-serif;
        font-size: 1.2rem;
        text-align: center;
        color: #7f8c8d;
        margin-bottom: 2rem;
    }
    
    .type-card {
        padding: 1.5rem;
        border-radius: 1rem;
        text-align: center;
        color: white;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    .insight-card {
        background: linear-gradient(135deg, #f5f7fa 0%, #e4e8ec 100%);
        padding: 1.5rem;
        border-radius: 1rem;
        margin: 1rem 0;
        border-left: 4px solid #667eea;
    }
    
    .gate-conscious {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 0.3rem 0.6rem;
        border-radius: 0.3rem;
        margin: 0.1rem;
        display: inline-block;
        font-size: 0.85rem;
    }
    
    .gate-unconscious {
        background: linear-gradient(135deg, #e74c3c 0%, #c0392b 100%);
        color: white;
        padding: 0.3rem 0.6rem;
        border-radius: 0.3rem;
        margin: 0.1rem;
        display: inline-block;
        font-size: 0.85rem;
    }
    
    .center-defined {
        background-color: #f39c12;
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 0.5rem;
        margin: 0.2rem;
        display: inline-block;
    }
    
    .center-open {
        background-color: #ecf0f1;
        color: #7f8c8d;
        padding: 0.5rem 1rem;
        border-radius: 0.5rem;
        margin: 0.2rem;
        display: inline-block;
        border: 1px dashed #bdc3c7;
    }
    
    .stTabs [data-baseweb="tab-list"] {
        gap: 1rem;
    }
    
    .stTabs [data-baseweb="tab"] {
        padding: 0.75rem 1.5rem;
        font-weight: 500;
    }
    
    .practice-box {
        background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
        padding: 1.5rem;
        border-radius: 1rem;
        margin: 1rem 0;
    }
    
    .warning-box {
        background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
        padding: 1.5rem;
        border-radius: 1rem;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="main-header">✨ Human Design Calculator</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Discover Your Unique Energetic Blueprint</div>', unsafe_allow_html=True)

# Sidebar for navigation
with st.sidebar:
    st.markdown("### 🧭 Navigation")
    page = st.radio(
        "Choose a section:",
        ["📊 Calculate Chart", "📖 Learn More", "🌙 Daily Transits"],
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
            "Generator": "#27ae60",
            "Manifesting Generator": "#e67e22",
            "Manifestor": "#8e44ad",
            "Projector": "#3498db",
            "Reflector": "#95a5a6"
        }
        
        hd_type = analysis['type']
        
        with col1:
            st.markdown(f"""
            <div class="type-card" style="background: {type_colors.get(hd_type, '#333')};">
                <h4 style="margin: 0; opacity: 0.9;">Type</h4>
                <h2 style="margin: 0.5rem 0;">{hd_type}</h2>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class="type-card" style="background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%);">
                <h4 style="margin: 0; opacity: 0.9;">Profile</h4>
                <h2 style="margin: 0.5rem 0;">{analysis['profile']}</h2>
                <p style="margin: 0; font-size: 0.8rem; opacity: 0.8;">{get_profile_name(analysis['profile'])}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown(f"""
            <div class="type-card" style="background: linear-gradient(135deg, #c0392b 0%, #e74c3c 100%);">
                <h4 style="margin: 0; opacity: 0.9;">Authority</h4>
                <h2 style="margin: 0.5rem 0;">{analysis['authority']}</h2>
            </div>
            """, unsafe_allow_html=True)
        
        with col4:
            st.markdown(f"""
            <div class="type-card" style="background: linear-gradient(135deg, #1abc9c 0%, #16a085 100%);">
                <h4 style="margin: 0; opacity: 0.9;">Definition</h4>
                <h2 style="margin: 0.5rem 0;">{analysis['definition']}</h2>
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
        tab1, tab2, tab3, tab4, tab5 = st.tabs([
            "🎨 Bodygraph", 
            "💫 Type & Authority", 
            "🔮 Gates & Channels", 
            "🧘 Centers",
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
            st.markdown("### 🧘 Understanding Your Centers")
            
            all_centers = ['Head', 'Ajna', 'Throat', 'G', 'Heart', 'Sacral', 'Spleen', 'Solar Plexus', 'Root']
            
            for center in all_centers:
                is_defined = center in analysis['defined_centers']
                center_insights = get_center_insights(center, is_defined)
                
                status = "🟡 Defined" if is_defined else "⚪ Open"
                
                with st.expander(f"**{center} Center** - {status}", expanded=False):
                    st.write(center_insights['description'])
                    
                    if is_defined:
                        st.markdown("**Your Fixed Energy:**")
                        st.write(center_insights['defined_meaning'])
                    else:
                        st.markdown("**Your Wisdom Potential:**")
                        st.write(center_insights['open_meaning'])
                        
                        st.markdown("**Not-Self Question:**")
                        st.info(center_insights['not_self_question'])
                        
                        st.markdown("**Wisdom When Aligned:**")
                        st.success(center_insights['wisdom'])
        
        with tab5:
            st.markdown("### 📝 Your Daily Practice")
            
            practice = get_daily_practice(hd_type, analysis['authority'])
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("#### 🌅 Morning Practice")
                st.markdown('<div class="practice-box">', unsafe_allow_html=True)
                st.write(practice['morning'])
                st.markdown('</div>', unsafe_allow_html=True)
                
                st.markdown("#### 🌙 Evening Reflection")
                st.markdown('<div class="practice-box">', unsafe_allow_html=True)
                st.write(practice['evening'])
                st.markdown('</div>', unsafe_allow_html=True)
            
            with col2:
                st.markdown("#### ⚠️ Not-Self Awareness")
                not_self = get_not_self_guidance(hd_type)
                st.markdown('<div class="warning-box">', unsafe_allow_html=True)
                st.markdown("**Signs you're in your Not-Self:**")
                for sign in not_self['signs']:
                    st.write(f"• {sign}")
                st.markdown('</div>', unsafe_allow_html=True)
                
                st.markdown("**How to Return to Self:**")
                for tip in not_self['return_to_self']:
                    st.write(f"✨ {tip}")
            
            st.markdown("---")
            
            st.markdown("#### 📌 Weekly Experiment")
            st.info(practice['weekly_experiment'])
            
            st.markdown("#### 🎯 Monthly Focus")
            st.success(practice['monthly_focus'])

elif page == "📖 Learn More":
    st.markdown("## 📖 Understanding Human Design")
    
    st.markdown("""
    Human Design is a synthesis of ancient wisdom and modern science, combining:
    - **Astrology** (planetary positions at birth)
    - **I Ching** (64 hexagrams = 64 gates)
    - **Kabbalah** (Tree of Life = centers and channels)
    - **Hindu-Brahmin Chakra System** (energy centers)
    - **Quantum Physics** (neutrino stream imprinting)
    """)
    
    tab1, tab2, tab3, tab4 = st.tabs(["Types", "Authorities", "Centers", "Profiles"])
    
    with tab1:
        st.markdown("### The 5 Types")
        
        types_data = {
            "Generator": {
                "percent": "~37%",
                "strategy": "Wait to Respond",
                "signature": "Satisfaction",
                "not_self": "Frustration",
                "description": "Generators are the life force of the planet. They have sustainable energy and are here to find work they love."
            },
            "Manifesting Generator": {
                "percent": "~33%",
                "strategy": "Wait to Respond, then Inform",
                "signature": "Satisfaction",
                "not_self": "Frustration & Anger",
                "description": "MGs are multi-passionate beings who move quickly. They're here to find shortcuts and do multiple things."
            },
            "Projector": {
                "percent": "~20%",
                "strategy": "Wait for Invitation",
                "signature": "Success",
                "not_self": "Bitterness",
                "description": "Projectors are natural guides and managers. They see others deeply and are here to guide energy."
            },
            "Manifestor": {
                "percent": "~8%",
                "strategy": "Inform before Acting",
                "signature": "Peace",
                "not_self": "Anger",
                "description": "Manifestors are here to initiate and impact. They have a powerful aura that repels and closes off."
            },
            "Reflector": {
                "percent": "~1%",
                "strategy": "Wait a Lunar Cycle",
                "signature": "Surprise",
                "not_self": "Disappointment",
                "description": "Reflectors are the mirrors of society. With no defined centers, they sample and reflect the health of their community."
            }
        }
        
        for type_name, info in types_data.items():
            with st.expander(f"**{type_name}** ({info['percent']} of population)"):
                st.write(info['description'])
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Strategy", info['strategy'])
                with col2:
                    st.metric("Signature", info['signature'])
                with col3:
                    st.metric("Not-Self", info['not_self'])
    
    with tab2:
        st.markdown("### The 7 Authorities")
        
        authorities = {
            "Emotional": "Wait through your emotional wave before making decisions. Clarity comes with time, never in the moment.",
            "Sacral": "Trust your gut response - the 'uh-huh' (yes) or 'uhn-uhn' (no). Your body knows before your mind.",
            "Splenic": "Trust your instant intuitive hits. Your spleen speaks once, in the moment - don't second-guess it.",
            "Ego": "Ask yourself 'Do I want this? Is my heart in it?' Your willpower guides correct decisions.",
            "Self-Projected": "Talk things out with trusted others. Your truth emerges through your voice.",
            "Mental": "You need to be in the right environment and talk to the right people. Your authority is external.",
            "Lunar": "Wait 28 days (full lunar cycle) before major decisions. Sample all the lunar energies first."
        }
        
        for auth, desc in authorities.items():
            with st.expander(f"**{auth} Authority**"):
                st.write(desc)
    
    with tab3:
        st.markdown("### The 9 Centers")
        
        centers_info = {
            "Head": "Pressure for inspiration and questions. Open: Easily overwhelmed by others' questions.",
            "Ajna": "Mental processing and conceptualization. Open: Can see all perspectives.",
            "Throat": "Communication and manifestation. Open: Pressure to speak or prove oneself.",
            "G/Identity": "Love, direction, and identity. Open: Searching for love and direction.",
            "Heart/Ego": "Willpower and self-worth. Open: Nothing to prove.",
            "Sacral": "Life force and work energy. Open: Not here to work in traditional ways.",
            "Spleen": "Intuition, health, and survival. Open: Can deeply attune to wellness.",
            "Solar Plexus": "Emotions and feelings. Open: Amplifies others' emotions.",
            "Root": "Adrenaline and pressure. Open: Rushing to be free of pressure."
        }
        
        for center, info in centers_info.items():
            with st.expander(f"**{center} Center**"):
                st.write(info)
    
    with tab4:
        st.markdown("### The 12 Profiles")
        
        profiles = {
            "1/3": "Investigator/Martyr - Foundation through trial and error",
            "1/4": "Investigator/Opportunist - Deep research meets networking",
            "2/4": "Hermit/Opportunist - Natural talent recognized by others",
            "2/5": "Hermit/Heretic - Called out to save the day",
            "3/5": "Martyr/Heretic - Learning through experience to help others",
            "3/6": "Martyr/Role Model - Experimentation leading to wisdom",
            "4/6": "Opportunist/Role Model - Building networks and modeling the way",
            "4/1": "Opportunist/Investigator - Fixed foundation through relationships",
            "5/1": "Heretic/Investigator - Practical solutions built on research",
            "5/2": "Heretic/Hermit - Called to share natural gifts",
            "6/2": "Role Model/Hermit - Three-part life journey",
            "6/3": "Role Model/Martyr - Optimism through experience"
        }
        
        for profile, desc in profiles.items():
            st.write(f"**{profile}**: {desc}")

elif page == "🌙 Daily Transits":
    st.markdown("## 🌙 Current Transits")
    
    col1, col2 = st.columns(2)
    
    with col1:
        use_current = st.checkbox("Use current time", value=True)
        
        if not use_current:
            transit_date = st.date_input("Transit Date", value=date.today(), key="transit_date")
            transit_time = st.time_input("Transit Time", value=datetime.now().time(), key="transit_time")
        else:
            transit_date = date.today()
            transit_time = datetime.now().time()
    
    with col2:
        transit_tz = st.selectbox(
            "Timezone",
            options=pytz.common_timezones,
            index=pytz.common_timezones.index('UTC') if 'UTC' in pytz.common_timezones else 0
        )
    
    calc_transit_btn = st.button("🔄 Calculate Current Transits", type="primary")
    
    if calc_transit_btn or use_current:
        transit_datetime = datetime.combine(transit_date, transit_time)
        
        with st.spinner("Calculating current transits..."):
            transit = calculate_transit_chart(transit_datetime, transit_tz)
            st.session_state['transit'] = transit
    
    if 'transit' in st.session_state:
        transit = st.session_state['transit']
        
        st.markdown("---")
        st.subheader(f"Transits for {transit['datetime'].strftime('%B %d, %Y at %H:%M')}")
        
        transit_data = create_gate_table(transit['gates'])
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("### Current Transit Gates")
            st.dataframe(
                pd.DataFrame(transit_data)[['Planet', 'Gate.Line', 'Longitude']],
                hide_index=True,
                use_container_width=True
            )
        
        with col2:
            if 'analysis' in st.session_state:
                st.markdown("### Transit Impact on Your Chart")
                
                natal_gates = set(st.session_state['analysis'].get('all_gates', []))
                transit_gate_nums = set()
                
                for planet, data in transit['gates'].items():
                    transit_gate_nums.add(data['gate'])
                
                activating = transit_gate_nums & natal_gates
                new_gates = transit_gate_nums - natal_gates
                
                if activating:
                    st.markdown("**🔥 Activating Your Gates:**")
                    st.write(", ".join(map(str, sorted(activating))))
                
                if new_gates:
                    st.markdown("**🌟 New Gates (Not in Natal):**")
                    st.write(", ".join(map(str, sorted(new_gates))))
            else:
                st.info("💡 Calculate your natal chart first to see how transits affect you personally.")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #7f8c8d; padding: 1rem;">
    <p>✨ Human Design Calculator using Swiss Ephemeris</p>
    <p style="font-size: 0.8rem;">Calculations based on planetary positions at time of birth</p>
    <p style="font-size: 0.7rem; margin-top: 1rem;">
        Human Design is a tool for self-discovery. This is not meant to limit you, but to help you understand your unique nature.
    </p>
</div>
""", unsafe_allow_html=True)