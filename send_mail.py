import smtplib
import getpass
from cfonts import render,say


output = render('SREEHARI', colors=['red', 'green'], align='center')
print(output)


def send_mail(email, passwd, send_to, subject, message):
    try:
        # Connect to google SMTP
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.ehlo()
        s.starttls()

        # Login to gmail
        s.login(email, passwd)

        # Sending message
        msg = 'Subject : ' + subject + '\n' + message
        s.sendmail(email, send_to, msg)
        s.quit()

    except:
        return 'Sending Failed'
    return f'\n\n\nSuccessfully sent mail to {send_to}.'

if __name__ == "__main__":
    # Login details
    email = input("Enter your email id : ")

    print('''\nNote: You cannot use your orginal gmail password you have to go to https://myaccount.google.com/apppasswords and generate app password for mail.''')

    password = getpass.getpass("\n\nEnter your password : ")

    # Mail details
    to_email = input("\nTo whom do you want to sent mail : ")

    subject = input("\nEnter the subject : ")

    message = input('\nEnter the message : ')

    send_mail(email, password, to_email, subject, message)
