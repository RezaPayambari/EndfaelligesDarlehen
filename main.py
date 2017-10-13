from decimal import *

'''darlehen=input("Geben Sie die Darlehen ein: ")'''
darlehen = Decimal(0)
zinssatz = Decimal(0)
laufzeit = Decimal(0)

while Decimal(darlehen)<=0:
    darlehen = input("Geben Sie bitte die Darlehen ein: (€) ")
while Decimal(zinssatz)<=0:
    zinssatz = input("Geben Sie bitte die Zinssatz ein: (%) ")
while Decimal(laufzeit) <= 0:
    laufzeit = input("Geben Sie bitte die Laufzeit ein: (Jahr) ")

jaehrlich = Decimal(darlehen)* (Decimal(zinssatz) / Decimal(100))
insgesamt= (Decimal(jaehrlich) * Decimal(laufzeit))+ Decimal(darlehen)

print("Jährlich: ",jaehrlich)
print("Gesamt: ", insgesamt)