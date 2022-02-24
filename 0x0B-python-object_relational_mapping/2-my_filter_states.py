#!/usr/bin/python3
"""Module 2-my_filter_states.py with function"""


if __name__ == "__main__":

    import MySQLdb
    import sys

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
        )
    cur = db.cursor()
    state_name = "'" + sys.argv[4] + "'"
    numrows = cur.execute("""
        SELECT id, name FROM states
        WHERE name = %s ORDER BY states.id ASC
        """ % state_name)
    for i in range(numrows):
        print(cur.fetchone())
    cur.close
    db.close
