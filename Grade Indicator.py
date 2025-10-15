# Taking Your All Marks and converting your marks in Your Grade My calss Edition :) 
math = int(input("Math Marks : "))
english = int(input("English Marks : "))
nepali = int(input("Nepali Marks : "))
optMath = int(input("OPTMath Marks : "))
science = int(input("Science Marks : "))
samagic = int(input("Samagic Marks : "))
account = int(input("Account Marks : "))
#Code that print your total marks by adding -
total_marks =  math + english + nepali + optMath + science + samagic + account
print("Your Total Marks is :", total_marks )
# Converting the marks into Persentage 
persentage = total_marks % 350 * 100 
print("Your Persentage Is :", persentage )
# Converting the marks into Percentage - 
total_marks = int(input("Enter your total marks: "))  # Example: 280
max_marks = 350  # Change to reflect the maximum possible marks

# Calculate percentage
percentage = (total_marks / max_marks) * 100 
print("Your Percentage Is:", percentage)

# GPA Indicator
if 90 <= percentage <= 100:  # Corrected condition for A+
    print("Grade = A+")
elif 80 <= percentage < 90:  # Corrected condition for A
    print("Grade = A")
elif 70 <= percentage < 80:  # Corrected condition for B+
    print("Grade = B+")
else:
    print("FAILLLL")