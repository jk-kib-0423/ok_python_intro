iepirkumi = ["sviests", "krejums", "maize", "piens"]
print(iepirkumi)
print(iepirkumi[1])
print(iepirkumi[3])
iepirkumi.append("jogurts") #pievienošana saraksta beigās
print(iepirkumi)

iepirkumi.insert(2, "siers") #pievienošana konkrētā pozīcijā
print(iepirkumi)

#idzēst
iepirkumi.remove("piens")
print(iepirkumi)

print("Izdzēsam konkrēto elementu no saraksta (3):")
iepirkumi.pop(3)
print(iepirkumi)

indeks = iepirkumi.index("sviests")
print("sviests index:, indeks")

iepirkumi.sort()
print(iepirkumi)

print("Sarakstā kopā ir", len(iepirkumi), "elementi!")

temp = iepirkumi[2]
iepirkumi[2] = iepirkumi[0]
iepirkumi[0] = temp
print(iepirkumi)

iepirkumi[0], iepirkumi[2]