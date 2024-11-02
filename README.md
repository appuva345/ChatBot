RuleBot: Train Ticket Booking Assistant

RuleBot is an interactive command-line application that assists users in booking train tickets. It guides users through the booking process, validating input, and sending OTP confirmations via email for enhanced security.

Features
User Interaction: Engages users by asking for their name and preferences, ensuring a personalized experience.
Input Validation: Checks the validity of user inputs for age, station names, and email addresses to prevent errors.
Email Confirmation: Sends an OTP (One Time Password) to the user's email for confirmation, utilizing Gmail's SMTP server for secure communication.
Exit Commands: Users can exit the interaction at any point with simple commands.

Requirements
Python 3.12+
python-dotenv for loading environment variables
smtplib for sending emails

Setup:-

Clone the repository:
git clone git@github.com:appuva345/ChatBot.git
cd rulebot

Install dependencies:
pip install python-dotenv

Create a .env file in the root directory with the following variables:
APP_PASS=your_email_password
MAIL_ID=your_email@gmail.com

Run the bot:
python ChatBot.py

Usage:-
Follow the prompts to enter your details, including age, boarding station, destination, and email.
Check your email for the OTP and enter it to confirm your ticket booking.
