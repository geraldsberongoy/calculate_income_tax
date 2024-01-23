# Exercise 12: Calculate income tax for the given income by adhering to the rules below

# Taxable Income	Rate (in %)
# First $10,000 	0
# Next $10,000	    10
# The remaining	    20

# Expected Output:

# For example, suppose the taxable income is 45000, and the income tax payable is

# 10000*0% + 10000*10%  + 25000*20% = $6000.

# CODE

income = 45_000

if income <= 10_000:
    total_tax = 0 * 10_000
elif income <= 20_000:
    total_tax = (income - 10_000) * 0.10
else:
    tax_below_10k = 0 * 10_000
    tax_below_20k = (20_000 - 10_000) * 0.10
    tax_above_20k = (income - 20000) * 0.20
    total_tax = tax_below_10k + tax_below_20k + tax_above_20k

print("Total tax to pay is", total_tax)

    