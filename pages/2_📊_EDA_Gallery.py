import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from load_data import get_sp500_data
import numpy as np

# Page config
st.set_page_config(page_title="EDA Gallery", page_icon="📊", layout="wide")

st.title("📊 Exploratory Data Analysis Gallery")
st.markdown("### Exploring S&P 500 Data Through 4 Different Visualization Types")

# Load data
companies_df, stocks_df, index_df = get_sp500_data()

st.markdown("---")

# ====================
# CHART 1: Exchange Performance Over Time (Line Chart)
# ====================

st.header("1️⃣ Exchange Performance: NYSE vs NASDAQ")
st.markdown("**Question:** How have the 2 US exchanges (NYSE & NASDAQ) performed against each other over time?")

# Merge stocks with companies to get exchange info
stocks_with_exchange = stocks_df.merge(companies_df[['Symbol', 'Exchange']], on='Symbol', how='left')

# Calculate average closing price by exchange and date
exchange_performance = stocks_with_exchange.groupby(['Date', 'Exchange'])['Close'].mean().reset_index()

# Filter for NYSE (NYQ) and NASDAQ (NMS) only
exchange_performance = exchange_performance[exchange_performance['Exchange'].isin(['NYQ', 'NMS'])]

# Rename for clarity
exchange_performance['Exchange'] = exchange_performance['Exchange'].map({'NYQ': 'NYSE', 'NMS': 'NASDAQ'})

# Create interactive line chart
fig1 = px.line(
    exchange_performance, 
    x='Date', 
    y='Close', 
    color='Exchange',
    title='Average Stock Price Performance: NYSE vs NASDAQ',
    labels={'Close': 'Average Closing Price ($)', 'Date': 'Date'},
    color_discrete_map={'NYSE': '#1f77b4', 'NASDAQ': '#ff7f0e'}
)

fig1.update_layout(hovermode='x unified', height=500)
st.plotly_chart(fig1, width='stretch')

# How to read this chart
with st.expander("📖 How to Read This Chart"):
    st.markdown("""
    - **X-axis:** Time (date range of the dataset)
    - **Y-axis:** Average closing price in dollars across all stocks on each exchange
    - **Lines:** Blue line represents NYSE, orange line represents NASDAQ
    - **Hover:** Move your cursor over the chart to see exact values for each date
    - **Interpretation:** Compare the trajectories to see which exchange's stocks performed better over time
    """)

# Observations
with st.expander("🔍 Key Observations"):
    st.markdown("""
    - **NASDAQ stocks show higher average prices** overall compared to NYSE stocks, likely due to the 
      concentration of high-growth technology companies on NASDAQ.
    - **Both exchanges follow similar trends**, indicating they respond to overall market conditions together.
    - **Price divergence varies over time** - the gap between exchanges widens and narrows based on 
      sector performance (tech vs traditional industries).
    - **Volatility appears similar** between both exchanges, with comparable peaks and troughs.
    """)

st.markdown("---")

# ====================
# CHART 2: Sector Performance Over Time (Multi-Line Chart)
# ====================

st.header("2️⃣ Sector Performance Trends")
st.markdown("**Question:** How have different sectors of the S&P 500 stocks performed over the last few years?")

# Merge stocks with sector information
stocks_with_sector = stocks_df.merge(companies_df[['Symbol', 'Sector']], on='Symbol', how='left')

# Calculate average closing price by sector and date
sector_performance = stocks_with_sector.groupby(['Date', 'Sector'])['Close'].mean().reset_index()

# Create interactive multi-line chart
fig2 = px.line(
    sector_performance,
    x='Date',
    y='Close',
    color='Sector',
    title='Stock Performance by Sector Over Time',
    labels={'Close': 'Average Closing Price ($)', 'Date': 'Date'}
)

fig2.update_layout(hovermode='x unified', height=600)
st.plotly_chart(fig2, width='stretch')

# Sector selector for detailed view
st.markdown("#### 🔎 Focus on Specific Sectors")
selected_sectors = st.multiselect(
    "Select sectors to compare:",
    options=sector_performance['Sector'].unique(),
    default=['Technology', 'Financial Services', 'Healthcare']
)

if selected_sectors:
    filtered_sector = sector_performance[sector_performance['Sector'].isin(selected_sectors)]
    fig2_filtered = px.line(
        filtered_sector,
        x='Date',
        y='Close',
        color='Sector',
        title=f'Comparison: {", ".join(selected_sectors)}',
        labels={'Close': 'Average Closing Price ($)', 'Date': 'Date'}
    )
    fig2_filtered.update_layout(hovermode='x unified', height=400)
    st.plotly_chart(fig2_filtered, width='stretch')

# How to read this chart
with st.expander("📖 How to Read This Chart"):
    st.markdown("""
    - **X-axis:** Time period covered by the dataset
    - **Y-axis:** Average closing price for stocks in each sector
    - **Multiple lines:** Each colored line represents a different sector (11 total sectors in S&P 500)
    - **Interactive filter:** Use the multiselect above to focus on specific sectors for clearer comparison
    - **Hover:** See exact sector names and values by hovering over the lines
    """)

# Observations
with st.expander("🔍 Key Observations"):
    st.markdown("""
    - **Technology sector shows highest growth trajectory**, with average prices significantly above other sectors,
      driven by major tech companies like Apple, Microsoft, and Google.
    - **Consumer Discretionary follows a similar upward trend** to Technology, reflecting strong consumer spending.
    - **Utilities and Real Estate show more stable, lower-volatility performance** - these defensive sectors
      have lower average prices but steadier returns.
    - **Financials experienced notable fluctuations**, particularly sensitive to interest rate changes and 
      economic cycles.
    - **Energy sector shows high volatility**, likely due to oil price fluctuations and geopolitical factors.
    - **All sectors show correlation during market-wide events** (market crashes, recoveries), but recovery 
      rates differ significantly.
    """)

st.markdown("---")

# ====================
# CHART 3: Market Cap vs Volatility (Scatter Plot) - OPTIMIZED & CLEAN
# ====================

st.header("3️⃣ Market Capitalization vs Stock Volatility")
st.markdown("**Question:** What is the relationship between a company's market capitalization and its stock price volatility?")

# Cache the volatility calculation to avoid recalculating every time
@st.cache_data
def calculate_volatility(stocks_df, companies_df):
    """
    Optimized volatility calculation using vectorized operations.
    """
    # Sort by symbol and date
    stocks_sorted = stocks_df.sort_values(['Symbol', 'Date']).copy()
    
    # Calculate returns for all stocks at once (vectorized)
    stocks_sorted['Returns'] = stocks_sorted.groupby('Symbol')['Close'].pct_change(fill_method=None)
    
    # Calculate volatility (std of returns) for each symbol
    volatility_series = stocks_sorted.groupby('Symbol')['Returns'].std()
    
    # Create dataframe with volatility
    volatility_df = volatility_series.reset_index()
    volatility_df.columns = ['Symbol', 'Volatility']
    
    # Merge with company data
    volatility_df = volatility_df.merge(
        companies_df[['Symbol', 'Marketcap', 'Sector', 'Shortname']], 
        on='Symbol', 
        how='left'
    )
    
    # Remove missing values
    volatility_df = volatility_df.dropna()
    
    return volatility_df

# Calculate volatility (cached - only runs once)
volatility_df = calculate_volatility(stocks_df, companies_df)

# Create scatter plot (no trend line - cleaner visualization)
fig3 = px.scatter(
    volatility_df,
    x='Marketcap',
    y='Volatility',
    color='Sector',
    hover_data=['Symbol', 'Shortname'],
    title='Market Capitalization vs Stock Price Volatility',
    labels={'Marketcap': 'Market Capitalization ($)', 'Volatility': 'Volatility (Std Dev of Returns)'},
    log_x=True  # Log scale for better visualization
)

fig3.update_layout(height=600, hovermode='closest')
st.plotly_chart(fig3, width='stretch')

# How to read this chart
with st.expander("📖 How to Read This Chart"):
    st.markdown("""
    - **X-axis:** Market capitalization (company size) on a logarithmic scale
    - **Y-axis:** Volatility measured as standard deviation of daily returns
    - **Points:** Each dot represents one company
    - **Colors:** Different sectors are color-coded
    - **Log scale:** X-axis uses logarithmic scale to better display the wide range of market caps
    - **Hover:** Click on points to see company name, symbol, and exact values
    """)

# Observations
with st.expander("🔍 Key Observations"):
    st.markdown("""
    - **Negative correlation exists:** Larger companies (higher market cap) tend to have lower volatility,
      suggesting they are more stable investments.
    - **Small-cap stocks show higher variability:** Smaller companies exhibit a wider range of volatility,
      from very stable to extremely volatile.
    - **Sector clustering:** Technology companies span a wide range of market caps but generally show 
      moderate volatility regardless of size.
    - **Outliers present:** Some large-cap stocks still show significant volatility, often due to 
      company-specific events or rapid growth phases.
    - **Defensive sectors like Utilities cluster in low-volatility regions** regardless of market cap.
    """)

st.markdown("---")

# ====================
# CHART 4: Revenue Growth by Sector (Box Plot)
# ====================

st.header("4️⃣ Revenue Growth Distribution Across Sectors")
st.markdown("""
**Question:** How does revenue growth vary across different sectors, and which sectors 
show the most consistent growth?

*Note: This shows the distribution of current year-over-year revenue growth rates for 
companies within each sector (snapshot data, not trends over time).*
""")

# Prepare data - remove missing revenue growth values
revenue_df = companies_df[['Sector', 'Revenuegrowth', 'Symbol', 'Shortname']].dropna()

# Create box plot
fig4 = px.box(
    revenue_df,
    x='Sector',
    y='Revenuegrowth',
    color='Sector',
    title='Revenue Growth Distribution by Sector',
    labels={'Revenuegrowth': 'Revenue Growth Rate', 'Sector': 'Sector'},
    hover_data=['Symbol', 'Shortname']
)

fig4.update_layout(
    height=600,
    xaxis_tickangle=-45,
    showlegend=False
)

fig4.update_yaxes(tickformat='.0%')  # Format as percentage

st.plotly_chart(fig4, width='stretch')

# Summary statistics
st.markdown("#### 📊 Revenue Growth Statistics by Sector")

summary_stats = revenue_df.groupby('Sector')['Revenuegrowth'].agg([
    ('Median', 'median'),
    ('Mean', 'mean'),
    ('Std Dev', 'std'),
    ('Min', 'min'),
    ('Max', 'max')
]).round(4)

summary_stats = summary_stats.sort_values('Median', ascending=False)
st.dataframe(summary_stats.style.format("{:.2%}"), width='stretch')

# How to read this chart
with st.expander("📖 How to Read This Chart"):
    st.markdown("""
    - **X-axis:** Different S&P 500 sectors
    - **Y-axis:** Revenue growth rate (as a percentage)
    - **Box:** The colored box shows the middle 50% of companies (25th to 75th percentile)
    - **Line in box:** The line inside each box is the median revenue growth for that sector
    - **Whiskers:** Extend to show the range of typical values (excluding outliers)
    - **Points beyond whiskers:** Outliers - companies with unusually high or low revenue growth
    - **Box height:** Taller boxes indicate more variability (less consistent growth) within that sector
    """)

# Observations
with st.expander("🔍 Key Observations"):
    st.markdown("""
    - **Technology and Communication Services show highest median growth rates**, reflecting the rapid 
      expansion of digital and tech-driven businesses.
    - **Consumer Discretionary shows high variability**, with a wide box indicating inconsistent growth 
      across companies - some high-flyers and some struggling retailers.
    - **Utilities and Real Estate show the most consistent growth**, with narrow boxes indicating stable, 
      predictable revenue patterns - characteristic of defensive sectors.
    - **Energy sector shows negative median growth with high volatility**, likely impacted by fluctuating 
      oil prices and transition to renewable energy.
    - **Healthcare shows moderate, consistent growth**, representing stable demand for medical services 
      and products.
    - **Outliers in multiple sectors** indicate individual companies significantly outperforming or 
      underperforming their sector peers.
    """)

st.markdown("---")

# Footer
st.caption("📊 EDA Gallery | S&P 500 Portfolio App")
st.caption("All charts are interactive - hover, zoom, and filter to explore the data!")
