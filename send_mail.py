import smtplib, ssl


port = 465
smtp_server = "smtp.gmail.com"
sender_email = "abc@gmail.com"  # enter your mail address
receiver_email = "xyz@gmail.com"  # enter receiver mail address
password = 'abcfdjhrjjk'  # password from  https://support.google.com/mail/?p=BadCredentials enter the app password
message = """this is the my message from python code"""


def send_mail():
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
        print("Email has sent successfully.")
    except Exception as e:
        print(f"an error occured : {str(e)}")


send_mail()
