def pf(n):
  print(str(n) + ". feladat")

# ez borzalmas, valaki pls találjon egy jobb megoldást
def egyszerusit(ip, full):
  final = list()
  for csoport in ip.split(":"):
    changed = csoport.lstrip("0")
    if (not full) and (changed == ""):
      changed = "0"
    final.append(changed)
  if not full:
    return ":".join(final)
  else:
    res = ":".join(final)
    got_it = False
    for n in range(5):
      tofind = ":"*(7-n)
      if ((res.count(tofind)) > 0) and not got_it:
        res = res.replace(tofind, "TMP")
        got_it = True
      if got_it:
        res = res.replace(tofind, "0".join(tofind))
  return res.replace("TMP", "::")

ip_file = open("ip.txt", "r")
ips = list()
for line in ip_file:
  ips.append(line)
ip_file.close()

pf(2)
ips_orig = list()
ips_orig.extend(ips.copy())
print("Az állományban {0} darab állománysor van.".format(len(ips)))

pf(3)
ips.sort()
print("A legalacsonyabb tárolt IP-cím: \n" + ips[0])

pf(4)
dok = list()
glo = list()
loc = list()

for ip in ips:
  if ip[0:9] == "2001:0db8":
    dok.append(ip)
  if ip[0:7] == "2001:0e":
    glo.append(ip)
  if (ip[0:2] == "fc") or (ip[0:2] == "fd"):
    loc.append(ip)

print("Dokumentációs cím: " + str(len(dok)) + " darab")
print("Globális egyedi cím: " + str(len(glo)) + " darab")
print("Helyi egyedi cím: " + str(len(loc)) + " darab")

out_file = open("sok.txt", "w")

i = 0
for ip in ips_orig:
  i += 1
  if ip.count("0") >= 18:
    out_file.write(str(i) + " " + ip)
out_file.close()

pf(6)
sorsz = int(input("Kérek egy sorszámot: "))
print(ips_orig[sorsz])
print(egyszerusit(ips_orig[sorsz], False))

pf(7)
if egyszerusit(ips_orig[sorsz], False) == egyszerusit(ips_orig[sorsz], True):
  print("Nem rövidíthető tovább.")
else:
  print(egyszerusit(ips_orig[sorsz], True))
