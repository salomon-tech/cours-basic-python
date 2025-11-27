
class SoldinsiffisantError(Exception):
  pass

class PorteMoney:
  def __init__(self, titulaire, solde_initial=0):
    self.titulaire = titulaire
    self.solde = solde_initial


  def deposer(self, montant):
    if montant <= 0:
      raise ValueError("montant insuffisante")
    self.solde += montant
    return f"depot de {montant}$ effectuer"
  

  def retirer(self, montant):
    if montant <= 0:
      raise ValueError("entrer un montant valide")
    if montant > self.solde:
      raise SoldinsiffisantError("solde insuffisant")
    return f"retrer de {montant}$ effectuer avec succee"


if __name__ == '__main__':
  compte = PorteMoney("salomon", 50000)
try:
  print(compte.deposer(500))
  print(compte.retirer(10000))
except SoldinsiffisantError as e:
  print(f"erreur: {e}")
except ValueError as e:
  print(f"erreur de valeur : {e}")