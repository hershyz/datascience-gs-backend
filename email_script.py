# email: guidedstudybot@gmail.com
# password: guidedstudy123

from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'guidedstudybot@gmail.com'
email_password = 'zqtvigzsakuydded'
email_reciver = 'hbagalkote@gmail.com'

subject = 'Test Email'
body = 'Message sent from Python'

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_reciver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_reciver, em.as_string())