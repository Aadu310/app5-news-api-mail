import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "ettaki23@gmail.com"
    password = "pthamgcotvyxrfzq"

    receiver = "adarshmanjunath88@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
