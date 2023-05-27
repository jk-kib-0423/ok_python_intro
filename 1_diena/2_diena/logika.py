""""
==     - salidzinas operators, vai ir vienads
!=   -   vai nav vienads
<
>
<=  - mazaks vai vienads
>= - lielaks vai vienads
"""

sk1 = 13    
sk2 = 7
sk3 = 7

print("sk1 == sk2:", sk1 == sk2)
print("sk1 != sk2:", sk1 != sk2)
print("sk1 <= sk2:", sk1 <= sk2)
print("sk1 >= sk2:", sk1 >= sk2)
print("sk1 <= sk2:", sk1 <= sk2)
print("sk1 >= sk2:", sk1 >= sk2)

print("===================================")



print("sk3 == sk2:", sk3 == sk2)
print("sk3 != sk2:", sk3 != sk2)
print("sk3 <= sk2:", sk3 <= sk2)
print("sk3 >= sk2:", sk3 >= sk2)
print("sk3 <= sk2:", sk3 <= sk2)
print("sk3 >= sk2:", sk3 >= sk2)


vards1 = "Olesja"
vards2 = "olesja"
vards3 = "olesja"

print("Olesja == olesja:", vards1 == vards2)
print("olesja == olesja", vards2 == vards3)

print("visi mazie burti salidzinasana", vards1.lower() == vards2.lower())

print("visi mazie burti salidzinasana", vards1.casefold() == vards2.casefold())

print("================================")

patiesiba = True
meli = False

print("patiesiba == meli", patiesiba == meli)
print("patiesiba != meli", patiesiba != meli)


# AND, OR, NOT(!) operatori
"""
AND- skatās vai abas puses ir True
OR - vai k
! apgriezt otradak

A    B       A and B      A or B    A == B       !A
True True      True        True      True       False
True False     False       True      False      False
False True     False       True      False      True    
False False    False       False     True       True


"""

sk1 = 1
sk2 = 2
sk3 = 3
sk4 = 3

print("Rezultats AND:", (sk2 > sk1) and (sk3 == sk4))
print("Rezultats AND:", (sk2 < sk1) and (sk3 == sk4))

print("Rezultats OR1:", (sk2 > sk1) or (sk3 == sk4))
print("Rezultats OR2:", (sk2 < sk1) or (sk3 == sk4))


sk1 >= 3 and sk1 <= 5