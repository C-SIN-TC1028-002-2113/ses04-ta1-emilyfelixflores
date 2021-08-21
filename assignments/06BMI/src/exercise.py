def main():
    #escribe tu código abajo de esta línea
    peso = float(input("Peso en kg: "))
    altura = float(input("Altura en m: "))

    if peso>0 and altura>0:
        if (peso/altura**2)<20:
            print("PESO BAJO")
        elif (peso/altura**2)<=20 or (peso/altura**2)<25:
            print("NORMAL")
        elif (peso/altura**2)<=25 or (peso/altura**2)<30:
            print("SOBREPESO")
        elif (peso/altura**2)<=30 or (peso/altura**2)<40:
            print("OBESIDAD")
        elif (peso/altura**2)>=40:
            print("OBESIDAD MORBIDA")
    else:
        print("Revisa tus datos, alguno de ellos es erróneo.")
    
    


if __name__=='__main__':
    main()