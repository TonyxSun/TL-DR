from util import *

from dotenv import load_dotenv
load_dotenv()

setup_state = False

def setup():
  """
  Should be called only ONCE
  """

  global setup_state
  if setup_state:
    raise "Setup Already Done"
  with DB() as db:
    db.exec_many([
      'DROP TABLE IF EXISTS tldr',
      'DROP TABLE IF EXISTS users',
      """
      CREATE TABLE IF NOT EXISTS users (
        id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
        email TEXT NOT NULL,
        creation_time TIMESTAMP NOT NULL DEFAULT now(),
        phone_number TEXT NOT NULL,
        verified BOOLEAN DEFAULT FALSE,
        encrypted_password TEXT NOT NULL,
        password_salt TEXT NOT NULL
      )
      """,
      """
      CREATE TABLE IF NOT EXISTS tldr (
        id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
        original_text TEXT NOT NULL,
        creation_time TIMESTAMP NOT NULL DEFAULT now(),
        url TEXT NOT NULL,
        tldr_text TEXT NOT NULL,
        version INTEGER NOT NULL DEFAULT 0,
        user_id UUID,
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
      )
      """
    ])
    setup_state = True