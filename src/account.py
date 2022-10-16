from src.util import *
from src.setup import setup
import bcrypt

def get_hashed_password(plain_text_password):
    return bcrypt.hashpw(plain_text_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def check_password(plain_text_password, hashed_password):
    return bcrypt.checkpw(plain_text_password.encode('utf-8'), hashed_password)


def login(email, password):
  pass
def logout(user_id):
  pass
def create(email, password, phone_number):
  with DB() as db:
    if db.exec_single(f"""SELECT 1 FROM users WHERE email = '{email}';""") != None:
      return {"success": False, "error": f"email {email} already exists"}
    elif db.exec_single(f"""SELECT 1 FROM users WHERE phone_number = '{phone_number}';""") != None:
      return {"success": False, "error": f"phone number {phone_number} already exists"}
    hashed_password = get_hashed_password(password)
    hashed_password = hashed_password.replace("$", "||||")
    db.exec_single(f"INSERT INTO users (email, phone_number, encrypted_password) VALUES ('{email}', '{phone_number}', '{hashed_password}');")
    return {"success": True}

def verify(email, token):
  pass

# if __name__ == '__main__':
#     setup()
#     Account.create("EMAIL", "PASSWORD", "PHONE_NUMBER")
#     Account.verify("EMAIL", "TOKEN")
#     Account.login("EMAIL", "PASSWORD")
#     Account.logout("USERID")