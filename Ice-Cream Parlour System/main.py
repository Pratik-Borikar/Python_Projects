from tkinter import*
import math, random, os
from tkinter import messagebox

class Bill_App:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x800+0+0")
        self.root.title("Billing Software")
        bg_color = "#074463"
        title = Label(self.root, text=" Ice-Cream Parlor Billing Software", bd=12, relief= GROOVE, bg= bg_color, fg="white", font=("times new roman",30,"bold"), pady=2).pack(fill=X)


        #----------Variables----------

        #-----Ice Cream-----
        self.vanilla = IntVar()
        self.butter_scotch = IntVar()
        self.strawbery = IntVar()
        self.chocolate = IntVar()
        self.kesar_pista = IntVar()
        self.mango = IntVar()
        self.tootifrooti =IntVar()

        #-----Scoops-----
        self.butterscotchs = IntVar()
        self.vanillas = IntVar()
        self.chocolates = IntVar()
        self.tootifrootis = IntVar()
        self.strawberys = IntVar()
        self.mangos = IntVar()
        self.chocochips = IntVar()

        #-----Kulfi-----
        self.matka = IntVar()
        self.mava = IntVar()
        self.badam = IntVar()
        self.mangok = IntVar()
        self.rabrimalai = IntVar()
        self.rajwadi = IntVar()
        self.rajbhog = IntVar()

        #-----Thic Shake-----
        self.vanillam = IntVar()
        self.strawberym = IntVar()
        self.chocolatem = IntVar()
        self.mangom = IntVar()
        self.kesarpistam = IntVar()
        self.oreom = IntVar()
        self.kitkat = IntVar()

        #-----Total Product Price Variable-----
        self.ice_cream_price = StringVar()
        self.scoops_price = StringVar()
        self.kulfi_price = StringVar()
        self.thic_shake_price = StringVar()

        #-----Customer Variable-----
        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.bill_no = StringVar()
        x = random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill = StringVar()


        #----------Customer Detail Frame---------
        F1 = LabelFrame(self.root, bd=10,relief=GROOVE, text="Customer Details", font=("times new roman",15,"bold"), fg="gold", bg=bg_color)
        F1.place(x=0, y=75, relwidth=1)

        cname_lbl = Label(F1, text="Customer Name",bg=bg_color, fg="white", font=("times new roman", 18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt = Entry(F1, width=20, textvariable=self.c_name, font="arial 15",bd=7, relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

        cphone_lbl = Label(F1, text="Phone Number",bg=bg_color, fg="white", font=("times new roman", 18,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphone_txt = Entry(F1, width=20, textvariable=self.c_phone, font="arial 15",bd=7, relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)

        cbill_lbl = Label(F1, text="Bill Number",bg=bg_color, fg="white", font=("times new roman", 18,"bold")).grid(row=0,column=4,padx=20,pady=5)
        cbill_txt = Entry(F1, width=20, textvariable=self.search_bill, font="arial 15",bd=7, relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)

        bill_btn = Button(F1, command=self.find_bill, text="Search",width=10, bd=7, font="arial 12 bold").grid(row=0,column=6,pady=10,padx=15)


        #----------Ice-Cream Frame----------
        F2 = LabelFrame(self.root,bd=10,relief=GROOVE, text="Ice-Cream", font=("times new roman",15,"bold"), fg="gold", bg=bg_color)
        F2.place(x=0, y=175, width=300, height=460)

        I1_lbl = Label(F2, text="Vanilla", font=("times new roman", 16, "bold"), bg=bg_color, fg="light green").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        I1_txt = Entry(F2, width=10, textvariable=self.vanilla, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        I2_lbl = Label(F2, text="ButterScotch", font=("times new roman", 16, "bold"), bg=bg_color, fg="light green").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        I2_txt = Entry(F2, width=10, textvariable=self.butter_scotch, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        I3_lbl = Label(F2, text="Strawbery", font=("times new roman", 16, "bold"), bg=bg_color, fg="light green").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        I3_txt = Entry(F2, width=10, textvariable=self.strawbery, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        I4_lbl = Label(F2, text="Chocolate", font=("times new roman", 16, "bold"), bg=bg_color, fg="light green").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        I4_txt = Entry(F2, width=10, textvariable=self.chocolate, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        I5_lbl = Label(F2, text="Kesar Pista", font=("times new roman", 16, "bold"), bg=bg_color, fg="light green").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        I5_txt = Entry(F2, width=10, textvariable=self.kesar_pista, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        I6_lbl = Label(F2, text="Mango", font=("times new roman", 16, "bold"), bg=bg_color, fg="light green").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        I6_txt = Entry(F2, width=10, textvariable=self.mango, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        I7_lbl = Label(F2, text="TootiFrooti", font=("times new roman", 16, "bold"), bg=bg_color, fg="light green").grid(row=6,column=0,padx=10,pady=10,sticky="w")
        I7_txt = Entry(F2, width=10, textvariable=self.tootifrooti, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=6,column=1,padx=10,pady=10)



        #----------Scoops----------
        F3 = LabelFrame(self.root,bd=10,relief=GROOVE, text="Ice-Cream Scoops", font=("times new roman",15,"bold"), fg="gold", bg=bg_color)
        F3.place(x=300, y=175, width=300, height=460)

        g1_lbl = Label(F3, text="ButterScotch", font=("times new roman", 16, "bold"), bg=bg_color, fg="light green").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        g1_txt = Entry(F3, width=10, textvariable=self.butterscotchs, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        g2_lbl = Label(F3, text="Vanilla", font=("times new roman", 16, "bold"), bg=bg_color, fg="light green").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        g2_txt = Entry(F3, width=10, textvariable=self.vanillas, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        g3_lbl = Label(F3, text="Chocolate", font=("times new roman", 16, "bold"), bg=bg_color, fg="light green").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        g3_txt = Entry(F3, width=10, textvariable=self.chocolates, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        g4_lbl = Label(F3, text="TootiFrooti", font=("times new roman", 16, "bold"), bg=bg_color, fg="light green").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        g4_txt = Entry(F3, width=10, textvariable=self.tootifrootis, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        g5_lbl = Label(F3, text="Strawbery", font=("times new roman", 16, "bold"), bg=bg_color, fg="light green").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        g5_txt = Entry(F3, width=10, textvariable=self.strawberys, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        g6_lbl = Label(F3, text="Mango", font=("times new roman", 16, "bold"), bg=bg_color, fg="light green").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        g6_txt = Entry(F3, width=10, textvariable=self.mangos, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        g7_lbl = Label(F3, text="ChocoChips", font=("times new roman", 16, "bold"), bg=bg_color, fg="light green").grid(row=6,column=0,padx=10,pady=10,sticky="w")
        g7_txt = Entry(F3, width=10, textvariable=self.chocochips, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=6,column=1,padx=10,pady=10)



        #----------Kulfi----------
        F4 = LabelFrame(self.root,bd=10,relief=GROOVE, text="Kulfi", font=("times new roman",15,"bold"), fg="gold", bg=bg_color)
        F4.place(x=600, y=175, width=300, height=460)

        F1_lbl = Label(F4, text="Matka", font=("times new roman", 16, "bold"), bg=bg_color, fg="light green").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        F1_txt = Entry(F4, width=10, textvariable=self.matka, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        F2_lbl = Label(F4, text="Mava", font=("times new roman", 16, "bold"), bg=bg_color, fg="light green").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        F2_txt = Entry(F4, width=10, textvariable=self.mava, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        F3_lbl = Label(F4, text="Badam", font=("times new roman", 16, "bold"), bg=bg_color, fg="light green").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        F3_txt = Entry(F4, width=10, textvariable=self.badam, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        F4_lbl = Label(F4, text="Mango", font=("times new roman", 16, "bold"), bg=bg_color, fg="light green").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        F4_txt = Entry(F4, width=10, textvariable=self.mangok, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        F5_lbl = Label(F4, text="RabriMalai", font=("times new roman", 16, "bold"), bg=bg_color, fg="light green").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        F5_txt = Entry(F4, width=10, textvariable=self.rabrimalai, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        F6_lbl = Label(F4, text="Rajwadi", font=("times new roman", 16, "bold"), bg=bg_color, fg="light green").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        F6_txt = Entry(F4, width=10, textvariable=self.rajwadi, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        F7_lbl = Label(F4, text="Rajbhog", font=("times new roman", 16, "bold"), bg=bg_color, fg="light green").grid(row=6,column=0,padx=10,pady=10,sticky="w")
        F7_txt = Entry(F4, width=10, textvariable=self.rajbhog, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=6,column=1,padx=10,pady=10)


        #----------Thic Shake----------
        F5 = LabelFrame(self.root,bd=10,relief=GROOVE, text="Thic Shake", font=("times new roman",15,"bold"), fg="gold", bg=bg_color)
        F5.place(x=900, y=175, width=300, height=460)

        F1_lbl = Label(F5, text="Vanilla", font=("times new roman", 16, "bold"), bg=bg_color, fg="light green").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        F1_txt = Entry(F5, width=10, textvariable=self.vanillam, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        F2_lbl = Label(F5, text="Strawbery", font=("times new roman", 16, "bold"), bg=bg_color, fg="light green").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        F2_txt = Entry(F5, width=10, textvariable=self.strawberym, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        F3_lbl = Label(F5, text="Chocolate", font=("times new roman", 16, "bold"), bg=bg_color, fg="light green").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        F3_txt = Entry(F5, width=10, textvariable=self.chocolatem, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        F4_lbl = Label(F5, text="Mango", font=("times new roman", 16, "bold"), bg=bg_color, fg="light green").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        F4_txt = Entry(F5, width=10, textvariable=self.mangom, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        F5_lbl = Label(F5, text="KesarPista", font=("times new roman", 16, "bold"), bg=bg_color, fg="light green").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        F5_txt = Entry(F5, width=10, textvariable=self.kesarpistam, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        F6_lbl = Label(F5, text="Oreo", font=("times new roman", 16, "bold"), bg=bg_color, fg="light green").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        F6_txt = Entry(F5, width=10, textvariable=self.oreom, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        F7_lbl = Label(F5, text="KitKat", font=("times new roman", 16, "bold"), bg=bg_color, fg="light green").grid(row=6,column=0,padx=10,pady=10,sticky="w")
        F7_txt = Entry(F5, width=10, textvariable=self.kitkat, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=6,column=1,padx=10,pady=10)



        #----------Bill Frame----------
        F6 = Frame(self.root,bd=10,relief=GROOVE)
        F6.place(x=1200, y=175, width=330, height=460)
        bill_title = Label(F6, text="Bill Area", font="arial 15 bold", bd=7, relief=GROOVE).pack(fill=X)
        scrol_y = Scrollbar(F6, orient=VERTICAL)
        self.txtarea = Text(F6, yscrollcommand= scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)


        #----------Button Frame----------
        F7 = LabelFrame(self.root,bd=10,relief=GROOVE, text="Bill Menu", font=("times new roman",15,"bold"), fg="gold", bg=bg_color)
        F7.place(x=0, y=640, relwidth=1, height=150)

        m1_lbl = Label(F7, text="Total Ice Cream Price", bg=bg_color, fg="white", font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=10,sticky="w")
        m1_txt = Entry(F7, width=18, textvariable=self.ice_cream_price, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        m2_lbl = Label(F7, text="Total Scoops Price", bg=bg_color, fg="white", font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=10,sticky="w")
        m2_txt = Entry(F7, width=18, textvariable=self.scoops_price, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        m3_lbl = Label(F7, text="Total Kulfi Price", bg=bg_color, fg="white", font=("times new roman",14,"bold")).grid(row=0,column=2,padx=20,pady=10,sticky="w")
        m3_txt = Entry(F7, width=18, textvariable=self.kulfi_price, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=0,column=3,padx=10,pady=10)

        m4_lbl = Label(F7, text="Total Thic Shake Price", bg=bg_color, fg="white", font=("times new roman",14,"bold")).grid(row=1,column=2,padx=20,pady=10,sticky="w")
        m4_txt = Entry(F7, width=18, textvariable=self.thic_shake_price, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=1,column=3,padx=10,pady=10)



        btn_F = Frame(F7, bd=7, relief=GROOVE)
        btn_F.place(x=850, width=580, height=105)

        total_btn = Button(btn_F, command=self.total, text="Total",bg="cadetblue",fg="white", bd=2, pady=15, width=10, font="arial 14 bold").grid(row=0,column=0,padx=5,pady=5)
        generate_btn = Button(btn_F, command=self.bill_area, text="Genrate Bill",bg="cadetblue",fg="white", bd=2, pady=15, width=10, font="arial 14 bold").grid(row=0,column=1,padx=5,pady=5)
        Clear_btn = Button(btn_F, command=self.clear_data, text="Clear",bg="cadetblue",fg="white", bd=2, pady=15, width=10, font="arial 14 bold").grid(row=0,column=2,padx=5,pady=5)
        Exit_btn = Button(btn_F, command=self.Exit_app, text="Exit",bg="cadetblue",fg="white", bd=2, pady=15, width=10, font="arial 14 bold").grid(row=0,column=3,padx=5,pady=5)
        self.welcome_bill()


    def total(self):
        self.total_ice_cream_price = float(
                    (self.vanilla.get()*40)+
                    (self.butter_scotch.get()*40)+
                    (self.strawbery.get()*40)+
                    (self.chocolate.get()*50)+
                    (self.kesar_pista.get()*50)+
                    (self.mango.get()*50)+
                    (self.tootifrooti.get()*60)
        )
        self.ice_cream_price.set("Rs. "+str(self.total_ice_cream_price))

        self.total_scoops_price = float(
                    (self.butterscotchs.get()*40)+
                    (self.vanillas.get()*40)+
                    (self.chocolates.get()*50)+
                    (self.tootifrootis.get()*50)+
                    (self.strawberys.get()*50)+
                    (self.mangos.get()*50)+
                    (self.chocochips.get()*60)
        )
        self.scoops_price.set("Rs. "+str(self.total_scoops_price))

        self.total_kulfi_price = float(
                    (self.matka.get()*20)+
                    (self.mava.get()*20)+
                    (self.badam.get()*30)+
                    (self.mangok.get()*30)+
                    (self.rabrimalai.get()*30)+
                    (self.rajwadi.get()*40)+
                    (self.rajbhog.get()*40)
        )
        self.kulfi_price.set("Rs. "+str(self.total_kulfi_price))

        self.total_thic_shake_price = float(
                    (self.vanillam.get()*60)+
                    (self.strawberym.get()*70)+
                    (self.chocolatem.get()*80)+
                    (self.mangom.get()*70)+
                    (self.kesarpistam.get()*70)+
                    (self.oreom.get()*100)+
                    (self.kitkat.get()*100)
        )
        self.thic_shake_price.set("Rs. "+str(self.total_thic_shake_price))


        self.Total_bill = self.total_ice_cream_price+self.total_scoops_price+self.total_kulfi_price+self.total_thic_shake_price

    
    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\t Ice Cream Parlour \n")
        self.txtarea.insert(END,f"\n  Bill Number : {self.bill_no.get()}")
        self.txtarea.insert(END,f"\n  Customer Name : {self.c_name.get()}")
        self.txtarea.insert(END,f"\n  Phone Number : {self.c_phone.get()} ")
        self.txtarea.insert(END,"\n====================================")
        self.txtarea.insert(END,"\n Products\t\tQTY\t   Price")
        self.txtarea.insert(END,"\n====================================")

    def bill_area(self):

        if self.c_name.get()=="" or self.c_phone.get()=="":
            messagebox.showerror("Error","Customer details are must")
        elif self.ice_cream_price.get()=="Rs. 0.0" and  self.scoops_price.get()=="Rs. 0.0" and  self.kulfi_price.get()=="Rs. 0.0" and  self.thic_shake_price.get()=="Rs. 0.0":
            messagebox.showerror("Error","Please Select the Product")
        else:
            self.welcome_bill()

            #-----Ice Cream Bill Print-----
            if self.vanilla.get()!=0:
                self.txtarea.insert(END,f"\n vanilla\t\t{self.vanilla.get()}\t   {self.vanilla.get()*40}")
            if self.butter_scotch.get()!=0:
                self.txtarea.insert(END,f"\n Butter Scotch\t\t{self.butter_scotch.get()}\t   {self.butter_scotch.get()*40}")
            if self.strawbery.get()!=0:
                self.txtarea.insert(END,f"\n Strawbery\t\t{self.strawbery.get()}\t   {self.strawbery.get()*40}")
            if self.chocolate.get()!=0:
                self.txtarea.insert(END,f"\n Chocolate\t\t{self.chocolate.get()}\t   {self.chocolate.get()*50}")
            if self.kesar_pista.get()!=0:
                self.txtarea.insert(END,f"\n Kesar Pista\t\t{self.kesar_pista.get()}\t   {self.kesar_pista.get()*50}")
            if self.mango.get()!=0:
                self.txtarea.insert(END,f"\n Mango\t\t{self.mango.get()}\t   {self.mango.get()*50}")
            if self.tootifrooti.get()!=0:
                self.txtarea.insert(END,f"\n Tooti Frooti\t\t{self.tootifrooti.get()}\t   {self.tootifrooti.get()*60}")
            
            #-----Scoops Bill Print-----
            if self.butterscotchs.get()!=0:
                self.txtarea.insert(END,f"\n Butterscotch\t\t{self.butterscotchs.get()}\t   {self.butterscotchs.get()*40}")
            if self.vanillas.get()!=0:
                self.txtarea.insert(END,f"\n Vanilla\t\t{self.vanillas.get()}\t   {self.vanillas.get()*40}")
            if self.chocolates.get()!=0:
                self.txtarea.insert(END,f"\n Chocolate\t\t{self.chocolates.get()}\t   {self.chocolates.get()*50}")
            if self.tootifrootis.get()!=0:
                self.txtarea.insert(END,f"\n Tooti Frooti\t\t{self.tootifrootis.get()}\t   {self.tootifrootis.get()*50}")
            if self.strawberys.get()!=0:
                self.txtarea.insert(END,f"\n Strawbery\t\t{self.strawberys.get()}\t   {self.strawberys.get()*50}")
            if self.mangos.get()!=0:
                self.txtarea.insert(END,f"\n Mango\t\t{self.mangos.get()}\t   {self.mangos.get()*50}")
            if self.chocochips.get()!=0:
                self.txtarea.insert(END,f"\n Chocochips\t\t{self.chocochips.get()}\t   {self.chocochips.get()*40}")
            
            #-----Kulfi Bill Print-----
            if self.matka.get()!=0:
                self.txtarea.insert(END,f"\n Matka\t\t{self.matka.get()}\t   {self.matka.get()*20}")
            if self.mava.get()!=0:
                self.txtarea.insert(END,f"\n Mava\t\t{self.mava.get()}\t   {self.mava.get()*20}")
            if self.badam.get()!=0:
                self.txtarea.insert(END,f"\n Badam\t\t{self.badam.get()}\t   {self.badam.get()*30}")
            if self.mangok.get()!=0:
                self.txtarea.insert(END,f"\n Mango\t\t{self.mangok.get()}\t   {self.mangok.get()*30}")
            if self.rabrimalai.get()!=0:
                self.txtarea.insert(END,f"\n Rabri Malai\t\t{self.rabrimalai.get()}\t   {self.rabrimalai.get()*30}")
            if self.rajwadi.get()!=0:
                self.txtarea.insert(END,f"\n Rajwadi\t\t{self.rajwadi.get()}\t   {self.rajwadi.get()*40}")
            if self.rajbhog.get()!=0:
                self.txtarea.insert(END,f"\n Rajbhog\t\t{self.rajbhog.get()}\t   {self.rajbhog.get()*40}")

            #-----Thic Shake Bill Print-----
            if self.vanillam.get()!=0:
                self.txtarea.insert(END,f"\n Vanilla\t\t{self.vanillam.get()}\t   {self.vanillam.get()*60}")
            if self.strawberym.get()!=0:
                self.txtarea.insert(END,f"\n Strawbery\t\t{self.strawberym.get()}\t   {self.strawberym.get()*70}")
            if self.chocolatem.get()!=0:
                self.txtarea.insert(END,f"\n Chocolate\t\t{self.chocolatem.get()}\t   {self.chocolatem.get()*80}")
            if self.mangom.get()!=0:
                self.txtarea.insert(END,f"\n Mango\t\t{self.mangom.get()}\t   {self.mangom.get()*70}")
            if self.kesarpistam.get()!=0:
                self.txtarea.insert(END,f"\n Kesarpista\t\t{self.kesarpistam.get()}\t   {self.kesarpistam.get()*70}")
            if self.oreom.get()!=0:
                self.txtarea.insert(END,f"\n Oreo\t\t{self.oreom.get()}\t   {self.oreom.get()*100}")
            if self.kitkat.get()!=0:
                self.txtarea.insert(END,f"\n KitKat\t\t{self.kitkat.get()}\t   {self.kitkat.get()*100}")
            
            self.txtarea.insert(END,"\n------------------------------------")
            self.txtarea.insert(END,f"\n Total :\t\t       Rs. {self.Total_bill}")
            self.txtarea.insert(END,"\n------------------------------------")
            self.save_bill()

        
    def save_bill(self):
        op = messagebox.askyesno("Save Bill","Do you want to save the bill")
        if op>0:
            self.bill_data = self.txtarea.get('1.0',END)  
            f1 = open("Bills/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill no. :{self.bill_no.get()} saved Successfully")
        else:
            return

    def find_bill(self):
        present = "no"
        for i in os.listdir("Bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1 = open(f"Bills/{i}","r")
                self.txtarea.delete('1.0',END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","Invalid Bill No.")


    def clear_data(self):
        op = messagebox.askyesno("Clear","Do you really want to Clear")
        if op>0:

            #-----Ice Cream-----
            self.vanilla.set(0)
            self.butter_scotch.set(0)
            self.strawbery.set(0)
            self.chocolate.set(0)
            self.kesar_pista.set(0)
            self.mango.set(0)
            self.tootifrooti.set(0)

            #-----Scoops-----
            self.butterscotchs.set(0)
            self.vanillas.set(0)
            self.chocolates.set(0)
            self.tootifrootis.set(0)
            self.strawberys.set(0)
            self.mangos.set(0)
            self.chocochips.set(0)

            #-----Kulfi-----
            self.matka.set(0)
            self.mava.set(0)
            self.badam.set(0)
            self.mangok.set(0)
            self.rabrimalai.set(0)
            self.rajwadi.set(0)
            self.rajbhog.set(0)

            #-----Thic Shake-----
            self.vanillam.set(0)
            self.strawberym.set(0)
            self.chocolatem.set(0)
            self.mangom.set(0)
            self.kesarpistam.set(0)
            self.oreom.set(0)
            self.kitkat.set(0)

            #-----Total Product Price Variable-----
            self.ice_cream_price.set("")
            self.scoops_price.set("")
            self.kulfi_price.set("")
            self.thic_shake_price.set("")

            #-----Customer Variable-----
            self.c_name.set("")
            self.c_phone.set("")
            self.bill_no.set("")
            x = random.randint(1000,9999)
            self.bill_no.set(str(x))
            self.search_bill.set("")

            self.welcome_bill()


    def Exit_app(self):
        op = messagebox.askyesno("Exit","Do you really want to exit")
        if op>0:
            self.root.destroy()
        



root=Tk()
obj = Bill_App(root)
root.mainloop()