from notification_service import NotificationService
from email_service import EmailService
from sms_service import SmsService
from whatsapp_service import WhatsappService


es=EmailService()
ns=NotificationService(es)
ns.notify("Hi")

ss=SmsService()
ns1=NotificationService(ss)
ns1.notify("Hola")

ws=WhatsappService()
ns2=NotificationService(ws)
ns2.notify("Konnichiwa")