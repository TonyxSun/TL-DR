from util import *
from setup import setup

class Account():
  def login(email, password):
    pass
  def logout(user_id):
    pass
  def create(email, password, phone_number):
    pass
  def verify(email, token):
    pass

if __name__ == '__main__':
    setup()
    Account.create("EMAIL", "PASSWORD", "PHONE_NUMBER")
    Account.verify("EMAIL", "TOKEN")
    Account.login("EMAIL", "PASSWORD")
    Account.logout("USERID")