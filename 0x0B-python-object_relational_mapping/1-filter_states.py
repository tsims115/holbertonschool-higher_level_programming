#!/usr/bin/python3
"""Module 1-filter_states.py with function"""


def only_n():

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
    numrows = cur.execute("""
        SELECT * FROM states
        WHERE name LIKE BINARY 'N%'
        ORDER BY states.id ASC
        """)
    for i in range(numrows):
        print(cur.fetchone())
    cur.close()
    db.close()


if __name__ == "__main__":
    only_n()
