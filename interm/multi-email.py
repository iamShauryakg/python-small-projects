import smtplib as s

ob = s.SMTP('smtp.gmail.com', 587)
ob.ehlo()
ob.starttls()

subject = "test Python "

body = 'I am shaurya Kumar gupta sending this email via python '