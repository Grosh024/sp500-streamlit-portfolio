import streamlit as st
from load_data import get_sp500_data

# Page configuration
st.set_page_config(
    page_title="S&P 500 Portfolio App",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load data
companies_df, stocks_df, index_df = get_sp500_data()

# Main page content
st.title("📈 S&P 500 Stock Analysis Portfolio")
st.markdown("### Welcome to My Data Visualization Portfolio")

st.write("""
This interactive Streamlit application explores the S&P 500 stock market data, 
providing insights into exchange performance, sector trends, and company characteristics.
""")

st.markdown("---")

# Navigation instructions
st.markdown("""
## 🧭 Navigate Through the App

Use the **sidebar** to explore different sections:

- **📄 Bio** - Learn about me and my data visualization philosophy
- **📊 EDA Gallery** - Explore 4+ different chart types analyzing S&P 500 data
- **📈 Dashboard** - Interactive dashboard with filters and insights
- **🧭 Future Work** - Planned enhancements and reflections

""")

st.markdown("---")

# Dataset overview
st.markdown("## 📊 About the Dataset")

col1, col2 = st.columns([2, 1])

with col1:
    st.write("""
    **Dataset:** S&P 500 Stocks (daily updated)  
    **Source:** [Kaggle - andrewmvd/sp-500-stocks](https://www.kaggle.com/datasets/andrewmvd/sp-500-stocks)  
    **Updated:** Daily via KaggleHub API  
    
    This dataset tracks all 505 stocks from the S&P 500 index, representing 500 large companies 
    listed on U.S. stock exchanges (NYSE and NASDAQ).
    """)

with col2:
    # Key metrics
    st.metric("Total Companies", f"{len(companies_df):,}")
    st.metric("Stock Records", f"{len(stocks_df):,}")
    st.metric("Date Range", f"{stocks_df['Date'].min().strftime('%Y-%m-%d')} to {stocks_df['Date'].max().strftime('%Y-%m-%d')}")

st.markdown("---")

# Quick data preview
st.markdown("## 📋 Quick Data Preview")

tab1, tab2, tab3 = st.tabs(["Companies", "Stock Prices", "S&P 500 Index"])

with tab1:
    st.markdown("**Company Information (502 companies)**")
    st.dataframe(companies_df.head(10), use_container_width=True)
    
    # Sector breakdown
    st.markdown("**Sector Distribution:**")
    sector_counts = companies_df['Sector'].value_counts()
    st.bar_chart(sector_counts)

with tab2:
    st.markdown("**Daily Stock Price Data**")
    st.dataframe(stocks_df.head(10), use_container_width=True)
    st.caption(f"Total records: {len(stocks_df):,}")

with tab3:
    st.markdown("**S&P 500 Index Historical Data**")
    st.dataframe(index_df.head(10), use_container_width=True)
    st.line_chart(index_df.set_index('Date')['S&P500'], use_container_width=True)

st.markdown("---")

# Footer
st.caption("Created by [Your Name] | MSU Denver CS Project 2 | Fall 2025")
st.caption("Data automatically updated daily via KaggleHub")
