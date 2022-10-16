from src.util import *
from src.setup import setup

def check_version(user_id, text):
  # return 0 if not in table, otherwise return the newest version number
  with DB() as db:
    res = db.exec_single(("SELECT * FROM tldr WHERE (url = %s or original_text = %s) and (user_id  = %s)", (text, text, user_id)))
    if res != None:
      return 1
  return 0

def tldr(user_id, text, tldr_text,  sentiment, neg, pos, neu, version, url=""):
  with DB() as db:
    version = check_version(user_id, text)
    users = db.exec_single('select * from users')
    print(users)
    tldr_insert = db.exec_single(("INSERT INTO tldr (original_text, url, tldr_text, sentiment, negativeVal, positiveVal, neutralVal, version, user_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (text, url, tldr_text, sentiment, neg, pos, neu, version, user_id)))
    tldr = db.exec_single('select * from tldr')
    print(tldr)
    return {'success':True}

def fetch_tldr(user_id, text, version):
  with DB() as db:
    res = db.exec_single(("SELECT tldr_text FROM tldr WHERE (url = %s or original_text = %s) and (user_id  = %s) and version = %s", (text, text, user_id, version)))
    print(res)

# def revise_tldr(user_id, text, tldr_text, url="",version=1):
#   with DB() as db:
#     tldr_reinsert = db.exec_single(("INSERT INTO tldr (original_text, url, tldr_text, version, user_id) VALUES (%s, %s, %s, %s, %s)", (text, url, tldr_text, version, user_id)))
#     tldr = db.exec_single('select * from tldr')
#     print(tldr)
#     return (tldr_reinsert,tldr)

if __name__ == "__main__":
  # setup()
  tldr("40e6215d-b5c6-4896-987c-f30f3678f608", "", "long_text", "tldr_text", 0)
