# key, value pairs, key unique
customer = {
    "name" : "John Smith",
    "age" : 40,
    "is_verified" : True
}
print(customer)
print(customer["name"])
print(customer.get("name"))

# ask phone number
dic = {
    "1" : "One",
    "2": "Two",
    "3": "Three"
}

phone = input("Phone: ");
output = ""
for item in phone:
    output +=dic.get(item, "!")
print(output)