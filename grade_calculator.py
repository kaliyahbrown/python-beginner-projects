print("Grade Calculator")

score = float(input("Enter your grade: "))

if score >= 90:
    print("Your letter grade is A")
elif score >= 80:
    print("Your letter grade is B")
elif score >= 70:
    print("Your letter grade is C")
elif score >= 60:
    print("Your letter grade is D")
else:
    print("Your letter grade is F")