score = int(input("Enter your grade: "))

if score >= 80:
    print("Grade A")
elif score >= 75 and score <= 79:
    print("Grade B+")
elif score >= 70 and score <= 74:
    print("Grade B")
elif score >= 65 and score <= 69:
    print("Grade C+")
elif score >= 60 and score <= 64:
    print("Grade C")
elif score >= 55 and score <= 59:
    print("Grade D+")
elif score >= 50 and score <= 54:
    print("Grade D")
else:
    print("Grade F Bruh")
