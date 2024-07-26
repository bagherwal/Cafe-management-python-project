#cafe menu
menu={
    "Pasta":50,
    "Burger":60,
    "Pizza":150,
    "Coffee":40,
    "Salad":80
}
#greet
print("Welcome to our Restaurent")
print("Pizza : rs 50\nBurger : rs 60\nCoffee : rs 40\nSalad : rs 80 ")

orders_total=0

item_1=input("Enter the name of your item you want to order= ")

if item_1 in menu:
    orders_total+=menu[item_1]
    print(f'Your item {item_1} is added to your order list' )
else:
    print(f"Sorry! Ordered item {item_1} is not availavle yet!") 

another_item=input("Do you want to order another order ?(Yes/No) ")

if another_item=="Yes":
    item_2=input("Enter your second item= ")
    if item_2 in menu:
        orders_total+=menu[item_2]
        print(f'Your item {item_2} is added to your order list' ) 
    else:
        print(f"Ordered item {item_2} is not available ")
print(f"the totel amount you have to pay is {orders_total}")                