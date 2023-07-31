import pymysql
from common.handle_config import conf


class HandleDB:
    def __init__(self):
        self.con = pymysql.connect(host=conf.get("mysql","host"),
                                   port=conf.getint("mysql","port"),
                                   user=conf.get("mysql","user"),
                                   password=conf.get("mysql","password"),
                                   charset="utf8")

    def find_count(self, sql):
        with self.con.cursor() as cur:
            res = cur.execute(sql)
        cur.close()
        return res

    def find_one(self, sql):
        with self.con.cursor() as cur:
            cur.execute(sql)
        res = cur.fetchone()
        cur.close()
        return res

    def find_all(self, sql):
        with self.con.cursor() as cur:
            cur.execute(sql)
        res = cur.fetchall()
        cur.close()
        return res


if __name__ == '__main__':
    db=HandleDB()
    sql="select user_name from nutricia_sun.sys_user_info where phone = 19939421096 "
    res=db.find_all(sql)
    print(res)

