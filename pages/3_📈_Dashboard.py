import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from load_data import get_sp500_data
from datetime import datetime

# Page config
st.set_page_config(page_title="Dashboard", page_icon="📈", layout="wide")

st.title("📈 Interactive S&P 500 Dashboard")
st.markdown("### Explore stock performance with dynamic filters")

# Load data
companies_df, stocks_df, index_df = get_sp500_data()

# Merge stocks with company info
stocks_with_info = stocks_df.merge(
    companies_df[['Symbol', 'Sector', 'Exchange', 'Shortname']], 
    on='Symbol', 
    how='left'
)

st.markdown("---")

# ====================
# SIDEBAR FILTERS
# ====================

st.sidebar.header("🎛️ Dashboard Filters")

# Filter 1: Date Range
st.sidebar.subheader("1. Date Range")
min_date = stocks_df['Date'].min().date()
max_date = stocks_df['Date'].max().date()

date_range = st.sidebar.date_input(
    "Select date range:",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

# Handle single date selection
if len(date_range) == 2:
    start_date, end_date = date_range
else:
    start_date = end_date = date_range[0]

# Filter 2: Sector Selection
st.sidebar.subheader("2. Sectors")
all_sectors = sorted(companies_df['Sector'].dropna().unique())
selected_sectors = st.sidebar.multiselect(
    "Select sectors to analyze:",
    options=all_sectors,
    default=all_sectors[:3]  # Default to first 3 sectors
)

# Filter 3: Exchange Selection
st.sidebar.subheader("3. Exchange")
exchange_map = {'NYQ': 'NYSE', 'NMS': 'NASDAQ'}
all_exchanges = sorted(companies_df['Exchange'].dropna().unique())
exchange_labels = [exchange_map.get(ex, ex) for ex in all_exchanges]

selected_exchange_labels = st.sidebar.multiselect(
    "Select exchanges:",
    options=exchange_labels,
    default=exchange_labels[:2]  # Default to all
)

# Map back to original exchange codes
reverse_map = {v: k for k, v in exchange_map.items()}
selected_exchanges = [reverse_map.get(label, label) for label in selected_exchange_labels]

# Filter 4: Top N Companies by Market Cap (slider)
st.sidebar.subheader("4. Company Size Filter")
top_n = st.sidebar.slider(
    "Show top N companies by market cap:",
    min_value=10,
    max_value=100,
    value=50,
    step=10
)

st.sidebar.markdown("---")
st.sidebar.caption("Adjust filters to update dashboard")

# ====================
# APPLY FILTERS
# ====================

# Filter by date
filtered_stocks = stocks_with_info[
    (stocks_with_info['Date'] >= pd.to_datetime(start_date)) & 
    (stocks_with_info['Date'] <= pd.to_datetime(end_date))
]

# Filter by sector
if selected_sectors:
    filtered_stocks = filtered_stocks[filtered_stocks['Sector'].isin(selected_sectors)]

# Filter by exchange
if selected_exchanges:
    filtered_stocks = filtered_stocks[filtered_stocks['Exchange'].isin(selected_exchanges)]

# Filter by top N market cap companies
top_companies = companies_df.nlargest(top_n, 'Marketcap')['Symbol'].tolist()
filtered_stocks = filtered_stocks[filtered_stocks['Symbol'].isin(top_companies)]

# ====================
# KEY PERFORMANCE INDICATORS (KPIs)
# ====================

st.header("📊 Key Metrics")

if len(filtered_stocks) > 0:
    # Calculate KPIs
    total_companies = filtered_stocks['Symbol'].nunique()
    avg_price = filtered_stocks['Close'].mean()
    total_volume = filtered_stocks['Volume'].sum()
    price_change = filtered_stocks.groupby('Symbol')['Close'].apply(
        lambda x: ((x.iloc[-1] - x.iloc[0]) / x.iloc[0] * 100) if len(x) > 1 else 0
    ).mean()
    
    # Display KPIs in columns
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="Companies Analyzed",
            value=f"{total_companies}",
            help="Number of unique companies in filtered data"
        )
    
    with col2:
        st.metric(
            label="Avg Stock Price",
            value=f"${avg_price:,.2f}",
            help="Average closing price across all filtered stocks"
        )
    
    with col3:
        st.metric(
            label="Total Volume Traded",
            value=f"{total_volume/1e9:.2f}B",
            help="Total trading volume in billions of shares"
        )
    
    with col4:
        st.metric(
            label="Avg Price Change",
            value=f"{price_change:+.2f}%",
            delta=f"{price_change:.2f}%",
            help="Average percentage change from start to end of selected period"
        )
    
    st.markdown("---")
    
# After KPIs section, replace visualizations:

st.header("📈 Linked Visualizations")

# ====================
# VISUALIZATION 1: Sector Correlation Heatmap (NEW)
# ====================

st.subheader("1. Sector Performance Correlation")

# Create pivot table of daily average prices by sector
sector_pivot = filtered_stocks.pivot_table(
    values='Close',
    index='Date',
    columns='Sector',
    aggfunc='mean'
)

# Calculate correlation matrix
correlation_matrix = sector_pivot.corr()

# Create heatmap
fig1 = px.imshow(
    correlation_matrix,
    text_auto='.2f',
    aspect='auto',
    title='How Do Sectors Move Together?',
    labels={'color': 'Correlation Coefficient'},
    color_continuous_scale='RdBu_r',
    zmin=-1,
    zmax=1
)

fig1.update_layout(height=500)
st.plotly_chart(fig1, width='stretch')

st.caption("💡 Values close to 1 (red) = sectors move together | Values close to -1 (blue) = sectors move oppositely | 0 (white) = no relationship")

# ====================
# VISUALIZATION 2: Trading Volume by Exchange (KEEP)
# ====================

st.subheader("2. Trading Volume Distribution by Exchange")

# Aggregate volume by exchange and date
exchange_volume = filtered_stocks.groupby(['Date', 'Exchange'])['Volume'].sum().reset_index()
exchange_volume['Exchange'] = exchange_volume['Exchange'].map(exchange_map).fillna(exchange_volume['Exchange'])

fig2 = px.area(
    exchange_volume,
    x='Date',
    y='Volume',
    color='Exchange',
    title='Trading Volume Over Time by Exchange',
    labels={'Volume': 'Total Volume', 'Date': 'Date'}
)

fig2.update_layout(hovermode='x unified', height=500)
st.plotly_chart(fig2, width='stretch')

# ====================
# VISUALIZATION 3: Market Cap Treemap (NEW)
# ====================

st.subheader("3. Market Capitalization Distribution")

# Get current market cap for filtered companies
filtered_companies = companies_df[companies_df['Symbol'].isin(filtered_stocks['Symbol'].unique())]

fig3 = px.treemap(
    filtered_companies,
    path=['Sector', 'Symbol'],
    values='Marketcap',
    color='Revenuegrowth',
    hover_data=['Shortname', 'Marketcap'],
    title='Market Cap Distribution by Sector and Company',
    color_continuous_scale='RdYlGn',
    labels={'Revenuegrowth': 'Revenue Growth (%)'}
)

fig3.update_layout(height=500)
st.plotly_chart(fig3, width='stretch')

st.caption("💡 Box size = Market Cap | Color = Revenue Growth (green = high growth, red = declining) | Click sectors to zoom in!")

st.markdown("---")
