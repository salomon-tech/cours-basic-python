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


  """Les CRUD en python

Les CRUD c'est un systeme qui fait la creation, la lecture,
les mise a jours et la supression des donnee dans une base de donnee!"""

  def ajouter_utlisateur(self, nom, email, age=None):
    try:
      self.curseur.execute('''
      INSERT INTO utilisateurs (nom, email, age) VALUES (?, ?, ?)      
''', (nom, email, age))
      self.connexion.commit()
      print(f"Utilisateur {nom} ajouter avec succee")
      return True
    except sqlite3.IntegrityError:
      print("erreur email existe deja")
      return False
  def obtenir_utilisateur(self):
    self.curseur.execute('SELECT * FROM Utilisatuers')
    return self.curseur.fetchall()
  
  def rechercher_utilisateur(self, nom=None, email=None):
    query = "SELECT * FROM Utilisatuers WHERE 1=1"
    params = []

    if nom:
      query += " AND nom LIKE ?"
      params.append(f"%{nom}%")
    if email:
      query += "AND email LIKE ?"
      params.append(f"%{email}%")
    self.curseur.execute(query, params)
    return self.curseur.fetchall()
  def mettre_a_jour_utilisateur(self, id_utilisateur, nom=None, email=None, age=None):
    update = []
    params = []

    if nom:
      update.append("nom = ?")
      params.append(nom)
    if email:
      update.append("email = ?")
      params.append(email)
    if age is not None:
      update.append("age = ?")
      params.append(age)
    if update:
      params.append(id_utilisateur)
      query = f"UPDATE Utilisateurs SET {','.join(update)} WHERE id = ?"
      self.curseur.execute(query, params)
      self.connexion.commit()
      print(f"Utilisateur {id_utilisateur} mis a jour")

  def supprimer_utilisateur(self, id_utilisatuer):
    self.curseur.execute('DELETE Utilisateur WHERE id = ?', (id_utilisatuer))
    self.connexion.commit()
    print(f"Utilisateur {id_utilisatuer} supprimer avec succee")

  def ferme_connexion(self):
    if self.connexion:
      self.connexion.close()
      print("connexion fermer")

if __name__=='__main__':
  bd = GestionnaireBD()
  bd.connecter()
  bd.creer_table()

  # ajout des infos dans la bd

  bd.ajouter_utlisateur('salomon HK7', 'salomon@gmail.com', 20)
  bd.ajouter_utlisateur("Bella RICHARD", 'rechard@gmail.fr', 26)

  # afficher les infos de la db

  Utilisateur = bd.obtenir_utilisateur()
  for user in Utilisateur:
    print(user)

  bd.ferme_connexion()
