#todas las UIs mal hechas...

import time


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

        def opcion1():
        
                print(menuIniciarSesion)
                preguntarUsuario = input("Escribe tu nombre de usuario: ")
                NombreUsuario = open("Proyecto Banco Beta/Datos/Usuarios/usuario_{}.txt".format(preguntarUsuario),"r")
                nombreUsuario = NombreUsuario.read()
                NombreUsuario.close()

                if preguntarUsuario == nombreUsuario:
                        preguntarContraseña = input("Escribe tu contraseña: ")
                        datoContraseña = open("Proyecto Banco Beta/Datos/Contraseñas/contraseña_{}.txt".format(nombreUsuario),"r")
                        contraseña = datoContraseña.read()
                        datoContraseña.close()
                        if preguntarContraseña == contraseña:
                                def tuCuenta():
                                        abrirDineroLeer = open("Proyecto Banco Beta/Datos/Dinero usuarios/dinero_{}.txt".format(nombreUsuario),"r")
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
                                                abrirDineroEscribir = open("Proyecto Banco Beta/Datos/Dinero usuarios/dinero_{}.txt".format(nombreUsuario),"w")       
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
                                                        dinero = dinero + 10
                                                        print("10 € ingresados correctamente")
                                                        print("Redirigiendo...Espera 6 segundos")
                                                        time.sleep(6)
                                                        abrirDineroEscribir.write(str(dinero))
                                                        abrirDineroEscribir.close()
                                                        tuCuenta()
                                                elif opcionesIngresar == "2":
                                                        dinero = dinero + 50
                                                        print("50 € ingresados correctamente")
                                                        print("Redirigiendo...Espera 6 segundos")
                                                        abrirDineroEscribir.write(str(dinero))
                                                        abrirDineroEscribir.close()
                                                        time.sleep(6)
                                                        tuCuenta()
                                                elif opcionesIngresar == "3":
                                                        dinero = dinero + 100
                                                        print("100 € ingresados correctamente")
                                                        print("Redirigiendo...Espera 6 segundos")
                                                        abrirDineroEscribir.write(str(dinero))
                                                        abrirDineroEscribir.close()
                                                        time.sleep(6)
                                                        tuCuenta()
                                                elif opcionesIngresar == "4":
                                                        dinero = dinero + 500
                                                        print("500 € ingresados correctamente")
                                                        print("Redirigiendo...Espera 6 segundos")
                                                        abrirDineroEscribir.write(str(dinero))
                                                        abrirDineroEscribir.close()
                                                        time.sleep(6)
                                                        tuCuenta()
                                                elif opcionesIngresar == "5":
                                                        dinero = dinero + 1000
                                                        print("1000 € ingresados correctamente")
                                                        print("Redirigiendo...Espera 6 segundos")
                                                        abrirDineroEscribir.write(str(dinero))
                                                        abrirDineroEscribir.close()
                                                        time.sleep(6)
                                                        tuCuenta()
                                                elif opcionesIngresar == "6":
                                                        preguntarDineroIngresar = input("Escribe una cantidad de dinero: ")
                                                        if preguntarDineroIngresar.isnumeric():
                                                                if int(preguntarDineroIngresar) <= 1000000000:
                                                                        dinero = dinero + int(preguntarDineroIngresar)
                                                                        print("{} € ingresado correctamente".format(preguntarDineroIngresar))
                                                                        print("Redirigiendo...Espera 6 segundos")
                                                                        abrirDineroEscribir.write(str(dinero))
                                                                        abrirDineroEscribir.close()
                                                                        time.sleep(6)
                                                                        tuCuenta()
                                                                else:
                                                                        print("No creo que tengas tanto dinero para meter  =D")
                                                                        abrirDineroEscribir.close()
                                                                        tuCuenta()
                                                        else:
                                                                print("No puedes ingresar letras")
                                                                print("Espera 6 segundos para reintentar")
                                                                time.sleep(6)
                                                                abrirDineroEscribir.close()
                                                                tuCuenta()

                                                else:
                                                        print("Elige una opcion valida")
                                                        print("Espera 6 segundos para reintentar")
                                                        time.sleep(6)
                                                        abrirDineroEscribir.write(str(dinero))
                                                        abrirDineroEscribir.close()
                                                        tuCuenta()


                                        elif opcionesCuenta == "2":
                                                abrirDineroEscribir1 = open("Proyecto Banco Beta/Datos/Dinero usuarios/dinero_{}.txt".format(nombreUsuario),"w")
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
                                                        if dinero >= 10:
                                                                dinero = dinero - 10
                                                                print("10 € sacados correctamente")
                                                                print("Redirigiendo...Espera 6 segundos")
                                                                abrirDineroEscribir1.write(str(dinero))
                                                                abrirDineroEscribir1.close()
                                                                time.sleep(6)
                                                                tuCuenta()
                                                        else:
                                                                print("No tienes suficiente dinero para sacar")  
                                                                print("Espera 6 segundos para reintentar")
                                                                time.sleep(6)
                                                                abrirDineroEscribir1.write(str(dinero))
                                                                tuCuenta()
                                                elif opcionesSacar == "2":
                                                        dinero = dinero - 50
                                                        print("50 € sacados correctamente")
                                                        print("Redirigiendo...Espera 6 segundos")
                                                        abrirDineroEscribir1.write(str(dinero))
                                                        abrirDineroEscribir1.close()
                                                        time.sleep(6)
                                                        tuCuenta()
                                                elif opcionesSacar == "3":
                                                        dinero = dinero - 100
                                                        print("100 € sacados correctamente")
                                                        print("Redirigiendo...Espera 6 segundos")
                                                        abrirDineroEscribir1.write(str(dinero))
                                                        abrirDineroEscribir1.close()
                                                        time.sleep(6)
                                                        tuCuenta()
                                                elif opcionesSacar == "4":
                                                        dinero = dinero - 500
                                                        print("500 € sacados correctamente")
                                                        print("Redirigiendo...Espera 6 segundos")
                                                        abrirDineroEscribir1.write(str(dinero))
                                                        abrirDineroEscribir1.close()
                                                        time.sleep(6)
                                                        tuCuenta()
                                                elif opcionesSacar == "5":
                                                        dinero = dinero - 1000
                                                        print("1000 € sacados correctamente")
                                                        print("Redirigiendo...Espera 6 segundos")
                                                        abrirDineroEscribir1.write(str(dinero))
                                                        abrirDineroEscribir1.close()
                                                        time.sleep(6)
                                                        tuCuenta()
                                                elif opcionesSacar == "6":
                                                        preguntarDineroSacar = input("Escribe una cantidad de dinero: ")
                                                        if preguntarDineroSacar.isnumeric():
                                                                dinero = dinero - int(preguntarDineroSacar)
                                                                print("{} € sacados correctamente".format(preguntarDineroSacar))
                                                                print("Redirigiendo...Espera 6 segundos")
                                                                abrirDineroEscribir1.write(str(dinero))
                                                                abrirDineroEscribir1.close()
                                                                time.sleep(6)
                                                                tuCuenta()
                                                        else:
                                                                print("No puedes ingresar letras")
                                                                print("Espera 6 segundos para reintentar")
                                                                time.sleep(6)
                                                                abrirDineroEscribir1.close()
                                                                tuCuenta()
                                                        
                                                else:
                                                        print("Elige una opcion valida")
                                                        print("Espera 6 segundos para reintentar")
                                                        time.sleep(6)
                                                        abrirDineroEscribir1.write(str(dinero))
                                                        abrirDineroEscribir1.close()
                                                        tuCuenta()


                                        else:
                                                print("Elige una opcion valida, intentalo de nuevo")
                                                print("Espera 6 segundos para reintentar")
                                                time.sleep(6)
                                                tuCuenta()
                                tuCuenta()
                
                        else:
                                print("La contraseña no es válida.")
                                print("Espera 6 segundos para reintentar.")
                                time.sleep(6)
                                opcion1()

        
                else:
                        print("No se encuentra una cuenta con ese nombre.")
                        print("Espera 6 segundos para volverlo a intentar")
                        time.sleep(6)
                        opcion1()
        def opcion2():
        
                print(menuCrearUsuario)
                usuarioCrear = input("| Escribe un nombre de usuario: ")
                datoNombreUsuario = open("Proyecto Banco Beta/Datos/Usuarios/usuario_{}.txt".format(usuarioCrear),"w")
                datoNombreUsuario.write(usuarioCrear)   
                datoNombreUsuario.close()
                dinero = open("Proyecto Banco Beta/Datos/Dinero usuarios/dinero_{}.txt".format(usuarioCrear),"w")
                dinero.write("0")
                dinero.close()
                datoContraseña = open("Proyecto Banco Beta/Datos/Contraseñas/contraseña_{}.txt".format(usuarioCrear),"w")      
                contraseñaCrear = input ("| Escribe una contraseña: ")
                contraseñaVerificar = input ("| Escribe otra vez la contraseña: ")
                if contraseñaCrear == contraseñaVerificar:
                        datoContraseña.write(contraseñaCrear)
                        print("   Cuenta creada ")
                        print("----------------------------")
                        print("Redirigiendo al menu principal...")
                        print("Espera 6 segundos")
                        time.sleep(6)
                        datoContraseña.close()
                        inicio()
                else:
                        print("Las contraseñas no coinciden, intentalo de nuevo.")
                        print("--------------------------------------------------")
                        print("Espera 6 segundos.")
                        time.sleep(6)
                        datoContraseña.close()
                        opcion2()
               
                
                
        


        if opcionMenu == "1":
                opcion1()

        elif opcionMenu == "2":
                opcion2()

        else:
                print("Elige una opcion valida.")
                print("Espera 6 segundos para volverlo a intentar")
                time.sleep(6)
                inicio()

inicio()