#question1-- input validation and test data

packet = [2,6,9,8,0,5,45,0,90,23]
if packet and len(packet) >= 10:
    print("Validation passed: Processing packet ....")
else:
    print("Validation failed : Packet is empty or too short.")
print("INITIAL PACKET",packet)

#question2 -- the midldle-out swap
    
midpoint = len(packet)//2
front_half = packet[:midpoint]
back_half = packet[midpoint:]
scrambled = back_half[::-1] + front_half
print(id(packet) == id(front_half))

print("AFTER STAGE 2 SCRAMBLED",scrambled)

#question3 -- in place correction

middle_index = len(scrambled) // 2
if type(scrambled[middle_index]) is int:
    scrambled.insert(middle_index+1,"SYNC-BIT")
print("AFTER SYNC BIT INSERTION ",scrambled)

while 0 in scrambled:
    scrambled.remove(0)
print("FINAL SCRAMBLED AFTER ZERO REMOVAL" ,scrambled)

#question 4-- memory intregrity check

first , *middle ,last = scrambled
print(f"HEADER: {first}  FOOTER: {last}  BODY LENGTH: {len(middle)}")


