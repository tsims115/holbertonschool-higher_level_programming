#!/usr/bin/python3
"""Module 1-filter_states.py with function"""

from ast import arg
import MySQLdb
import sys


db = MySQLdb.connect(
    host="localhost",
    user=sys.argv[1],
    passwd=sys.argv[2],
    db=sys.argv[3],
    )
cur = db.cursor()
state_name = "'" + sys.argv[4] + "'"
numrows = cur.execute("""
    SELECT id, name FROM states
    WHERE name = %s ORDER BY states.id ASC
    """ %  state_name)
for i in range(numrows):
    print("(%s, '%s')" % cur.fetchone())
