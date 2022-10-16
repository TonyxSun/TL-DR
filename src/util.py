import logging
import os
import psycopg
from psycopg.errors import ProgrammingError


class DB():
    def __init__(self):
        self._connection = None

    def exec_single(self, statement):
        line = None
        vars = None
        if type(statement) is tuple:
            line, vars = tuple
        else:
            line = statement

        conn = self._connection
        try:
            with conn.cursor() as cur:
                try:
                    conn.rollback()
                    cur.execute(line, vars)
                    row = cur.fetchone()
                    conn.commit()
                    if row:
                        return row
                except Exception as e:
                    print(e)
        except Exception as e:
            print(e)
            return

    def exec_many(self, statements):
        conn = self._connection
        try:
            with conn.cursor() as cur:
                for statement in statements:
                    line = None
                    vars = None
                    if type(statement) is tuple:
                        line, vars = tuple
                    else:
                        line = statement
                    cur.execute(line, vars)
                conn.commit()
        except ProgrammingError:
            return

    def __enter__(self):
        self._connection = psycopg.connect(
            os.environ["DATABASE_URL"], application_name="$ docs_quickstart_python")
        return self

    def __exit__(self, *exc_details):
        self._connection.close()
