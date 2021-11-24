import tkinter as tk
from tkinter import * 
from tkinter.ttk import *
from tkinter import messagebox

def pilihN():
  global paket
  paket = IntVar()
  window2 = tk.Toplevel()
  window2.geometry('250x200')
  window2.minsize(250, 200)
  window2.maxsize(250, 200)
  window2.title("Paket Netflix")
  Label(window2, text = 'Pilih Paket', font =('Verdana', 15)).pack(side = TOP, pady = 10)
  quit_button = Button(window2, text= "CANCEL", command= window2.destroy).place(x=90, y=150)
  paket1 = Radiobutton(window2, text= "Rp. 54.000/Bulan", variable= paket, value = 1)
  paket2 = Radiobutton(window2, text= "Rp. 120.000/bulan", variable= paket, value = 2)
  paket3 = Radiobutton(window2, text= "Rp. 153.000/bulan", variable= paket, value = 3)
  paket1.pack()
  paket2.pack()
  paket3.pack()
  btn1 = Button(window2, command = submit, text="SUBMIT").place(x=90, y=120)
  window2.iconphoto(False, icon)
  window2.mainloop()
  

def pilihD():
  global paket
  paket = IntVar()
  window2 = Toplevel()
  window2.geometry('250x200')
  window2.minsize(250, 200)
  window2.maxsize(250, 200)
  window2.title("Paket Disney+")
  Label(window2, text = 'Pilih Paket', font =('Verdana', 15)).pack(side = TOP, pady = 10)
  quit_button = Button(window2, text= "CANCEL", command= window2.destroy).place(x=90, y=150)
  paket1 = Radiobutton(window2, text= "Rp. 20.000 (Langganan 1 bulan)", variable= paket, value = 1)
  paket2 = Radiobutton(window2, text= "Rp. 49.000 (Langganan 3 bulan)", variable= paket, value = 2)
  paket3 = Radiobutton(window2, text= "Rp. 79.000 (Langganan 6 bulan)", variable= paket, value = 3)
  paket1.pack()
  paket2.pack()
  paket3.pack()
  btn1 = Button(window2, command = submit, text="SUBMIT").place(x=90, y=120)
  window2.iconphoto(False, icon)
  window2.mainloop()

def pilihS():
  global paket
  paket = IntVar()
  window2 = Toplevel()
  window2.geometry('250x200')
  window2.minsize(250, 200)
  window2.maxsize(250, 200)
  window2.title("Paket Spotify")
  Label(window2, text = 'Pilih Paket', font =(
  'Verdana', 15)).pack(side = TOP, pady = 10)
  quit_button = Button(window2, text= "TUTUP", command= window2.destroy).place(x=90, y=150)
  paket1 = Radiobutton(window2, text= "Rp. 2.500 (Langganan 1 Hari)", variable= paket, value = 1)
  paket2 = Radiobutton(window2, text= "Rp. 54.900 (Langganan 2 Bulan)", variable= paket, value = 2)
  paket3 = Radiobutton(window2, text= "Rp. 153.000 (Langganan 6 Bulan)", variable= paket, value = 3)
  paket1.pack()
  paket2.pack()
  paket3.pack()
  btn1 = Button(window2, command = submit, text="SUBMIT").place(x=90, y=120)
  window2.iconphoto(False, icon)
  window2.mainloop()

def submit():
  if paket.get() == 0 :
    messagebox.showerror("Error","Silahkan pilih satu paket")
  else:
    global nomer
    nomer = StringVar()
    window3 = tk.Toplevel()
    window3.geometry('250x200')
    window3.minsize(250, 200)
    window3.maxsize(250, 200)
    window3.iconphoto(False, icon)
    window3.title("Konfirmasi")
    Label(window3, text = 'Masukkan no HP anda').pack(side = TOP, pady = 10)
    noHP = tk.Entry(window3, textvariable=nomer)
    noHP.pack()
    quit_button = Button(window3, text= "CANCEL", command= window3.destroy).place(x=90, y=130)
    btn1 = Button(window3, command = konfirmasi, text="SUBMIT").place(x=90, y=100)
    window3.mainloop()

def konfirmasi():
  if len(nomer.get()) <= 10 :
    messagebox.showerror("Error", "Masukan nomer HP yang valid")
  else :
    pesan = "Pembayaran anda telah diambil dari nomer " + nomer.get()
    messagebox.showinfo("Konfirmasi", pesan)

root = Tk()
root.minsize(500, 200)
root.maxsize(500, 200)
root.title("Kel16 Store")
icon = PhotoImage(file= r"D:\Undip\Semester 3\PBO\Pembelian Paket Premium\logo-1.png")
root.iconphoto(False, icon)
Label(root, text = 'Pilih Layanan', font =(
  'Verdana', 15)).pack(side = TOP, pady = 10)
  
photo1 = PhotoImage(file = r"D:\Undip\Semester 3\PBO\Pembelian Paket Premium\Disney+.png")
photoimage1 = photo1.subsample(7, 7)
Button(root, text = 'Disney+', image = photoimage1,
                    compound = TOP, command=pilihD).place(x = 120, y = 50)

photo2 = PhotoImage(file = r"D:\Undip\Semester 3\PBO\Pembelian Paket Premium\spotify.png")
photoimage2 = photo2.subsample(7, 7)
Button(root, text = 'Spotify', image = photoimage2,
                    compound = TOP ,command=pilihS).place(x = 295, y = 50)

photo3 = PhotoImage(file = r"D:\Undip\Semester 3\PBO\Pembelian Paket Premium\Netflix.png")
photoimage3 = photo3.subsample(7, 7)
Button(root, text = 'Netflix', image = photoimage3,compound = TOP, command=pilihN).pack()
  
root.mainloop()
