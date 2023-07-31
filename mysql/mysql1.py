import pymysql

class HandleDB:
    def __init__(self):
            self.con = pymysql.connect(host="rm-uf65510iu9s529ng65o.mysql.rds.aliyuncs.com",
                      port=3306,
                      user="nutricia",
                      password="Gm859230",
                      charset="utf8")



    def find_all(self, sql):
        with self.con as cur:
            # cur=self.con.cursor()
            cur.execute(sql)
            """查询所有数据"""
            res = cur.fetchall()
            cur.close()
            return res

    def find_one(self, sql):
        with self.con as cur:
            cur = self.con.cursor()
            cur.execute(sql)
            """查询一条数据"""
            res = cur.fetchone()
            cur.close()
            return res
    def find_count(self, sql):
        with self.con as cur:
            cur = self.con.cursor()
            res = cur.execute(sql)
            """sql执行完成后，查询返回的条数"""
        return res
    # def __del__(self):
    #     """执行完成后自动关闭"""
    #     self.con.close()


if __name__ == "__main__":
    """库名.表明"""
sql = "select user_name from nutricia_sun.sys_user_info where phone = 19939421096 "
# 如果项目涉及到多个数据库，可创建多个对象时进行传参
db = HandleDB()
res = db.find_all(sql)
print(res)
