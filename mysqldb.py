# encoding:utf-8
# !/usr/bin/python


import MySQLdb

db = MySQLdb.connect("172.31.8.8", "keystone", "watone", "keystone")
cursor = db.cursor()
# cursor.execute("SELECT VERSION()")
# data = cursor.fetchone()
# print "Database version : %s" % data

sql = "SELECT * FROM endpoint WHERE interface = 'public'"

try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        print "fname=%s,lname=%s,age=%s,sex=%s,income=%s" % \
            (fname, lname, age, sex, income)
except:
    print "Error:unable to fetch data"

db.close()
