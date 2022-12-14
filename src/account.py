from curses import flash
import os
from src.util import *
from src.setup import setup
import bcrypt
from twilio.rest import Client
import random
import string
from dotenv import load_dotenv
load_dotenv()


def get_hashed_password(plain_text_password):
    return bcrypt.hashpw(plain_text_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')


def check_password(plain_text_password, hashed_password):
    return bcrypt.checkpw(plain_text_password.encode('utf-8'), hashed_password.encode('utf-8'))


def login_user(email, password):
    with DB() as db:
        if db.exec_single(("SELECT 1 FROM users WHERE email = %s;", (email, ))) == None:
            return {"success": False, "error": f"email {email} does not exist"}

        hashed_password = db.exec_single(
            ("SELECT encrypted_password FROM users WHERE email = %s;", (email, )))[0]

        password_correct = check_password(password, hashed_password)

        return {"success": password_correct}


def logout_user(user_id):
    pass


def create_user(email, password, phone_number):
    with DB() as db:
        if db.exec_single(("SELECT * FROM users WHERE email = %s", (email, ))) != None:
            return {"success": False, "error": f"email {email} already exists"}
        elif db.exec_single(("SELECT * FROM users WHERE phone_number = %s", (phone_number, ))) != None:
            return {"success": False, "error": f"phone number {phone_number} already exists"}
        hashed_password = get_hashed_password(password)
        returning_id = db.exec_single(("INSERT INTO users (email, phone_number, encrypted_password) VALUES (%s, %s, %s) Returning id",
                                       (email, phone_number, hashed_password)))
        if returning_id != None:
            return {"success": True}
        return {"success": False}


def request_verify_user(email):
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    token = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    hashed_token = get_hashed_password(token)
    with DB() as db:
        if db.exec_single(("SELECT * FROM users WHERE email = %s", (email, ))) == None:
            return {"success": False}
        db.exec_single(
            ("UPDATE users SET token = %s WHERE email = %s returning id", (hashed_token, email)))
        phone_number = db.exec_single(
            ("SELECT phone_number From users WHERE email = %s", (email, )))[0]
        message = client.messages.create(
            messaging_service_sid='MGa7584f83c0cf733ebf385a02363bbde8',
            body=f"Your auth token is {token}",
            to=phone_number
        )
    return {"success": True, "message.id": message.sid}


def verify_user(email, token):
    with DB() as db:
        if db.exec_single(("SELECT * FROM users WHERE email = %s", (email, ))) == None:
            return {"success": False}

        hashed_password = db.exec_single(
            ("SELECT token FROM users WHERE email = %s;", (email, )))[0]
        correct_token = check_password(token, hashed_password)
        if correct_token:
            db.exec_single(
                ("UPDATE users SET verified = TRUE where email = %s returning id"), (email, ))
        return {"success": correct_token}


def send_to_mobile_func(user_email, tldr_content):
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    with DB() as db:
        phone_number = db.exec_single(
            ("SELECT phone_number From users WHERE email = %s", (user_email, )))[0]
    message = client.messages.create(
        messaging_service_sid='MGa7584f83c0cf733ebf385a02363bbde8',
        body=tldr_content,
        to=phone_number
    )
    return {"success": True, "message.id": message.sid}

# if __name__ == '__main__':
#     setup()
#     Account.create("EMAIL", "PASSWORD", "PHONE_NUMBER")
#     Account.verify("EMAIL", "TOKEN")
#     Account.login("EMAIL", "PASSWORD")
#     Account.logout("USERID")
