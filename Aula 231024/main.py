import os
os.system("cls")

def aumenta(inicial: int, porcentagem:int, anos: int):
    valor = inicial
    for i in range(anos):
        valor += valor * (porcentagem / 100)
    return valor

print(aumenta(500, 20, 2))

def aumentav2(inicial, porcentagem, anos):
    return inicial*(1+porcentagem/100)**anos

print(aumentav2(500, 20 , 2))

def montante(inicial, porcentagem, meses):
    return inicial*(1+porcentagem/100)**meses

print(f"A) {montante(8000, 1, 3):.2f}")
print(f"B) {montante(8000, 1, 36):.2f}")
print("C) 8000 * (1+porcentagem/100)**t")
print(f"D) {montante(8000, 1, 60):.2f}") 