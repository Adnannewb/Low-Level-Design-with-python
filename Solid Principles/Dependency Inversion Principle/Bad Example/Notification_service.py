from email_service import EmailService
from sms_service import SmsService

class NotificationService():
    def __init__(self):
        self.email_service=EmailService()
        self.sms_service=SmsService()
    def notify_by_email(self,message):
        self.email_service.send_email(message)
    def notify_by_sms(self,message):
        self.sms_service.send_sms(message)
ns=NotificationService()
ns.notify_by_email("Good Morning")
ns.notify_by_sms("Good Evening")