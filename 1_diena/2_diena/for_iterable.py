iepirkumi = ["sviests", "krejums", "maize", "piens"]
skaitļi = [1, 5, 3, 21, 4, 15, 16, 99, 22, 55, 43, -10, -5, 0]

for prece in iepirkumi:
    print(prece)

for skaitlis in skaitļi:
    print(skaitlis)

for skaitlis in skaitļi:
    if skaitlis % 5 == 0:
        print("Atradu skaitli, kas dalās ar 5:", skaitlis)

