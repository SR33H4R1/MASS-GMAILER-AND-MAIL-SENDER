from send_mail import send_mail
from cfonts import render
import getpass

output = render('SREEHARI', colors=['red', 'green'], align='center')
print(output)

count = int(input("How many mails do you want to send : "))

# Login details

email = input("\nEnter your email id : ")

print('''\nNote: You cannot use your orginal gmail password you have to go to https://myaccount.google.com/apppasswords
          and generate app password for mail.''')

password = getpass.getpass("\n\nEnter your password : ")

# Mail details
to_email = input("\nTo whom do you want to sent mail : ")

subject = input("\nEnter the subject : ")

message = input('\nEnter the message : ')

for x in range(count):

    r = send_mail(email, password, to_email, subject, message)

    if r == 'Sending Failed':
        print("\n\n" + r)
        break

    if x == count - 1:
        print(r)
