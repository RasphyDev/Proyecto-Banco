# Sys para abir ventanas
import sys

# Importar PySide6
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QCloseEvent

# Os para saber la ruta
import os

# Re para conmprobar las letras especiales
import re

# Datetime para la fecha del historial
from datetime import datetime
from datetime import date

# Saber ruta
filePath = os.path.dirname(os.path.realpath(__file__))
ruta = filePath.replace("\\","/")

# Para poder importar .ui y definir app
loader = QUiLoader()
app = QtWidgets.QApplication(sys.argv)

# Actualiza los valores de dinero de ventanas
def actualizarDinero():
    abrirDineroLeer = open(ruta+"/Datos/Dinero usuarios/dinero_{}.txt".format(nombreUsuario),"r")
    dinero = int(abrirDineroLeer.read())
    abrirDineroLeer.close()
    ventanaTuCuenta.labelDinero.setText("Dinero: "+str(dinero)+" €")
    ventanaIngresarDinero.labelDinero.setText("Dinero: "+str(dinero)+" €")
    ventanaSacarDinero.labelDinero.setText("Dinero: "+str(dinero)+" €")
    ventanaTransferirDinero2.labelDinero.setText("Dinero: "+str(dinero)+" €")

# Crear una cuenta
def crearCuenta():
    usuarioCrear = ventanaCrearCuenta.lineEditUsuario.text()
    
    # Comprobar si el usuario ya existe
    if os.path.isfile(ruta+"/Datos/Usuarios/usuario_{}.txt".format(usuarioCrear)) == True:
        errorUsuario.show()
    else:
        pass

    # Comprobar si usuarioCrear tiene caracteres especiales y la contraseña
    comprobarCaracteres = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if (comprobarCaracteres.search(usuarioCrear) == None):
        datoContraseña = open(ruta+"/Datos/Contraseñas/contraseña_{}.txt".format(usuarioCrear),"w")      
        contraseñaCrear = ventanaCrearCuenta.lineEditContrasena.text()
        contraseñaVerificar = ventanaCrearCuenta.lineEditContrasenaVerificar.text()
        if contraseñaCrear == "" and contraseñaVerificar == "":
            errorContraseña3.show()
            datoContraseña.close()

        else:
            if contraseñaCrear == contraseñaVerificar:
                datoContraseña.write(contraseñaCrear)
                datoNombreUsuario = open(ruta+"/Datos/Usuarios/usuario_{}.txt".format(usuarioCrear),"w")
                datoNombreUsuario.write(usuarioCrear)   
                datoNombreUsuario.close()
                dinero = open(ruta+"/Datos/Dinero usuarios/dinero_{}.txt".format(usuarioCrear),"w")
                dinero.write("0")
                dinero.close()
                historialAbrir = open(ruta+"/Datos/Historial/historial_{}.txt".format(usuarioCrear),"w")
                historialAbrir.close()
                ventanaCrearCuenta.close()
                datoContraseña.close()
                ventanaCrearCuenta.lineEditUsuario.setText("")
                ventanaCrearCuenta.lineEditContrasena.setText("")
                ventanaCrearCuenta.lineEditContrasenaVerificar.setText("")
                correcto.show()
            else:
                errorContraseña.show()
                datoContraseña.close()
               
    else:
        errorContraseña2.show()

# Iniciar sesion
def iniciarSesion():
    # Comprobar que el usuario existe
    cuentaCorrecta = False
    preguntarUsuario = ventanaIniciarSesion.lineEditUsuario.text()
    try:
        NombreUsuario = open(ruta+"/Datos/Usuarios/usuario_{}.txt".format(preguntarUsuario),"r")
        global nombreUsuario
        cuentaCorrecta = True
        nombreUsuario = NombreUsuario.read()
        NombreUsuario.close()

    except FileNotFoundError:
        errorUsuario2.show()

    # Comprobar contraseña
    if cuentaCorrecta == True:
        preguntarContraseña = ventanaIniciarSesion.lineEditContrasena.text()
        datoContraseña = open(ruta+"/Datos/Contraseñas/contraseña_{}.txt".format(nombreUsuario),"r")
        contraseña = datoContraseña.read()
        datoContraseña.close()

        if preguntarContraseña == contraseña:
            ventanaInicio.close()
            ventanaIniciarSesion.close()
            tuCuenta()

        else:
            errorContraseña4.show()

    else:
        errorUsuario2.show()

# Ventana de acciones de cuenta
def tuCuenta():
    global dinero
    abrirDineroLeer = open(ruta+"/Datos/Dinero usuarios/dinero_{}.txt".format(nombreUsuario),"r")
    dinero = int(abrirDineroLeer.read())
    abrirDineroLeer.close()
    actualizarDinero()
    ventanaTuCuenta.show()
    
    
# Ingresar dinero
def ingresarDinero():

    actualizarDinero()
    ventanaIngresarDinero.show()

def ingresarDineroScript(dineroIngresar):
    abrirDineroLeer = open(ruta+"/Datos/Dinero usuarios/dinero_{}.txt".format(nombreUsuario),"r")
    dinero = int(abrirDineroLeer.read())
    abrirDineroLeer.close()
    dinero = dinero + int(dineroIngresar)
    historial("Ingresados {} €".format(dineroIngresar))
    abrirDineroEscribir = open(ruta+"/Datos/Dinero usuarios/dinero_{}.txt".format(nombreUsuario),"w")
    abrirDineroEscribir.write(str(dinero))
    abrirDineroEscribir.close()
    actualizarDinero()
    correcto.show()
    

def ingresarDineroCustomScript():
    preguntarDineroIngresar = ventanaPreguntarDineroIngresar.lineEdit.text()
    if preguntarDineroIngresar.isnumeric():
        if int(preguntarDineroIngresar) <= 1000000000:
            abrirDineroLeer = open(ruta+"/Datos/Dinero usuarios/dinero_{}.txt".format(nombreUsuario),"r")
            dinero = int(abrirDineroLeer.read())
            abrirDineroLeer.close()
            dinero = dinero + int(preguntarDineroIngresar)  
            ventanaPreguntarDineroIngresar.lineEdit.setText("")
            abrirDineroEscribir = open(ruta+"/Datos/Dinero usuarios/dinero_{}.txt".format(nombreUsuario),"w")
            abrirDineroEscribir.write(str(dinero))
            historial("Ingresados {} €".format(dinero))
            abrirDineroEscribir.close()
            actualizarDinero()
            ventanaPreguntarDineroIngresar.close()
            correcto.show()
        else:
            errorDinero.show()
    else:
        errorLetras.show()
    

# Sacar dinero  
def sacarDinero():
    actualizarDinero()
    ventanaSacarDinero.show()

# Comprueba si hay dinero suficiente y mas
def comprobadorDinero(dineroComprobar):
    abrirDineroLeer = open(ruta+"/Datos/Dinero usuarios/dinero_{}.txt".format(nombreUsuario),"r")
    dinero = int(abrirDineroLeer.read())
    abrirDineroLeer.close()

    if dineroComprobar <= dinero:
        dinero = dinero - int(dineroComprobar)
        historial("Sacados {} €".format(dineroComprobar))
        abrirDineroSacar = open(ruta+"/Datos/Dinero usuarios/dinero_{}.txt".format(nombreUsuario),"w")
        abrirDineroSacar.write(str(dinero))
        abrirDineroSacar.close()
        actualizarDinero()
        correcto.show()

    else:
        errorDinero2.show()

def comprobadorDineroCustom():
    ventanaPreguntarDineroSacar.show()
    preguntarDineroSacar = ventanaPreguntarDineroSacar.lineEdit.text()
    abrirDineroLeer = open(ruta+"/Datos/Dinero usuarios/dinero_{}.txt".format(nombreUsuario),"r")
    dinero = int(abrirDineroLeer.read())
    abrirDineroLeer.close()
    if preguntarDineroSacar.isnumeric():
        abrirDineroLeer = open(ruta+"/Datos/Dinero usuarios/dinero_{}.txt".format(nombreUsuario),"r")
        dinero = int(abrirDineroLeer.read())
        abrirDineroLeer.close()
        if int(preguntarDineroSacar) <= dinero:
            dinero = dinero - int(preguntarDineroSacar)
            correcto.show()
            historial("Sacados {} €".format(preguntarDineroSacar))
            abrirDineroSacar = open(ruta+"/Datos/Dinero usuarios/dinero_{}.txt".format(nombreUsuario),"w")
            abrirDineroSacar.write(str(dinero))
            abrirDineroSacar.close()
            actualizarDinero()
            ventanaPreguntarDineroSacar.close()
            ventanaPreguntarDineroSacar.lineEdit.setText("")
            correcto.show()
        else:
            errorDinero2.show()
    else:
        errorLetras.show()
    

# Ver ventana historial
def historialVer():
    historialAbrir = open(ruta+"/Datos/Historial/historial_{}.txt".format(nombreUsuario),"r+")
    textoHistorial = historialAbrir.read()
    historialAbrir.close
    ventanaHistorial.textEdit.setText(textoHistorial)
    ventanaHistorial.show()

# Escribe en el archivo del historial
def historial(accion):
    historialAbrir = open(ruta+"/Datos/Historial/historial_{}.txt".format(nombreUsuario),"a")
    now = datetime.now()
    hora = str(now.hour)
    minuto = str(now.minute)
    fecha = str(date.today())+" "+hora+":"+minuto
    historialAbrir.write(""+fecha+" "+accion+"\n")  
    historialAbrir.close()

    historialAbrir = open(ruta+"/Datos/Historial/historial_{}.txt".format(nombreUsuario),"r")
    lineas = historialAbrir.readlines()

    historialAbrir.close()
    numeroLineas = len(lineas)
    if numeroLineas > 100:
        with open(ruta+"/Datos/Historial/historial_{}.txt".format(nombreUsuario), 'r') as fin:
            data = fin.read().splitlines(True)
        with open(ruta+"/Datos/Historial/historial_{}.txt".format(nombreUsuario), 'w') as fout:
            fout.writelines(data[1:])
    else:
        pass

# Cambiar contraseña
def cambiarContraseña():
    contraseñaCambiar = ventanaCambiarContraseña.lineEditContrasenaActual.text()
    datoContraseña = open(ruta+"/Datos/Contraseñas/contraseña_{}.txt".format(nombreUsuario),"r")
    contraseña = datoContraseña.read()
    datoContraseña.close()
    if contraseñaCambiar == contraseña:
        preguntarContraseñaCambiar = ventanaCambiarContraseña.lineEditContrasenaNueva.text()
        datoContraseña = open(ruta+"/Datos/Contraseñas/contraseña_{}.txt".format(nombreUsuario),"w")
        datoContraseña.write(preguntarContraseñaCambiar)
        datoContraseña.close()
        historial("Se cambio la contraseña")
        ventanaCambiarContraseña.close()
        correcto.show()

    else:
        errorContraseña4.show()

# Transferir dinero

def transferirDineroScript(dineroTransferir):
    abrirDineroLeer = open(ruta+"/Datos/Dinero usuarios/dinero_{}.txt".format(nombreUsuario),"r")
    dinero = int(abrirDineroLeer.read())
    abrirDineroLeer.close()
    abrirDineroTransferirDar = open(ruta+"/Datos/Dinero usuarios/dinero_{}.txt".format(nombreUsuario),"r")
    abrirDineroTransferirRecibir = open(ruta+"/Datos/Dinero usuarios/dinero_{}.txt".format(preguntarCuentaTransferir),"r")
    dineroDar = int(abrirDineroTransferirDar.read())
    dineroRecibir = int(abrirDineroTransferirRecibir.read())
    abrirDineroTransferirDar.close()
    abrirDineroTransferirRecibir.close()
    if dineroTransferir <= dineroDar:
        dineroDar = dineroDar - dineroTransferir
        dineroRecibir = dineroRecibir + dineroTransferir
        abrirDineroTransferirDarEscribir = open(ruta+"/Datos/Dinero usuarios/dinero_{}.txt".format(nombreUsuario),"w")
        abrirDineroTransferirRecibirEscribir = open(ruta+"/Datos/Dinero usuarios/dinero_{}.txt".format(preguntarCuentaTransferir),"w")
        historialAbrirTu = open(ruta+"/Datos/Historial/historial_{}.txt".format(nombreUsuario),"a")
        historialAbrirOtro = open(ruta+"/Datos/Historial/historial_{}.txt".format(preguntarCuentaTransferir),"a")
        now = datetime.now()
        hora = str(now.hour)
        minuto = str(now.minute)
        fecha = str(date.today())+" "+hora+":"+minuto
        historialAbrirTu.write(fecha+" Has transferido "+str(dineroTransferir)+" € a "+preguntarCuentaTransferir+"\n")
        historialAbrirOtro.write(fecha+" "+nombreUsuario+" te ha transferido "+str(dineroTransferir)+ "€"+"\n")
        historialAbrirTu.close()
        historialAbrirOtro.close()

        historialAbrir = open(ruta+"/Datos/Historial/historial_{}.txt".format(nombreUsuario),"r")
        lineas = historialAbrir.readlines()

        historialAbrir.close()
        numeroLineas = len(lineas)

        if numeroLineas > 100:
            with open(ruta+"/Datos/Historial/historial_{}.txt".format(nombreUsuario), 'r') as fin:
                data = fin.read().splitlines(True)
            with open(ruta+"/Datos/Historial/historial_{}.txt".format(nombreUsuario), 'w') as fout:
                fout.writelines(data[1:])
        else:
            pass

        abrirDineroTransferirDarEscribir.write(str(dineroDar))
        abrirDineroTransferirRecibirEscribir.write(str(dineroRecibir))
        abrirDineroTransferirDarEscribir.close()
        abrirDineroTransferirRecibirEscribir.close()
        actualizarDinero()
        ventanaPreguntarDineroTransferir.lineEdit.setText("")
        correcto.show()
                                    
    else:
        errorDinero2.show()

def transferirDineroCustomScript():
    abrirDineroLeer = open(ruta+"/Datos/Dinero usuarios/dinero_{}.txt".format(nombreUsuario),"r")
    dinero = int(abrirDineroLeer.read())
    abrirDineroLeer.close()
    preguntarDineroTransferir = ventanaPreguntarDineroTransferir.lineEdit.text()
    if preguntarDineroTransferir.isnumeric():
        abrirDineroTransferirDar = open(ruta+"/Datos/Dinero usuarios/dinero_{}.txt".format(nombreUsuario),"r")
        abrirDineroTransferirRecibir = open(ruta+"/Datos/Dinero usuarios/dinero_{}.txt".format(preguntarCuentaTransferir),"r")
        dineroDar = int(abrirDineroTransferirDar.read())
        dineroRecibir = int(abrirDineroTransferirRecibir.read())
        abrirDineroTransferirDar.close()
        abrirDineroTransferirRecibir.close()
        if int(preguntarDineroTransferir) <= dineroDar:
            dineroDar = dineroDar - int(preguntarDineroTransferir)
            dineroRecibir = dineroRecibir + int(preguntarDineroTransferir)
            abrirDineroTransferirDarEscribir = open(ruta+"/Datos/Dinero usuarios/dinero_{}.txt".format(nombreUsuario),"w")
            abrirDineroTransferirRecibirEscribir = open(ruta+"/Datos/Dinero usuarios/dinero_{}.txt".format(preguntarCuentaTransferir),"w")                     
                
            historialAbrirTu = open(ruta+"/Datos/Historial/historial_{}.txt".format(nombreUsuario),"a")
            historialAbrirOtro = open(ruta+"/Datos/Historial/historial_{}.txt".format(preguntarCuentaTransferir),"a")
            now = datetime.now()
            hora = str(now.hour)
            minuto = str(now.minute)
            fecha = str(date.today())+" "+hora+":"+minuto
            historialAbrirTu.write(fecha+" Has transferido "+str(preguntarDineroTransferir)+" € a "+preguntarCuentaTransferir+"\n")
            historialAbrirOtro.write(fecha+" "+nombreUsuario+" te ha transferido "+str(preguntarDineroTransferir)+ "€"+"\n")
            historialAbrirTu.close()
            historialAbrirOtro.close()

            historialAbrir = open(ruta+"/Datos/Historial/historial_{}.txt".format(nombreUsuario),"r")
            lineas = historialAbrir.readlines()

            historialAbrir.close()
            numeroLineas = len(lineas)

            if numeroLineas > 100:
                with open(ruta+"/Datos/Historial/historial_{}.txt".format(nombreUsuario), 'r') as fin:
                    data = fin.read().splitlines(True)
                with open(ruta+"/Datos/Historial/historial_{}.txt".format(nombreUsuario), 'w') as fout:
                    fout.writelines(data[1:])
            else:
                pass

            abrirDineroTransferirDarEscribir.write(str(dineroDar))
            abrirDineroTransferirRecibirEscribir.write(str(dineroRecibir))
            abrirDineroTransferirDarEscribir.close()
            abrirDineroTransferirRecibirEscribir.close()
            actualizarDinero()
            ventanaPreguntarDineroTransferir.lineEdit.setText("")
            correcto.show()
            ventanaPreguntarDineroTransferir.close()

        else:
            errorDinero2.show()               
                                    
    else:
        errorLetras.show()

def transferirDinero():
    cuentaCorrecta = False
    global preguntarCuentaTransferir
    preguntarCuentaTransferir = ventanaTransferirDinero.lineEdit.text()
    try:
        NombreUsuario = open(ruta+"/Datos/Dinero usuarios/dinero_{}.txt".format(preguntarCuentaTransferir),"r")
        cuentaCorrecta = True
        NombreUsuario.close()

    except FileNotFoundError:
        errorUsuario2.show()
        cuentaCorrecta = False

    if preguntarCuentaTransferir == nombreUsuario:
        errorTransferir.show()

    else:
        if cuentaCorrecta == True:
            ventanaTransferirDinero.close()
            ventanaTransferirDinero.lineEdit.setText("")
            abrirDineroLeer = open(ruta+"/Datos/Dinero usuarios/dinero_{}.txt".format(nombreUsuario),"r")
            dinero = int(abrirDineroLeer.read())
            abrirDineroLeer.close()
            ventanaTransferirDinero2.show()
            ventanaTransferirDinero2.labelUsuario.setText(preguntarCuentaTransferir)
            historialAbrir2 = open(ruta+"/Datos/Historial/historial_{}.txt".format(preguntarCuentaTransferir),"a")
            historialAbrir2.close()
            actualizarDinero()
            ventanaTransferirDinero2.show()
        

        else:
            errorUsuario2.show()

    
# Cerrar sesion
def cerrarSesion():
    ventanaIniciarSesion.lineEditUsuario.setText("")
    ventanaIniciarSesion.lineEditContrasena.setText("")
    ventanaInicio.show()
    ventanaTuCuenta.close()
    
# Importar todas las ventanas
ventanaInicio = loader.load(ruta+"/UIs/Inicio.ui", None)
ventanaIniciarSesion = loader.load(ruta+"/UIs/IniciarSesion.ui", None)
ventanaCrearCuenta = loader.load(ruta+"/UIs/crearCuenta.ui", None)
ventanaTuCuenta = loader.load(ruta+"/UIs/tuCuenta.ui", None)
ventanaIngresarDinero = loader.load(ruta+"/UIs/ingresarDinero.ui", None)
ventanaSacarDinero = loader.load(ruta+"/UIs/sacarDinero.ui", None)
errorUsuario = loader.load(ruta+"/UIs/errorUsuario.ui", None)
errorContraseña = loader.load(ruta+"/UIs/errorContraseña.ui", None)
errorContraseña2 = loader.load(ruta+"/UIs/errorContraseña2.ui", None)
errorContraseña3 = loader.load(ruta+"/UIs/errorContraseña3.ui", None)
errorContraseña4 = loader.load(ruta+"/UIs/errorContraseña4.ui", None)
errorUsuario2 = loader.load(ruta+"/UIs/errorUsuario2.ui", None)
correcto = loader.load(ruta+"/UIs/correcto.ui", None)
ventanaPreguntarDineroIngresar = loader.load(ruta+"/UIs/preguntarDinero.ui", None)
ventanaPreguntarDineroSacar = loader.load(ruta+"/UIs/preguntarDinero.ui", None)
ventanaPreguntarDineroTransferir = loader.load(ruta+"/UIs/preguntarDinero.ui", None)
errorDinero = loader.load(ruta+"/UIs/errorDinero.ui", None)
errorLetras = loader.load(ruta+"/UIs/errorLetras.ui", None)
errorDinero2 = loader.load(ruta+"/UIs/errorDinero2.ui", None)
ventanaHistorial = loader.load(ruta+"/UIs/historial.ui", None)
ventanaCambiarContraseña = loader.load(ruta+"/UIs/cambiarContraseña.ui", None)
ventanaTransferirDinero = loader.load(ruta+"/UIs/transferirDinero.ui", None)
ventanaTransferirDinero2 = loader.load(ruta+"/UIs/transferirDinero2.ui", None)
errorTransferir = loader.load(ruta+"/UIs/errorTransferir.ui", None)

# Abrir ventana inicio
ventanaInicio.show()

# Acciones de botones varios
ventanaInicio.btnIniciarSesion.clicked.connect(lambda: ventanaIniciarSesion.show())
ventanaInicio.btnCrearCuenta.clicked.connect(lambda: ventanaCrearCuenta.show())
ventanaIniciarSesion.Cancelar.clicked.connect(lambda: ventanaIniciarSesion.close())
ventanaCrearCuenta.Cancelar.clicked.connect(lambda: ventanaCrearCuenta.close())
ventanaCrearCuenta.Aceptar.clicked.connect(lambda: crearCuenta())
ventanaIniciarSesion.Aceptar.clicked.connect(lambda: iniciarSesion())
ventanaCambiarContraseña.pushButtonAceptar.clicked.connect(lambda: cambiarContraseña())
ventanaCambiarContraseña.pushButtonCancelar.clicked.connect(lambda: ventanaCambiarContraseña.close())
ventanaTransferirDinero.aceptar.clicked.connect(lambda: transferirDinero())
ventanaTransferirDinero.cancelar.clicked.connect(lambda: ventanaTransferirDinero.close())
ventanaTuCuenta.pushButtonIngresar.clicked.connect(lambda: ingresarDinero())
ventanaTuCuenta.pushButtonSacarDinero.clicked.connect(lambda: sacarDinero())
ventanaTuCuenta.pushButtonHistorial.clicked.connect(lambda: historialVer())
ventanaTuCuenta.pushButtonCambiarContrasena.clicked.connect(lambda: ventanaCambiarContraseña.show())
ventanaTuCuenta.pushButtonTransferir.clicked.connect(lambda: ventanaTransferirDinero.show())
ventanaTuCuenta.pushButtonCerrarSesion.clicked.connect(lambda: cerrarSesion())
ventanaIngresarDinero.pushButton10.clicked.connect(lambda: ingresarDineroScript(10))
ventanaIngresarDinero.pushButton50.clicked.connect(lambda: ingresarDineroScript(50))
ventanaIngresarDinero.pushButton100.clicked.connect(lambda: ingresarDineroScript(100))
ventanaIngresarDinero.pushButton500.clicked.connect(lambda: ingresarDineroScript(500))
ventanaIngresarDinero.pushButton1000.clicked.connect(lambda: ingresarDineroScript(1000))
ventanaIngresarDinero.pushButtonElegir.clicked.connect(lambda: ventanaPreguntarDineroIngresar.show())
ventanaPreguntarDineroIngresar.aceptar.clicked.connect(lambda: ingresarDineroCustomScript())
ventanaSacarDinero.pushButton10.clicked.connect(lambda: comprobadorDinero(10))
ventanaSacarDinero.pushButton50.clicked.connect(lambda: comprobadorDinero(50))
ventanaSacarDinero.pushButton100.clicked.connect(lambda: comprobadorDinero(100))
ventanaSacarDinero.pushButton500.clicked.connect(lambda: comprobadorDinero(500))
ventanaSacarDinero.pushButton1000.clicked.connect(lambda: comprobadorDinero(1000))
ventanaSacarDinero.pushButtonElegir.clicked.connect(lambda: ventanaPreguntarDineroSacar.show())
ventanaPreguntarDineroSacar.aceptar.clicked.connect(lambda: comprobadorDineroCustom())
ventanaTransferirDinero2.pushButton10.clicked.connect(lambda: transferirDineroScript(10))
ventanaTransferirDinero2.pushButton50.clicked.connect(lambda: transferirDineroScript(50))
ventanaTransferirDinero2.pushButton100.clicked.connect(lambda: transferirDineroScript(100))
ventanaTransferirDinero2.pushButton500.clicked.connect(lambda: transferirDineroScript(500))
ventanaTransferirDinero2.pushButton1000.clicked.connect(lambda: transferirDineroScript(1000))
ventanaTransferirDinero2.pushButtonElegir.clicked.connect(lambda: ventanaPreguntarDineroTransferir.show())
ventanaPreguntarDineroTransferir.aceptar.clicked.connect(lambda: transferirDineroCustomScript())

# Ejecutar app
app.exec()
