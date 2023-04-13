text=input("Enter the text\n")
if("make a lot of money\n" in text):
    spam=True
elif("by now" in text):
    spam=True
elif("Click this" in text):
    spam=True
elif("suscribe this " in text):
    spam=True
else:
    spam=False
if(spam):
        print("This text is spam")
else:
       print("This text is not spam")
            
