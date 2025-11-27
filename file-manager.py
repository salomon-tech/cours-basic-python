"""La gestion des fichiers en python

est essentielle pour lire, ecrire et manipuler des donnees stockees dans des fichiers externes."""

# writing file

with open("file.txt", "w", encoding="utf-8") as f:
  f.write("hi i'm HK7\n")
  f.write("Student from ISESOD-GOMA\n")

# reading file

with open("file.txt", "r", encoding="utf-8") as f:
  content = f.read()
  print(content)

# Reading line by line

with open("file.txt", "r", encoding="utf-8") as f:
  for line in f:
    print(line.strip())