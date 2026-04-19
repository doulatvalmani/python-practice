python
#
emails = [
    "john.doe@example.com",
    "sarah.smith@example.com",
    "mike.johnson@example.com",
    "emma.wilson@example.com",
    "alex.brown@example.com"
]

for email in emails:
    print(f"Sending email to {email}")

print(f"\nTotal emails sent: {len(emails)}")
    

python
#
emails = ["a@gmail.com", "b@gmail.com", "c@gmail.com", "d@gmail.com", "e@gmail.com", "t.stark@iron.io", "n.fury@eye.net", "c.danvers@star.org", "p.parker@web.com",
  "o.octavius@arms.io", "n.osborn@goblin.net", "m.jane@mj.com", "g.stacy@ghost.org",
  "e.brock@venom.io", "c.kent@planet.com", "l.lane@news.net", "l.luthor@lex.io",
  "j.olsen@photo.org", "b.allen@speed.net", "i.west@journal.com", "h.jordan@lantern.org",
  "s.sinestro@fear.io", "b.wayne@industries.com", "a.pennyworth@manor.net", "h.dent@justice.org",
  "p.isley@ivy.com", "e.nigma@riddle.io", "s.kyle@cat.net", "j.napier@smile.com",
  "h.quinzel@arkham.org", "v.fries@cold.com", "w.cobblepot@ice.net", "r.ghul@shadow.org",
  "t.drake@robin.net", "d.grayson@night.io", "b.gordon@oracle.com", "k.kane@bat.net",
  "j.todd@red.io", "c.cain@silent.net", "s.brown@spoiler.org", "d.wayne@son.io"
"c@gmail.com", "d@gmail.com", "e@gmail.com"]
for email in emails:
    print(email)
    print("Email sent to " + email)


python
#
delivered = ["ali@gmail.com", "sara@yahoo.com", "umar@hotmail.com"]
bounced = ["bad@fake.com", "wrong@nowhere.com"]
print("Delivered emails:",delivered)
print("Bounced emails:",bounced)
print("Success rate:",len(delivered)/(len(delivered)+len(bounced))*100,"%")
