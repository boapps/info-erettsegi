def pf(n):
  print("\n" + str(n) + ". feladat")

foglaltsag_file = open("foglaltsag.txt", "r")
szekek_foglaltsag = list()
for sor in foglaltsag_file:
  szek_sor = list()
  for fog in sor:
    szek_sor.append(fog)
  szekek_foglaltsag.append(szek_sor)
foglaltsag_file.close()

kategoria_file = open("kategoria.txt", "r")
szekek_kategoria = list()
for sor in kategoria_file:
  szek_sor = list()
  for kat in sor:
    szek_sor.append(kat)
  szekek_kategoria.append(szek_sor)
kategoria_file.close()

pf(2)

sor = int(input("sor: ")) - 1
szek = int(input("szek: ")) - 1
print("foglalt" if (szekek_foglaltsag[sor][szek] == "x") else "(még) szabad")

pf(3)

foglalt = 0
for sor in szekek_foglaltsag:
  for fog in sor:
    if fog == "x":
      foglalt += 1

print("Eddig {0} jegyet adtak el és ez a nézőtér {1} százaléka".format(foglalt, round(100*foglalt/(15*20), 2)))

pf(4)

egy, ket, har, neg, ot = 0,0,0,0,0
for kat in szekek_kategoria:
  egy += kat.count("1")
  ket += kat.count("2")
  har += kat.count("3")
  neg += kat.count("4")
  ot += kat.count("5")

max_kat = max(egy, ket, har, neg, ot)
max_kat_str = ""
if (max_kat == egy): max_kat_str = "1"
if (max_kat == ket): max_kat_str = "2"
if (max_kat == har): max_kat_str = "3"
if (max_kat == neg): max_kat_str = "4"
if (max_kat == ot): max_kat_str = "5"

print("A legtöbb jegyet a(z) {}. árkategóriában értékesítették.".format(max_kat_str))

pf(5)

print("A színház bevétele most {0} Ft lenne.".format(egy*5000 + ket*4000 + har*3000 + neg*2000 + ot*1000))

pf(6)

egyedula = 0
for sor in range(14):
  for szek in range(19):
    if (szekek_foglaltsag[sor][szek] == "o") and (szekek_foglaltsag[sor][szek-1] == "x") and (szekek_foglaltsag[sor][szek+1] == "x"):
      egyedula += 1
print(str(egyedula) + " db egyedülálló üres hely van.")

szabad_file = open("szabad.txt", "w")
for sor in range(14):
  uj_sor = ""
  for szek in range(19):
    if (szekek_foglaltsag[sor][szek] == "x"):
      uj_sor += "x"
    else:
      uj_sor += szekek_kategoria[sor][szek]
  szabad_file.write(uj_sor + "\n")
szabad_file.close()
