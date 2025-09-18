def addmultiplenumbers(numbers):
    return sum(numbers)


def multiplymultiplenumbers(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product


def isiteven(num):
    if isinstance(num, int):
        return num % 2 == 0
    if isinstance(num, float):
        
        if num.is_integer():
            return int(num) % 2 == 0
    return False


def isitaninteger(num):
    if isinstance(num, int):
        return True
    if isinstance(num, float):
        return num.is_integer()
    return False


def main():
    print("Ingrese dos numeros para sumar:")
    print("Numero 1:")
    num1 = float(input())
    print("Numero 2:")
    num2 = float(input())
    suma = num1 + num2

    if suma.is_integer():
        print(int(suma))
    else:
        print(suma)

    # Funciones adicionales para después del pytest
    while True:
        print("\nElija la operacion adicional a realizar:")
        print("1. Restar")
        print("2. Multiplicar")
        print("3. Dividir")
        print("4. Modúlo(residuo de una division)")
        print("5. Sumar tres numeros")
        print("6. Operacion mixta con 3 o mas numeros")
        print("0. No hacer nada y probar pytest")

        opcion = input("Ingrese opcion: ")

        if opcion == "0":
            print("Chauuu...")
            break

        if opcion in ["1", "2", "3", "4"]:
            num3 = float(input("Ingrese primer numero: "))
            num4 = float(input("Ingrese segundo numero: "))

            if opcion == "1":
                print("Resultado:", num3 - num4)
            elif opcion == "2":
                print("Resultado:", num3 * 2, num4 * 2)
            elif opcion == "3":
                if num4 == 0:
                    print("Error: Division por cero no permitida")
                else:
                    print("Resultado:", num3 / num4)
            elif opcion == "4":
                if num4 == 0:
                    print("Error: Modulo por cero no permitido")
                else:
                    print("Resultado:", num3 % num4)

        elif opcion == "5":
            num3 = float(input("Numero 1: "))
            num4 = float(input("Numero 2: "))
            num1 = float(input("Numero 3: "))
            print("Resultado:", num3 + num4 + num1)

        elif opcion == "6":
            expr = input("Ingrese expresion matematica (ejemplo: 2 + 4 - 3 * 2): ")
            try:
                resultado = eval(expr)
                print("Resultado:", resultado)
            except Exception as e:
                print("Error en la expresion:", e)

        else:
            print("Opcion invalida, intente de nuevo.")


if __name__ == "__main__":
    main()
