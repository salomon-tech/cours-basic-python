import tkinter as ttk
import tkinter as tk
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

    # les titre label

    titre_label = ttk.Label(main_frame, text="Tkinter GUI App", style="Header.TLabel")
    titre_label.pack(pady=10)

    # les labels et entrees

    ttk.Label(input_frame, text='nom : ').grid(row=0, column=0, sticky=tk.w, padx=5, pady=5)
    self.entry_nom = ttk.Entry(input_frame, width=30)
    self.entry_nom.grid(row=0, column=1, padx=5, pady=5)

    ttk.Label(input_frame, text="email : ").grid(row=1, column=0, sticky=tk.w, padx=5, pady=5)
    self.entry_email = ttk.Entry(input_frame, width=30)
    self.entry_email.grid(row=1, colomn=1, padx=5, pady=5)

    # les boutons

    button = ttk.Frame(main_frame)
    button.pack(pady=20)

    ttk.Button(button, text="ajouter", command=self.ajouter).pack(side=tk.LEFT, padx=5)
    ttk.Button(button, text="afficher", command=self.afficher).pack(side=tk.LEFT, padx=5)
    ttk.Button(button, text="quiter", command=self.afficher).pack(side=tk.LEFT, padx=5)

    # treeview pour l'affichage des donnees

    columns = ("id", "nom", "email")
    self.tree = ttk.Treeview(main_frame, columns=columns, show="headings", height=15)

    # definition des headings

    for colonne in columns:
      self.tree.heading(colonne, text=colonne)
      self.tree.column(colonne, width=150)

    self.tree.pack(fill=tk.BOTH, exepend=True, pady=10)
    

