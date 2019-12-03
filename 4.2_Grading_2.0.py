'''
GRADING 2.0
-------------------
Copy your Grading 1.0 program and modify it to also print out the letter grade depending on the numerical grade.
If they fail, tell them to "Transfer to Johnston!"
'''

print()
print("Welcome to Peggy's Grade Calculator")
print()
sg = float(input("What is your semester grade percentage?"))
fe = float(input("What is your final exam grade percentage?"))
ew = float(input("What is your exam worth?"))
ew = ew/100
grade = sg*(1-ew) + fe*(ew)
print()

if grade >= 93.00:
    print("Your grade is:", total, "(A)")
elif grade >= 90.00:
    print("Your grade is:", total, "(A-)")
elif grade >= 87.00:
    print("Your grade is:", total, "(B+)")
elif grade >= 83.00:
    print("Your grade is:", total, "(B)")
elif grade >= 80.00:
    print("Your grade is:", total, "(B-)")
elif grade >= 77.00:
    print("Your grade is:", total, "(C+)")
elif grade >= 73.00:
    print("Your grade is:", total, "(C)")
elif grade >= 70.00:
    print("Your grade is:", total, "(C-)")
elif grade >= 67.00:
    print("Your grade is:", grade, "(D+)")
elif grade >= 60.00:
    print("Your grade is:", grade, "(D)")
elif grade >= 0.00:
    print("Your final grade is:", grade, "(F)")
    print("Transfer to Johnston!")
