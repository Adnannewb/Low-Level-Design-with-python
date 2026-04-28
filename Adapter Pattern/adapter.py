from abc import ABC , abstractmethod
class NotificationService(ABC):
    @abstractmethod
    def send(self,to:str,subject:str,body:str):
        pass

class EmailNotificationService(NotificationService):
    def send(self,to:str,subject:str,body:str):
        print("Sending through Email Notification Service.")
        print(f"To: {to}")
        print(f"Subject: {subject}")
        print(f"Body: {body}")

class SendGridEmailService:
    def send_email(self,recipient:str,subject:str,content:str):
        print("Sending through Send Grid Email Notification Service.")
        print(f"Recipient: {recipient}")
        print(f"Subject: {subject}")
        print(f"Content: {content}")
    
class OrderService:
    def __init__(self,notification_service:NotificationService):
        self.notification_service=notification_service
    
    def create_order(self):
        self.notification_service.send("just@edu.bd","Order created","Thank you for ordering")

# e=EmailNotificationService()
# o=OrderService(e)
# o.create_order()

#this same thing i cannot done by sendrgrid email service and for that i need an adapter . 

class SendGridEmailServiceAdapter(NotificationService):
    def __init__(self,send_grid_service:SendGridEmailService):
        self.send_grid_service=send_grid_service
        
    def send(self,to:str,subject:str,body:str):
        self.send_grid_service.send_email(to,subject,body)

s=SendGridEmailService()
adapter=SendGridEmailServiceAdapter(s)
o1=OrderService(adapter)
o1.create_order()
