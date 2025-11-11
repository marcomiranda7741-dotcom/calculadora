# calculadora.py
# Calculadora mejorada en Python

def calcular():
    while True:
        try:
            numero_1 = float(input("👉 Primer número: "))
            numero_2 = float(input("👉 Segundo número: "))
            operacion = input("👉 Operación (+, -, *, /) o 'q' para salir: ").strip()

            if operacion.lower() == 'q':
                print("👋 Saliendo de la calculadora...")
                break

            if operacion == '+':
                resultado = numero_1 + numero_2
            elif operacion == '-':
                resultado = numero_1 - numero_2
            elif operacion == '*':
                resultado = numero_1 * numero_2
            elif operacion == '/':
                if numero_2 == 0:
                    print("❌ Error: no se puede dividir por cero.")
                    continue
                resultado = numero_1 / numero_2
            else:
                print("⚠️ Operación no válida. Usa +, -, *, / o q para salir.")
                continue

            print(f"✅ Resultado: {resultado:.2f}\n")

        except ValueError:
            print("⚠️ Error: ingresa solo números válidos.\n")

if _name_ == "_main_":
    calcular()