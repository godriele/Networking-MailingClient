import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP('smtp.gmail.com', 587)
# This will create a SMTP client sessiong connecting to Gmail's SMTP server at port 587
server.ehlo() # 
server.starttls()  

server.login('godriele9@gmail.com', 'Godriele10')  # Email / Password -> Use you own to try 

msg = MIMEMultipart() # Initializes a MIMEMultipart object to create a multipart email message
# Allows adding both text and attachments

msg['From'] = 'Buko Papi'
msg['To'] = 'goodydelacruz6@gmail.com'
msg['Subject'] = 'Just a test'

with open('msg.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain')) # Attaches the plain text content to the email as a MIME text part

filename = 'lebron.webp'
with open(filename, 'rb') as attachment:
    p = MIMEBase('application', 'octet-stream')
    p.set_payload(attachment.read())

encoders.encode_base64(p) # This will make sure safe transport over email 
p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)

text = msg.as_string()
server.sendmail('godriele9@gmail.com', 'goodydelacruz6@gmail.com', text) 
# Sends the email!!
print("It worked")
server.quit()  
