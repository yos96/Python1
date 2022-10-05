while True:
    print("""Opciones
    Ingrese '+' para sumar dos numeros
    Ingrese '-' para restar dos numeros
    Ingrese '*' para multiplicar dos numeros
    Ingrese '/' para dividir dos numeros
    Ingrese 'x' para finalizar""")

    teclado=input(":")

    if teclado=="x" or teclado=="X":
        break
    elif teclado=="+":
        num1=float(input("Ingrese un numero:"))
        num2=float(input("Ingrese otro numero:"))
        num3=float(input("Ingrese otro numero:"))
        result=str(num1+num2+num3)
        print("Respuesta: "+result)
    elif teclado=="-":
        num1=float(input("Ingrese un numero:"))
        num2=float(input("Ingrese otro numero:"))
        result=str(num1-num2)
        print("Respuesta: "+result)
    elif teclado=="*":
        num1=float(input("Ingrese un numero:"))
        num2=float(input("Ingrese otro numero:"))
        result=str(num1*num2)
        print("Respuesta: "+result)
    elif teclado=="/":
        try:
            num1=float(input("Ingrese un numero:"))
            num2=float(input("Ingrese otro numero:"))
            result=str(num1/num2)
            print("Respuesta: "+result)
        except ZeroDivisionError:
            print("Math Error: Division por 0")
    elif teclado=="%":
        try:
            num1=float(input("Ingrese un numero:"))
            num2=float(input("Ingrese otro numero:"))
            result=str(int(num1%num2))
            print("Respuesta: "+result)
        except ZeroDivisionError:
            print("Math Error: Division por 0")
    else:
        print("Opcion inválida")