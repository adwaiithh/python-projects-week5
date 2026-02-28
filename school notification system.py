class Notification:
    def send_message(self):
        print("Sending notification...")

class EmailNotification(Notification):
    def send_message(self):
        print("Sending notification via Email.")
        print("Email sent successfully!\n")


class SMSNotification(Notification):
    def send_message(self):
        print("Sending notification via SMS.")
        print("SMS sent successfully!\n")


class AppNotification(Notification):
    def send_message(self):
        print("Sending notification via Mobile App.")
        print("App notification delivered!\n")


def notify_user(notification):
    notification.send_message()

email = EmailNotification()
sms = SMSNotification()
app = AppNotification()

notify_user(email)
notify_user(sms)
notify_user(app)