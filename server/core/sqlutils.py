from core.log import LOGGER

import sqlite3

try:
	conn = sqlite3.connect("user.db")
	LOGGER.info("connect to database successfully")
except Exception as e:
	LOGGER.error(e)

# conn = sqlite3.connect("../user.db")
global c

def db_init():
	c = conn.cursor()
	c.execute('''CREATE TABLE IF NOT EXISTS USER_INFO
	       (ID INTEGER PRIMARY KEY autoincrement,
	       user           TEXT    NOT NULL UNIQUE,
	       pwd            TEXT    NOT NULL,
	       type           int     NOT NULL,
	       balance        REAL    NOT NULL
	       interest       REAL    );''')

	c.execute('''CREATE TABLE IF NOT EXISTS TRAN_RECORD
	       (ID INTEGER PRIMARY KEY autoincrement,
	       createtime     TimeStamp NOT NULL,
	       type           TEXT      NOT NULL,
	       amount         REAL      NOT NULL,
	       balance        REAL      NOT NULL,
	       description    TEXT      );''')

	c.execute("INSERT OR IGNORE INTO USER_INFO (user, pwd, type, balance, interest) VALUES ('root', 'toor', 0, 0, 0)")
	c.execute("INSERT OR IGNORE INTO USER_INFO (user, pwd, type, balance, interest) VALUES ('rambo', '123456', 1, 99.9, 0)")
	conn.commit()
	LOGGER.info("create test account successfully")

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
    	d[col[0]] = row[idx]
    	return d

conn.row_factory = dict_factory

global cur
cur = conn.cursor()

def query_user_info(uname):
	cur.execute("SELECT * FROM PLAYERS WHERE user=?", (uname, ))
	return cur.fetchall()

if __name__ == '__main__':
	db_init()