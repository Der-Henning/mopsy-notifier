import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Mailer:

    def __init__(self, host, port, username, password):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.connect()

    def __del__(self):
        self.server.quit()

    def connect(self):
        self.server = smtplib.SMTP(self.host, self.port)
        self.server.starttls()
        self.server.login(self.username, self.password)

    def stay_connected(self):
        try:
            status = self.server.noop()[0]
        except:  # smtplib.SMTPServerDisconnected
            self.connect()
        # return True if status == 250 else False

    def send(self, recipient, sender, subject='', body='', type='plain'):
        message = MIMEMultipart('alternative')
        message['From'] = sender
        message['To'] = recipient
        message['Subject'] = subject
        message.attach(MIMEText(body, type))
        text = message.as_string()
        self.stay_connected()
        self.server.sendmail(sender,recipient,text)