def calculate_tax(*salaries):
    try:
        taxes = list(map(lambda salary: salary * 0.10, salaries))
        print("Taxes for each month:", taxes)
        total_tax = sum(taxes)
        return total_tax
    except TypeError:
        print("Error: Only numeric values.")
    except Exception as e: 
        print("Error occurred:", e)

total = calculate_tax(50000, 60000, 45000, 70000)
print("Total Tax:", total)