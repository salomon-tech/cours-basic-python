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
    self.style.configure("Header.TLabel", font=("arial", 14, "bold"), foreground=("#333333"))


    #  intro a la creation des widgets avec tkinter en python

    self.creer_widgets()

  def creer_widgets(self):

    # le frame principal
    main_frame = ttk.Frame(self.root, padding="20")
    main_frame.pack(fill="both", expend=True)

    # titre

    titre = ttk.Label(main_frame)
    titre.pack(pady=10)

    # les frames pour les entree

    input_frame = ttk.Frame(main_frame, padding="10")
    input_frame.pack(pady=10)

    # les boutons

