monthlyinc = int(input("Enter your monthly income: "))
totalex = int(input("Enter your total monthly expenses: "))
monthlysavings = monthlyinc - totalex
projectsav = monthlysavings * 12 + (monthlysavings * 12 * 0.05)
print(f"Your monthly savings are ${monthlysavings}")
print(f"Projectec savings after one year, with interest, is: ${projectsav}")