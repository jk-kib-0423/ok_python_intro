"""
If <boolean loģika>:
    komandas
    kas jāveic, rezultats ir True
else: 
    komandas
    vai vairaka
    kas jāveic, ja rezultāts ir False
----------------------------------------------------------
If <boolean loģika>:
    komandas
    kas jāveic, rezultats ir True
elif <boolean loģika>:
    komandas
    vai varākas
    kas jāveic, rezultats ir True
elif <boolean loģika>:
    komandas
    vai vairākas
    kas jāveic, rezultats ir True
else: #'šis nav obligāts
    komandas
    kas jāveic, rezultats ir True
"""

vecums = int(input("Cik tev ir gadu?"))
                   
if vecums >= 18:
    print("Tu esi pilngadīgs")
    print("Tu vari doties tālāk")
else:
    print("Tu neesi pilngadīgs")
    print("Tev ir nepieciešama vecāku atļauja")

if vecums >= 65:
    print("Tu esi pensionārs")

if vecums < 10:
    print("Pirmā desmitgade")
elif vecums < 20:
    print("Otrā desmitgade")
elif vecums < 30:
    print("Trešā desmitgade")
elif vecums < 40:
    print("Ceturtā desmitgade")
else:
    print("Tālāk vairs neskaitām")

    