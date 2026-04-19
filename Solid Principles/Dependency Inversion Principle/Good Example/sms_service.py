from notification_channel import NotificationChannel
class SmsService(NotificationChannel):
    def send(self,message):
        print(f"Sending SMS: {message}")
        
        
    