# Monte Carlo Simulation Guide

## Overview
The Monte Carlo Simulation feature provides a comprehensive statistical analysis tool for the Roulette game, allowing users to run thousands of simulations to understand probability distributions, expected outcomes, and risk profiles.

## Features

### 1. **Basic Configuration**
- **Number of Simulations**: Run from 100 to 10,000,000 simulations
- **Bet Amount**: Set the wagering amount per simulation
- **Bet Type**: Choose from:
  - Specific Number (13:1 payout)
  - Color (Red/Black) (2:1 payout)
  - Parity (Odd/Even) (2:1 payout)
- **Bet Value**: Select the specific value based on bet type

### 2. **Advanced Options**

#### Random Seed Control
- Enable reproducible results by setting a random seed
- Same seed = identical simulation results
- Useful for:
  - Testing strategies
  - Comparing different configurations
  - Scientific analysis

#### Custom Probability Distribution
- Adjust probability percentages for each number (0-12)
- Probabilities must total 100%
- Pre-built configurations:
  - **Equalize All**: Fair distribution (7.69% each)
  - **Favor House**: Increased probability for 0 (green)
- Only affects the simulation, not the live game

### 3. **Comprehensive Analytics**

#### Win/Loss Statistics
- Total wins and losses
- Win rate percentage
- Loss rate percentage

#### Financial Metrics
- Total amount wagered
- Total payout received
- Net profit/loss
- Return on Investment (ROI)
- Expected value per bet

#### House Edge Analysis
- House profit calculation
- House edge percentage
- Comparison with industry standards

#### Distribution Analysis
- Outcome frequency distribution (bar chart)
- Visual representation of number occurrences
- Color-coded by number type (red/black/green)

#### Cumulative Profit Tracking
- Real-time profit/loss progression chart
- Visualize bankroll volatility
- Identify winning/losing streaks
- Interactive line chart with hover details

### 4. **Actionable Insights**

The simulation automatically generates insights including:

- **ROI Analysis**: Positive or negative expected value warnings
- **House Edge Warnings**: Alerts for unfavorable configurations
- **Win Rate Commentary**: Context for high/low win frequencies
- **Volatility Assessment**: Bankroll fluctuation analysis
- **Strategic Recommendations**: Tips based on bet type and results

### 5. **Export Options**

Export simulation results in multiple formats:
- **JSON**: Complete data structure for further analysis
- **CSV**: Spreadsheet-compatible format for Excel/Google Sheets

## How to Access

1. From the login page, click **"📊 Monte Carlo Simulation"**
2. Configure your simulation parameters
3. Click **"▶ Run Simulation"**
4. Review detailed results and insights
5. Export data if needed

## Use Cases

### Strategy Testing
Test betting strategies without risking real money:
- Compare number vs. outside bets
- Analyze risk/reward ratios
- Understand long-term expectations

### Probability Education
Learn about gambling mathematics:
- House edge concepts
- Law of large numbers
- Expected value calculations
- Variance and volatility

### Game Configuration Analysis
For administrators:
- Test impact of probability adjustments
- Verify fair game settings
- Compare tweaked vs. fair distributions
- Optimize house edge

## Tips for Best Results

1. **Run Sufficient Simulations**: Use at least 10,000 runs for reliable statistics
2. **Use Seeds for Comparison**: Enable random seed when comparing configurations
3. **Analyze Volatility**: Check cumulative profit chart for bankroll requirements
4. **Read Insights**: Review actionable insights for strategic guidance
5. **Export Data**: Save results for offline analysis and record-keeping

## Technical Details

- **Random Number Generation**: Python's `random.choices()` with weighted probabilities
- **Visualization**: Chart.js for interactive graphs
- **Performance**: Optimized for up to 10 million simulations
- **Accuracy**: High-precision floating-point calculations

## Example Scenarios

### Scenario 1: Fair Game Analysis
- **Setup**: Default probabilities (7.69% each)
- **Bet**: Red color
- **Runs**: 100,000
- **Expected Result**: ~7.7% house edge, slight negative ROI

### Scenario 2: Number Bet Risk Assessment
- **Setup**: Fair probabilities
- **Bet**: Number 7
- **Runs**: 50,000
- **Expected Result**: Low win rate (~7.7%), high volatility, potential for big swings

### Scenario 3: Custom Probability Impact
- **Setup**: 15% on 0, 7.08% on others
- **Bet**: Black color
- **Runs**: 100,000
- **Expected Result**: Increased house edge, more negative player ROI

---

**Note**: Simulation results represent statistical probabilities over many trials. Individual gameplay sessions may vary significantly from simulation averages.
