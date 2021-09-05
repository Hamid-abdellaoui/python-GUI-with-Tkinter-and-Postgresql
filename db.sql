-- After connecting to the database using your credentials or use the next :
/**
 
 host = "batyr.db.elephantsql.com",
 database="sgjdjzxk",
 user = "sgjdjzxk",
 password = "dmhA58uYe2KOGhyVRTooyNKGLr3SwLHc",
 port = "5432"
 
 **/
create table if not exists MyTable (
    id INTEGER PRIMARY KEY,
    var1 text,
    var2 int,
    var3 int,
    var4 text,
    var11 int,
    var5 int,
    var6 int,
    var7 int,
    var8 text,
    var9 text,
    var10 int
)
insert into
    MyTable (
        id,
        var1,
        var2,
        var3,
        var4,
        var11,
        var5,
        var6,
        var7,
        var8,
        var9,
        var10
    )
values
    (
        7,
        'data',
        25,
        36,
        'a dataa',
        23330,
        43,
        65,
        2,
        'DaTa',
        'da ta',
        88
    )
select
    *
from
    MyTable