from dataclasses import dataclass

class EmailService:
    def send_email(self, recipient, subject):
        print(f"Sending email to {recipient} with subject '{subject}'")

@dataclass
class NotificationService:
    email_service: EmailService  # Injected class

    def notify(self, user_email):
        self.email_service.send_email(user_email, "Welcome to our service!")

# Dependency Injection
email_service = EmailService()
notification_service = NotificationService(email_service)

# Call method
notification_service.notify("test@example.com")
