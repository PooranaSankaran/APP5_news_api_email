import smtplib, ssl

def send_email(message):
    host = 'smtp.gmail.com'
    port = 465

    user_name = 'app8flask@gmail.com'
    password = 'YOUR_GMAIL_APP_PASSWORD'

    receiver = 'app8flask#gmail.com'
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context= context) as server:
        server.login(user_name, password)
        server.sendmail(user_name,receiver,message)