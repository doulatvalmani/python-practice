python
# 
contact = {
    "name": "Doulat",
    "email": "doulat@gmail.com",
    "city": "Hyderabad",
    "goal": "AWS Freelancer"
}

print(contact["name"])
print(contact["email"])
print(contact["city"])
print(contact["goal"])

print("Hello Brothers, My name is", contact["name"], "and I am from", contact["city"], ". I am an aspiring", contact["goal"], "and my email is", contact["email"])

for key, value in contact.items():
    print(key, ":", value)



python
# 
contact = {
    "name": "Doulat",
    "email": "doulat@gmail.com",
    "city": "Hyderabad",
    "goal": "AWS Freelancer",
    "skill": "Python",
    "experience_months": 0
}

print(contact["name"])
print(contact["email"])
print(contact["city"])
print(contact["goal"])
print(contact["skill"])
print(contact["experience_months"])

print("Hello Brothers, My name is", contact["name"], "and I am from", contact["city"], ". I am an aspiring", contact["goal"], "and my email is", contact["email"])

for key, value in contact.items():
    print(key, ":", value)


python
#
contacts = [
    {"name": "Ali",  "email": "ali@gmail.com",  "subscribed": True},
    {"name": "Sara", "email": "sara@yahoo.com", "subscribed": False},
    {"name": "Umar", "email": "umar@hotmail.com","subscribed": True}
]

# now loop through and only send to subscribed contacts
# use if contact["subscribed"]:
for contact in contacts:
    if contact["subscribed"]:
        print(f"Sending to {contact['name']} at {contact['email']}") 
