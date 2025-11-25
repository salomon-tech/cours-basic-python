# writing file

with open("file.txt", "w", encoding="utf-8") as f:
  f.write("line 1\n")
  f.write("line 2\n")

# reading file

with open("file.txt", "r", encoding="utf-8") as f:
  content = f.read()
  print(content)

# Reading line by line

with open("file.txt", "r", encoding="utf-8") as f:
  for line in f:
    print(line.strip())