import tkinter as tk
from tkinter import messagebox
def calc(b_text):
    if b_text == "=":
        try:
            res=eval(expression.get())
            expression.set(res)
        except Exception:
            messagebox.showerror("Error","Invalid Expression")
    elif b_text == "C":
        expression.set("")
    else:
        expression.set(expression.get()+b_text)
root=tk.Tk()
root.title("Calculator")
root.geometry("400x350")

expression=tk.StringVar()
text=tk.Entry(root, textvariable=expression, font=("Arial",26),justify="right", bd=10)
text.pack(fill="both",padx=10,pady=10)

buttons=[
    ("C","0","=","+"),
    ("1","2","3","-"),
    ("4","5","6","*"),
    ("7","8","9","/")
]
frame=tk.Frame(root)
frame.pack()
for i in buttons:
    i_frame=tk.Frame(frame)
    i_frame.pack(side="top",fill="both",expand=True)
    for _ in i:
        btn=tk.Button(i_frame, text=_, font=("Arial",18), command=lambda b=_: calc(b),width=5,height=1)
        btn.pack(side="left",fill="both",expand=True,padx=5,pady=5)
root.mainloop()