#!/usr/bin/env python

import MySQLdb

def main():
    # Open database connection
    db = MySQLdb.connect("localhost","root","","wikicoding_db" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    sql = "SELECT * FROM wiki_language ORDER BY language_displayname ASC"

    cursor.execute(sql)

    results = cursor.fetchall()

    s = ""
    fieldlens = [30, 38]

    for row in results:
      lang_di = row[0]
      lang_de = row[1]
      lang = row[2]
      #s += "[[%s:Hello_World|%s]], " % (lang, lang_di)
      #s += "%s%s%s%s\n\n" % (lang_di, '.' * (fieldlens[0]-len(lang_di)), lang, '.' * (fieldlens[1]-len(lang)))
      s += "| %s | %s | %s |\n" % (lang_di, lang, "")

    print(s)

    db.close()


if __name__ == "__main__":
    main()
