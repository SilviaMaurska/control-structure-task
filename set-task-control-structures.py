# calculate cost of lawn cutting program 

# customer name information
customer_first_name = input("Please enter your first name:\n ")
customer_second_name = input("Please enter your second name:\n")


# customer address information
customer_house_number = (input("Please enter your house number:\n"))
customer_street = input("Please enter your street name:\n")
customer_postcode = input("Please enter your postcode:\n")

# concatonates customer address information into one string with commas 
customer_address = customer_house_number + ' , ' + customer_street + ' , ' + customer_postcode 


# customer phone number information and length check 
customer_number = (input("Please enter phone number:\n"))
# checks length of number is 11 
while len(customer_number) <= 10 or len(customer_number) >= 12:
    print("incorrect phone number length")
    customer_number = int(input("Please enter phone number:\n"))


# customer lawn information 

# input of customer lawn length 
lawn_length = float(input("Please enter length of lawn in meters:\n"))
# checks lawn width is within range of 2 - 50 meters 
while lawn_length < 2 or lawn_length > 50:
    print("not suitable length")
    lawn_length = float(input("Please enter length of lawn in meters:\n"))

# input of customer lawn width 
lawn_width = float(input("Please enter width of lawn in meters:\n"))
# checks lawn width is within range of 2 - 30 meters 
while lawn_width <= 2 or lawn_width >= 30:
    print("Not suitable width")
    lawn_width = float(input("Please enter width of lawn in meters:\n"))


# calculate lawn area ( width x length )
# round to 2 decimal points 

lawn_area = float(round(lawn_length * lawn_width,2))

# lawn care products 

luxury = 1.15
standard = 0.80 
economy = 0.45 

# Choose care products from multiple choices

product_choice = input("Please select from the following products (1, 2 or 3):\n 1. Luxury \n 2. Standard \n 3.Economy:\n")

# assign choice of product to price 
if product_choice == "1":
    product = luxury
    # calculate product cost (product x lawn area)
    product_cost = float(round(product * lawn_area,2))
elif product_choice == "2":
    product = standard
    # calculate product cost (product x lawn area)
    product_cost = float(round(product * lawn_area,2))
else:
    product = economy
    # calculate product cost (product x lawn area)
    product_cost = float(round(product * lawn_area,2))


# calculate cost of labour 

cost_of_labour = float(round(lawn_area * 0.5,2)) 

# calculate total cost (labour + product cost )

total_cost = float(round(cost_of_labour + product_cost,2))

# calculate VAT of total cost (20% of total cost = VAT)

vat = float(round(total_cost * 0.20,2)) 

# calculate final cost (final cost + VAT )

final_cost = float(round(total_cost + vat,2)) 

# print out itemised bill : 

print(f"Itemised bill: \n First name: {customer_first_name} \n Surname: {customer_second_name} \n Customer number: {customer_number} \n customer_address = {customer_address} \n Total lawn area: {lawn_area} \n Cost of Labour: {cost_of_labour} \n Cost of Lawn Care: {product_cost} \n Total cost (not including VAT): {total_cost} \n Total cost (including VAT): {final_cost}")




