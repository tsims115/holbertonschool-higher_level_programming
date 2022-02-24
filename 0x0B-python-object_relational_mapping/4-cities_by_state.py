#!/usr/bin/python3
"""Module 4-cities_by_state with main function"""

if __name__ == "__main__":
    import MySQLdb
    import sys
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
        )
    cur = db.cursor()
    numrows = cur.execute("""
        SELECT cities.id, cities.name, states.name FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
        """)
    for i in range(numrows):
        print(cur.fetchone())
    cur.close()
    db.close()
