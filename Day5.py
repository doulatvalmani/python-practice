python
# 
def send_welcome(name, email):
    print(f"Welcome {name}!")
    print(f"Sending to: {email}")
    print("Thank you for subscribing!")
    print(f"Dear {name}, we are glad to have you with us.")

send_welcome("Ali", "ali@gmail.com")
send_welcome("Sara", "sara@yahoo.com")
send_welcome("Doulat", "doulat@gmail.com")


python
# 
def campaign_report(campaign_name, total, bounced):
    # calculate delivered
    delivered = total - bounced
    # calculate success rate
    success_rate = (delivered / total) * 100 if total > 0 else 0
    # print everything
    print(f"Campaign: {campaign_name}")
    print(f"Total: {total}")
    print(f"Bounced: {bounced}")
    print(f"Delivered: {delivered}")
    print(f"Success Rate: {success_rate:.2f}%")
    # use if/else to print status
    if success_rate >= 80:
        print("Status: Excellent")
    elif success_rate >= 60:
        print("Status: Good")
    else:
        print("Status: Needs Improvement")

# call it twice with different campaigns
campaign_report("Welcome Email", 1000, 80)
campaign_report("Black Friday", 5000, 900)

