from src.util import *
from src.setup import setup
import bcrypt
from twilio.rest import Client
import random, string

def get_hashed_password(plain_text_password):
    return bcrypt.hashpw(plain_text_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def check_password(plain_text_password, hashed_password):
    return bcrypt.checkpw(plain_text_password.encode('utf-8'), hashed_password.encode('utf-8'))


def login_user(email, password):
  with DB() as db:
    if db.exec_single(("SELECT 1 FROM users WHERE email = %s;", (email, ))) == None:
      return {"success": False, "error": f"email {email} does not exist"}

    hashed_password = db.exec_single(("SELECT encrypted_password FROM users WHERE email = %s;", (email, )))[0]

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
    db.exec_single(("INSERT INTO users (email, phone_number, encrypted_password) VALUES (%s, %s, %s)", (email, phone_number, hashed_password)))
    return {"success": True}

def request_verify_user(email):
  token = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
  with DB() as db:
    db.exec_single(("INSERT INTO users (token) VALUES (%s) WHERE email = %s;", (token, email)))

    print(db.exec_single(f"SELECT * FROM users"))
  return {"success": True}

def verify_user(email, token):
  pass

# if __name__ == '__main__':
#     setup()
#     Account.create("EMAIL", "PASSWORD", "PHONE_NUMBER")
#     Account.verify("EMAIL", "TOKEN")
#     Account.login("EMAIL", "PASSWORD")
#     Account.logout("USERID")