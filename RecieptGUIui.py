#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk


class RecieptGUIUI:
    def __init__(self, master=None):
        # build ui
        self.Main = tk.Tk(master)
        self.Main.configure(background="#ffffff", height=500, width=1000)
        self.Main.overrideredirect("false")
        self.Main.title("Water Bill")
        self.left = tk.Canvas(self.Main, name="left")
        self.left.configure(
            background="#ffffff",
            highlightbackground="#0080c0",
            relief="flat",
            state="normal",
            takefocus=False)
        self.left.place(
            anchor="nw",
            relwidth=0.46,
            relx=0.03,
            rely=0.20,
            x=0,
            y=0)
        self.right = tk.Canvas(self.Main, name="right")
        self.right.configure(
            background="#ffffff",
            highlightbackground="#0080c0")
        self.right.place(
            anchor="nw",
            relwidth=0.46,
            relx=0.51,
            rely=0.20,
            x=0,
            y=0)
        self.Header = ttk.Label(self.Main, name="header")
        self.Header.configure(
            background="#ffffff",
            font="{times new roman} 12 {}",
            foreground="#0080c0",
            justify="left",
            text='CAGAYAN DE ORO CITY WATER DISTRICT')
        self.Header.pack(side="top")
        self.Address = ttk.Label(self.Main, name="address")
        self.Address.configure(
            background="#ffffff",
            font="{times new roman} 8 {}",
            foreground="#0080c0",
            justify="center",
            text='Corrales Avenue 27 Cagayan de Oro City NON-VAT REG. TIN 000-550-995-000')
        self.Address.pack(side="top")
        self.BILL = ttk.Label(self.Main, name="bill")
        self.BILL.configure(
            background="#ffffff",
            font="{arial } 11 {}",
            foreground="#0080c0",
            justify="left",
            text='WATER BILL')
        self.BILL.pack(side="top")
        self.Instructions1 = ttk.Label(self.Main, name="instructions1")
        self.Instructions1.configure(
            background="#ffffff",
            font="{arial } 7 {bold}",
            foreground="#ff0000",
            text='PLEASE READ INSTRUCTIONS\nAT THE BACK')
        self.Instructions1.place(relx=0.51, rely=0.88, x=0, y=0)
        self.RanNo1 = ttk.Label(self.Main, name="ranno1")
        self.RanNo1.configure(
            background="#ffffff",
            font="{arial} 14 {}",
            foreground="#ff0000",
            text='19738708')
        self.RanNo1.place(relx=0.06, rely=0.88, x=0, y=0)
        self.RanNo2 = ttk.Label(self.Main, name="ranno2")
        self.RanNo2.configure(
            background="#ffffff",
            font="{arial} 10 {}",
            foreground="#ff0000",
            justify="left",
            text='No.')
        self.RanNo2.place(relx=0.03, rely=0.89, x=0, y=0)
        self.Instructions2 = ttk.Label(self.Main, name="instructions2")
        self.Instructions2.configure(
            background="#ffffff",
            font="{arial } 7 {bold}",
            foreground="#ff0000",
            takefocus=False,
            text='NOT VALID AS OFFICIAL RECIEPT')
        self.Instructions2.place(relx=0.03, rely=0.16, x=0, y=0)
        self.left1 = tk.Canvas(self.Main, name="left1")
        self.left1.configure(
            background="#ffffff",
            cursor="arrow",
            highlightbackground="#0080c0")
        self.left1.place(
            anchor="nw",
            height=150,
            relwidth=0.46,
            relx=0.03,
            rely=0.20,
            x=0,
            y=120)
        self.NameAdd = ttk.Label(self.Main, name="nameadd")
        self.NameAdd.configure(
            background="#ffffff",
            font="{arial} 7 {bold}",
            foreground="#0080c0",
            text='NAME AND ADDRESS')
        self.NameAdd.place(anchor="nw", relx=0.035, rely=0.21, x=0, y=0)
        self.AccNo = ttk.Label(self.Main, name="accno")
        self.AccNo.configure(
            background="#ffffff",
            cursor="arrow",
            font="{arial} 7 {bold}",
            foreground="#0080c0",
            justify="left",
            takefocus=False,
            text='ACCOUNT NUMBER')
        self.AccNo.place(anchor="nw", relx=0.035, rely=0.33, x=0, y=0)
        self.left2 = tk.Canvas(self.Main, name="left2")
        self.left2.configure(
            background="#ffffff",
            cursor="arrow",
            highlightbackground="#0080c0")
        self.left2.place(
            anchor="nw",
            height=90,
            relwidth=0.46,
            relx=0.03,
            rely=0.12,
            x=0,
            y=120)
        self.left3 = tk.Canvas(self.Main, name="left3")
        self.left3.configure(
            background="#ffffff",
            cursor="arrow",
            highlightbackground="#0080c0")
        self.left3.place(
            anchor="nw",
            height=25,
            relwidth=0.32,
            relx=0.03,
            rely=0.12,
            x=0,
            y=120)
        self.left4 = tk.Canvas(self.Main, name="left4")
        self.left4.configure(
            background="#ffffff",
            cursor="arrow",
            highlightbackground="#0080c0")
        self.left4.place(
            anchor="nw",
            height=25,
            relwidth=0.32,
            relx=0.03,
            rely=0.16,
            x=0,
            y=120)
        self.left5 = tk.Canvas(self.Main, name="left5")
        self.left5.configure(
            background="#ffffff",
            cursor="arrow",
            highlightbackground="#0080c0")
        self.left5.place(
            anchor="nw",
            height=90,
            relwidth=0.12,
            relx=0.23,
            rely=0.16,
            x=0,
            y=100)
        self.Readings = ttk.Label(self.Main, name="readings")
        self.Readings.configure(
            background="#ffffff",
            cursor="arrow",
            font="{@Arial Unicode MS} 5 {bold}",
            foreground="#0080c0",
            justify="left",
            relief="flat",
            state="normal",
            takefocus=False,
            text='READINGS')
        self.Readings.place(anchor="nw", relx=0.104, rely=0.37, x=0, y=0)
        self.CuM = ttk.Label(self.Main, name="cum")
        self.CuM.configure(
            background="#ffffff",
            cursor="arrow",
            font="{arial} 6 {bold}",
            foreground="#0080c0",
            justify="center",
            relief="flat",
            state="normal",
            takefocus=True,
            text='Cubic Meter')
        self.CuM.place(anchor="nw", relx=0.258, rely=0.37, x=0, y=0)
        self.left6 = tk.Canvas(self.Main, name="left6")
        self.left6.configure(
            background="#ffffff",
            cursor="arrow",
            highlightbackground="#0080c0")
        self.left6.place(
            anchor="nw",
            height=25,
            relwidth=0.32,
            relx=0.03,
            rely=0.16,
            x=0,
            y=120)
        self.left7 = tk.Canvas(self.Main, name="left7")
        self.left7.configure(
            background="#ffffff",
            cursor="arrow",
            highlightbackground="#0080c0")
        self.left7.place(
            anchor="nw",
            height=25,
            relwidth=0.202,
            relx=0.03,
            rely=0.16,
            x=0,
            y=120)
        self.left8 = tk.Canvas(self.Main, name="left8")
        self.left8.configure(
            background="#ffffff",
            cursor="arrow",
            highlightbackground="#0080c0")
        self.left8.place(
            anchor="nw",
            height=25,
            relwidth=0.101,
            relx=0.03,
            rely=0.16,
            x=0,
            y=120)
        self.PREV = ttk.Label(self.Main, name="prev")
        self.PREV.configure(
            background="#ffffff",
            font="{arial} 6 {bold}",
            foreground="#0080c0",
            justify="center",
            state="disabled",
            takefocus=True,
            text='PREVIOUS')
        self.PREV.place(anchor="nw", relx=0.05, rely=0.41, x=0, y=0)
        self.PRES = ttk.Label(self.Main, name="pres")
        self.PRES.configure(
            background="#ffffff",
            cursor="arrow",
            font="{PREV} 6 {bold}",
            foreground="#0080c0",
            justify="center",
            state="normal",
            takefocus=True,
            text='PRESENT')
        self.PRES.place(anchor="nw", relx=0.155, rely=0.41, x=0, y=0)
        self.left9 = tk.Canvas(self.Main, name="left9")
        self.left9.configure(
            background="#ffffff",
            cursor="arrow",
            highlightbackground="#0080c0")
        self.left9.place(
            anchor="nw",
            height=47,
            relwidth=0.101,
            relx=0.03,
            rely=0.245,
            x=0,
            y=100)
        self.CONSUMED = ttk.Label(self.Main, name="consumed")
        self.CONSUMED.configure(
            background="#ffffff",
            cursor="arrow",
            font="{PREV} 6 {bold}",
            foreground="#0080c0",
            justify="center",
            state="normal",
            takefocus=True,
            text='CONSUMED')
        self.CONSUMED.place(anchor="nw", relx=0.258, rely=0.41, x=0, y=0)
        self.left10 = tk.Canvas(self.Main, name="left10")
        self.left10.configure(
            background="#ffffff",
            cursor="arrow",
            highlightbackground="#0080c0")
        self.left10.place(
            anchor="nw",
            height=90,
            relwidth=0.146,
            relx=0.344,
            rely=0.16,
            x=0,
            y=100)
        self.left11 = tk.Canvas(self.Main, name="left11")
        self.left11.configure(
            background="#ffffff",
            cursor="arrow",
            highlightbackground="#0080c0")
        self.left11.place(
            anchor="nw",
            height=45,
            relwidth=0.146,
            relx=0.344,
            rely=0.16,
            x=0,
            y=100)
        self.Amount = ttk.Label(self.Main, name="amount")
        self.Amount.configure(
            background="#ffffff",
            compound="top",
            cursor="based_arrow_down",
            font="{PREV} 6 {bold}",
            foreground="#0080c0",
            justify="center",
            state="disabled",
            takefocus=True,
            text='AMOUNT\n(PESOS)')
        self.Amount.place(anchor="nw", relx=0.392, rely=0.38, x=0, y=0)
        self.Main.pack_propagate(0)

        # Main widget
        self.mainwindow = self.Main

    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    app = RecieptGUIUI()
    app.run()
