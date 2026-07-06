import numpy as np

months = np.array(["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                   "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])

sales = []

print("Enter the sales (in $1000) for each month:")

for month in months:
    value = int(input(f"{month}: "))
    sales.append(value)

# Convert list to NumPy array after taking all inputs
sales = np.array(sales)

print("\n---- Company Sales Analysis ----")

print("Total Sales of the year :", np.sum(sales), "$")
print("Average Monthly Sales :", np.mean(sales), "$")

print("Month with highest sales :", months[np.argmax(sales)], "-", np.max(sales), "$")
print("Month with lowest sales :", months[np.argmin(sales)], "-", np.min(sales), "$")

best_month = months[np.argmax(sales)]
worst_month = months[np.argmin(sales)]

print("Best month :", best_month)
print("Worst month :", worst_month)

above_average_months = months[sales > np.mean(sales)]
print("Months with above-average sales :", above_average_months)

below_average_months = months[sales < np.mean(sales)]
print("Months with below-average sales :", below_average_months)
