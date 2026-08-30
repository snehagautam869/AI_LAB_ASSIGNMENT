
#-----------------------------    LECTURE 2 AI CLASS  ----------------------------
#variable
age = 18
gpa = 8.7
name = "AI"
print(type(age))
print(type(gpa))
print(type(name))

#Boolean
rain = True
ticket = False
print(type(rain))
print(bool("")) 
print(bool(0))
print(bool("0"))

marks = 67
print(marks >= 40)
print(marks == 56)

#assignmnet(=) vs comparison (==)
score = 90
print(score == 90)

# if ,elif, else
number = 72
if number  >= 90:
    print("Grade : A")
elif number >= 75:
    print("Grade : B")
elif number >= 60:
    print("Grade : C")
else:
    print("Grade : F")

#exercise
gpa = 7.5
attendance = 80
if(gpa <= 8.0 and attendance >= 75):
    print("Eligible for scholarship")
else:
    print("Not eligible")
