import tkinter as tk
import tkinter.font as tkFont

import psycopg2


def supprimer(id):
    conn = psycopg2.connect(host = "batyr.db.elephantsql.com",
            database="sgjdjzxk",
            user = "sgjdjzxk",
            password = "dmhA58uYe2KOGhyVRTooyNKGLr3SwLHc",
            port = "5432")
    cursor = conn.cursor()
    query = '''DELETE from MyTable where id=%s'''
    cursor.execute(query, (id,))
    conn.commit()
    conn.close()
    display_MyTable()
    print("SUPPRIMER")

def newindow(root):
        #setting title
        root.title("Modification")
        #setting window size
        width=262
        height=574
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_626=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_626["font"] = ft
        GLabel_626["fg"] = "#333333"
        GLabel_626["justify"] = "center"
        GLabel_626["text"] = "id"
        GLabel_626.place(x=30,y=50,width=70,height=25)

        GLabel_51=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_51["font"] = ft
        GLabel_51["fg"] = "#333333"
        GLabel_51["justify"] = "center"
        GLabel_51["text"] = "var1"
        GLabel_51.place(x=30,y=90,width=70,height=25)

        GLabel_231=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_231["font"] = ft
        GLabel_231["fg"] = "#333333"
        GLabel_231["justify"] = "center"
        GLabel_231["text"] = "var2"
        GLabel_231.place(x=30,y=130,width=70,height=25)

        GLabel_948=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_948["font"] = ft
        GLabel_948["fg"] = "#333333"
        GLabel_948["justify"] = "center"
        GLabel_948["text"] = "var3"
        GLabel_948.place(x=30,y=170,width=70,height=25)

        GLabel_294=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_294["font"] = ft
        GLabel_294["fg"] = "#333333"
        GLabel_294["justify"] = "center"
        GLabel_294["text"] = "var4"
        GLabel_294.place(x=30,y=210,width=70,height=25)

        GLabel_376=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_376["font"] = ft
        GLabel_376["fg"] = "#333333"
        GLabel_376["justify"] = "center"
        GLabel_376["text"] = "var11"
        GLabel_376.place(x=30,y=250,width=70,height=25)

        GLabel_897=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_897["font"] = ft
        GLabel_897["fg"] = "#333333"
        GLabel_897["justify"] = "center"
        GLabel_897["text"] = "var5"
        GLabel_897.place(x=30,y=290,width=70,height=25)

        GLabel_885=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_885["font"] = ft
        GLabel_885["fg"] = "#333333"
        GLabel_885["justify"] = "center"
        GLabel_885["text"] = "var6"
        GLabel_885.place(x=30,y=330,width=70,height=25)

        GLabel_76=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_76["font"] = ft
        GLabel_76["fg"] = "#333333"
        GLabel_76["justify"] = "center"
        GLabel_76["text"] = "var7"
        GLabel_76.place(x=30,y=370,width=70,height=25)

        GLabel_705=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_705["font"] = ft
        GLabel_705["fg"] = "#333333"
        GLabel_705["justify"] = "center"
        GLabel_705["text"] = "var8"
        GLabel_705.place(x=30,y=410,width=70,height=25)

        GLabel_983=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_983["font"] = ft
        GLabel_983["fg"] = "#333333"
        GLabel_983["justify"] = "center"
        GLabel_983["text"] = "var9"
        GLabel_983.place(x=30,y=450,width=70,height=25)

        GLabel_842=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_842["font"] = ft
        GLabel_842["fg"] = "#333333"
        GLabel_842["justify"] = "center"
        GLabel_842["text"] = "emplyee"
        GLabel_842.place(x=30,y=490,width=70,height=25)

        id=tk.Entry(root)
        id["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        id["font"] = ft
        id["fg"] = "#333333"
        id["justify"] = "center"
        id["text"] = "Entry1"
        id.place(x=120,y=50,width=70,height=25)

        var1=tk.Entry(root)
        var1["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        var1["font"] = ft
        var1["fg"] = "#333333"
        var1["justify"] = "center"
        var1["text"] = "Entry2"
        var1.place(x=120,y=90,width=70,height=25)

        var2=tk.Entry(root)
        var2["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        var2["font"] = ft
        var2["fg"] = "#333333"
        var2["justify"] = "center"
        var2["text"] = "Entry3"
        var2.place(x=120,y=130,width=70,height=25)

        var3=tk.Entry(root)
        var3["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        var3["font"] = ft
        var3["fg"] = "#333333"
        var3["justify"] = "center"
        var3["text"] = "Entry4"
        var3.place(x=120,y=170,width=70,height=25)

        var4=tk.Entry(root)
        var4["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        var4["font"] = ft
        var4["fg"] = "#333333"
        var4["justify"] = "center"
        var4["text"] = "Entry5"
        var4.place(x=120,y=210,width=70,height=25)

        var11=tk.Entry(root)
        var11["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        var11["font"] = ft
        var11["fg"] = "#333333"
        var11["justify"] = "center"
        var11["text"] = "Entry6"
        var11.place(x=120,y=250,width=70,height=25)

        var5=tk.Entry(root)
        var5["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        var5["font"] = ft
        var5["fg"] = "#333333"
        var5["justify"] = "center"
        var5["text"] = "Entry7"
        var5.place(x=120,y=290,width=70,height=25)

        var6=tk.Entry(root)
        var6["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        var6["font"] = ft
        var6["fg"] = "#333333"
        var6["justify"] = "center"
        var6["text"] = "Entry8"
        var6.place(x=120,y=330,width=70,height=25)

        var7=tk.Entry(root)
        var7["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        var7["font"] = ft
        var7["fg"] = "#333333"
        var7["justify"] = "center"
        var7["text"] = "Entry9"
        var7.place(x=120,y=370,width=70,height=25)

        var8=tk.Entry(root)
        var8["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        var8["font"] = ft
        var8["fg"] = "#333333"
        var8["justify"] = "center"
        var8["text"] = "Entry10"
        var8.place(x=120,y=410,width=70,height=25)

        var9=tk.Entry(root)
        var9["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        var9["font"] = ft
        var9["fg"] = "#333333"
        var9["justify"] = "center"
        var9["text"] = "Entry11"
        var9.place(x=120,y=450,width=70,height=25)

        var10=tk.Entry(root)
        var10["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        var10["font"] = ft
        var10["fg"] = "#333333"
        var10["justify"] = "center"
        var10["text"] = "Entry12"
        var10.place(x=120,y=490,width=70,height=25)

        GButton_816=tk.Button(root,command=lambda:update(var1.get(),var2.get(),var3.get(),var4.get(),var11.get(),var5.get(),var6.get(),
        var7.get(),var8.get(),var9.get(),var10.get(),id.get()))
        GButton_816["bg"] = "#efcf75"
        ft = tkFont.Font(family='Times',size=16)
        GButton_816["font"] = ft
        GButton_816["fg"] = "#009688"
        GButton_816["justify"] = "center"
        GButton_816["text"] = "Modifier"
        GButton_816.place(x=100,y=530,width=140,height=30)

        GLabel_568=tk.Label(root)
        GLabel_568["bg"] = "#009688"
        ft = tkFont.Font(family='Times',size=13)
        GLabel_568["font"] = ft
        GLabel_568["fg"] = "#fad400"
        GLabel_568["justify"] = "center"
        GLabel_568["text"] = "Entrer les nouvelles valeures"
        GLabel_568.place(x=10,y=10,width=238,height=30)

def update(id, var1, var2, var3, var4, var11, var5, var6, var7, var8, var9, var10):
    conn = psycopg2.connect(host = "batyr.db.elephantsql.com",
            database="sgjdjzxk",
            user = "sgjdjzxk",
            password = "dmhA58uYe2KOGhyVRTooyNKGLr3SwLHc",
            port = "5432")
    cursor = conn.cursor()
    query = '''UPDATE  MyTable SET var1=%s,var2=%s, var3=%s,var4=%s,var11=%s, var5=%s,var6=%s,var7=%s,var8=%s,var9=%s,var10=%s where id=%s'''
    cursor.execute(query, (id,var1, var2, var3, var4, var11, var5, var6, var7, var8, var9, var10))
    conn.commit()
    conn.close()
    display_MyTable()
    print("modifier")

def chercher(id):
    conn = psycopg2.connect(host = "batyr.db.elephantsql.com",
            database="sgjdjzxk",
            user = "sgjdjzxk",
            password = "dmhA58uYe2KOGhyVRTooyNKGLr3SwLHc",
            port = "5432")
    cursor = conn.cursor()
    query = '''SELECT * FROM MyTable where id=%s'''
    cursor.execute(query, (id,))

    row = cursor.fetchone()
    total_columns = 12

    def table(listbox):
        for j in range(total_columns):
            e =tk.Label(listbox, width=10,height=2, fg='red',font=('Arial', 10, 'bold'), text=row[j], borderwidth=1, relief="groove")
            e.grid(row=1, column=j)
    

    listbox = tk.Listbox(root, width=20, height=5)
    listbox["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times', size=14)
    listbox["font"] = ft
    listbox["fg"] = "#000"
    listbox["justify"] = "center"
    listbox.place(x=340, y=600, width=1011, height=32)
    table(listbox)

    conn.commit()
    conn.close()
    print(row)
    print("chercher")

def inserer(id, var1, var2, var3, var4, var11, var5, var6, var7, var8, var9, var10):
    conn = psycopg2.connect(host="batyr.db.elephantsql.com",
                            database="sgjdjzxk",
                            user="sgjdjzxk",
                            password="dmhA58uYe2KOGhyVRTooyNKGLr3SwLHc",
                            port="5432")
    cursor = conn.cursor()
    query = '''INSERT INTO MyTable(id, var1,var2, var3,var4,var11, var5,var6,var7,var8,var9,var10) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
    cursor.execute(query, (id, var1, var2, var3, var4, var11, var5, var6, var7, var8, var9, var10))
    print("succesfully data inserted")
    conn.commit()
    conn.close()
    # refraichir avec nouvelle communauté
    display_MyTable()
    print("inserer")

def display_MyTable():
    conn = psycopg2.connect(host="batyr.db.elephantsql.com",
                            database="sgjdjzxk",
                            user="sgjdjzxk",
                            password="dmhA58uYe2KOGhyVRTooyNKGLr3SwLHc",
                            port="5432")
    cursor = conn.cursor()
    query = '''SELECT * FROM MyTable order by id'''
    cursor.execute(query)

    
    def table(listbox):
        for i in range(0,total_rows):
            for j in range(total_columns):
                e =tk.Label(listbox, width=10, fg='#3d8f17',
                          font=('Arial', 10, 'bold'), text=rows[i][j], borderwidth=1, relief="groove")
                e.grid(row=i+1, column=j)
    rows = cursor.fetchall()
    total_rows = len(rows)
    total_columns = len(rows[0])

    listbox = tk.Listbox(root, width=20, height=5)
    listbox["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times', size=14)
    listbox["font"] = ft
    listbox["fg"] = "#000"
    listbox["justify"] = "center"
    listbox.place(x=340, y=130, width=1011, height=300)
    header=['id', 'var1', 'var2', 'var3', 'var4', 'var11', 'var5', 'var6', 'var7', 'var8', 'var1 area', 'var10']
    for k in range(12):
        e =tk.Label(listbox, width=10, fg='#e27013',font=('Arial', 10, 'bold'), text=header[k], borderwidth=1, relief="groove")
        e.grid(row=0, column=k)
    table(listbox)

    conn.commit()
    conn.close()





def interface(root):
    # setting title
    root.title("projet")
    # setting window size
    width = 1360
    height = 679
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    root.geometry(alignstr)
    root.resizable(width=False, height=False)

    # THE TITLE
    GLabel_185 = tk.Label(root, bg='#009688')
    GLabel_185["justify"] = "center"
    GLabel_185.place(x=330, y=0, width=700, height=61)

    GLabel_185 = tk.Label(root,text=" BIENVENUE  ||   WELCOME ", bg='white')
    ft = tkFont.Font(family='Courier', size=30, weight='bold', slant='roman')
    GLabel_185["font"] = ft
    GLabel_185["fg"] = "#fad400"
    GLabel_185["justify"] = "center"
    GLabel_185.place(x=334, y=0, width=692, height=56)

    # A green line
    GLabel_997 = tk.Label(root)
    GLabel_997["bg"] = "#009688"
    GLabel_997["justify"] = "center"
    GLabel_997["text"] = ""
    GLabel_997.place(x=307, y=90, width=3, height=565)

    # la partie insertion
    GLabel_972 = tk.Label(root)
    GLabel_972["bg"] = "#009688"
    ft = tkFont.Font(family='Times', size=18, weight='bold', slant='roman')
    GLabel_972["font"] = ft
    GLabel_972["fg"] = "#fad400"
    GLabel_972["justify"] = "center"
    GLabel_972["text"] = "INSERTION"
    GLabel_972.place(x=10, y=90, width=252, height=30)

    # les libelées (nom des colonnes)
    GLabel_174 = tk.Label(root)
    GLabel_174["bg"] = "#fad400"
    ft = tkFont.Font(family='Times', size=10)
    GLabel_174["font"] = ft
    GLabel_174["fg"] = "#333333"
    GLabel_174["justify"] = "center"
    GLabel_174["text"] = "id"
    GLabel_174.place(x=40, y=140, width=70, height=25)

    GLabel_585 = tk.Label(root)
    GLabel_585["bg"] = "#fad400"
    ft = tkFont.Font(family='Times', size=10)
    GLabel_585["font"] = ft
    GLabel_585["fg"] = "#333333"
    GLabel_585["justify"] = "center"
    GLabel_585["text"] = "var2"
    GLabel_585.place(x=40, y=220, width=70, height=25)

    GLabel_899 = tk.Label(root)
    GLabel_899["bg"] = "#fad400"
    ft = tkFont.Font(family='Times', size=10)
    GLabel_899["font"] = ft
    GLabel_899["fg"] = "#333333"
    GLabel_899["justify"] = "center"
    GLabel_899["text"] = "var1"
    GLabel_899.place(x=40, y=180, width=70, height=25)

    GLabel_232 = tk.Label(root)
    GLabel_232["bg"] = "#fad400"
    ft = tkFont.Font(family='Times', size=10)
    GLabel_232["font"] = ft
    GLabel_232["fg"] = "#333333"
    GLabel_232["justify"] = "center"
    GLabel_232["text"] = "var3"
    GLabel_232.place(x=40, y=260, width=70, height=25)

    GLabel_283 = tk.Label(root)
    GLabel_283["bg"] = "#fad400"
    ft = tkFont.Font(family='Times', size=10)
    GLabel_283["font"] = ft
    GLabel_283["fg"] = "#333333"
    GLabel_283["justify"] = "center"
    GLabel_283["text"] = "var4"
    GLabel_283.place(x=40, y=300, width=70, height=25)

    GLabel_734 = tk.Label(root)
    GLabel_734["bg"] = "#fad400"
    ft = tkFont.Font(family='Times', size=10)
    GLabel_734["font"] = ft
    GLabel_734["fg"] = "#333333"
    GLabel_734["justify"] = "center"
    GLabel_734["text"] = "var11"
    GLabel_734.place(x=40, y=340, width=70, height=25)

    GLabel_651 = tk.Label(root)
    GLabel_651["bg"] = "#fad400"
    ft = tkFont.Font(family='Times', size=10)
    GLabel_651["font"] = ft
    GLabel_651["fg"] = "#333333"
    GLabel_651["justify"] = "center"
    GLabel_651["text"] = "var5"
    GLabel_651.place(x=40, y=380, width=70, height=25)

    GLabel_830 = tk.Label(root)
    GLabel_830["bg"] = "#fad400"
    ft = tkFont.Font(family='Times', size=10)
    GLabel_830["font"] = ft
    GLabel_830["fg"] = "#333333"
    GLabel_830["justify"] = "center"
    GLabel_830["text"] = "var6"
    GLabel_830.place(x=40, y=420, width=70, height=25)

    GLabel_327 = tk.Label(root)
    GLabel_327["bg"] = "#fad400"
    ft = tkFont.Font(family='Times', size=10)
    GLabel_327["font"] = ft
    GLabel_327["fg"] = "#333333"
    GLabel_327["justify"] = "center"
    GLabel_327["text"] = "var7"
    GLabel_327.place(x=40, y=460, width=70, height=25)

    GLabel_945 = tk.Label(root)
    GLabel_945["bg"] = "#fad400"
    ft = tkFont.Font(family='Times', size=10)
    GLabel_945["font"] = ft
    GLabel_945["fg"] = "#333333"
    GLabel_945["justify"] = "center"
    GLabel_945["text"] = "var8"
    GLabel_945.place(x=40, y=500, width=70, height=25)

    GLabel_216 = tk.Label(root)
    GLabel_216["bg"] = "#fad400"
    ft = tkFont.Font(family='Times', size=8)
    GLabel_216["font"] = ft
    GLabel_216["fg"] = "#333333"
    GLabel_216["justify"] = "center"
    GLabel_216["text"] = "var1 AREA"
    GLabel_216.place(x=40, y=540, width=70, height=25)

    GLabel_21 = tk.Label(root)
    GLabel_21["bg"] = "#fad400"
    ft = tkFont.Font(family='Times', size=10)
    GLabel_21["font"] = ft
    GLabel_21["fg"] = "#333333"
    GLabel_21["justify"] = "center"
    GLabel_21["text"] = "var10"
    GLabel_21.place(x=40, y=580, width=70, height=25)

    # les champs d'entrées
    Entry1 = tk.Entry(root)
    Entry1["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times', size=10)
    Entry1["font"] = ft
    Entry1["fg"] = "#333333"
    Entry1["justify"] = "center"
    Entry1["text"] = "Entry1"
    Entry1.place(x=140, y=140, width=90, height=25)

    Entry2 = tk.Entry(root)
    Entry2["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times', size=10)
    Entry2["font"] = ft
    Entry2["fg"] = "#333333"
    Entry2["justify"] = "center"
    Entry2["text"] = "Entry2"
    Entry2.place(x=140, y=180, width=90, height=25)

    Entry3 = tk.Entry(root)
    Entry3["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times', size=10)
    Entry3["font"] = ft
    Entry3["fg"] = "#333333"
    Entry3["justify"] = "center"
    Entry3["text"] = "Entry3"
    Entry3.place(x=140, y=220, width=90, height=25)

    Entry4 = tk.Entry(root)
    Entry4["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times', size=10)
    Entry4["font"] = ft
    Entry4["fg"] = "#333333"
    Entry4["justify"] = "center"
    Entry4["text"] = "Entry4"
    Entry4.place(x=140, y=260, width=90, height=25)

    Entry5 = tk.Entry(root)
    Entry5["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times', size=10)
    Entry5["font"] = ft
    Entry5["fg"] = "#333333"
    Entry5["justify"] = "center"
    Entry5["text"] = "Entry5"
    Entry5.place(x=140, y=300, width=90, height=25)

    Entry6 = tk.Entry(root)
    Entry6["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times', size=10)
    Entry6["font"] = ft
    Entry6["fg"] = "#333333"
    Entry6["justify"] = "center"
    Entry6["text"] = "Entry6"
    Entry6.place(x=140, y=340, width=90, height=25)

    Entry7 = tk.Entry(root)
    Entry7["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times', size=10)
    Entry7["font"] = ft
    Entry7["fg"] = "#333333"
    Entry7["justify"] = "center"
    Entry7["text"] = "Entry7"
    Entry7.place(x=140, y=380, width=90, height=25)

    Entry8 = tk.Entry(root)
    Entry8["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times', size=10)
    Entry8["font"] = ft
    Entry8["fg"] = "#333333"
    Entry8["justify"] = "center"
    Entry8["text"] = "Entry8"
    Entry8.place(x=140, y=420, width=90, height=25)

    Entry9 = tk.Entry(root)
    Entry9["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times', size=10)
    Entry9["font"] = ft
    Entry9["fg"] = "#333333"
    Entry9["justify"] = "center"
    Entry9["text"] = "Entry9"
    Entry9.place(x=140, y=460, width=90, height=25)

    Entry10 = tk.Entry(root)
    Entry10["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times', size=10)
    Entry10["font"] = ft
    Entry10["fg"] = "#333333"
    Entry10["justify"] = "center"
    Entry10["text"] = "Entry10"
    Entry10.place(x=140, y=500, width=90, height=25)

    Entry11 = tk.Entry(root)
    Entry11["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times', size=10)
    Entry11["font"] = ft
    Entry11["fg"] = "#333333"
    Entry11["justify"] = "center"
    Entry11["text"] = "Entry11"
    Entry11.place(x=140, y=540, width=90, height=25)

    Entry12 = tk.Entry(root)
    Entry12["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times', size=10)
    Entry12["font"] = ft
    Entry12["fg"] = "#333333"
    Entry12["justify"] = "center"
    Entry12["text"] = "Entry12"
    Entry12.place(x=140, y=580, width=90, height=25)

    # button d'insertion
    GButton_ = tk.Button(root, command=lambda: inserer( Entry1.get(), Entry2.get(),
                                                               Entry3.get(), Entry4.get(), Entry5.get(), Entry6.get(),
                                                               Entry7.get(), Entry8.get(), Entry9.get(),Entry10.get(),
                                                               Entry11.get(), Entry12.get()))
    GButton_["bg"] = "#df58e8"
    ft = tkFont.Font(family='Times', size=14)
    GButton_["font"] = ft
    GButton_["fg"] = "#fad400"
    GButton_["justify"] = "center"
    GButton_["text"] = "Ajouter"
    GButton_.place(x=40, y=620, width=190, height=30)

    # Affichage de données
    GLabel_0 = tk.Label(root)
    GLabel_0["bg"] = "#009688"
    ft = tkFont.Font(family='Times', size=18, weight='bold', slant='roman')
    GLabel_0["font"] = ft
    GLabel_0["fg"] = "#fad400"
    GLabel_0["justify"] = "center"
    GLabel_0["text"] = "  Table de Données : MyTable   "
    GLabel_0.place(x=340, y=90, width=1011, height=30)

    # green backgound of "supprimer" et "modifier"
    GLabel_673 = tk.Label(root)
    GLabel_673["bg"] = "#009688"
    GLabel_673["text"] = ""
    GLabel_673.place(x=340, y=440, width=1011, height=54)

    # green backgound of "chercher"
    GLabel_472 = tk.Label(root)
    GLabel_472["bg"] = "#009688"
    GLabel_472["text"] = ""
    GLabel_472.place(x=340, y=520, width=1011, height=52)

    # premier text
    GLabel_172 = tk.Label(root)
    GLabel_172["bg"] = "#009688"
    ft = tkFont.Font(family='Times', size=15, weight='bold', slant='roman')
    GLabel_172["font"] = ft
    GLabel_172["fg"] = "#fad400"
    GLabel_172["justify"] = "center"
    GLabel_172["text"] = "Etrer id"
    GLabel_172.place(x=390, y=450, width=93, height=30)

    # champs d'entreé du id
    GLineEdit_704 = tk.Entry(root)
    GLineEdit_704["bg"] = "#ffffff"
    GLineEdit_704["borderwidth"] = "2px"
    ft = tkFont.Font(family='Times', size=12)
    GLineEdit_704["font"] = ft
    GLineEdit_704["fg"] = "#a30dc1"
    GLineEdit_704["justify"] = "center"
    GLineEdit_704["text"] = "EntryD"
    GLineEdit_704.place(x=500, y=450, width=258, height=30)

    # button de supprimer
    GButton_944 = tk.Button(root, command=lambda:supprimer(GLineEdit_704.get()))
    GButton_944["bg"] = "#df58e8"
    ft = tkFont.Font(family='Times', size=14)
    GButton_944["font"] = ft
    GButton_944["fg"] = "#fff"
    GButton_944["justify"] = "center"
    GButton_944["text"] = "Supprimer"
    GButton_944["relief"] = "raised"
    GButton_944.place(x=770, y=450, width=240, height=30)

    # button de modifier
    GButton_97 = tk.Button(root, command=lambda:newindow(tk.Toplevel(root)))
    GButton_97["bg"] = "#df58e8"
    ft = tkFont.Font(family='Times', size=14)
    GButton_97["font"] = ft
    GButton_97["fg"] = "#fff"
    GButton_97["justify"] = "center"
    GButton_97["text"] = "Modifier"
    GButton_97["relief"] = "raised"
    GButton_97.place(x=1020, y=450, width=290, height=30)

    # pour la recherche
    GLabel_380 = tk.Label(root)
    GLabel_380["bg"] = "#009688"
    ft = tkFont.Font(family='Times', size=15, weight='bold', slant='roman')
    GLabel_380["font"] = ft
    GLabel_380["fg"] = "#fad400"
    GLabel_380["justify"] = "center"
    GLabel_380["text"] = "Rechercher par id"
    GLabel_380.place(x=380, y=530, width=200, height=30)

    GLineEdit_531 = tk.Entry(root)
    GLineEdit_531["bg"] = "#fffefe"
    GLineEdit_531["borderwidth"] = "2px"
    ft = tkFont.Font(family='Times', size=14)
    GLineEdit_531["font"] = ft
    GLineEdit_531["fg"] = "#a30dc1"
    GLineEdit_531["justify"] = "center"
    GLineEdit_531["text"] = "EntryC"
    GLineEdit_531.place(x=598, y=530, width=380, height=30)

    # button de recherche
    GButton_725 = tk.Button(root, command=lambda:chercher(GLineEdit_531.get()))
    GButton_725["bg"] = "#df58e8"
    ft = tkFont.Font(family='Times', size=14)
    GButton_725["font"] = ft
    GButton_725["fg"] = "#fff"
    GButton_725["justify"] = "center"
    GButton_725["text"] = "Chercher"
    GButton_725.place(x=990, y=530, width=320, height=30)
    

    GLabel_953 = tk.Label(root)
    ft = tkFont.Font(family='Times', size=14)
    GLabel_953["font"] = ft
    GLabel_953["fg"] = "#097066"
    GLabel_953["justify"] = "center"
    GLabel_953["text"] = "By Hamid Abdellaoui"
    GLabel_953.place(x=1180, y=650, width=170, height=30)
    display_MyTable()


if __name__ == "__main__":
    root = tk.Tk()
    interface(root)
    root.mainloop()
