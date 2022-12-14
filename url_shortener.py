import pyshorteners

current_link = input("Enter link: ")
s = pyshorteners.Shortener()
short_link = s.tinyurl.short(current_link)
print("Shortened Link:",short_link)

# print(s.tinyurl.expand(short_link)) for expanded link
