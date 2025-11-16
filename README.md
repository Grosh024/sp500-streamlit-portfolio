# 📈 S&P 500 Stock Analysis Portfolio

Interactive Streamlit portfolio app analyzing S&P 500 stock data with exploratory data analysis, interactive dashboards, and actionable insights.

**MSU Denver | CS-39AE | Project 2 | Fall 2025**

---

## 👤 Contact Information

**Name:** Nathan Groshek  
**Email:** [ngroshek@msudenver.edu]
**GitHub:** [github.com/Grosh024](https://github.com/Grosh024)

---

## 🚀 Live Application

**Streamlit App URL:** [Coming Soon - Will be deployed to Streamlit Cloud]

---

## 🧭 App Navigation Overview

This multi-page Streamlit application includes four main sections:

### 📄 **Bio Page**
- Professional summary and background
- Technical skills and tools
- Data visualization philosophy
- Contact information and links

### 📊 **EDA Gallery**
- Four different visualization types exploring S&P 500 data:
  1. **Line Chart:** NYSE vs NASDAQ exchange performance comparison over time
  2. **Multi-Line Chart:** Sector performance trends with interactive filtering
  3. **Scatter Plot:** Market capitalization vs stock price volatility analysis
  4. **Box Plot:** Revenue growth distribution across sectors
- Each chart includes "How to Read This Chart" explainers and key observations

### 📈 **Dashboard**
- **Interactive Filters:**
  - Date range selector
  - Multi-select sector filter
  - Exchange selector (NYSE/NASDAQ)
  - Top N companies slider (by market cap)
- **Key Performance Indicators (KPIs):**
  - Total companies analyzed
  - Average stock price
  - Total trading volume
  - Average price change
- **Linked Visualizations:**
  - Sector correlation heatmap
  - Trading volume by exchange (area chart)
  - Market cap distribution treemap
- **Dynamic Insights:** Updates based on selected filters

### 🧭 **Future Work**
- Five planned enhancements (predictive modeling, real-time data, portfolio simulation, accessibility, advanced filtering)
- Reflection on project evolution from prototype to production

---

## 📊 Dataset Information

**Dataset Name:** S&P 500 Stocks (daily updated)  
**Source:** [Kaggle - andrewmvd/sp-500-stocks](https://www.kaggle.com/datasets/andrewmvd/sp-500-stocks)  
**Update Frequency:** Daily (automated via KaggleHub API)  
**License:** CC0 Public Domain

### Dataset Contents:
- **sp500_companies.csv:** 502 companies with sector, exchange, market cap, revenue growth, and financial metrics
- **sp500_stocks.csv:** Historical daily stock prices (Open, High, Low, Close, Volume) for all S&P 500 stocks
- **sp500_index.csv:** Historical S&P 500 index values over time

### Number of Records:
- **Companies:** 502 unique S&P 500 companies
- **Stock Records:** 600,000+ daily price records
- **Date Range:** February 2013 - Present (updated daily)

### Data Preprocessing:
- Date columns converted to `datetime` format for time-series analysis
- Missing values in revenue growth handled via `.dropna()` for box plot analysis
- Exchange codes mapped to readable names (NYQ → NYSE, NMS → NASDAQ)
- Volatility calculated as standard deviation of daily returns using vectorized operations
- Outliers retained in visualizations to show full data distribution

### Ethics Note:
This dataset represents historical stock market data aggregated from public financial exchanges. The data reflects market valuations and trading activity, which can be influenced by various factors including economic conditions, company performance, investor sentiment, and systemic biases in financial markets. 

**Limitations:**
- Past performance does not guarantee future results
- Data may not capture all market events or external factors affecting stock prices
- Analysis should not be used as the sole basis for investment decisions
- Market data may reflect existing economic inequalities and access disparities

---

## 🛠️ Requirements

All dependencies are listed in `requirements.txt`:


---

## 🎨 Features & Highlights

### Accessibility & UDL Compliance:
- ✅ Color-blind-safe palettes (Plotly default and RdBu)
- ✅ Sufficient color contrast throughout
- ✅ Clear axis labels and legends on all charts
- ✅ "How to Read This Chart" explainers for each visualization
- ✅ Alt-text recommendations in code comments
- ✅ Ethics note addressing data limitations

### Technical Highlights:
- ✅ Automated daily data updates via KaggleHub API
- ✅ Performance optimization with `@st.cache_data` decorators
- ✅ Vectorized pandas operations for fast calculations
- ✅ Interactive Plotly charts with hover details and zoom
- ✅ Responsive layout using Streamlit columns and containers
- ✅ Clean, modular code structure with reusable functions

### Interactive Elements:
- ✅ Multi-dimensional filtering (date, sector, exchange, market cap)
- ✅ Dynamic KPIs that update with filters
- ✅ Linked visualizations responding to user input
- ✅ Expandable sections for detailed explanations
- ✅ Drill-down capabilities in treemap visualization

---

## 🤖 AI Assistance Acknowledgment

This project was developed with assistance from AI tools (Perplexity AI) for:
- Code optimization and debugging
- Visualization design suggestions
- Documentation structure and clarity
- Best practices for Streamlit development

All final code implementation, data analysis, and design decisions were made by the project author.

---

## 📝 License

This project is created for educational purposes as part of MSU Denver coursework.

Dataset License: CC0 Public Domain (Kaggle) 

---

**Last Updated:** November 16, 2025
