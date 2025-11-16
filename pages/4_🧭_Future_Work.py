import streamlit as st

# Page config
st.set_page_config(page_title="Future Work", page_icon="🧭", layout="wide")

st.title("🧭 Future Work & Reflections")
st.markdown("### Planned Enhancements and Project Evolution")

st.markdown("---")

# ====================
# FUTURE ENHANCEMENTS
# ====================

st.header("🚀 Planned Future Enhancements")

st.markdown("""
This project serves as a foundation for more advanced stock market analysis. Here are concrete next steps 
I plan to implement to expand functionality and provide deeper insights:
""")

# Enhancement 1
st.subheader("1. Predictive Modeling for Stock Prices")
st.markdown("""
**Goal:** Build machine learning models to forecast future stock prices.

**Implementation Plan:**
- Use time-series models (LSTM, ARIMA, or Prophet) to predict next-day closing prices
- Create lag features (previous 7, 14, 30 days) and rolling averages
- Add volatility measures and volume indicators as features
- Display predictions alongside historical data with confidence intervals
- Allow users to select stocks and forecast time horizons interactively

**Expected Impact:** Enable users to explore potential future trends based on historical patterns, 
with clear disclaimers about model limitations.
""")

# Enhancement 2
st.subheader("2. Real-Time Data Integration")
st.markdown("""
**Goal:** Replace daily batch updates with real-time or intraday stock data.

**Implementation Plan:**
- Integrate Alpha Vantage or Yahoo Finance API for live stock prices
- Add a refresh button to fetch latest market data on-demand
- Display real-time price changes with up/down indicators
- Implement WebSocket connections for streaming data updates
- Add "Last Updated" timestamp to all visualizations

**Expected Impact:** Make the dashboard more actionable for current market analysis rather than 
purely historical exploration.
""")

# Enhancement 3
st.subheader("3. Portfolio Simulation & Backtesting")
st.markdown("""
**Goal:** Allow users to simulate investment strategies and see historical performance.

**Implementation Plan:**
- Create a "Build Your Portfolio" feature where users select stocks and allocations
- Backtest portfolio performance over historical data
- Calculate metrics: total return, Sharpe ratio, max drawdown, volatility
- Compare user portfolio against S&P 500 index benchmark
- Visualize cumulative returns and risk-adjusted performance

**Expected Impact:** Transform the app from exploratory tool into a practical strategy testing platform.
""")

# Enhancement 4
st.subheader("4. Enhanced Accessibility Features")
st.markdown("""
**Goal:** Make visualizations accessible to all users, including those with visual impairments.

**Implementation Plan:**
- Conduct accessibility audit using WAVE or axe DevTools
- Implement sonification (audio representations) of price trends
- Add comprehensive alt-text for all charts with detailed descriptions
- Provide tabular data alternatives for every visualization
- Test with screen readers (NVDA, JAWS) and fix navigation issues
- Ensure WCAG 2.1 AA compliance for color contrast and keyboard navigation

**Expected Impact:** Broaden the app's usability to a wider audience and follow universal design principles.
""")

# Enhancement 5
st.subheader("5. Advanced Filtering & Comparison Tools")
st.markdown("""
**Goal:** Enable side-by-side comparison of individual stocks and custom metrics.

**Implementation Plan:**
- Add stock comparison tool (select 2-5 stocks, view metrics side-by-side)
- Create custom metric builder (users define formulas like P/E ratio, dividend yield)
- Implement saved filter presets ("My Tech Watchlist", "High Growth Stocks")
- Add export functionality (download filtered data as CSV, charts as PNG)
- Build alerts system (notify when stock hits target price or metric threshold)

**Expected Impact:** Give power users more control and customization for their specific analysis needs.
""")

st.markdown("---")

# ====================
# REFLECTION
# ====================

st.header("💭 Reflection: From Prototype to Production")

st.markdown("""
### Key Evolutions During Development:

**1. Multi-Page Architecture**
- **Initial Plan:** Simple single-page dashboard with basic charts
- **Final Implementation:** Four distinct pages (Bio, EDA Gallery, Dashboard, Future Work)
- **Reason for Change:** Separating content into pages creates a more professional portfolio structure 
  and better organizes different types of analysis.

**2. Expanded Visualization Variety**
- **Initial Plan:** Basic line charts for stock prices
- **Final Implementation:** Six different chart types (line, scatter, box plot, heatmap, area, treemap)
- **Reason for Change:** Different analytical questions require different visualizations. Adding variety 
  demonstrates broader data visualization skills and makes exploration more comprehensive.

**3. Interactive Filtering System**
- **Initial Plan:** Static visualizations from paper sketch
- **Final Implementation:** Dynamic filters (date range, sector, exchange, market cap slider)
- **Reason for Change:** Interactive filters let users explore their own questions rather than viewing 
  pre-determined analysis. This makes the dashboard more useful and engaging.

**4. Automated Data Loading**
- **Initial Plan:** Manual dataset management
- **Final Implementation:** KaggleHub API with automatic daily updates and caching
- **Reason for Change:** Automation keeps data current and demonstrates production-ready development 
  practices for portfolio projects.
""")

st.markdown("""
### Biggest Lessons Learned:

- **Paper vs. Code:** Sketching on paper helps visualize layout, but actually building reveals 
  technical constraints and better design possibilities.

- **Performance Matters:** Initial code was slow when calculating metrics for 500+ stocks. 
  Learning to use caching and vectorization improved loading times significantly.

- **User-Focused Design:** Adding "How to Read This Chart" sections and clear labels makes 
  visualizations accessible to viewers who aren't data science experts.

- **Scope Management:** Focused on core features (visualizations, filters, insights) rather than 
  adding too many complex features within the project deadline.
""")

st.markdown("""
### Biggest Lessons Learned:

- **Planning vs. Reality:** Initial sketches are starting points, not contracts. Iterative development 
  revealed better approaches and features I hadn't initially considered.

- **User Perspective:** What makes sense to me as the developer doesn't always align with what's intuitive 
  to users. Adding explainers ("How to Read This Chart") improved clarity.

- **Technical Constraints:** Not all visualizations I wanted were feasible with the available data. 
  For example, I couldn't track revenue growth over time because the dataset only includes current snapshots.

- **Balance Complexity:** More features aren't always better. I cut several ideas (stock news integration, 
  sentiment analysis) to focus on doing core functionality well within the project timeline.
""")

st.markdown("---")

# ====================
# CLOSING NOTE
# ====================

st.header("📝 Closing Thoughts")

st.markdown("""
This project demonstrates the end-to-end process of building a data visualization application: 
from dataset selection and exploratory analysis, through interactive dashboard design, to deployment 
and future planning.

The S&P 500 dataset provided a rich foundation for exploring various analytical questions through 
multiple visualization techniques. By implementing filters, KPIs, and diverse chart types, this app 
serves as both a learning tool for understanding stock market data and a professional portfolio piece 
showcasing data science and web development skills.

Moving forward, the planned enhancements will transform this from a static analysis tool into a dynamic, 
predictive platform that can support real-world investment research and education.
""")

st.markdown("---")

st.caption("🧭 Future Work & Reflections | S&P 500 Portfolio App")
st.caption("MSU Denver CS Project 2 | Fall 2025")
