def safe_report(sent, total):
    try:
        rate = (sent / total) * 100 
        print("Success rate: " + str(rate) + "%")
    except ZeroDivisionError:
        print("No emails were sent")
safe_report(0, 0)       # total is 0 → prints "No emails were sent!"
safe_report(850, 1000)  # total is 1000 → prints "Success rate: 85.00%"
#Test it with: safe_report(0, 0) and safe_report(850, 1000)
