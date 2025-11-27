import os
import sqlite3

class GestionnaireBD:
  def __init__(self, name="database.db"):
    self.name = name
    self.connexion = None
    self.curseur = None

  def connecter(self):
    self.connexion = sqlite3.connect(self.name)
    curseur = self.connexion.cursor()
    print("connextion a la base de donnee etablie")

  def creer_table(self):
    self.curseur.execute(

      #users table
      '''
          CREATE TABLE IF NOT EXIST Utilisateurs (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          nom TEXT NOT NULL,
          email TEXT UNIQUE NOT NULL,
          date_creation DATETIME DEFAULT CURRENT_TIMESTAMP
          )
      '''

    )

    #products table

    self.connexion.execute(
      '''
          CREATE TABLE IF NOT EXIST Products(
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          nom TEXT NOT NULL,
          Prix REAL NOT NULL,
          Quantite INTEGER AUTOINCREMENT 0,
          Categorie TEXT
          )
      '''
    )

    self.connexion.commit()
    print("tables creer avec succees")
