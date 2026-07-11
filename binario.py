Prefijo_bin = (128,64,32,16,8,4,2,1)
prefijo_bin = (8,4,2,1)
Historial = {}
prefijo_hexa = {'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
prefijo_Hexa = {10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
print("______Transformador de Sistemas de Númeración.______")
print(f'\n-  Menú;  \n 1. Binario -> Decimal \n 2. Decimal -> Binario \n 3. Hexadecimal -> Decimal \n 4. Binario -> Hexadecimal \n 5. Decimal -> Hexadecimal \n 6. Historial \n 7. Salida')  
while True:
    opcion = input('Ingrese una de las opciones enumeradas; ')
 
    if opcion == '1':
        print("\n_____Convertidor de Binario a Decimal._____")
        número10 = 0
        binario = input('Ingrese un número binario: ')
        while len(binario) != 8 or any(caracter not in '01' for caracter in binario):
            print("Debe tener 8 caracteres binarios (1 o 0)")
            binario = input('Ingrese un número binario:')
        for bit, valor in zip(binario, Prefijo_bin):
            if bit == '1':
                número10 += valor
            elif bit == '0':
                número10 += 0
        print(f"Tú número binario {binario}, pasado a decimal es {número10}.")
        Historial[binario] = número10
    
    elif opcion == '2':
        print('\n_____Convertidor de Decimal a binario._____')         
        try:
            Decimal = int(input('Ingrese un número: '))
            while Decimal < 0 or Decimal > 255:
                print("Debe ser un número entero entre 0 y 255.")
                Decimal = int(input('Ingrese un número: '))
            copia = str(Decimal)
            resultado = ""
            for i in Prefijo_bin:
                if Decimal >= i:
                    resultado += "1"
                    Decimal = Decimal - i 
                elif Decimal < i:
                    resultado += "0"
                    Decimal = Decimal
            print(f"Tú número decimal {copia}, pasado a binario es {resultado}.")
            Historial[copia] = resultado
        except:
            print('Prohibido Ingresar letras, Devuelta al Menú...')
        Historial[copia] = resultado
    
    elif opcion == '3':
        print('\n_____Convertidor de Hexadecimal a Decimal._____') #trabajo en progreso...
        '''num_hexa = input('Ingrese un Número Hexadecimal: ')
        while len(num_hexa) != 2 or any(caracter not in '0123456789ABCDEFabcdef' for caracter in num_hexa):
            num_hexa = input('Ingrese un Número Hexadecimal: ')
        for j in num_hexa:
            if  "1234567890" in num_hexa:
                j = int(j)
            elif  'ABCDEF' in num_hexa.upper(j):
                j = prefijo_hexa[j]'''
                
    elif opcion == '4':
        print('\n____Convertidor de binario a hexadecimal.____')
        num_binario = input('Ingrese un número binario; ')
        while len(num_binario) != 4 or any(caracter not in '01' for caracter in num_binario):  
            print("Debe tener 4 caracteres binarios (1 o 0)")
            num_binario = input('Ingrese un número binario; ')
        numero16 = 0
        for Valor, BIT in zip(prefijo_bin, num_binario):
            if BIT == '1':
                numero16 += Valor
            elif BIT == '0':
                numero16 += 0
        if numero16 >= 10:
            numero16 = prefijo_Hexa[numero16]
        else:
            numero16 = str(numero16)
        print(f'Tú número binario {num_binario}, pasado a Hexadecimal es {numero16}')
        Historial[num_binario] = numero16
    
    elif opcion == '5':
        print('\n_____Convertidor de Decimal a hexadecimal._____')
        try:
            decimal = int(input('Ingrese un Número Decimal'))
            while decimal <= 0 or decimal > 255:
                print('Tiene que ser positivo.')
                decimal = int(input('Ingrese un Número Decimal'))
            resultado_hexadecimal = ''
            decimal1 = decimal
            decimal2 = decimal
            divisor = decimal1 // 16 
            if 0 <= divisor <= 9:
                resultado_hexadecimal += str(divisor)
            else:
                resultado_hexadecimal += prefijo_Hexa[divisor]
            resto = decimal2 % 16
            if 0 <= resto <= 9:
                resultado_hexadecimal += str(resto)
            else:
                resultado_hexadecimal += prefijo_Hexa[resto]    
            print(decimal , resultado_hexadecimal)
        except:
            print('Solo se aceptan Números.')

    elif opcion == '6':    
        print('\n____Historial de Uso.____')
        for aporte_X, valor_X in Historial.items():
            print(f'  - {aporte_X} --> {valor_X}')
    
    elif opcion == '7':
        print('\n Cerrando programa...')
        break
    
    else:
        print("\n  Opción no valida, escribe '7' para cerrar el programa.")
                
