from src.util import *
from src.setup import setup

def tldr(user_id, pre_text, post_text, url="",version=0):
  with DB() as db:
    tldr_insert = db.exec_single(f'INSERT INTO tldr (original_text, url, tldr_text, version, user_id)' \
        f"VALUES ('{pre_text}', '{url}', '{post_text}', '{version}', '{user_id}')")
    tldr = db.exec_single('select * from tldr')
    print(tldr)
    return (tldr_insert,tldr)

def revise_tldr(text, tldr_text):
  # Revising the text
  pass

if __name__ == "__main__":
  setup()
  tldr("40e6215d-b5c6-4896-987c-f30f3678f608", "", "long_text", "tldr_text", 0)
