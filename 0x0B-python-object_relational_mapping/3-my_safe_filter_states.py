#!/usr/bin/python3
"""Module 2-my_filter_states.py with function"""


if __name__ == "__main__":

    import MySQLdb
    import sys

    i = 0
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
        )
    cur = db.cursor()
    for c in sys.argv[4]:
        if c == "'" or c == "," or c == ";" or c == ":":
            sys.argv[4] = sys.argv[4][:i]
        i += 1
    numrows = cur.execute("""
        SELECT * FROM states
        WHERE name LIKE BINARY '{}'
        ORDER BY states.id ASC
        """.format(sys.argv[4]))
    for i in range(numrows):
        print(cur.fetchone())
    cur.close
    db.close
