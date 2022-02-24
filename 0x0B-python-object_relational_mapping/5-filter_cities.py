#!/usr/bin/python3
"""Module 5-filter_cities with main function"""

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
        SELECT cities.name FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = '{}'
        ORDER BY cities.id ASC
        """.format(sys.argv[4]))
    for i in range(numrows):
        if i == numrows - 1:
            print("%s" % cur.fetchone())
            break
        print("%s" % cur.fetchone(), end=", ")
    cur.close()
    db.close()
