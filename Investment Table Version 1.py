# Write a program that will generate a compound interest table for an initial principal amount
# and a fixed annual interest  rate. The program must prompt the user to enter the amount
# initially invested, the annual rate and the number of years the principal is invested.
# Once these have been entered, the program will format a table showing
# the value of the investment and the end of each year.

principalAmount = int(input("What is your prinncipal amount inversted?: "))
interestRate = float(input("what is the annual interest rate (in percent)?: "))
yearEntered = int(input("How many years will this be invested for ?: "))

# principalAmount = principalAmount * ( 1 + interestRate/100) ** years

print("\n")
print("Year", "\t"+"\t", " Balance")

year = 1
while  year <= yearEntered :
    print(" ",year, "\t"+"\t", "${:.2f}".format(principalAmount*(1 + interestRate /100)**year))
    year += 1


