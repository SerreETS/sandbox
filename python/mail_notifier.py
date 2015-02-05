import smtplib

class MailNotifier(object):
    def __init__(self):
        self.email = 'serreets@gmail.com'
        self.password = 'CHANGE_ME'
        self.recipients = ['CHANGE_ME@gmail.com']
        self.server = 'smtp.gmail.com'
        self.port = 587

        session = smtplib.SMTP(self.server, self.port)
        session.ehlo()
        session.starttls()
        session.ehlo
        session.login(self.email, self.password)

        self.session = session

    def send_mail(self, subject, body):
        headers = [
            "From: " + self.email,
            "Subject: " + subject,
            "To: " + ", ".join(self.recipients),
            "MIME-Version: 1.0",
            "Content-Type: text/html"]
        headers = "\r\n".join(headers)

        self.session.sendmail(
            self.email,
            self.recipients,
            headers + "\r\n\r\n" + body)

    def send_alert_mail(self, message):
        self.send_mail('SerreETS Alert', message)
