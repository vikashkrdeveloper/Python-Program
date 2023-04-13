letter='''Dear <|name|>
Greeting from ABC coding house.I am happpy to tell you about your selection
you are selected
Have a great day a head!
Thanks and regards,
Paint
Date: <|Date|> 
'''
name=input("enter your name\n")
Date=input("enter your Date\n")
letter=letter.replace("<|name|>",name)
letter=letter.replace("<|Date|>",Date)
print(letter)
