
# Game Simulation : Mini Roulette - Comprehensive User Guide

### CSEC 413 - MODELING AND SIMULATION 
**Date:** DEC 2025



![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.8+-green.svg)
![Flask](https://img.shields.io/badge/flask-2.3.0-red.svg)
![License](https://img.shields.io/badge/license-Educational-yellow.svg)

##  Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation Guide](#installation-guide)
- [Quick Start](#quick-start)
- [User Guide](#user-guide)
  - [For Players](#for-players)
  - [For Administrators](#for-administrators)
  - [Monte Carlo Simulation](#monte-carlo-simulation)
- [Game Rules](#game-rules)
- [Technical Details](#technical-details)
- [Troubleshooting](#troubleshooting)
- [FAQ](#faq)
- [Contributing](#contributing)
- [License](#license)

---

##  Overview

**Roulette Game Simulation** is an educational web application that demonstrates probability theory, house edge, and Monte Carlo simulation through an interactive roulette game. This project allows users to:

- Play a simplified roulette game (numbers 0-12)
- Experience fair and "tweaked" probability distributions
- Run Monte Carlo simulations (10,000+ plays) instantly
- Analyze statistical outcomes with comprehensive analytics
- Understand the mathematics behind casino games

**Educational Purpose**: This project is designed for students, educators, and anyone interested in understanding probability, statistics, and gambling mathematics.

---

##  Features

###  Interactive Gameplay
- Real-time roulette game with smooth animations
- Multiple bet types: Number, Color (Red/Black), Parity (Odd/Even)
- Virtual currency system ($1,000 starting balance)
- Win/loss tracking and balance management

###  Admin Dashboard
- Adjust probability weights for each number (0-12)
- Toggle between fair and tweaked game modes
- Manage user accounts and balances
- View game analytics and statistics
- Handle player fund requests

###  Monte Carlo Simulation
- Run 100 to 10,000,000 simulations instantly
- Custom probability distributions
- Random seed support for reproducibility
- Comprehensive statistical analysis
- Interactive charts (outcome distribution, cumulative profit)
- Export results (JSON/CSV)

###  Security Features
- Password hashing with Werkzeug
- User authentication with Flask-Login
- Admin-only access controls
- Session management

---

##  Installation Guide

### Prerequisites

Before installing, ensure you have:

- **Python 3.8 or higher** ([Download Python](https://www.python.org/downloads/))
- **pip** (Python package manager - usually included with Python)
- **Git** (optional, for cloning) ([Download Git](https://git-scm.com/downloads))
- **Web browser** (Chrome, Firefox, Edge, Safari)

### Step 1: Download the Project

#### Option A: Clone with Git
```bash
git clone https://github.com/yourusername/GameSimulation.git
cd GameSimulation
```

#### Option B: Download ZIP
1. Click the green "Code" button on GitHub
2. Select "Download ZIP"
3. Extract the ZIP file to your desired location
4. Open terminal/command prompt in the extracted folder

### Step 2: Create Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` appear in your terminal prompt.

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- Flask (Web framework)
- Flask-Login (User authentication)
- Flask-SQLAlchemy (Database management)
- Werkzeug (Security utilities)

### Step 4: Initialize Database

```bash
python init_db.py
```

This creates:
- SQLite database (`instance/database.db`)
- Admin account (username: `admin`, password: `admin123`)
- Database tables for users, game results, and money requests

### Step 5: Run the Application

```bash
python app.py
```

You should see:
```
 * Running on http://127.0.0.1:5000
 * Debug mode: on
```

### Step 6: Access the Application

Open your web browser and navigate to:
```
http://localhost:5000
```

**Success!** You should see the login page. 

---

##  Quick Start

### For First-Time Users

1. **Access the Application**
   - Open browser: `http://localhost:5000`

2. **Create a Player Account**
   - Click "Create New Account"
   - Enter username and password
   - Click "Create Account"
   - You'll receive $1,000 virtual currency

3. **Play Your First Game**
   - Select a bet (click on a number or color)
   - Enter bet amount (default: $10)
   - Click "SPIN"
   - Watch the wheel spin and see your result!

4. **Try Monte Carlo Simulation**
   - Click " Monte Carlo Simulation" on login page
   - Set simulations to 10,000
   - Select bet type (e.g., Color - Red)
   - Click "▶ Run Simulation"
   - Analyze the results!

### For Administrators

1. **Login as Admin**
   - Click "Admin Panel" on login page
   - Username: `admin`
   - Password: `administration` ( Change this in production!)

2. **Adjust Game Settings**
   - Go to "Game Settings" tab
   - Modify probability weights using sliders
   - Click "Save Settings"
   - Test with "Try Game" button

---

##  User Guide

See for complete documentation including:
- Detailed player guide
- Comprehensive admin manual  
- Monte Carlo simulation tutorial
- Game rules and probability explanations
- Technical implementation details

---

## 🎲 Game Rules

### Bet Types and Payouts

| Bet Type | Numbers | Payout | Win Probability (Fair) |
|----------|---------|--------|----------------------|
| **Number** | Single (0-12) | 13:1 | 7.69% (1/13) |
| **Color** | Red or Black | 2:1 | 46.15% (6/13) |
| **Parity** | Odd or Even | 2:1 | 46.15% (6/13) |

### Color Distribution
- **Green (0)**: House number
- **Red**: 1, 3, 5, 7, 9, 11
- **Black**: 2, 4, 6, 8, 10, 12

### House Edge
- **Fair Game**: ~7.69% (equal probabilities)
- **Tweaked Game**: ~20% (green favored)

---

## 🔧 Technical Details

### Technology Stack
- **Backend**: Python 3.8+, Flask 2.3.0
- **Database**: SQLite (SQLAlchemy ORM)
- **Frontend**: HTML5, CSS3, JavaScript ES6+
- **Visualization**: Chart.js

### File Structure
```
GameSimulation/
├── app.py                  # Main application
├── game_logic.py           # Game mechanics
├── models.py               # Database models
├── init_db.py              # DB initialization
├── requirements.txt        # Dependencies
├── README.md               # This file
├── SIMULATION_GUIDE.md     # Simulation details
├── templates/              # HTML templates
├── static/                 # CSS/JS/images
└── instance/               # Database storage
```

### System Requirements
- **OS**: Windows 7+, macOS 10.12+, Linux
- **Python**: 3.8 or higher
- **RAM**: 2 GB minimum, 4 GB recommended
- **Storage**: 100 MB
- **Browser**: Chrome 90+, Firefox 88+, Edge 90+, Safari 14+

---

## 🔧 Troubleshooting

### Installation Issues

**Problem: `ModuleNotFoundError: No module named 'flask'`**
```bash
# Activate virtual environment first
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux

# Then install
pip install -r requirements.txt
```

**Problem: Port 5000 already in use**
```bash
# Option 1: Kill process on port (Windows)
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# Option 2: Use different port
# Edit app.py, change: app.run(debug=True, port=5001)
```

### Gameplay Issues

**Problem: Spin button disabled**
- Solution: Select a bet first (click number/color)
- Check balance is sufficient for bet amount

**Problem: Charts not showing**
- Enable JavaScript in browser
- Check internet connection (Chart.js CDN)
- Try different browser

### Performance Issues

**Problem: Simulation taking too long**
- Reduce simulation count (100K instead of 1M)
- Close other browser tabs
- Use faster computer
- Run in incognito mode

---

##  FAQ

**Q: Is this real gambling?**  
A: No. Virtual currency only, for educational purposes.

**Q: What's the best betting strategy?**  
A: Mathematically, no strategy beats the house edge long-term.

**Q: How accurate is the simulation?**  
A: Very accurate. 100K+ runs converge to theoretical values within 0.1%.

**Q: Can I change my password?**  
A: Currently requires database update or admin assistance.

**Q: Why do I always lose?**  
A: The house edge (green 0) ensures long-term house profit.

**Q: Can multiple users play simultaneously?**  
A: Yes, if running on a server. Localhost supports one at a time per instance.

For more questions, see [DOCUMENTATION.md](DOCUMENTATION.md).

---

##  Contributing

Contributions welcome! To contribute:

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

### Ideas for Contributions
- Multi-language support
- Advanced betting strategies
- Mobile app version
- Additional chart types
- Performance optimizations
- Unit tests
- Better UI/UX

---

##  License

**Educational Use License**

This project is for **educational purposes only**.

**Permitted:**
- ✅ Learning and academic use
- ✅ Personal modifications
- ✅ Sharing with attribution

**Not Permitted:**
- ❌ Commercial use
- ❌ Real money gambling
- ❌ Removing attribution

**Disclaimer**: Provided "as is" without warranty. Use at your own risk.

---

##  Support

**Documentation:**
- [README.md](README.md) - This guide
- [SIMULATION_GUIDE.md](SIMULATION_GUIDE.md) - Monte Carlo details


**Resources:**
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Chart.js Documentation](https://www.chartjs.org/docs/)
- [Python Documentation](https://docs.python.org/3/)

**Contact:**
- GitHub Issues: [Report bugs/request features]
- Email: [eugeneaquilino@gmail.com]

---

## 🎓 Learning Objectives

### Skills Developed
- **Programming**: Full-stack web development, Python, JavaScript
- **Mathematics**: Probability, expected value, Monte Carlo methods
- **Data Science**: Simulation, visualization, statistical analysis
- **Software Engineering**: Project structure, security, documentation

### Educational Value
This project demonstrates:
- How casinos maintain mathematical advantage
- Impact of probability manipulation
- Power of Monte Carlo simulation
- Importance of transparency in gambling

---

## 🏆 Acknowledgments

**Built with:**
- Flask (Web framework)
- Chart.js (Visualization)
- SQLAlchemy (Database ORM)
- Python (Programming language)

---

## 📊 Project Statistics

- **Lines of Code**: ~6,700
- **Files**: 15
- **Features**: 30+
- **API Endpoints**: 14
- **Database Tables**: 3
- **Max Simulations**: 10,000,000

---

**Thank you for using Roulette Game Simulation!**

Happy learning! 

---

*Last Updated: December 13, 2025*  
*Version: 1.0.0*