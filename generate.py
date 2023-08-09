import requests
import os
import sqlite3
from datetime import datetime

urls = {
    "ABUSE.CH BOTNET C2 IOC": [0, "https://feodotracker.abuse.ch/downloads/ipblocklist.txt"],
    "ABUSE.CH BOTNET C2": [0, "https://feodotracker.abuse.ch/downloads/ipblocklist_recommended.txt"],
    "BLOCKLIST.DE": [0, "https://lists.blocklist.de/lists/all.txt"],
    "SGBOX BAD REPUTATION IP": [0, "https://download.sgbox.it/dnld/feeds/sgbox_badreputation_ip.txt"],
    "SGBOX BOTNET":  [0, "https://download.sgbox.it/dnld/feeds/sgbox_botnet.txt"],
    "TOR EXIT POINT": [0, "https://check.torproject.org/torbulkexitlist"],
    "IPC2s-30day": [1, "https://raw.githubusercontent.com/drb-ra/C2IntelFeeds/master/feeds/IPC2s-30day.csv"],
    "IPC2s": [1, "https://raw.githubusercontent.com/drb-ra/C2IntelFeeds/master/feeds/IPC2s.csv"],
    "3CORESEC": [0, "https://blacklist.3coresec.net/lists/et-open.txt"]

}

ips = []
current_path = os.path.dirname(os.path.realpath(__file__))


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
 

def create_table(conn):
    try:
        c = conn.cursor()
        sql = "DROP TABLE ips"
        c.execute(sql)
        sql_create_tbl = """ CREATE TABLE IF NOT EXISTS ips (
                                        ip text PRIMARY KEY,
                                        source text NOT NULL,
                                        note text,
                                        insert_date text
                                    ); """
        c.execute(sql_create_tbl)
    except sqlite3.Error as e:
        print(e)


def insert_data(conn):
    for site, url in urls.items():
        try:
            req = requests.get(url[1])
            if req.status_code == 200:
                for ip in req.text.split("\n"):
                    if not ip.replace("\r", "").startswith("#") and (ip.replace("\r", "") not in ips):
                        if url[0] == 0:
                            i = ip.replace("\r", "")
                            note = ""
                        else:
                            i = ip.replace("\r", "").split(",")[0]
                            note = ip.replace("\r", "").split(",")[1]

                        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        data = (i, site, note, dt)
                        sql = "INSERT INTO ips(ip, source, note, insert_date) VALUES(?, ?, ?, ?)"
                        try:
                            cur = conn.cursor()
                            cur.execute(sql, data)
                            conn.commit()
                            ips.append(i)
                        except sqlite3.Error as e:
                            print(f"IP {i} duplicato. Fonte: {site}")
        except Exception as e:
            print(f"[EXP] {e}")

    if os.path.isfile("out.txt"):
        os.remove("out.txt")

    with open("out.txt", "w") as f_out:
        for ip in ips:
            f_out.write("%s\n" % ip)



if __name__ == '__main__':
    
    conn = create_connection(f"{current_path}/db.sqlite")
    if conn is not None:
        create_table(conn)
        insert_data(conn)
    else:
        print("Errore")




























