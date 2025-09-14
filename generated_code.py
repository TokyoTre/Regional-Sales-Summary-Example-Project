import pandas as pd

def generate_sales_summary(input_file, output_file):
    try:
        # Read input CSV file
        sales_data = pd.read_csv(input_file)

        # Convert 'Sales' column to numeric, handling errors with 'coerce' option
        sales_data['Sales'] = pd.to_numeric(sales_data['Sales'], errors='coerce')

        # Drop rows with missing or non-numeric sales data
        sales_data = sales_data.dropna(subset=['Sales'])

        # Group by region and calculate total sales
        region_sales = sales_data.groupby('Region')['Sales'].sum().reset_index()
        region_sales.columns = ['Region', 'TotalSales']  # Rename column

        # Sort regions by total sales in descending order
        region_sales = region_sales.sort_values(by='TotalSales', ascending=False)

        # Reset index after sorting
        region_sales = region_sales.reset_index(drop=True)

        # Add rank based on total sales
        region_sales['Rank'] = range(1, len(region_sales) + 1)

        # Select top 3 regions
        top_regions = region_sales.head(3)

        # Save the summary to output CSV file
        top_regions.to_csv(output_file, index=False)

        # Return top 3 regions as list of dictionaries
        return top_regions.to_dict(orient='records')

    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Test the function
output = generate_sales_summary('problems/regional_sales_summary/input_data.csv', 'outputs/output_summary.csv')
print(output)