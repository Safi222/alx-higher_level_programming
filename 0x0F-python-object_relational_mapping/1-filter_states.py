#!/usr/bin/python3
"""
    script that lists all states from the
    database hbtn_0e_0_usa starting with N
 """


if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    conn = MySQLdb.connect(host="localhost", port=3306,
                            user=argv[1], password=argv[2], db=argv[3])
    
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%'")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
