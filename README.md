# ✨ Human Design Calculator

A comprehensive Human Design chart calculator built with Streamlit and Swiss Ephemeris.

![Human Design Calculator](https://img.shields.io/badge/Human%20Design-Calculator-purple)
![Python](https://img.shields.io/badge/Python-3.11+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red)

## Features

- 🔮 **Accurate Calculations**: Uses Swiss Ephemeris for precise planetary positions
- 📊 **Complete Chart Analysis**: Type, Authority, Profile, Definition, Centers, Channels, Gates
- 🎨 **Beautiful Bodygraph Visualization**: Interactive chart display
- 💡 **Deep Insights**: Comprehensive interpretations for every aspect of your design
- 🌙 **Transit Tracking**: See current planetary transits and their impact
- 📝 **Daily Practice Guidance**: Personalized tips for living your design

## Quick Start

### Local Development

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/human-design-calculator.git
cd human-design-calculator
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the app**
```bash
streamlit run app.py
```

5. **Open in browser**: http://localhost:8501

---

## 🚀 Deployment Options

### Option 1: Streamlit Community Cloud (RECOMMENDED - FREE!)

The easiest and fastest way to deploy. Perfect for personal projects.

1. **Push your code to GitHub**
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/yourusername/human-design-calculator.git
git push -u origin main
```

2. **Go to [share.streamlit.io](https://share.streamlit.io)**

3. **Click "New app"**

4. **Connect your GitHub repo**:
   - Repository: `yourusername/human-design-calculator`
   - Branch: `main`
   - Main file path: `app.py`

5. **Click "Deploy!"**

Your app will be live at: `https://yourusername-human-design-calculator.streamlit.app`

**Pros**: Free, fast, automatic deploys from GitHub, SSL included
**Cons**: May sleep after inactivity (wakes on access)

---

### Option 2: Railway (Easy, with Free Tier)

Great for more control with a simple deployment experience.

1. **Create a `Procfile`** (already included):
```
web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
```

2. **Go to [railway.app](https://railway.app)**

3. **Connect GitHub repo**

4. **Deploy!**

---

### Option 3: Render (Free Tier Available)

1. **Create `render.yaml`**:
```yaml
services:
  - type: web
    name: human-design-calculator
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
```

2. **Go to [render.com](https://render.com)**

3. **Connect GitHub and deploy**

---

### Option 4: Embed in Your Website (iframe)

If you want to embed this in your existing website:

1. **Deploy to Streamlit Cloud** (see Option 1)

2. **Add iframe to your website**:
```html
<iframe 
    src="https://yourusername-human-design-calculator.streamlit.app/?embed=true"
    width="100%"
    height="800px"
    style="border: none; border-radius: 10px;"
></iframe>
```

3. **Style the container**:
```html
<div style="max-width: 1200px; margin: 0 auto; padding: 20px;">
    <iframe 
        src="https://yourusername-human-design-calculator.streamlit.app/?embed=true"
        width="100%"
        height="900px"
        style="border: none; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.1);"
    ></iframe>
</div>
```

---

### Option 5: Vercel (Alternative - API Only)

⚠️ **Note**: Vercel doesn't natively support Streamlit's websocket connections. 

**For Vercel, consider these alternatives**:

1. **Use Streamlit Cloud** (recommended) and embed in your Vercel site via iframe

2. **Build a React/Next.js frontend** on Vercel that calls a separate Python API:
   - Deploy Python backend to Railway/Render
   - Deploy Next.js frontend to Vercel
   - Call API endpoints for calculations

3. **Convert to Flask/FastAPI** (significant rewrite required)

---

### Option 6: Docker Deployment

For self-hosting or cloud providers like DigitalOcean, AWS, GCP:

**Dockerfile**:
```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies for pyswisseph
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

**Build and run**:
```bash
docker build -t human-design-calculator .
docker run -p 8501:8501 human-design-calculator
```

---

## 📁 Project Structure

```
human-design-calculator/
├── app.py                 # Main Streamlit application
├── hd_calculations.py     # Swiss Ephemeris calculations
├── hd_bodygraph.py        # Chart analysis logic
├── hd_visualization.py    # Plotly visualizations
├── hd_insights.py         # Comprehensive interpretations
├── requirements.txt       # Python dependencies
├── .streamlit/
│   └── config.toml        # Streamlit configuration
├── Procfile               # For Railway/Heroku
└── README.md              # This file
```

---

## 🔧 Configuration

### Environment Variables (Optional)

For production deployments, you can set:

```env
STREAMLIT_SERVER_PORT=8501
STREAMLIT_SERVER_HEADLESS=true
STREAMLIT_BROWSER_GATHER_USAGE_STATS=false
```

---

## 📊 Accuracy

This calculator uses:
- **Swiss Ephemeris** for planetary positions (sub-arcsecond precision)
- **Verified gate boundaries** based on official Human Design specifications
- **Proper design date calculation** (88° solar arc before birth)

---

## ⚠️ Disclaimer

Human Design is a tool for self-discovery and personal growth. This calculator is meant for educational and entertainment purposes. It is not intended to replace professional advice or guidance.

---

## 🙏 Credits

- **Swiss Ephemeris** by Astrodienst (https://www.astro.com/swisseph/)
- **Human Design System** originated by Ra Uru Hu
- Built with ❤️ using Streamlit

---

## 📝 License

MIT License - Feel free to use and modify for your own projects!

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request
