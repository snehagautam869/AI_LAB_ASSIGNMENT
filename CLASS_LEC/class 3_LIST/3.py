#---------------------------------------- LECTURE 3 -------------------------------------------------------

#LIST
score = [88,90,78,68]
mixed = ["AI",3.14,True,[1,2]]
print(score[-1])
print(mixed[3])
print(score)
print(mixed)
print("--------------------------------------------------------------")

fruits = ["apple","Banana","mango"]
print("banana" in fruits) # return bool value
print("grape" not in fruits)
print("---------------------------------------------------------------------")

enrolled = ["Asha","Raj","Meera"]
name = "Kabir"
if  name not in enrolled:
    print(name,"must registered first")
print("---------------------------------------------------------------------")

#append() method --- adding to the end
enrolled.append("Kabir")
print(enrolled)
print(len(enrolled)) #len for length finding 
print("------------------------------------------------------------")

#extend() method --- for merge two list
enrolled_1 = ["Asha","Tina"]
enrolled.extend(enrolled_1)
print(enrolled)
print(enrolled_1)
print("---------------------------------------------------------------------")

#insert(index,value) method ------ only when position matters
enrolled_1.insert(1,"barbie")
print(enrolled_1)
print("-------------------------------------------------------------------------")

#practice
cart = ["Bread","Milk"]
cart.append("eggs")
print(cart,": after append ")
cart_1 = ["butter","jam"]
cart.extend(cart_1)
print(cart,": After extended")
cart.insert(0,"coupon")
print(cart,"; insert coupon at index first")
print("Milk" in cart)
