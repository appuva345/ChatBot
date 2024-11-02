import random
import re
from dotenv import load_dotenv
import os

load_dotenv()

secret_key = os.getenv("APP_PASS")
email_s = os.getenv("MAIL_ID")
print(secret_key)


class TicketBookingBot:
    negative_responses = ("no", "nah", "not really", "nope", "not today", "bye")
    exit_commands = ("quit", "exit", "stop", "goodbye", "see you later", "later")

    def start_booking_process(self):
        user_name = input("🌟 Welcome! Could you please tell me your name?\n")
        self.check_exit_command(user_name)
        proceed = input(
            f"😊 Nice to meet you, {user_name}! Are you interested in booking a train ticket today? (yes/no)\n")
        self.check_exit_command(proceed)
        self.confirm_booking()

    def confirm_booking(self):
        user_age = input("🎉 Great! First, can I know your age?\n")
        if user_age in self.negative_responses or user_age in self.exit_commands:
            print("👋 No worries! Have a lovely day!")
            exit()
        if not user_age.isdigit():
            print("🤔 Hmm, that doesn't look like a valid age. Could you try again?")
            self.confirm_booking()
        elif int(user_age) < 18:
            print("🚫 I'm sorry, but you must be at least 18 years old to book a ticket.")
        else:
            print("👍 Awesome! Let's get started with your booking.")
            self.get_departure_location()

    def get_departure_location(self):
        departure = input("🚉 Where will you be boarding from? Please share the station name:\n").lower()
        self.check_exit_command(departure)
        if not departure.isalpha():
            print("❌ That doesn't seem right. Please enter a valid station name using letters only.")
            self.get_departure_location()
        else:
            print(f"🌍 Fantastic! You will be boarding from {departure.title()}.")
            self.get_destination(departure)

    def get_destination(self, departure):
        destination = input("🌈 Now, where would you like to travel to?\n").lower()
        self.check_exit_command(destination)
        if not destination.isalpha():
            self.get_destination(departure)
        else:
            if destination == departure:
                print("⚠️ It looks like you've chosen the same station for departure and destination. Let's try again.")
                self.get_destination(departure)
            else:
                print(f"🚄 Perfect! You're traveling from {departure.title()} to {destination.title()}.")
                self.get_confirmation_email()

    def get_confirmation_email(self):
        email_input = input("📧 To confirm your booking, please enter your email address:\n")
        self.check_exit_command(email_input)

        email_regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
        if re.match(email_regex, email_input):
            print(f"👍 Thank you! We'll send the confirmation to {email_input}.")
            self.generate_otp(email_input)
        else:
            print(f"❌ Oops! The email '{email_input}' seems to be invalid. Let’s try that again.")
            self.get_confirmation_email()

    def generate_otp(self, email):
        import smtplib
        from email.mime.text import MIMEText

        subject = "🚀 Your Train Ticket Confirmation"
        otp_code = random.randint(1000, 9999)
        body = f"Hello! Your OTP for ticket confirmation is {otp_code}. Please enter this code to verify your email."
        sender_email = email_s
        recipient_email = email
        password = secret_key

        message = MIMEText(body)
        message['Subject'] = subject
        message['From'] = sender_email
        message['To'] = recipient_email

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, recipient_email, message.as_string())

            print("📬 An OTP has been sent to your email! Please check your inbox.")

        self.verify_otp(otp_code)

    def verify_otp(self, actual_otp):
        user_otp = input("🔑 Please enter the OTP you received:\n")
        if user_otp == str(actual_otp):
            print("✅ Verification successful! Your ticket will be confirmed shortly.")
        else:
            print("❌ Hmm, that OTP doesn't match. Let's try again.")
            retry_otp = input("🔄 Would you like to re-enter the OTP? (yes/no)\n").lower()
            if retry_otp in ("yes", "y"):
                self.verify_otp(actual_otp)
            else:
                print("👋 No problem! If you need help later, just let me know. Have a great day!")
                exit()

    def check_exit_command(self, user_input):
        if user_input in self.exit_commands or user_input in self.negative_responses:
            print("👋 Thank you for visiting! Take care!")
            exit()


if __name__ == "__main__":
    bot = TicketBookingBot()
    bot.start_booking_process()
