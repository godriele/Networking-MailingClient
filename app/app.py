import smtplib
# This module defines an SMPT client session object that can be used to send email to
# any internet machine with an SMTP or ESMTP listener daemon.

server = smtplib.SMTP('smtp.gmail.com', 25)

server.ehlo()
# Call this function to start the process

server.login('godriel9@gmial.com', 'Godriele10') # Test account

from email import encoders
# This module provides utility functions for encoding message payloads for secure transport
from email.mime.text import MIMEText
# This calls is used to create MIME (Multipurpose Internet Mail Extensions) objects for plain text email content
from email.mime.base import MIMEBase
# This is the base calss for creating MIME-compliant email messages with arbitraty content types
from email.mime.multipart import MIMEMultipart
# This class is used to create multipart email messages, which can contain multiple MIME parts


msg = MIMEMultipart()
msg['From'] = 'Buko Papi'
msg['To'] = 'goodydelacruz6@gmail.com'
msg['subject'] = 'Just a test'

with open('msg.txt', 'f') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))