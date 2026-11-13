# Simple Shopping Cart

customer_name = input("Enter customer name: ")

product1 = input("Enter Product 1 name: ")
price1 = float(input("Enter Product 1 price: "))

product2 = input("Enter Product 2 name: ")
price2 = float(input("Enter Product 2 price: "))

product3 = input("Enter Product 3 name: ")
price3 = float(input("Enter Product 3 price: "))

subtotal = price1 + price2 + price3

if subtotal >= 5000:
    discount_rate = 0.20
elif subtotal >= 3000:
    discount_rate = 0.10
elif subtotal >= 1000:
    discount_rate = 0.05
else:
    discount_rate = 0

discount = subtotal * discount_rate
final_total = subtotal - discount

print("\n----- Shopping Summary -----")
print(f"Customer Name: {customer_name}")
print(f"Product 1: {product1} | Price: {price1}")
print(f"Product 2: {product2} | Price: {price2}")
print(f"Product 3: {product3} | Price: {price3}")
print(f"Subtotal: {subtotal}")
print(f"Discount: {discount}")
print(f"Final Total: {final_total}")