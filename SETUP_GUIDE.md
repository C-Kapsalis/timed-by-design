# 🔧 Setup Guide for Human Design Calculator

## The Issue
You're using Python 3.13 which is too new - `pyswisseph` hasn't been updated for it yet.

## Solution 1: Use Python 3.11 (Recommended)

### Option A: Install Python 3.11 via Homebrew
```bash
# Install Python 3.11
brew install python@3.11

# Create virtual environment with Python 3.11
python3.11 -m venv venv

# Activate it
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Option B: Use pyenv (Best for managing multiple Python versions)
```bash
# Install pyenv if you don't have it
brew install pyenv

# Install Python 3.11
pyenv install 3.11.7

# Set it for this project
cd timed-by-design
pyenv local 3.11.7

# Create venv
python -m venv venv
source venv/bin/activate

# Install
pip install -r requirements.txt
```

## Solution 2: Use flatlib Instead (Pure Python - No Compilation!)

If you want to avoid C compilation issues entirely, we can use `flatlib` which is pure Python.

See `hd_calculations_flatlib.py` for an alternative implementation.

```bash
# This works with any Python version
pip install flatlib pytz geopy timezonefinder streamlit plotly pandas
```

## Solution 3: Deploy to Streamlit Cloud (Easiest!)

Streamlit Cloud uses Python 3.11 by default, so just push to GitHub and deploy there - it will work automatically!

1. Push your code to GitHub
2. Go to share.streamlit.io
3. Connect your repo
4. Deploy!

No local installation needed at all.

---

## Quick Test After Installation

```bash
# Activate your environment
source venv/bin/activate

# Test Swiss Ephemeris
python -c "import swisseph; print('Swiss Ephemeris works!')"

# Run the app
streamlit run app.py
```
