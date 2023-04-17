import sqlite3

conn = sqlite3.connect('wholelist.db')

cur = conn.cursor()
# cur.execute('''UPDATE ds_users SET name = ? WHERE login = ?''', ('Sviatoslav', 'r3dbk'))
# conn.commit()
cur.execute("SELECT * FROM ds_rem;")
one_res = cur.fetchall()
print(one_res)
