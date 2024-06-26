#!/usr/bin/python3
""" 
    script that takes in an argument and displays all values
    in the states table of hbtn_0e_0_usa
    where name matches the argument but safer from MySQL injections.
 """

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    conn = MySQLdb.connect(host="localhost", port=3306,
                            user=argv[1], password=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s", (argv[4], ))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
