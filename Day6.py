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
