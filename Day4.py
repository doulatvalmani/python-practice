python
#
delivered = ["ali@gmail.com", "sara@yahoo.com", "umar@hotmail.com"]
bounced = ["bad@fake.com", "wrong@nowhere.com"]
print("Delivered emails:",delivered)
print("Bounced emails:",bounced)
print("Success rate:",len(delivered)/(len(delivered)+len(bounced))*100,"%")
