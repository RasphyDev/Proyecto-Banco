# "time" para el tiempo
import time
filePath = __file__
ruta1 = filePath.replace("\\","/")
ruta = ruta1.strip("ProyectoBanco.py")



# definir menús
menuPrincipal = """
----------------------------------------------
|             Bienvenido al banco            |
|                                            |
|    [1] Iniciar Sesión                      |
|    [2] Crear cuenta                        |
|                                            |
----------------------------------------------
"""
menuCrearUsuario = """
----------------------------------------------
|               Crear cuenta:                |
|                                            |
|       Escribe los datos necesarios         |
|       para crear una cuenta:               |
|                                            |
"""
menuIniciarSesion = """
----------------------------------------------
|             Iniciar Sesion:                |
|                                            |
|       Escribe los datos necesarios         |
|       para iniciar sesion:                 |
|                                            |
"""

def inicio():
        print(menuPrincipal)

        opcionMenu = input("Elige una opcion: ")

        # opcion de iniciar sesion
        def opcion1():
                print(menuIniciarSesion)
                preguntarUsuario = input("Escribe tu nombre de usuario: ")
                try:
                    NombreUsuario = open("c"+ruta+"/Datos/Usuarios/usuario_{}.txt".format(preguntarUsuario),"r")
                    nombreUsuario = NombreUsuario.read()
                    NombreUsuario.close()

                except FileNotFoundError:
                    print("No se encuentra una cuenta con ese nombre.")
                    print("Espera 4 segundos para volverlo a intentar")
                    time.sleep(4)
                    opcion1()

                
                preguntarContraseña = input("Escribe tu contraseña: ")
                datoContraseña = open("c"+ruta+"Datos/Contraseñas/contraseña_{}.txt".format(nombreUsuario),"r")
                contraseña = datoContraseña.read()
                datoContraseña.close()

                if preguntarContraseña == contraseña:
                    abrirDineroLeer = open("c"+ruta+"Datos/Dinero usuarios/dinero_{}.txt".format(nombreUsuario),"r")
                    dinero = int(abrirDineroLeer.read())
                    abrirDineroLeer.close()
                    def tuCuenta():
                        abrirDineroLeer = open("c"+ruta+"Datos/Dinero usuarios/dinero_{}.txt".format(nombreUsuario),"r")
                        dinero = int(abrirDineroLeer.read())
                        abrirDineroLeer.close()
                        print("----------------------------------------------")
                        print("|                 Tu cuenta:                 |")
                        print("|                                            |")
                        print("|         Saldo: {} {}                       |".format(dinero,"€"))
                        print("|                                            |")
                        print("|         Opciones:                          |")
                        print("|         [1] Ingresar dinero                |")
                        print("|         [2] Sacar dinero                   |")
                        print("|                                            |")
                        opcionesCuenta = input("Elige una opcion: ")
                        if opcionesCuenta == "1":

                            def ingresarDinero(dineroIngresar):
                                abrirDineroLeer = open("c"+ruta+"Datos/Dinero usuarios/dinero_{}.txt".format(nombreUsuario),"r")
                                dinero = int(abrirDineroLeer.read())
                                abrirDineroLeer.close()
                                dinero = dinero + dineroIngresar
                                print("{} € ingresados correctamente".format(dineroIngresar))
                                print("Redirigiendo...Espera 4 segundos")
                                abrirDineroEscribir = open("c"+ruta+"Datos/Dinero usuarios/dinero_{}.txt".format(nombreUsuario),"w")
                                time.sleep(4)
                                abrirDineroEscribir.write(str(dinero))
                                abrirDineroEscribir.close()
                                tuCuenta()
                            
                            print("----------------------------------------------")
                            print("|              Ingresar dinero:              |")
                            print("|                                            |")
                            print("|         Saldo: {} {}                       |".format(dinero,"€"))
                            print("|                                            |")
                            print("|         Ingresar:                          |")
                            print("|      [1] 10€    [2] 50€    [3] 100€        |")
                            print("|      [4] 500€   [5] 1000€  [6] Elegir      |")
                            print("|                                            |")
                            opcionesIngresar = input("Elige una opcion: ")
                            if opcionesIngresar == "1":
                                ingresarDinero(10)
                            elif opcionesIngresar == "2":
                                ingresarDinero(50)
                            elif opcionesIngresar == "3":
                                ingresarDinero(100)
                            elif opcionesIngresar == "4":
                                ingresarDinero(500)
                            elif opcionesIngresar == "5":
                                ingresarDinero(1000)
                            elif opcionesIngresar == "6":

                                preguntarDineroIngresar = input("Escribe una cantidad de dinero: ")
                                if preguntarDineroIngresar.isnumeric():
                                    
                                    if int(preguntarDineroIngresar) <= 1000000000:
                                        dinero = dinero + int(preguntarDineroIngresar)
                                        print("{} € ingresados correctamente".format(preguntarDineroIngresar))
                                        print("Redirigiendo...Espera 4 segundos")
                                        abrirDineroEscribir = open("c"+ruta+"Datos/Dinero usuarios/dinero_{}.txt".format(nombreUsuario),"w")
                                        abrirDineroEscribir.write(str(dinero))
                                        abrirDineroEscribir.close()
                                        time.sleep(4)
                                        tuCuenta()
                                    else:
                                        print("No creo que tengas tanto dinero para meter  =D")
                                        print("Espera 4 segundos para reintentar")
                                        time.sleep(4)
                                        tuCuenta()
                                else:
                                    print("No puedes ingresar letras")
                                    print("Espera 4 segundos para reintentar")
                                    time.sleep(4)
                                    tuCuenta()

                        elif opcionesCuenta == "2":

                            # comprobadorDinero comprueba si hay suficiente dinero para sacar y repite todo
                            def comprobadorDinero(dineroComprobar):
                                abrirDineroLeer = open("c"+ruta+"Datos/Dinero usuarios/dinero_{}.txt".format(nombreUsuario),"r")
                                dinero = int(abrirDineroLeer.read())
                                abrirDineroLeer.close()
                                if dinero < dineroComprobar:
                                    print("No hay dinero suficiente para sacar de tu cuenta")
                                    print("Redirigiendo...Espera 4 segundos")
                                    time.sleep(4)
                                    tuCuenta()

                                else:
                                    dinero = dinero - dineroComprobar
                                    print("{} € retirados correctamente".format(dineroComprobar))
                                    print("Redirigiendo...Espera 4 segundos")
                                    abrirDineroSacar = open("c"+ruta+"Datos/Dinero usuarios/dinero_{}.txt".format(nombreUsuario),"w")
                                    time.sleep(4)
                                    abrirDineroSacar.write(str(dinero))
                                    abrirDineroSacar.close()
                                    tuCuenta()

                            print("----------------------------------------------")
                            print("|                Sacar dinero:               |")
                            print("|                                            |")
                            print("|         Saldo: {} {}                          |".format(dinero,"€"))
                            print("|                                            |")
                            print("|         Sacar:                             |")
                            print("|      [1] 10€    [2] 50€    [3] 100€        |")
                            print("|      [4] 500€   [5] 1000€  [6] Elegir      |")
                            print("|                                            |")
                            opcionesSacar = input("Elige una opcion: ")
                            if opcionesSacar == "1":
                                comprobadorDinero(10)
                            elif opcionesSacar == "2":                           
                                comprobadorDinero(50)
                            elif opcionesSacar == "3":
                                comprobadorDinero(100)
                            elif opcionesSacar == "4":
                                comprobadorDinero(500)
                            elif opcionesSacar == "5":
                                comprobadorDinero(1000)
                            elif opcionesSacar == "6":
                                preguntarDineroSacar = input("Escribe una cantidad de dinero: ")
                                if preguntarDineroSacar.isnumeric():
                                    if int(preguntarDineroSacar) < 0:
                                        dinero = dinero - int(preguntarDineroSacar)
                                        print("{} € retirados correctamente".format(preguntarDineroSacar))
                                        print("Redirigiendo...Espera 4 segundos")
                                        abrirDineroSacar = open("c"+ruta+"Datos/Dinero usuarios/dinero_{}.txt".format(nombreUsuario),"w")
                                        abrirDineroSacar.write(str(dinero))
                                        abrirDineroSacar.close()
                                        time.sleep(4)
                                        tuCuenta()
                                    else:
                                        print("No tienes suficiente dinero para sacar  =D")
                                        print("Espera 4 segundos para reintentar")
                                        time.sleep(4)
                                        tuCuenta()
                                else:
                                    print("No puedes sacar letras")
                                    print("Espera 4 segundos para reintentar")
                                    time.sleep(4)
                                    tuCuenta()

                        else:
                            print("Elige una opcion valida, intentalo de nuevo")
                            print("Espera 4 segundos para reintentar")
                            time.sleep(4)
                            tuCuenta()

                    tuCuenta()
                    
                else:
                    print("La contraseña no es válida.")
                    print("Espera 4 segundos para reintentar.")
                    time.sleep(4)
                    opcion1()
                
            # opcion crear usuario
        def opcion2():
        
                print(menuCrearUsuario)
                usuarioCrear = input("| Escribe un nombre de usuario: ")
                datoNombreUsuario = open("c"+ruta+"Datos/Usuarios/usuario_{}.txt".format(usuarioCrear),"w")
                datoNombreUsuario.write(usuarioCrear)   
                datoNombreUsuario.close()
                dinero = open("c"+ruta+"Datos/Dinero usuarios/dinero_{}.txt".format(usuarioCrear),"w")
                dinero.write("0")
                dinero.close()
                datoContraseña = open("c"+ruta+"Datos/Contraseñas/contraseña_{}.txt".format(usuarioCrear),"w")      
                contraseñaCrear = input ("| Escribe una contraseña: ")
                contraseñaVerificar = input ("| Escribe otra vez la contraseña: ")
                if contraseñaCrear == contraseñaVerificar:
                        datoContraseña.write(contraseñaCrear)
                        print("   Cuenta creada ")
                        print("----------------------------")
                        print("Redirigiendo al menu principal...")
                        print("Espera 4 segundos")
                        time.sleep(4)
                        datoContraseña.close()
                        inicio()
                else:
                        print("Las contraseñas no coinciden, intentalo de nuevo.")
                        print("--------------------------------------------------")
                        print("Espera 4 segundos.")
                        time.sleep(4)
                        datoContraseña.close()
                        opcion2()
               
                
                
        


        if opcionMenu == "1":
                opcion1()

        elif opcionMenu == "2":
                opcion2()

        else:
                print("Elige una opcion valida.")
                print("Espera 4 segundos para volverlo a intentar")
                time.sleep(4)
                inicio()

inicio()