import psycopg2

#connect to the db
con = psycopg2.connect(
            host = "batyr.db.elephantsql.com",
            database="sgjdjzxk",
            user = "sgjdjzxk",
            password = "dmhA58uYe2KOGhyVRTooyNKGLr3SwLHc",
            port = "5432")

#cursor
cur = con.cursor()

cur.execute("create table if not exists MyTable (id INTEGER PRIMARY KEY,"
            " var1 text, var2 int, var3 int,"
            "var4 text, var11 int, var5 int, var6 int,"
            "var7 int, var8 text, var9 text, var10 int)")

cur.execute("insert into MyTable (id, var1,var2, var3,var4,var11,"
            "var5,var6,var7,var8,var9,var10) "
            "values (7, 'data', 25, 36,'a dataa',23330,43,65,2,'DaTa','da ta',88)")
cur.execute("select * from MyTable")

rows = cur.fetchall()
for r in rows:
    print (r)


con.commit()
cur.close()

con.close()