def send_email(message, recipient, sender="university.help@gmail.com"):
    if recipient and sender  is not ('@' and '.'):
     message = recipient, sender
    print (input('В ведите email: '[message ]))
print(send_email(message))