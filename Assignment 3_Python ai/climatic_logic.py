"""
Assignment 2.1 - Climatic Risk Intelligence Module

Name : Sneha Gautam

This program takes temperature, humidity and wind speed.
It calculates Heat Stress Index (HSI) and tells the
safety level.
"""

# Name with default value
name = input("Enter your name: ").strip() or "Guest User"
print("Welcome,", name)

#----------------Temperature------------------
if(temp_str := input("Enter temperature (c): " ).strip()):
    try:
        temperature = float(temp_str)
    except ValueError:
        print("Safety level : unknown")
        quit()
else:
    print("Safety level:unknown")
    quit()

#---------------Humidity----------------------------
if(hum_str := input("Enter Humidity (%): ").strip()):
    try:
        humidity = float(hum_str)
    except ValueError:
        print("Safety level : unknown")
        quit()
else:
    print("Safety level : unknown")
    quit()

#-----------------------humidity cannot be negative----------
assert humidity >=0, "Telemetry error : Negative humidity"

#----------------------------Wind Speed-----------------------
if(wind_str := input("enter wind speed (km/h): ").strip()):
    try:
        wind_speed = float(wind_str)
    except ValueError:
        print("Safety level : unknown")
        quit()
else:
    print("safety level : unknown")
    quit()

#--------------------------------Calculate HSI ------------------
hsi = temperature +(0.5 * humidity)
print("\n Heat stress index =", hsi)

#--------------------------Decide Safety Level ----------------
if temperature <= 0:
    safety_level = "FREEZE ALERT"

elif hsi > 45 or (temperature > 38 and humidity > 70):
    safety_level = "CRITICAL"

elif 30 <= hsi <= 45 and wind_speed < 5:
    safety_level = "CAUTIONARY"

    # Bonus Task
    if (battery_str := input("Enter Battery Level (%): ").strip()):

        try:
            battery = float(battery_str)

        except ValueError:
            print("Invalid Battery Input")
            quit()

    else:
        print("Invalid Battery Input")
        quit()

    if battery < 20:
        safety_level = "CRITICAL"

    elif battery > 80:
        safety_level = "OPERATIONAL"

else:
    safety_level = "OPERATIONAL"

# Ternary Operator
risk = "Safe" if safety_level == "OPERATIONAL" else "Unsafe"

# ---------- Output ----------
print("\n========== RESULT ==========")
print("Name          :", name)
print("Temperature   :", temperature, "°C")
print("Humidity      :", humidity, "%")
print("Wind Speed    :", wind_speed, "km/h")
print("HSI           :", round(hsi, 2))
print("Safety Level  :", safety_level)
print("Risk          :", risk)
