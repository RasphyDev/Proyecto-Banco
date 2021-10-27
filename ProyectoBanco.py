# "time" para el tiempo
import time

# "re" para conmprobar las letras especiales
import re

import os
filePath = os.path.dirname(os.path.realpath(__file__))
ruta1 = filePath.replace("\\","/")
ruta = ruta1.strip("ProyectoBanco.py")

# "datetime para la fecha"
from datetime import datetime
from datetime import date

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
                    NombreUsuario = open(ruta+"/Datos/Usuarios/usuario_{}.txt".format(preguntarUsuario),"r")
                    nombreUsuario = NombreUsuario.read()
                    NombreUsuario.close()

                except FileNotFoundError:
                    print("No se encuentra una cuenta con ese nombre.")
                    print("Espera 4 segundos para volverlo a intentar")
                    time.sleep(4)
                    opcion1()

                
                preguntarContraseña = input("Escribe tu contraseña: ")
                datoContraseña = open(ruta+"/Datos/Contraseñas/contraseña_{}.txt".format(nombreUsuario),"r")
                contraseña = datoContraseña.read()
                datoContraseña.close()

                if preguntarContraseña == contraseña:
                    abrirDineroLeer = open(ruta+"/Datos/Dinero usuarios/dinero_{}.txt".format(nombreUsuario),"r")
                    dinero = int(abrirDineroLeer.read())
                    abrirDineroLeer.close()
                    def tuCuenta():
                        abrirDineroLeer = open(ruta+"/Datos/Dinero usuarios/dinero_{}.txt".format(nombreUsuario),"r")
                        dinero = int(abrirDineroLeer.read())
                        abrirDineroLeer.close()
 
                        def historial(accion):
                            historialAbrir = open(ruta+"/Datos/Historial/historial_{}.txt".format(nombreUsuario),"a")
                            now = datetime.now()
                            hora = str(now.hour)
                            minuto = str(now.minute)
                            fecha = str(date.today())+" "+hora+":"+minuto
                            historialAbrir.write("|"+fecha+" "+accion+"\n")
                            historialAbrir.close()

                            historialAbrir = open(ruta+"/Datos/Historial/historial_{}.txt".format(nombreUsuario),"r")
                            lineas = historialAbrir.readlines()

                            historialAbrir.close()
                            numeroLineas = len(lineas)
                            if numeroLineas > 30:
                                with open(ruta+"/Datos/Historial/historial_{}.txt".format(nombreUsuario), 'r') as fin:
                                    data = fin.read().splitlines(True)
                                with open(ruta+"/Datos/Historial/historial_{}.txt".format(nombreUsuario), 'w') as fout:
                                    fout.writelines(data[1:])
                            else:
                                pass

                        print("----------------------------------------------")
                        print("|              Bienvenido, {}             ".format(nombreUsuario))
                        print("|                                            |")
                        print("|         Saldo: {} {}                       ".format(dinero,"€"))
                        print("|                                            |")
                        print("|         Opciones:                          |")
                        print("|         [1] Ingresar dinero                |")
                        print("|         [2] Sacar dinero                   |")
                        print("|         [3] Historial                      |")
                        print("|         [4] Cambiar contraseña             |")
                        print("|         [5] Transferir                     |")
                        print("|         [6] Cerrar sesion                  |")
                        print("|                                            |")

                        opcionesCuenta = input("Elige una opcion: ")
                        if opcionesCuenta == "1":

                            def ingresarDinero(dineroIngresar):
                                abrirDineroLeer = open(ruta+"/Datos/Dinero usuarios/dinero_{}.txt".format(nombreUsuario),"r")
                                dinero = int(abrirDineroLeer.read())
                                abrirDineroLeer.close()
                                dinero = dinero + dineroIngresar
                                print("{} € ingresados correctamente".format(dineroIngresar))
                                print("Redirigiendo...Espera 4 segundos")
                                historial("Ingresados {} €".format(dineroIngresar))
                                abrirDineroEscribir = open(ruta+"/Datos/Dinero usuarios/dinero_{}.txt".format(nombreUsuario),"w")
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
                                        abrirDineroEscribir = open(ruta+"/Datos/Dinero usuarios/dinero_{}.txt".format(nombreUsuario),"w")
                                        abrirDineroEscribir.write(str(dinero))
                                        historial("Ingresados {} €".format(preguntarDineroIngresar))
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
                                abrirDineroLeer = open(ruta+"/Datos/Dinero usuarios/dinero_{}.txt".format(nombreUsuario),"r")
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
                                    historial("Sacados {} €".format(dineroComprobar))
                                    abrirDineroSacar = open(ruta+"/Datos/Dinero usuarios/dinero_{}.txt".format(nombreUsuario),"w")
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
                                    if int(preguntarDineroSacar) < dinero:
                                        dinero = dinero - int(preguntarDineroSacar)
                                        print("{} € retirados correctamente".format(preguntarDineroSacar))
                                        print("Redirigiendo...Espera 4 segundos")
                                        historial("Sacados {} €".format(preguntarDineroSacar))
                                        abrirDineroSacar = open(ruta+"/Datos/Dinero usuarios/dinero_{}.txt".format(nombreUsuario),"w")
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
                                print("Elige una opcion valida")
                                print("Espera 4 segundos para reintentar")
                                time.sleep(4)
                                tuCuenta()

                        elif opcionesCuenta == "3":
                            historialAbrir = open(ruta+"/Datos/Historial/historial_{}.txt".format(nombreUsuario),"r+")
                            historial = historialAbrir.read()
                            print("----------------------------------------------")
                            print("|                 Historial:                 |")
                            print("|                                            |")
                            print(historial)
                            salir = input("Pulsa enter para salir")
                            historialAbrir.close
                            tuCuenta()

                        elif opcionesCuenta == "4":
                            print("----------------------------------------------")
                            print("|                                            |")
                            print("|            Cambiar contraseña              |")
                            print("|                                            |")
                            contraseñaCambiar = input("|Escribe tu contraseña actual: ")
                            datoContraseña = open(ruta+"/Datos/Contraseñas/contraseña_{}.txt".format(nombreUsuario),"r")
                            contraseña = datoContraseña.read()
                            datoContraseña.close()
                            if contraseñaCambiar == contraseña:
                                preguntarContraseñaCambiar = input("|Escribe tu nueva contraseña: ")
                                datoContraseña = open(ruta+"/Datos/Contraseñas/contraseña_{}.txt".format(nombreUsuario),"w")
                                datoContraseña.write(preguntarContraseñaCambiar)
                                datoContraseña.close()
                                historial("Se cambio la contraseña")
                                print("|¡Contraseña cambiada!")
                                print("Redirigiendo... Espera 4 segundos")
                                time.sleep(4)
                                tuCuenta()

                            else:
                                print("Contraseña incorrecta, intentalo de nuevo")
                                tuCuenta()

                        elif opcionesCuenta == "5":
                            def transferirDinero(dineroTransferir):
                                abrirDineroTransferirDar = open(ruta+"/Datos/Dinero usuarios/dinero_{}.txt".format(nombreUsuario),"r")
                                abrirDineroTransferirRecibir = open(ruta+"/Datos/Dinero usuarios/dinero_{}.txt".format(preguntarCuentaTransferir),"r")
                                dineroDar = int(abrirDineroTransferirDar.read())
                                dineroRecibir = int(abrirDineroTransferirRecibir.read())
                                abrirDineroTransferirDar.close()
                                abrirDineroTransferirRecibir.close()
                                if dineroDar < dineroTransferir:
                                    print("No hay dinero suficiente en tu cuenta para transferir")
                                    print("Redirigiendo...Espera 4 segundos")
                                    time.sleep(4)
                                    tuCuenta()
                                    
                                else:
                                    dineroDar = dineroDar - dineroTransferir
                                    dineroRecibir = dineroRecibir + dineroTransferir
                                    print("{} € transferidos correctamente".format(dineroTransferir))
                                    print("Redirigiendo...Espera 4 segundos")
                                    abrirDineroTransferirDarEscribir = open(ruta+"/Datos/Dinero usuarios/dinero_{}.txt".format(nombreUsuario),"w")
                                    abrirDineroTransferirRecibirEscribir = open(ruta+"/Datos/Dinero usuarios/dinero_{}.txt".format(preguntarCuentaTransferir),"w")

                                    historial("Transferidos {} € a {}".format(dineroTransferir, preguntarCuentaTransferir))
                                    historialAbrir = open(ruta+"/Datos/Historial/historial_{}.txt".format(preguntarCuentaTransferir),"a")
                                    accion = "Recibidos {} € de {}".format(dineroTransferir, nombreUsuario)
                                    now = datetime.now()
                                    hora = str(now.hour)
                                    minuto = str(now.minute)
                                    fecha = str(date.today())+" "+hora+":"+minuto
                                    historialAbrir.write("|"+fecha+" "+accion+"\n")
                                    historialAbrir.close()

                                    abrirDineroTransferirDarEscribir.write(str(dineroDar))
                                    abrirDineroTransferirRecibirEscribir.write(str(dineroRecibir))
                                    abrirDineroTransferirDarEscribir.close()
                                    abrirDineroTransferirRecibirEscribir.close()
                                    time.sleep(4)
                                    tuCuenta()

                            print("----------------------------------------------")
                            print("|                                            |")
                            print("|           Gestor de transacciones          |")
                            print("|                                            |")
                            print("|Escribe el nombre de la cuenta a la         |") 
                            preguntarCuentaTransferir = input("|que quieres transferir: ")
                            try:
                                NombreUsuario = open(ruta+"/Datos/Dinero usuarios/dinero_{}.txt".format(preguntarCuentaTransferir),"r")
                                NombreUsuario.close() 

                            except FileNotFoundError:
                                print("|No se encuentra una cuenta con ese nombre.")
                                print("|Prueba a distinguir entre MaYuSuLaS y mInUsCuLaS.")
                                print("|Espera 4 segundos para volverlo a intentar")
                                time.sleep(4)
                                tuCuenta()

                            print("----------------------------------------------")
                            print("| ¿Cuanto dinero quieres transferir a {}?  ".format(preguntarCuentaTransferir))
                            print("|                                            |")
                            print("|      Saldo: {} €                           ".format(dinero))
                            print("|                                            |")
                            print("|      [1] 10€    [2] 50€    [3] 100€        |")
                            print("|      [4] 500€   [5] 1000€  [6] Elegir      |")
                            print("|                                            |")
                            opcionesTransferir = input("|Elige una opcion: ")
                            if opcionesTransferir == "1":
                                transferirDinero(10)
                            elif opcionesTransferir == "2":
                                transferirDinero(50)
                            elif opcionesTransferir == "3":
                                transferirDinero(100)
                            elif opcionesTransferir == "4":
                                transferirDinero(500)
                            elif opcionesTransferir == "5":
                                transferirDinero(1000)
                            elif opcionesTransferir == "6":
                                preguntarDineroTransferir = input("|Escribe una cantidad de dinero: ")
                                if preguntarDineroTransferir.isnumeric():
                                    abrirDineroTransferirDar = open(ruta+"/Datos/Dinero usuarios/dinero_{}.txt".format(nombreUsuario),"r")
                                    abrirDineroTransferirRecibir = open(ruta+"/Datos/Dinero usuarios/dinero_{}.txt".format(preguntarCuentaTransferir),"r")
                                    dineroDar = int(abrirDineroTransferirDar.read())
                                    dineroRecibir = int(abrirDineroTransferirRecibir.read())
                                    abrirDineroTransferirDar.close()
                                    abrirDineroTransferirRecibir.close()
                                    if int(preguntarDineroTransferir) < dineroDar:
                                        dineroDar = dineroDar - int(preguntarDineroTransferir)
                                        dineroRecibir = dineroRecibir + int(preguntarDineroTransferir)
                                        print("{} € transferidos correctamente".format(preguntarDineroTransferir))
                                        print("Redirigiendo...Espera 4 segundos")
                                        abrirDineroTransferirDarEscribir = open(ruta+"/Datos/Dinero usuarios/dinero_{}.txt".format(nombreUsuario),"w")
                                        abrirDineroTransferirRecibirEscribir = open(ruta+"/Datos/Dinero usuarios/dinero_{}.txt".format(preguntarCuentaTransferir),"w")
                                        
                                        historial("Transferidos {} € a {}".format(preguntarDineroTransferir, preguntarCuentaTransferir))
                                        historialAbrir = open(ruta+"/Datos/Historial/historial_{}.txt".format(preguntarCuentaTransferir),"a")
                                        accion = "Recibidos {} € de {}".format(preguntarDineroTransferir, nombreUsuario)
                                        now = datetime.now()
                                        hora = str(now.hour)
                                        minuto = str(now.minute)
                                        fecha = str(date.today())+" "+hora+":"+minuto
                                        historialAbrir.write("|"+fecha+" "+accion+"\n")
                                        historialAbrir.close()
                                        abrirDineroTransferirDarEscribir.write(str(dineroDar))
                                        abrirDineroTransferirRecibirEscribir.write(str(dineroRecibir))
                                        abrirDineroTransferirDarEscribir.close()
                                        abrirDineroTransferirRecibirEscribir.close()

                                        time.sleep(4)
                                        tuCuenta()

                                    else:
                                        print("No tienes suficiente dinero para transferir  =D")
                                        print("Espera 4 segundos para reintentar")
                                        time.sleep(4)
                                        tuCuenta()
                                        
                                    
                                else:
                                    print("No puedes transferir letras")
                                    print("Espera 4 segundos para reintentar")
                                    time.sleep(4)
                                    tuCuenta()
    

                        elif opcionesCuenta == "6":
                            inicio()

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
                comprobarCaracteres = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
                if (comprobarCaracteres.search(usuarioCrear) == None):
                    datoNombreUsuario = open(ruta+"/Datos/Usuarios/usuario_{}.txt".format(usuarioCrear),"w")
                    datoNombreUsuario.write(usuarioCrear)   
                    datoNombreUsuario.close()
                    dinero = open(ruta+"/Datos/Dinero usuarios/dinero_{}.txt".format(usuarioCrear),"w")
                    dinero.write("0")
                    dinero.close()
                    datoContraseña = open(ruta+"/Datos/Contraseñas/contraseña_{}.txt".format(usuarioCrear),"w")      
                    contraseñaCrear = input ("| Escribe una contraseña: ")
                    contraseñaVerificar = input ("| Escribe otra vez la contraseña: ")
                    if contraseñaCrear == contraseñaVerificar:
                            datoContraseña.write(contraseñaCrear)
                            historialAbrir = open(ruta+"/Datos/Historial/historial_{}.txt".format(usuarioCrear),"w")
                            historialAbrir.close()
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
               
                else:
                    print("Tu nombre de usuario no puede tener caracteres especiales")
                    print("----------------------------------------------------------")
                    print("Espera 4 segundos para reintentar.")
                    time.sleep(4)
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
