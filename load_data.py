import kagglehub
import pandas as pd
import os

def load_sp500_data():
    """
    Downloads the latest S&P 500 dataset from Kaggle using kagglehub.
    Returns dataframes for companies, stocks, and index.
    """
    print("📥 Downloading latest S&P 500 data from Kaggle...")
    
    # Download latest dataset (kagglehub handles caching and updates)
    path = kagglehub.dataset_download("andrewmvd/sp-500-stocks")
    
    print(f"✅ Dataset downloaded to: {path}")
    
    # Load the three CSV files
    companies_df = pd.read_csv(os.path.join(path, "sp500_companies.csv"))
    stocks_df = pd.read_csv(os.path.join(path, "sp500_stocks.csv"))
    index_df = pd.read_csv(os.path.join(path, "sp500_index.csv"))
    
    # Convert date columns to datetime
    stocks_df['Date'] = pd.to_datetime(stocks_df['Date'])
    index_df['Date'] = pd.to_datetime(index_df['Date'])
    
    print(f"📊 Loaded {len(companies_df)} companies")
    print(f"📈 Loaded {len(stocks_df)} stock records")
    print(f"📉 Loaded {len(index_df)} index records")
    
    return companies_df, stocks_df, index_df

# Add caching for Streamlit to avoid re-downloading on every interaction
import streamlit as st

@st.cache_data(ttl=86400)  # Cache for 24 hours (86400 seconds)
def get_sp500_data():
    """
    Cached version for Streamlit.
    Re-downloads data once per day.
    """
    return load_sp500_data()
