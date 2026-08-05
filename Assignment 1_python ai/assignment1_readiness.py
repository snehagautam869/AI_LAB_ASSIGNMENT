"""
Program : Temporal Profile Analyzer
Purpose : Computes an AI Era Readiness Score from user metadata.
Author  : Sneha Gautam
Date    : 01-07-2026
"""

import datetime
# Taking user's full name
user_fullname = input("Enter your full name: ").strip()

# Checking if name is empty
if user_fullname == "":
    print("Error: Name cannot be empty.")
    exit()

# Finding length of the name
name_length = len(user_fullname)

# Converting the name into Title Case
New_name = user_fullname.title()

# Taking user's age as input
user_age = input("Enter your current age: ")

# Checking if age contains only digits
if not user_age.isdigit():
    print("Error: Age contain only numeric digits.")
    exit()

# Convert age from string to integer
user_age = int(user_age)

# Getting the current year automatically
current_year = datetime.date.today().year

# Calculating age in the year 2045
age_in_2045 = user_age + (2045 - current_year)

# Calculating AI Readiness Score
ai_readiness_score = (name_length * 10 + age_in_2045) / 2

print("\n========== USER REPORT ==========")
print("Formatted Name :", New_name)
print("Length of name :", name_length)
print("Current Age :", user_age)
print("Age in 2045 :", age_in_2045)
print(f"AI Readiness Score : {ai_readiness_score:.2f}")

# Bonus Question

first_digit = str(age_in_2045)[0]

Bonus_task = first_digit * 3

print("Bonus task :", Bonus_task)
