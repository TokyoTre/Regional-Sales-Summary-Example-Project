import csv

def generate_sales_summary(input_file='problems/regional_sales_summary/input_data.csv', output_file='outputs/output_summary.csv'):
    sales_data = []

    # Step 1: Read input CSV file
    with open(input_file, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            sales_data.append(row)

    # Step 2: Process sales data and calculate total sales for each row
    for sale in sales_data:
        try:
            units_sold = int(sale.get('UnitsSold', 0))
            unit_price = float(sale.get('UnitPrice', 0))
            total_sales = units_sold * unit_price
            sale['TotalSales'] = total_sales
        except (KeyError, ValueError):
            sale['TotalSales'] = None

    # Step 3: Aggregate total sales by region
    total_sales_by_region = {}
    for sale in sales_data:
        region = sale.get('Region')
        total_sales = sale.get('TotalSales')
        if region and total_sales:
            total_sales_by_region[region] = total_sales_by_region.get(region, 0) + total_sales

    # Step 4: Rank regions from highest to lowest total sales
    sorted_regions = sorted(total_sales_by_region.items(), key=lambda x: x[1], reverse=True)

    # Step 5: Select the top 3 regions
    top_regions = sorted_regions[:3]

    # Step 6: Write output to output file
    with open(output_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['Region', 'TotalSales', 'Rank'])
        writer.writeheader()
        for idx, (region, total_sales) in enumerate(top_regions, start=1):
            writer.writerow({'Region': region, 'TotalSales': total_sales, 'Rank': idx})

    # Step 7: Return the list of dictionaries containing the top 3 regions
    return [{'Region': region, 'TotalSales': total_sales, 'Rank': idx} for idx, (region, total_sales) in enumerate(top_regions, start=1)]

# Call the function and store the top 3 regions data
top_regions_data = generate_sales_summary()

# Print the top 3 regions data
print(top_regions_data)