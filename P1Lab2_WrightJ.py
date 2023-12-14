"""
CTI110
P1Lab2 -Sales
WrightJ
8/31
Simple point of sales program

"""

# set up our store 
store_name = "CTI 110 Hut"
product = "shoes"
stock = 20
price = 49.99


print("Welcome to", store_name, "!")
print("What's your name?")
customer_name = input()
print("Nice to meet you,", customer_name)

# Explain product
print("Our Hot Sale today is:", product)
print("On sale for: $", price)
print("Only", stock, "remaining!")


# Take order
print("How many", product, "Wwould you like?")
# input gives us a string
# convert it to a number
# or... 
order = int(input())
# finish up 
# optional
if (order > stock):
  order = stock
  print("Sorry, we can only sell you", order)
total_price = order*price
print("So you would like")
print(order,product,"for a total of: $", total_price)
print("<y/n>",sep='')
confirm = input()
if (confirm == "y"):
  print("Shipped!")
else: 
  print("Order canceled.")
print("Will you be paying with cash or card today?")
payment = input()
print("You're all set", customer_name, "Have a great day and thank you for shopping with", store_name, "!")