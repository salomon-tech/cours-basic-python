import tkinter as ttk
from tkinter import messagebox

class Interface:
  def __init__(self, root):
    self.root = root
    self.root.title = ("App")
    self.root.geometry("1900x900")
    self.root.configure("#f0f0f0")
    self.root.resizable(False, False)


    # style
    self.style = ttk.Style()
    self.style.configure("TFrame", background="#f0f0f0")
    self.style.configure("TLabel", background="#f0f0f0")
    self.style.configure("TButton", background="#4caf50", foreground="#ffffff", font=("arial", 10, "bold"))