# Human Design Calculator

## Overview
A Python-based Human Design app using pyswissephemeris (Swiss Ephemeris) for calculating natal and transit charts. The application provides an interactive interface to discover one's energetic blueprint through Human Design principles.

## Current State
- Fully functional natal chart calculator
- Transit chart analysis
- Interactive bodygraph visualization
- Complete Human Design type, profile, authority, and definition calculations

## Project Architecture

### File Structure
```
├── app.py                 # Main Streamlit application
├── hd_calculations.py     # Swiss Ephemeris calculations for planetary positions
├── hd_bodygraph.py        # Bodygraph data structures (centers, channels, gates)
├── hd_visualization.py    # Plotly-based bodygraph visualization
├── .streamlit/
│   └── config.toml        # Streamlit server configuration
```

### Key Components

#### hd_calculations.py
- Planetary position calculations using Swiss Ephemeris
- Gate and line calculations from zodiac positions
- Design date calculation (88 degrees of Sun before birth)
- Location geocoding and timezone detection
- Profile calculations

#### hd_bodygraph.py
- Complete Human Design center definitions (9 centers)
- All 36 channels with gate connections
- Type calculation logic (Generator, Manifesting Generator, Manifestor, Projector, Reflector)
- Authority determination
- Definition analysis (Single, Split, Triple Split, Quadruple Split)
- Incarnation Cross calculation

#### hd_visualization.py
- Plotly-based interactive bodygraph chart
- Center shapes (triangles, squares, diamonds)
- Channel connections with defined/undefined states
- Color coding for defined vs open centers

#### app.py
- Streamlit interface with two main tabs:
  1. Natal Chart - Birth data input and full chart analysis
  2. Transit Chart - Current planetary transits and their impact
- Responsive design with color-coded type displays
- Planetary activation tables for personality and design

## Technical Details

### Dependencies
- streamlit: Web application framework
- pyswisseph: Swiss Ephemeris for astronomical calculations
- plotly: Interactive chart visualizations
- pytz: Timezone handling
- geopy: Location geocoding
- timezonefinder: Timezone detection from coordinates

### Human Design Calculations
- Uses tropical zodiac positions
- Converts planetary longitudes to 64 I Ching gates
- Each gate spans 5.625 degrees of the zodiac
- Lines 1-6 calculated within each gate

### Running the Application
```bash
streamlit run app.py --server.port 5000
```

## Recent Changes
- November 28, 2025: Initial implementation
  - Complete natal chart calculation
  - Transit chart analysis
  - Interactive bodygraph visualization
  - Type, Profile, Authority, and Definition calculations

## User Preferences
- (None recorded yet)
