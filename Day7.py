python
# ================================
# Bulk Email Campaign Manager
# by Doulat Valmani
# ================================

# Step 1: contact list
contacts = [
    {"name": "Ali", "email": "ali@gmail.com", "subscribed": True},
    {"name": "Sara", "email": "sara@yahoo.com", "subscribed": False},
    {"name": "Umar", "email": "umar@hotmail.com", "subscribed": True},
    {"name": "Fatima", "email": "fatima@gmail.com", "subscribed": False},
    {"name": "Ahmed", "email": "ahmed@outlook.com", "subscribed": True},
    {"name": "Zara", "email": "zara@gmail.com", "subscribed": True}
]

# Step 2: send email function
def send_email(contact):
    print(f"Sending email to {contact['name']} at {contact['email']}")

# Step 3: campaign function
def run_campaign(campaign_name, contacts):
    sent = 0
    skipped = 0
    for contact in contacts:
        if contact["subscribed"]:
            send_email(contact)
            sent += 1
        else:
            skipped += 1
    total = len(contacts)
    success_rate = (sent / total) * 100 if total > 0 else 0
    print(f"\nCampaign '{campaign_name}' completed.")
    print(f"Emails sent: {sent}")
    print(f"Emails skipped: {skipped}")
    print(f"Success rate: {success_rate:.2f}%")
    if sent > skipped:
        print("Campaign status: Successful")
    else:
        print("Campaign status: Needs improvement")

# Step 4: run it!
run_campaign("Welcome Campaign", contacts) 



