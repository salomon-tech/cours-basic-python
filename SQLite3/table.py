import os
import sqlite3

class GestionnaireBD:
  def __init__(self, name="database.db"):
    self.name = name
    self.connexion = None
    self.curseur = None

  def connecter(self):
    self.connexion = sqlite3.connect(self.name)
    self.curseur = self.connexion.cursor()
    print("connexion à la base de données établie")

  def creer_table(self):
    # table Utilisateurs
    self.curseur.execute('''
      CREATE TABLE IF NOT EXISTS Utilisateurs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        age INTEGER,
        date_creation DATETIME DEFAULT CURRENT_TIMESTAMP
      )
    ''')

    # table Products
    self.curseur.execute('''
      CREATE TABLE IF NOT EXISTS Products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT NOT NULL,
        prix REAL NOT NULL,
        quantite INTEGER DEFAULT 0,
        categorie TEXT
      )
    ''')

    self.connexion.commit()
    print("tables créées avec succès")


  """Les CRUD en python

Les CRUD c'est un systeme qui fait la creation, la lecture,
les mise a jours et la supression des donnee dans une base de donnee!"""

  def ajouter_utilisateur(self, nom, email, age=None):
    try:
      self.curseur.execute('''
        INSERT INTO Utilisateurs (nom, email, age) VALUES (?, ?, ?)
      ''', (nom, email, age))
      self.connexion.commit()
      print(f"Utilisateur {nom} ajouté avec succès")
      return True
    except sqlite3.IntegrityError:
      print("erreur: l'email existe déjà")
      return False
  def obtenir_utilisateur(self):
    self.curseur.execute('SELECT * FROM Utilisateurs')
    return self.curseur.fetchall()
  
  def rechercher_utilisateur(self, nom=None, email=None):
    query = "SELECT * FROM Utilisateurs WHERE 1=1"
    params = []

    if nom:
      query += " AND nom LIKE ?"
      params.append(f"%{nom}%")
    if email:
      query += " AND email LIKE ?"
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
    self.curseur.execute('DELETE FROM Utilisateurs WHERE id = ?', (id_utilisatuer,))
    self.connexion.commit()
    print(f"Utilisateur {id_utilisatuer} supprimé avec succès")

  def ferme_connexion(self):
    if self.connexion:
      self.connexion.close()
      print("connexion fermer")

if __name__=='__main__':
  bd = GestionnaireBD()
  bd.connecter()
  bd.creer_table()

  # ajout des infos dans la bd

  bd.ajouter_utilisateur('salomon HK7', 'salomon@gmail.com', 20)
  bd.ajouter_utilisateur('Bella RICHARD', 'rechard@gmail.fr', 26)

  # afficher les infos de la db

  utilisateurs = bd.obtenir_utilisateur()
  for user in utilisateurs:
    print(user)

  bd.ferme_connexion()
