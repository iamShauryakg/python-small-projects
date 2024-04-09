import smtplib as s

eml = s.SMTP('smtp.gmail.com', 587)
eml.ehlo()
eml.starttls()

# your ID and Password
eml.login(
    'email123@gmail.com',
    'Password'
)
#   """Log in on an SMTP server that requires authentication.

#         The arguments are:
#             - user:         The user name to authenticate with.
#             - password:     The password for the authentication.

#         Keyword arguments:
#             - initial_response_ok: Allow sending the RFC 4954 initial-response
#               to the AUTH command, if the authentication methods supports it.

#         If there has been no previous EHLO or HELO command this session, this
#         method tries ESMTP EHLO first.

#         This method will return normally if the authentication was successful.

#         This method may raise the following exceptions:

#          SMTPHeloError            The server didn't reply properly to
#                                   the helo greeting.
#          SMTPAuthenticationError  The server didn't accept the username/
#                                   password combination.
#          SMTPNotSupportedError    The AUTH command is not supported by the
#                                   server.
#          SMTPException            No suitable authentication method was
#                                   found.
#         """

subject = "test Python "

body = 'I am shaurya Kumar gupta sending this email via python '

message = " subject : {}\n\n{}".format(subject,body)
# all the email you want to send your email to 
listadd = [
    'iamshauryakgupta@gmail.com',
           ]
# finaly send email
eml.sendmail('hikki02003@gmail.com', listadd, message)
print("sended mail")

eml.quit