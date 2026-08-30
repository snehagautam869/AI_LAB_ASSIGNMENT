#--------------------------------------LECTURE 3---------------------------------------------------

#LOOPS --- WHILE LOOP

count = 1
while count <=5:
    print(count)
    count += 1
print("Done!")
print("---------------------------------------------------------------------------")

#for loop

cats = ["tom","whiskers","luna"]
for cat in cats:
    print(cat, "says meow")
for letters in "AI":
    print(letters)
print("------------------------------------------------------------------------------")

#range
for i in range(5):
    print(i, "Hii!")

#exclude last value as in slicing we do
for day in range(1,5):
    print("DAY" ,day)
print("--------------------------------------------------------------------------------")

#BREAK
for num in range(1,5):
    if num == 3:
        break
    print(num)
print("------------------------------------------------------------------------------------")

#COMTINUE
for no in range(1,6):
    if no == 4:
        continue
    print(no)
print("--------------------------------------------------------------------------------------")

#LOOP Else - only runs if loop finish normally without break
for index in [2,4,6,8]:
    if index % 2 != 0:
        break
else:
    print("ALL NUM ARE EVEN ....")
print("-----------------------------------------------------------------------------------")

#Searching with break
enroll = ["asha","baby","tina","raj"]
target = "tina"
for name in enroll:
    if name == target:
        print("Target found")
        break
else:
    print("Target not found !")
print("------------------------------------------------------------------------------------------")

#practice ques
Number = [4,9,15,22,7,3,18]
for num in Number:
    if(num%2 == 0):
        print(num)

for num in Number:
    if(num > 20):
        print("break executes ")
        break
else:
    print("There is no such greater number more than 20")

count = 5
while(count>=1):
    print("countdown!")
    count = count -1

for i in range (0,31,3):
    print(i)
    
