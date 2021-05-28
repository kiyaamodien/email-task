import smtplib

s = smtplib.SMTP('smtp.gmail.com', 587)
sender_email_id = 'kiyaamudienkhan@gmail.com'
receiver_email_id = ['jeandreross@gmail.com', 'abdullah.isaacs@gmail.com', 'jessenterblanche@gmail.com']
password = input("Enter senders email password")

s.starttls()

s.login(sender_email_id, password)

message = "Hi there, hope you are doing well\n"
message = message + "How was your task yesterday"

s.sendmail(sender_email_id, receiver_email_id, message)

s.quit()