"""
Program : Weather-Bot 3000
Purpose : Gives simple lifestyle advice based on temperature and rain
Author  : Sneha Gautam
Date    : 03-Aug-2026
"""
#---------------------------TASK 1 -----------------------------------
# Boolean Experiments - Tests equality ( == )
42 == 42  #True 

'AI' == 'ai' #false -- As python is Case sensitive

10>5 and 2<1  #false

#--------------------------TASK 2 : Building the Weather-Bot----------------------

#take temperature input
t = input("Current temperature in degree Celsius: ")

#remove extra spaces from input
t = t.strip()

#validate input
if t.isdigit():

    #convert input into integer
    temp = int(t)

    #temperature condtions
    if temp>30:
        print("It's hot! AI suggests turning on the AC.")
    elif temp<15:
        print("Chilly! AI suggests a jacket.")
    else:
        print("Temperature is optimal. Enjoy Your day!")

    #Bonus feature
    rain_check = input("Is it raining outside?(yes/no): ")

    if "yes" in rain_check.lower() and temp < 15:
        print("AI Recommendation: Stay indoors today, and carry an umbrella.")
    elif "yes" in rain_check.lower():
        print("AI Recommendation: Carry an Umbrella.")
    else:
        print("AI Recommendation: No umbrella needed.Have a great day!")
else:
    print("Invalid input! Please enter the correct input.")
