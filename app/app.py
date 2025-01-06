import smtplib
# This module defines an SMPT client session object that can be used to send email to
# any internet machine with an SMTP or ESMTP listener daemon.

server = smtplib.SMTP('smtp.gmail.com', 25)

server.ehlo()
# Call this function to start the process

