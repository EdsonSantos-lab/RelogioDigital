import tkinter as tk
from time import strftime

relogio= tk.Tk()
relogio.title("Relogio Digital")
def relogio_digital():
    hora = strftime('%H:%M:%S')
    label.config(text= hora)
    label.after(1000, relogio_digital)
label = tk.Label(relogio, font=('Helvetica', 48), background= 'black', foreground= 'cyan')

label.pack(anchor='center')

relogio_digital()
relogio.mainloop()