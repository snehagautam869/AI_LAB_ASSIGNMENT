# functions
def greet(name):
    msg = "Hello , " + name + "!"
    return msg
result = greet("Sneha")
#result = greet("")
print(result)

def add(a: int,b : int) -> int:
    return a+b
print(add(2,3))
print(add("2","3"))

def min_max(numbers : list)->tuple:
    return min(numbers) , max(numbers)
result = min_max([4,9,7,8])
print(result)
lowest,maximum = min_max([2,4,5,6])
print(lowest)
print(maximum)

def summarize(readings : list)->tuple:
    total = sum(readings)
    average = total/len(readings)
    return total,average,max(readings)
data = [12.5,13.1,11.8,14.2,15.0]
total ,average ,peak = summarize(data)
print(f'Total: {total}, Average{average:.2f}, peak:{peak}')

#practice
def split_name(full_name: str)->tuple:
    name = full_name.split()
    first_name = name[0]
    last_name = name[-1]
    return first_name,last_name
full_name = "Sneha Gautam"
print(split_name(full_name))

#11-sep-26
def describe_pet(name:str,species:str)-> str:
    return f'{name} is a {species}'
print(describe_pet(species="cat",name="tom"))
print(describe_pet(name="tom" , species="cat"))

def describe_pet1(name:str ,species:str ="dog")-> str:
    return f'{name} is a {species}'
print(describe_pet1('rex'))
print(describe_pet1('tom','cat'))

#semantic error - mistake in code

def add_item(cart):
    cart.append('eggs')
grocery = ['bread','milk']
add_item(grocery)
print(grocery)

def replace(cart):
    cart = ['only','this']
groceries = ['bread','milk']
replace(groceries)
print(groceries)
print(replace)

def add_item_safely(cart):
    local_cart = cart[:]
    local_cart.append('eggs')
    return local_cart
groc = ['bread','milk']
new_cart = add_item_safely(groc)
print(groc)
print(new_cart)
