import re

text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"

emails = re.findall(r"\b[A-Za-z0-9._%+-]+@domain+\.[A-Z|a-z]{2,}\b", text)


print(emails)
