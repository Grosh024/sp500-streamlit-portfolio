from load_data import load_sp500_data

# Test loading the data
companies_df, stocks_df, index_df = load_sp500_data()

print("\n📋 Companies DataFrame:")
print(companies_df.head())
print(f"\nShape: {companies_df.shape}")

print("\n📈 Stocks DataFrame:")
print(stocks_df.head())
print(f"\nShape: {stocks_df.shape}")

print("\n📉 Index DataFrame:")
print(index_df.head())
print(f"\nShape: {index_df.shape}")
