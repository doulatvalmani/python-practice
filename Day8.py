# 
import csv  # pick up the tool

# your contact list in CSV format
csv_data = """name,email,subscribed
Ali,ali@gmail.com,True
Sara,sara@yahoo.com,False
Doulat,doulat@gmail.com,True"""

# convert to dictionaries (like Day 6!)
reader = csv.DictReader(csv_data.splitlines())
sent = 0
skipped = 0
# loop through like Day 4!
for row in reader:
    if row["subscribed"] == "True":  # only print if subscribed
        print(f"Sending to: {row['name']} at {row['email']}")
        sent += 1
    else:
        skipped += 1
        
total = sent + skipped
success_rate = sent / total * 100
print(f"\nsent:{sent}")
print(f"skipped:{skipped}")
print(f"success rate: {success_rate:.2f}%")
