# test_cases.py
# Format: (function_name, args, expected_output)

test_case_1 = (
    "generate_sales_summary",
    ["problems/regional_sales_summary/input_data.csv", "outputs/output_summary.csv"],
    [
        {"Region": "South", "TotalSales": 150.0, "Rank": 1},
        {"Region": "North", "TotalSales": 140.0, "Rank": 2},
        {"Region": "East", "TotalSales": 75.0, "Rank": 3}
    ]
)

test_cases = [test_case_1]
