from email.message import EmailMessage
import ssl
import smtplib
# I would recomend using gmail

def sendMail(email_rec, message):
    # put email you want to send from
    email = ""
    # password. You can generate it in your google account apppassword
    password = ""

    subjest = "Notification bridge PKL"

    em = EmailMessage()
    em['From'] = email
    em["To"] = email_rec
    em["subject"] = subjest
    em.set_content(message)

    context = ssl.create_default_context()

    # If you dont use gmail you will need to change this line 'smtp.gmail.com',465
    with smtplib.SMTP_SSL('smtp.gmail.com',465, context=context) as smtp:
        smtp.login(email,password)
        smtp.sendmail(email,email_rec,em.as_string())
