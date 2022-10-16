from src.util import *
from src.setup import setup

def login(email, password):
  pass
def logout(user_id):
  pass
def create(email, password, phone_number):
  with DB() as db:
    return db.exec_single(f"""SELECT 1 FROM users WHERE email = "{email}";""")
def verify(email, token):
  pass

# if __name__ == '__main__':
#     setup()
#     Account.create("EMAIL", "PASSWORD", "PHONE_NUMBER")
#     Account.verify("EMAIL", "TOKEN")
#     Account.login("EMAIL", "PASSWORD")
#     Account.logout("USERID")