#!/usr/bin/python3
"""Module 1-filter_states.py with function"""

if __name__ == "__main__":
    import MySQLdb
    import sys
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        )
    cur = db.cursor()
    numrows = cur.execute("""
        SELECT id, name FROM states
        WHERE name LIKE 'N%'
        ORDER BY states.id ASC
        """)
    for i in range(numrows):
        print(cur.fetchone())
    cur.close()
    db.close()
