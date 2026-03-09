pais=input("Ingrese un pais (Ecuador-Colombia-Peru):")
zona=input("Ingrese el tipo de zona (Urbana-Rural-Perimetral)")
velocidad=float(input("Ingrese la velocidad"))

if pais=="Ecuador":
    if zona=="Urbana":
        if velocidad <10:
            print(f"estas por debajo de la velocidad minima (10 km/h)")
        elif velocidad>40:
            print("superaste la velocidad maxima permitida (40 km/h)")
        else:
            print("Velocidad normal")
    elif zona=="Rural":
         if velocidad <41:
            print("estas por debajo de la velocidad minima (41 km/h)")
         elif velocidad>60:
            print("superaste la velocidad maxima permitida (60 km/h)")
         else:
            print("Velocidad normal")
    elif zona=="Perimetral":
         if velocidad <61:
            print("estas por debajo de la velocidad minima (41 km/h)")
         elif velocidad>120:
            print("superaste la velocidad maxima permitida (60 km/h)")
         else:
            print("Velocidad normal")
    else:
        print("Ingrese una zona valida")
elif pais=="Colombia":
    if zona=="Urbana":
         if velocidad <10:
            print("estas por debajo de la velocidad minima (10 km/h)")
         elif velocidad>30:
            print("superaste la velocidad maxima permitida (30 km/h)")
         else:
            print("Velocidad normal")
    elif zona=="Rural":
         if velocidad <31:
            print("estas por debajo de la velocidad minima (31 km/h)")
         elif velocidad>80:
            print("superaste la velocidad maxima permitida (80 km/h)")
         else:
            print("Velocidad normal")
    elif zona=="Perimetral":
         if velocidad <81:
            print("estas por debajo de la velocidad minima (41 km/h)")
         elif velocidad>100:
            print("superaste la velocidad maxima permitida (60 km/h)")
         else:
            print("Velocidad normal")
    else:
        print("Ingrese una zona valida")
elif pais=="Peru":
    if zona=="Urbana":
         if velocidad <10:
            print("estas por debajo de la velocidad minima (10 km/h)")
         elif velocidad>40:
            print("superaste la velocidad maxima permitida (40 km/h)")
         else:
            print("Velocidad normal")
    elif zona=="Rural":
         if velocidad <41:
            print("estas por debajo de la velocidad minima (41 km/h)")
         elif velocidad>60:
            print("superaste la velocidad maxima permitida (60 km/h)")
         else:
            print("Velocidad normal")
    elif zona=="Perimetral":
         if velocidad <61:
            print("estas por debajo de la velocidad minima (61 km/h)")
         elif velocidad>120:
            print("superaste la velocidad maxima permitida (120 km/h)")
         else:
            print("Velocidad normal")
    else:
        print("Ingrese una zona valida")
else:
    print("Seleccione un pais valido")