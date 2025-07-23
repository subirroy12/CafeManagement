menu = {
    "Pizza":180,
    "Burger":50,
    "Coffee":30,
    "Tea":10,
    "Chicken Biriyani":100,
    "Pasta":50
}
chosenmenuList = ""
print("Welcome To The Resturant\n" "What Would You Like To Order?")
print("Click To Order")
print("Pizza: Rs180\n Pasta: Rs50\n Burger:Rs50\n Coffee:Rs30\n Tea:Rs10\n Chicken Biriyani:Rs100")
order_total = 0

item1 = input("Select Item: ") 
if item1 in menu:
    order_total+=menu[item1]
    print(f"Your item {item1} added to cart")
    chosenmenuList+=item1
else:
     print(f"This item {item1} is not available")
another_order = input("Do you want to place another order? (Yes/No)")
if another_order == "Yes":
     item2 = input("Select Item: ")
     if item2 in menu:
      order_total+=menu[item2]
      print(f"Your item {item2} added to cart")
      chosenmenuList+=item2
     else:
         print(f"This item {item2} is not available")
elif another_order == "No":
    print("Exit")
print(f"Your total Order: {chosenmenuList}={order_total}")