num1 = 42 # variable declaration, initialize number
num2 = 2.3 # variable declaration, initialize number
boolean = True #variable declaration, initialize boolean
string = 'Hello World' #variable declaration, initialize string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration, initialize list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declatation, initialize dictionary
fruit = ('blueberry', 'strawberry', 'banana') #variable declaration, initialize tuple
print(type(fruit)) #access value
print(pizza_toppings[1]) #access value
pizza_toppings.append('Mushrooms') #add value
print(person['name']) #access value
person['name'] = 'George' #access value
person['eye_color'] = 'blue' #access value
print(fruit[2]) #call function, access value

if num1 > 45: #conditional if
    print("It's greater")
else:
    print("It's lower") #conditional else

if len(string) < 5: #conditional if
    print("It's a short word!")
elif len(string) > 15: #conditional else if
    print("It's a long word!")
else: #conditional else
    print("Just right!") 

for x in range(5): 
    print(x)
for x in range(2,5): 
    print(x)
for x in range(2,10,3): 
    print(x)
x = 0
while(x < 5): 
    print(x)
    x += 1

pizza_toppings.pop() #function
pizza_toppings.pop(1) #remove value 

print(person) #access value
person.pop('eye_color') #remove value
print(person) #access value

for topping in pizza_toppings: #for start
    if topping == 'Pepperoni': 
        continue #for continue
    print('After 1st if statement')
    if topping == 'Olives':
        break #for break

def print_hello_ten_times():
    for num in range(10): #function parameter
        print('Hello') #function return

print_hello_ten_times()

def print_hello_x_times(x):
    for num in range(x): #function parameter
        print('Hello') #function return

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)