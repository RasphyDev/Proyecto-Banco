"""                                                                     

 ________  ________  ________      ___    ___ _______   ________ _________  ________          ________  ________  ________   ________  ________     
|\   __  \|\   __  \|\   __  \    |\  \  /  /|\  ___ \ |\   ____\\___   ___\\   __  \        |\   __  \|\   __  \|\   ___  \|\   ____\|\   __  \    
\ \  \|\  \ \  \|\  \ \  \|\  \   \ \  \/  / | \   __/|\ \  \___\|___ \  \_\ \  \|\  \       \ \  \|\ /\ \  \|\  \ \  \\ \  \ \  \___|\ \  \|\  \   
 \ \   ____\ \   _  _\ \  \\\  \   \ \    / / \ \  \_|/_\ \  \       \ \  \ \ \  \\\  \       \ \   __  \ \   __  \ \  \\ \  \ \  \    \ \  \\\  \  
  \ \  \___|\ \  \\  \\ \  \\\  \   \/  /  /   \ \  \_|\ \ \  \____   \ \  \ \ \  \\\  \       \ \  \|\  \ \  \ \  \ \  \\ \  \ \  \____\ \  \\\  \ 
   \ \__\    \ \__\\ _\\ \_______\__/  / /      \ \_______\ \_______\  \ \__\ \ \_______\       \ \_______\ \__\ \__\ \__\\ \__\ \_______\ \_______\
    \|__|     \|__|\|__|\|_______|\___/ /        \|_______|\|_______|   \|__|  \|_______|        \|_______|\|__|\|__|\|__| \|__|\|_______|\|_______|
                                 \|___|/                                                                                                            
por Rasphy: https://github.com/Rasphy2009/Proyecto-Banco  
V 4.1                                                                                                                                          
                                                                                                                                                    
""" 

# Para encriptar/ desencriptar
import base64

def encriptar(variable):
    global encriptado
    encriptado = variable.encode("utf-8")
    return encriptado

# Sys para abir ventanas
import sys

# Importar PySide6
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QCloseEvent, QGuiApplication, QIcon, QPixmap

# Os para saber la ruta
import os

# Re para conmprobar las letras especiales
import re

# Datetime para la fecha del historial
from datetime import datetime
from datetime import date

# Time para el tiempo
import time

# Saber ruta
filePath = os.path.dirname(os.path.realpath(__file__))
ruta = filePath.replace("\\","/")

# Para poder importar .ui y definir app
loader = QUiLoader()
app = QtWidgets.QApplication(sys.argv)

# StyleSheet para botones
styleSheetBoton = """QPushButton{\ntext-align: left;\npadding-left: 11px;\nbackground-color: fondo;\nborder-radius: 5px;\n}\nQPushButton::hover{\nbackground-color: rgb(199, 199, 205);\n}\nQPushButton::pressed{\nbackground-color: rgb(185, 185, 185);\n}"""

def vaciarLineEdits():
    # Iniciar sesion
    ventanaIniciarSesion.lineEditUsuario.setText("")
    ventanaIniciarSesion.lineEditContrasena.setText("")
    ventanaIniciarSesion.lineEditUsuario2.setText("")
    ventanaIniciarSesion.lineEditContrasena2.setText("")
    ventanaIniciarSesion.lineEditContrasenaVerificar.setText("")
    # Ingresar dinero
    ventanaPrincipal.lineEdit_2.setText("")
    # Sacar dinero
    ventanaPrincipal.lineEdit_3.setText("")
    # Cambiar contraseña
    ventanaPrincipal.lineEditContrasenaActual.setText("")
    ventanaPrincipal.lineEditNuevaContrasena.setText("")
    ventanaPrincipal.lineEditRepetirContrasena.setText("")
    # Transferir
    ventanaPrincipal.lineEdit_6.setText("")
    ventanaPrincipal.lineEdit_7.setText("")
    # Cambiar usuario
    ventanaPrincipal.lineEditNombreUsuario.setText("")

def quitarErrores():
    # Iniciar sesion
    ventanaIniciarSesion.labelErrorUsuario2.hide()
    ventanaIniciarSesion.labelErrorContrasena4.hide()
    ventanaIniciarSesion.labelErrorUsuario.hide()
    ventanaIniciarSesion.labelErrorContrasena2.hide()
    ventanaIniciarSesion.correcto.hide()
    ventanaIniciarSesion.labelErrorContrasena2_2.hide()
    ventanaIniciarSesion.labelErrorContrasena.hide()
    # Ingresar dinero
    ventanaPrincipal.errorDinero.hide()
    ventanaPrincipal.errorLetras.hide()
    # Sacar dinero
    ventanaPrincipal.errorDinero_2.hide()
    ventanaPrincipal.errorLetras_2.hide()
    # Cambiar contraseña
    ventanaPrincipal.errorContrasena.hide()
    ventanaPrincipal.errorContrasena4.hide()
    # Transferir
    ventanaPrincipal.errorDinero_5.hide()
    ventanaPrincipal.errorLetras_5.hide()
    ventanaPrincipal.errorNombre.hide()
    # Cambiar usuario
    ventanaPrincipal.labelErrorUsuario.hide()

# Actualiza los valores de dinero de ventanas
def actualizarDinero():
    abrirDineroLeer = open(ruta+"/Datos/Dinero usuarios/dinero_{}.txt".format(nombreUsuario),"r")
    dinero = bytes.decode(base64.b64decode(abrirDineroLeer.read()))
    abrirDineroLeer.close()
    ventanaPrincipal.labelDinero.setText(str(dinero)+" €")
    ventanaPrincipal.labelDinero_2.setText(str(dinero)+" €")
    ventanaPrincipal.labelDinero_3.setText(str(dinero)+" €")
    ventanaPrincipal.labelDinero_4.setText(str(dinero)+" €")
    ventanaPrincipal.labelDinero_5.setText(str(dinero)+" €")

# Splash screen
def splashScreen():
    # Quitar barra de titulo
    ventanaSplashScreen.setWindowFlag(QtCore.Qt.FramelessWindowHint)
    ventanaSplashScreen.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    # Logo
    ventanaSplashScreen.label.setPixmap(QPixmap(ruta+"/UIs/Imgs/logo.png"))
    ventanaSplashScreen.label_2.setPixmap(QPixmap(ruta+"/UIs/Imgs/fondo.png"))
    ventanaSplashScreen.label.setScaledContents(True)

    # Abrir ventana
    ventanaSplashScreen.show()

    # Progreso
    for porcentaje in range(1, 35):
        time.sleep(0.003)
        ventanaSplashScreen.labelCargando.setText("Iniciando componentes...")
        QGuiApplication.processEvents()
        if porcentaje == 99:
            ventanaSplashScreen.close()
            iniciarSesion()
            break

    for porcentaje in range(35, 75):
        time.sleep(0.005)
        ventanaSplashScreen.labelCargando.setText("Cargando interfaces...")
        QGuiApplication.processEvents()
        if porcentaje == 99:
            ventanaSplashScreen.close()
            iniciarSesion()
            break

    for porcentaje in range(75, 100, 2):
        time.sleep(0.002)
        ventanaSplashScreen.labelCargando.setText("Iniciando...")
        QGuiApplication.processEvents()
        if porcentaje == 99:
            ventanaSplashScreen.close()
            iniciarSesion()
            break


# Iniciar sesion y crear cuenta
def iniciarSesion():
    # Quitar barra de titulo, maximizar y cambiar tamaño
    ventanaIniciarSesion.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint, False)
    ventanaIniciarSesion.logo.setPixmap(QPixmap(ruta+"/UIs/Imgs/logo4.png"))
    ventanaIniciarSesion.setFixedSize(ventanaIniciarSesion.width(), ventanaIniciarSesion.height())
    ventanaIniciarSesion.show()
    quitarErrores()

# Comprueba si checkBox esta pulsado
def comprobadorCheckBox1():
    valor = ventanaIniciarSesion.checkBox_Contrasena.checkState()
    
    if str(valor) == "PySide6.QtCore.Qt.CheckState.Checked":
        ventanaIniciarSesion.lineEditContrasena.setEchoMode(QtWidgets.QLineEdit.Normal)
    else:
        ventanaIniciarSesion.lineEditContrasena.setEchoMode(QtWidgets.QLineEdit.Password)

def comprobadorCheckBox2():
    valor = ventanaIniciarSesion.checkBox_Contrasena2.checkState()
    
    if str(valor) == "PySide6.QtCore.Qt.CheckState.Checked":
        ventanaIniciarSesion.lineEditContrasena2.setEchoMode(QtWidgets.QLineEdit.Normal)
        ventanaIniciarSesion.lineEditContrasenaVerificar.setEchoMode(QtWidgets.QLineEdit.Normal)
    else:
        ventanaIniciarSesion.lineEditContrasena2.setEchoMode(QtWidgets.QLineEdit.Password)
        ventanaIniciarSesion.lineEditContrasenaVerificar.setEchoMode(QtWidgets.QLineEdit.Password)

# Animacion
def animacionUnfade(ventana1, ventana2):
    ventana1.hide()
    ventana2.show()
    # Unfade
    ventanaIniciarSesion.effect = QtWidgets.QGraphicsOpacityEffect()
    ventana2.setGraphicsEffect(ventanaIniciarSesion.effect)

    ventanaIniciarSesion.animation = QtCore.QPropertyAnimation(ventanaIniciarSesion.effect, b"opacity")
    ventanaIniciarSesion.animation.setDuration(500)
    ventanaIniciarSesion.animation.setStartValue(0)
    ventanaIniciarSesion.animation.setEndValue(1)
    ventanaIniciarSesion.animation.start()

# Crear una cuenta
def crearCuentaScript():
    usuarioCrear = ventanaIniciarSesion.lineEditUsuario2.text()
    
    # Comprobar si el usuario ya existe
    if os.path.isfile(ruta+"/Datos/Usuarios/usuario_{}.txt".format(usuarioCrear)) == True:
        ventanaIniciarSesion.labelErrorUsuario.show()
        error = 1
        return error
    else:
        pass

    # Comprobar si usuarioCrear tiene caracteres especiales y la contraseña
    comprobarCaracteres = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if (comprobarCaracteres.search(usuarioCrear) == None):
        datoContraseña = open(ruta+"/Datos/Contraseñas/contraseña_{}.txt".format(usuarioCrear),"w")      
        contraseñaCrear = ventanaIniciarSesion.lineEditContrasena2.text()
        contraseñaVerificar = ventanaIniciarSesion.lineEditContrasenaVerificar.text()
        if contraseñaCrear == "" and contraseñaVerificar == "":
            ventanaIniciarSesion.labelErrorContrasena2.show()
            datoContraseña.close()
            error = 1
            return error

        else:
            if contraseñaCrear == contraseñaVerificar:
                datoContraseña.write(bytes.decode(base64.b64encode(encriptar(contraseñaCrear))))
                datoNombreUsuario = open(ruta+"/Datos/Usuarios/usuario_{}.txt".format(usuarioCrear),"w")
                datoNombreUsuario.write(usuarioCrear)   
                datoNombreUsuario.close()
                dinero = open(ruta+"/Datos/Dinero usuarios/dinero_{}.txt".format(usuarioCrear),"w")
                dinero.write(bytes.decode(base64.b64encode(encriptar("0"))))
                dinero.close()
                historialAbrir = open(ruta+"/Datos/Historial/historial_{}.txt".format(usuarioCrear),"w")
                historialAbrir.close()
                datoContraseña.close()
                ventanaIniciarSesion.lineEditUsuario2.setText("")
                ventanaIniciarSesion.lineEditContrasena2.setText("")
                ventanaIniciarSesion.lineEditContrasenaVerificar.setText("")
                ventanaIniciarSesion.correcto.show()
            else:
                ventanaIniciarSesion.labelErrorContrasena.show()
                datoContraseña.close()
                error = 1
                return error
               
    else:
        ventanaIniciarSesion.labelErrorContrasena2.show()
        error = 1
        return error

# Iniciar sesion
def iniciarSesionScript():
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
        ventanaIniciarSesion.labelErrorUsuario2.show()
        error = 1
        return error

    # Comprobar contraseña
    if cuentaCorrecta == True:
        preguntarContraseña = ventanaIniciarSesion.lineEditContrasena.text()
        datoContraseña = open(ruta+"/Datos/Contraseñas/contraseña_{}.txt".format(nombreUsuario),"r")
        contraseña = bytes.decode(base64.b64decode(datoContraseña.read()))
        datoContraseña.close()

        if preguntarContraseña == contraseña:
            ventanaIniciarSesion.close()
            tuCuenta()

        else:
            ventanaIniciarSesion.labelErrorContrasena4.show()
            error = 1
            return error

    else:
        ventanaIniciarSesion.labelErrorUsuario2.show()
        error = 1
        return error


# Ventana principal
# Funcion animacion barra lateral
def pulsarBotonExpandir(ventanaPrincipal):
    menuWidth = ventanaPrincipal.barraLateral.width()

    # Comprobar
    width = 50
    if menuWidth == 50:
        width = 190

    # Empezar animacion
    ventanaPrincipal.animExp = QtCore.QPropertyAnimation(ventanaPrincipal.barraLateral, b"minimumWidth")
    ventanaPrincipal.animExp.setDuration(300)
    ventanaPrincipal.animExp.setStartValue(menuWidth)
    ventanaPrincipal.animExp.setEndValue(width)
    ventanaPrincipal.animExp.setEasingCurve(QtCore.QEasingCurve.InOutCirc)
    ventanaPrincipal.animExp.start()


# Animacion fade unfade
def animacionFadeUnfade(opcion):
    # Mostrar
    ventanaPrincipal.stackedWidget.setCurrentWidget(opcion)

    # Unfade
    ventanaPrincipal.effect = QtWidgets.QGraphicsOpacityEffect()
    opcion.setGraphicsEffect(ventanaPrincipal.effect)
    ventanaPrincipal.animTuCuenta = QtCore.QPropertyAnimation(ventanaPrincipal.effect, b"opacity")
    ventanaPrincipal.animTuCuenta.setDuration(300)
    ventanaPrincipal.animTuCuenta.setStartValue(0)
    ventanaPrincipal.animTuCuenta.setEndValue(1)
    ventanaPrincipal.animTuCuenta.start()

# Comprueba si checkBox esta pulsado en ventanaPrincipal
def comprobadorCheckBox3():
    valor = ventanaPrincipal.checkBox_Contrasena.checkState()
    
    if str(valor) == "PySide6.QtCore.Qt.CheckState.Checked":
        ventanaPrincipal.lineEditContrasenaActual.setEchoMode(QtWidgets.QLineEdit.Normal)
        ventanaPrincipal.lineEditNuevaContrasena.setEchoMode(QtWidgets.QLineEdit.Normal)
        ventanaPrincipal.lineEditRepetirContrasena.setEchoMode(QtWidgets.QLineEdit.Normal)
    else:
        ventanaPrincipal.lineEditContrasenaActual.setEchoMode(QtWidgets.QLineEdit.Password)
        ventanaPrincipal.lineEditNuevaContrasena.setEchoMode(QtWidgets.QLineEdit.Password)
        ventanaPrincipal.lineEditRepetirContrasena.setEchoMode(QtWidgets.QLineEdit.Password)


# Ventana de acciones de cuenta (ventanaPrincipal)
def tuCuenta():
    global dinero
    abrirDineroLeer = open(ruta+"/Datos/Dinero usuarios/dinero_{}.txt".format(nombreUsuario),"r")
    dinero = bytes.decode(base64.b64decode(abrirDineroLeer.read()))
    int(dinero)
    abrirDineroLeer.close()
    actualizarDinero()
    ventanaPrincipal.labelUsuario.setText("<strong>"+nombreUsuario+"</strong>")
    ventanaPrincipal.show()
    animacionFadeUnfade(ventanaPrincipal.tuCuenta)


# Ingresar dinero
def ingresarDinero():
    actualizarDinero()
    animacionFadeUnfade(ventanaPrincipal.ingresarDinero)
    quitarErrores()

def ingresarDineroScript(dineroIngresar):
    abrirDineroLeer = open(ruta+"/Datos/Dinero usuarios/dinero_{}.txt".format(nombreUsuario),"r")
    dinero = int(bytes.decode(base64.b64decode(abrirDineroLeer.read())))
    abrirDineroLeer.close()
    dinero = dinero + int(dineroIngresar)
    historial("Ingresados {} €".format(dineroIngresar))
    abrirDineroEscribir = open(ruta+"/Datos/Dinero usuarios/dinero_{}.txt".format(nombreUsuario),"w")
    abrirDineroEscribir.write(bytes.decode(base64.b64encode(encriptar(str(dinero)))))
    abrirDineroEscribir.close()
    actualizarDinero()
    animacionFadeUnfade(ventanaPrincipal.correcto)
    vaciarLineEdits()
    

def ingresarDineroCustomScript():
    preguntarDineroIngresar = ventanaPrincipal.lineEdit_2.text()
    if preguntarDineroIngresar.isnumeric():
        if int(preguntarDineroIngresar) <= 1000000000:
            abrirDineroLeer = open(ruta+"/Datos/Dinero usuarios/dinero_{}.txt".format(nombreUsuario),"r")
            dinero = int(bytes.decode(base64.b64decode(abrirDineroLeer.read())))
            abrirDineroLeer.close()
            dinero = dinero + int(preguntarDineroIngresar)  
            ventanaPrincipal.lineEdit_2.setText("")
            abrirDineroEscribir = open(ruta+"/Datos/Dinero usuarios/dinero_{}.txt".format(nombreUsuario),"w")
            abrirDineroEscribir.write(bytes.decode(base64.b64encode(encriptar(str(dinero)))))
            historial("Ingresados {} €".format(dinero))
            abrirDineroEscribir.close()
            actualizarDinero()
            animacionFadeUnfade(ventanaPrincipal.correcto)
            vaciarLineEdits()
        else:
            ventanaPrincipal.errorDinero.show()
            error = 1
            return error
    else:
        ventanaPrincipal.errorLetras.show()
        error = 1
        return error


# Sacar dinero  
def sacarDinero():
    actualizarDinero()
    animacionFadeUnfade(ventanaPrincipal.sacarDinero)
    quitarErrores()

# Comprueba si hay dinero suficiente y mas
def comprobadorDinero(dineroComprobar):
    abrirDineroLeer = open(ruta+"/Datos/Dinero usuarios/dinero_{}.txt".format(nombreUsuario),"r")
    dinero = int(bytes.decode(base64.b64decode(abrirDineroLeer.read())))
    abrirDineroLeer.close()

    if dineroComprobar <= dinero:
        dinero = dinero - int(dineroComprobar)
        historial("Sacados {} €".format(dineroComprobar))
        abrirDineroSacar = open(ruta+"/Datos/Dinero usuarios/dinero_{}.txt".format(nombreUsuario),"w")
        abrirDineroSacar.write(bytes.decode(base64.b64encode(encriptar(str(dinero)))))
        abrirDineroSacar.close()
        actualizarDinero()
        animacionFadeUnfade(ventanaPrincipal.correcto)
        vaciarLineEdits()

    else:
        animacionFadeUnfade(ventanaPrincipal.error)
        ventanaPrincipal.titulo.setText("No hay suficiente dinero")
        ventanaPrincipal.relleno.setText("No hay suficiente dinero. ¿Quieres ingresar mas?")
        error = 1
        return error

def comprobadorDineroCustom():
    preguntarDineroSacar = ventanaPrincipal.lineEdit_3.text()
    abrirDineroLeer = open(ruta+"/Datos/Dinero usuarios/dinero_{}.txt".format(nombreUsuario),"r")
    dinero = int(bytes.decode(base64.b64decode(abrirDineroLeer.read())))
    abrirDineroLeer.close()
    if preguntarDineroSacar.isnumeric():
        abrirDineroLeer = open(ruta+"/Datos/Dinero usuarios/dinero_{}.txt".format(nombreUsuario),"r")
        dinero = int(bytes.decode(base64.b64decode(abrirDineroLeer.read())))
        abrirDineroLeer.close()
        if int(preguntarDineroSacar) <= dinero:
            dinero = dinero - int(preguntarDineroSacar)
            animacionFadeUnfade(ventanaPrincipal.correcto)
            historial("Sacados {} €".format(preguntarDineroSacar))
            abrirDineroSacar = open(ruta+"/Datos/Dinero usuarios/dinero_{}.txt".format(nombreUsuario),"w")
            abrirDineroSacar.write(bytes.decode(base64.b64encode(encriptar(str(dinero)))))
            abrirDineroSacar.close()
            actualizarDinero()
            ventanaPrincipal.lineEdit_3.setText("")
            vaciarLineEdits()
        else:
            ventanaPrincipal.errorDinero_2.show()
            error = 1
            return error
    else:
        ventanaPrincipal.errorLetras_2.show()
        error = 1
        return error


# Historial
# Ver ventana historial
def historialVer():
    historialAbrir = open(ruta+"/Datos/Historial/historial_{}.txt".format(nombreUsuario),"r+")
    textoHistorial = historialAbrir.read()
    historialAbrir.close()
    ventanaPrincipal.textEdit.setText(textoHistorial)
    animacionFadeUnfade(ventanaPrincipal.historial)

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
    animacionFadeUnfade(ventanaPrincipal.cambiarContrasena)
    quitarErrores()

def cambiarContraseñaScript():
    contraseñaActual = ventanaPrincipal.lineEditContrasenaActual.text()
    datoContraseña = open(ruta+"/Datos/Contraseñas/contraseña_{}.txt".format(nombreUsuario),"r")
    contraseña = bytes.decode(base64.b64decode(datoContraseña.read()))
    datoContraseña.close()
    contraseñaVerificar = ventanaPrincipal.lineEditRepetirContrasena.text()
    contraseñaCambiar = ventanaPrincipal.lineEditNuevaContrasena.text()
    if contraseñaActual == contraseña:
        if contraseñaVerificar == contraseñaCambiar:
            preguntarContraseñaCambiar = ventanaPrincipal.lineEditNuevaContrasena.text()
            datoContraseña = open(ruta+"/Datos/Contraseñas/contraseña_{}.txt".format(nombreUsuario),"w")
            datoContraseña.write(bytes.decode(base64.b64encode(encriptar(preguntarContraseñaCambiar))))
            datoContraseña.close()
            historial("Se cambio la contraseña")
            animacionFadeUnfade(ventanaPrincipal.correcto)
        else:
            ventanaPrincipal.errorContrasena.show()
            error = 1
            return error
    else:
        ventanaPrincipal.errorContrasena4.show()
        error = 1
        return error


# Transferir dinero
def transferirDineroScript(dineroTransferir):
    cuentaCorrecta = False
    global preguntarCuentaTransferir
    preguntarCuentaTransferir = ventanaPrincipal.lineEdit_7.text()
    try:
        NombreUsuario = open(ruta+"/Datos/Dinero usuarios/dinero_{}.txt".format(preguntarCuentaTransferir),"r")
        cuentaCorrecta = True
        NombreUsuario.close()

    except FileNotFoundError:
        ventanaPrincipal.errorNombre.setText("No se encuentra esa cuenta")
        cuentaCorrecta = False

    if preguntarCuentaTransferir == nombreUsuario:
        ventanaPrincipal.errorNombre.setText("¿Por que quieres transferirte a ti mismo?")

    else:
        if cuentaCorrecta == True:
            ventanaPrincipal.lineEdit_7.setText("")
            historialAbrir2 = open(ruta+"/Datos/Historial/historial_{}.txt".format(preguntarCuentaTransferir),"a")
            historialAbrir2.close()
            actualizarDinero()
            abrirDineroLeer = open(ruta+"/Datos/Dinero usuarios/dinero_{}.txt".format(nombreUsuario),"r")
            dinero = int(bytes.decode(base64.b64decode(abrirDineroLeer.read())))
            abrirDineroLeer.close()
            abrirDineroTransferirDar = open(ruta+"/Datos/Dinero usuarios/dinero_{}.txt".format(nombreUsuario),"r")
            abrirDineroTransferirRecibir = open(ruta+"/Datos/Dinero usuarios/dinero_{}.txt".format(preguntarCuentaTransferir),"r")
            dineroDar = int(bytes.decode(base64.b64decode(abrirDineroTransferirDar.read())))
            dineroRecibir = int(bytes.decode(base64.b64decode(abrirDineroTransferirRecibir.read())))
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

                abrirDineroTransferirDarEscribir.write(bytes.decode(base64.b64encode(encriptar(str(dineroDar)))))
                abrirDineroTransferirRecibirEscribir.write(bytes.decode(base64.b64encode(encriptar(str(dineroRecibir)))))
                abrirDineroTransferirDarEscribir.close()
                abrirDineroTransferirRecibirEscribir.close()
                actualizarDinero()
                ventanaPrincipal.lineEdit_6.setText("")
                animacionFadeUnfade(ventanaPrincipal.correcto)
                vaciarLineEdits()
                                            
            else:
                ventanaPrincipal.errorNombre.setText("No hay suficiente dinero :(")
                ventanaPrincipal.errorNombre.show()
                error = 1
                return error
        
        else:
            ventanaPrincipal.errorNombre.setText("No se encuentra esa cuenta")
            ventanaPrincipal.errorNombre.show()
            error = 1
            return error

def transferirDineroCustomScript():
    cuentaCorrecta = False
    global preguntarCuentaTransferir
    preguntarCuentaTransferir = ventanaPrincipal.lineEdit_7.text()
    try:
        NombreUsuario = open(ruta+"/Datos/Dinero usuarios/dinero_{}.txt".format(preguntarCuentaTransferir),"r")
        cuentaCorrecta = True
        NombreUsuario.close()

    except FileNotFoundError:
        ventanaPrincipal.errorNombre.setText("No se encuentra esa cuenta")
        cuentaCorrecta = False

    if preguntarCuentaTransferir == nombreUsuario:
        ventanaPrincipal.errorNombre.setText("¿Por que quieres transferirte a ti mismo?")

    else:
        if cuentaCorrecta == True:
            ventanaPrincipal.lineEdit_7.setText("")
            historialAbrir2 = open(ruta+"/Datos/Historial/historial_{}.txt".format(preguntarCuentaTransferir),"a")
            historialAbrir2.close()
            actualizarDinero()
        
        else:
            ventanaPrincipal.errorNombre.setText("No se encuentra esa cuenta")
            error = 1
            return error


        abrirDineroLeer = open(ruta+"/Datos/Dinero usuarios/dinero_{}.txt".format(nombreUsuario),"r")
        dinero = int(bytes.decode(base64.b64decode(abrirDineroLeer.read())))
        abrirDineroLeer.close()
        preguntarDineroTransferir = ventanaPrincipal.lineEdit_6.text()
        if preguntarDineroTransferir.isnumeric():
            abrirDineroTransferirDar = open(ruta+"/Datos/Dinero usuarios/dinero_{}.txt".format(nombreUsuario),"r")
            abrirDineroTransferirRecibir = open(ruta+"/Datos/Dinero usuarios/dinero_{}.txt".format(preguntarCuentaTransferir),"r")
            dineroDar = int(bytes.decode(base64.b64decode(abrirDineroTransferirDar.read())))
            dineroRecibir = int(bytes.decode(base64.b64decode(abrirDineroTransferirRecibir.read())))
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

                abrirDineroTransferirDarEscribir.write(bytes.decode(base64.b64encode(encriptar(str(dineroDar)))))
                abrirDineroTransferirRecibirEscribir.write(bytes.decode(base64.b64encode(encriptar(str(dineroRecibir)))))
                abrirDineroTransferirDarEscribir.close()
                abrirDineroTransferirRecibirEscribir.close()
                actualizarDinero()
                ventanaPrincipal.lineEdit_6.setText("")
                animacionFadeUnfade(ventanaPrincipal.correcto)

            else:
                ventanaPrincipal.errorNombre.setText("No se encuentra esa cuenta") 
                ventanaPrincipal.errorNombre.show()
                error = 1
                return error             
                                    
        else:
            ventanaPrincipal.errorNombre.setText("No puedes ingresar letras")
            ventanaPrincipal.errorNombre.show()
            error = 1
            return error

def transferirDinero():
    ventanaPrincipal.errorNombre.setText("")
    quitarErrores()
    animacionFadeUnfade(ventanaPrincipal.transferir)
    
# Cerrar sesion
def cerrarSesion():
    ventanaPrincipal.close()
    ventanaIniciarSesion.show()


# Eliminar cuenta
def eliminarCuenta():
    os.remove(ruta+"/Datos/Usuarios/usuario_{}.txt".format(nombreUsuario))
    os.remove(ruta+"/Datos/Contraseñas/contraseña_{}.txt".format(nombreUsuario))
    os.remove(ruta+"/Datos/Dinero usuarios/dinero_{}.txt".format(nombreUsuario))
    os.remove(ruta+"/Datos/Historial/historial_{}.txt".format(nombreUsuario))
    ventanaPrincipal.close()
    ventanaIniciarSesion.show()

# Cambiar nombre usuario
def cambiarNombreUsuario():
    nuevoNombre = ventanaPrincipal.lineEditNombreUsuario.text()

    # Usuario
    # Comprobar si el usuario ya existe
    if os.path.isfile(ruta+"/Datos/Usuarios/usuario_{}.txt".format(nuevoNombre)) == True:
        ventanaPrincipal.labelErrorUsuario.show()
        error = 1
        return error
    else:
        pass

    if nuevoNombre == "":
        ventanaPrincipal.labelErrorUsuario.setText("Tu nombre no puede estar vacio")
        error = 1
        return error

    else:
        nombreAntiguo = nombreUsuario

        datoNombreUsuario = open(ruta+"/Datos/Usuarios/usuario_{}.txt".format(nuevoNombre),"w")
        datoNombreUsuario.write(nuevoNombre)   
        datoNombreUsuario.close()

        # Dinero
        abrirDineroLeerEscribir = open(ruta+"/Datos/Dinero usuarios/dinero_{}.txt".format(nombreAntiguo),"r")
        dinero = int(bytes.decode(base64.b64decode(abrirDineroLeerEscribir.read())))
        abrirDineroLeerEscribir.close()
        abrirDineroNuevo = open(ruta+"/Datos/Dinero usuarios/dinero_{}.txt".format(nuevoNombre),"w")
        abrirDineroNuevo.write(bytes.decode(base64.b64encode(encriptar(str(dinero)))))
        abrirDineroNuevo.close()

        # Historial
        historialAbrir = open(ruta+"/Datos/Historial/historial_{}.txt".format(nombreAntiguo),"r+")
        textoHistorial = historialAbrir.read()
        historialAbrir.close()
        historialNuevo = open(ruta+"/Datos/Historial/historial_{}.txt".format(nuevoNombre),"w+")
        historialNuevo.write(textoHistorial)
        historialNuevo.close()

        # Contraseña
        datoContraseña = open(ruta+"/Datos/Contraseñas/contraseña_{}.txt".format(nombreAntiguo),"r+")
        contraseñaActual = bytes.decode(base64.b64decode(datoContraseña.read()))
        datoContraseña.close()
        contraseñaNueva = open(ruta+"/Datos/Contraseñas/contraseña_{}.txt".format(nuevoNombre),"w+")
        contraseñaNueva.write(bytes.decode(base64.b64encode(encriptar(contraseñaActual))))
        contraseñaNueva.close()

        os.remove(ruta+"/Datos/Usuarios/usuario_{}.txt".format(nombreAntiguo))
        os.remove(ruta+"/Datos/Contraseñas/contraseña_{}.txt".format(nombreAntiguo))
        os.remove(ruta+"/Datos/Dinero usuarios/dinero_{}.txt".format(nombreAntiguo))
        os.remove(ruta+"/Datos/Historial/historial_{}.txt".format(nombreAntiguo))
        animacionFadeUnfade(ventanaPrincipal.tuCuenta)

        abrirDineroLeer = open(ruta+"/Datos/Dinero usuarios/dinero_{}.txt".format(nuevoNombre),"r")
        dinero = int(bytes.decode(base64.b64decode(abrirDineroLeer.read())))
        abrirDineroLeer.close()
        
        animacionFadeUnfade(ventanaPrincipal.asegurarCambiarNombre)


# Definir ventanas y otros ajustes
ventanaSplashScreen = loader.load(ruta+"/UIs/splashScreen.ui", None)
ventanaIniciarSesion = loader.load(ruta+"/UIs/IniciarSesion.ui", None)
ventanaPrincipal = loader.load(ruta+"/UIs/ventanaPrincipal.ui", None)
ventanaPrincipal.stackedWidget.setCurrentWidget(ventanaPrincipal.tuCuenta)
ventanaPrincipal.btnAtras.hide()
ventanaPrincipal.textEdit.setTextInteractionFlags(QtCore.Qt.NoTextInteraction) 
ventanaIniciarSesion.setWindowIcon(QIcon(ruta+"/UIs/Imgs/icono.ico"))

# Establecer iconos e imagenes
ventanaPrincipal.btnMinMax.setIcon(QIcon(ruta+"/UIs/Imgs/iconoMinMax.png"))
ventanaPrincipal.btnTuCuenta.setIcon(QIcon(ruta+"/UIs/Imgs/iconoCasaPulsado.png"))
ventanaPrincipal.btnConfig.setIcon(QIcon(ruta+"/UIs/Imgs/iconoConfig.png")) 
ventanaPrincipal.btnAtras.setIcon(QIcon(ruta+"/UIs/Imgs/iconoAtras.png"))
ventanaPrincipal.btnCerrarSesion.setIcon(QIcon(ruta+"/UIs/Imgs/iconoCerrarSesion.png"))
ventanaPrincipal.tick.setPixmap(QPixmap(ruta+"/UIs/Imgs/iconoCorrecto.png"))
ventanaPrincipal.iconoInterrogacion.setPixmap(QPixmap(ruta+"/UIs/Imgs/iconoInterrogacion.png"))
ventanaPrincipal.iconoInterrogacion_2.setPixmap(QPixmap(ruta+"/UIs/Imgs/iconoInterrogacion.png"))
ventanaPrincipal.iconoError.setPixmap(QPixmap(ruta+"/UIs/Imgs/iconoError.png"))
ventanaPrincipal.btnTuCuenta.setStyleSheet(styleSheetBoton.replace("fondo","qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(203, 203, 203, 255), stop:1 rgba(229, 229, 229, 255))"))

# Acciones de botones varios
# Botones acceder y registrase
ventanaIniciarSesion.btnAcceder.clicked.connect(lambda: iniciarSesionScript())
ventanaIniciarSesion.btnRegistrarse.clicked.connect(lambda: crearCuentaScript())
# Comprueba si checkBox esta seleccionado y cambia echoMode en iniciar sesion
ventanaIniciarSesion.checkBox_Contrasena.clicked.connect(lambda: comprobadorCheckBox1())
ventanaIniciarSesion.checkBox_Contrasena2.clicked.connect(lambda: comprobadorCheckBox2())
# Acciones ventanaIniciarSesion
# Quitar errores
ventanaIniciarSesion.lineEditUsuario.textChanged.connect(lambda: quitarErrores())
ventanaIniciarSesion.lineEditContrasena.textChanged.connect(lambda: quitarErrores())
ventanaIniciarSesion.lineEditUsuario2.textChanged.connect(lambda: quitarErrores())
ventanaIniciarSesion.lineEditContrasena2.textChanged.connect(lambda: quitarErrores())
ventanaIniciarSesion.lineEditContrasenaVerificar.textChanged.connect(lambda: quitarErrores())
# Oculta algo y muestra algo en iniciar sesion
ventanaIniciarSesion.btnIniciarSesion.clicked.connect(lambda: animacionUnfade(ventanaIniciarSesion.frameCrearCuenta, ventanaIniciarSesion.frameIniciarSesion))
ventanaIniciarSesion.btnIniciarSesion.clicked.connect(lambda: quitarErrores())
ventanaIniciarSesion.btnIniciarSesion.clicked.connect(lambda: vaciarLineEdits())
ventanaIniciarSesion.btnCrearCuenta.clicked.connect(lambda: animacionUnfade(ventanaIniciarSesion.frameIniciarSesion, ventanaIniciarSesion.frameCrearCuenta))
ventanaIniciarSesion.btnCrearCuenta.clicked.connect(lambda: quitarErrores())
ventanaIniciarSesion.btnCrearCuenta.clicked.connect(lambda: vaciarLineEdits())
# Boton ocultar pulsado
ventanaPrincipal.btnMinMax.clicked.connect(lambda: pulsarBotonExpandir(ventanaPrincipal))
# Boton tu cuenta pulsado
ventanaPrincipal.btnTuCuenta.clicked.connect(lambda: ventanaPrincipal.btnTuCuenta.setIcon(QIcon(ruta+"/UIs/Imgs/iconoCasaPulsado.png")))
ventanaPrincipal.btnTuCuenta.clicked.connect(lambda: ventanaPrincipal.btnConfig.setIcon(QIcon(ruta+"/UIs/Imgs/iconoConfig.png")))
ventanaPrincipal.btnTuCuenta.clicked.connect(lambda: ventanaPrincipal.btnTuCuenta.setStyleSheet(styleSheetBoton.replace("fondo","qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(203, 203, 203, 255), stop:1 rgba(229, 229, 229, 255))")))
ventanaPrincipal.btnTuCuenta.clicked.connect(lambda: ventanaPrincipal.btnConfig.setStyleSheet(styleSheetBoton.replace("fondo","rgb(255, 255, 255)")))
ventanaPrincipal.btnTuCuenta.clicked.connect(lambda: animacionFadeUnfade(ventanaPrincipal.tuCuenta))
ventanaPrincipal.btnTuCuenta.clicked.connect(lambda: ventanaPrincipal.btnAtras.hide())
# Boton configuracion pulsado
ventanaPrincipal.btnConfig.clicked.connect(lambda: ventanaPrincipal.btnConfig.setIcon(QIcon(ruta+"/UIs/Imgs/iconoConfigPulsado.png")))
ventanaPrincipal.btnConfig.clicked.connect(lambda: ventanaPrincipal.btnTuCuenta.setIcon(QIcon(ruta+"/UIs/Imgs/iconoCasa.png")))
ventanaPrincipal.btnConfig.clicked.connect(lambda: ventanaPrincipal.btnConfig.setStyleSheet(styleSheetBoton.replace("fondo","qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(203, 203, 203, 255), stop:1 rgba(229, 229, 229, 255))")))
ventanaPrincipal.btnConfig.clicked.connect(lambda: ventanaPrincipal.btnTuCuenta.setStyleSheet(styleSheetBoton.replace("fondo","rgb(255, 255, 255)")))
ventanaPrincipal.btnConfig.clicked.connect(lambda: animacionFadeUnfade(ventanaPrincipal.config))
ventanaPrincipal.btnConfig.clicked.connect(lambda: ventanaPrincipal.btnAtras.hide())
# Boton atras pulsado
ventanaPrincipal.btnAtras.clicked.connect(lambda: animacionFadeUnfade(ventanaPrincipal.tuCuenta))
ventanaPrincipal.btnAtras.clicked.connect(lambda: ventanaPrincipal.btnAtras.hide())
# Boton ingresar dinero pulsado
ventanaPrincipal.pushButtonIngresar.clicked.connect(lambda: ingresarDinero())
ventanaPrincipal.pushButtonIngresar.clicked.connect(lambda: quitarErrores())
ventanaPrincipal.pushButtonIngresar.clicked.connect(lambda: ventanaPrincipal.btnAtras.show())
ventanaPrincipal.pushButtonIngresar.clicked.connect(lambda: quitarErrores())
ventanaPrincipal.pushButtonIngresar.clicked.connect(lambda: vaciarLineEdits())
ventanaPrincipal.btnIngresarDinero.clicked.connect(lambda: ingresarDinero())
ventanaPrincipal.btnIngresarDinero.clicked.connect(lambda: quitarErrores())
ventanaPrincipal.btnIngresarDinero.clicked.connect(lambda: vaciarLineEdits())
ventanaPrincipal.btnIngresarDinero.clicked.connect(lambda: ventanaPrincipal.btnAtras.show())
ventanaPrincipal.lineEdit_2.textChanged.connect(lambda: quitarErrores())
# Acciones transferir dinero
ventanaPrincipal.pushButton10_5.clicked.connect(lambda: transferirDineroScript(10))
ventanaPrincipal.pushButton50_5.clicked.connect(lambda: transferirDineroScript(50))
ventanaPrincipal.pushButton100_5.clicked.connect(lambda: transferirDineroScript(100))
ventanaPrincipal.pushButton500_5.clicked.connect(lambda: transferirDineroScript(500))
ventanaPrincipal.pushButton1000_5.clicked.connect(lambda: transferirDineroScript(1000))
ventanaPrincipal.pushButton10000_5.clicked.connect(lambda: transferirDineroScript(10000))
ventanaPrincipal.pushButtonTransferir_3.clicked.connect(lambda: transferirDineroCustomScript())
ventanaPrincipal.lineEdit_6.textChanged.connect(lambda: quitarErrores())
ventanaPrincipal.lineEdit_7.textChanged.connect(lambda: quitarErrores())
# Boton sacar dinero pulsado
ventanaPrincipal.pushButtonSacarDinero.clicked.connect(lambda: sacarDinero())
ventanaPrincipal.pushButtonSacarDinero.clicked.connect(lambda: vaciarLineEdits())
ventanaPrincipal.pushButtonSacarDinero.clicked.connect(lambda: quitarErrores())
ventanaPrincipal.pushButtonSacarDinero.clicked.connect(lambda: ventanaPrincipal.btnAtras.show())
# Boton historial pulsado
ventanaPrincipal.pushButtonHistorial.clicked.connect(lambda: historialVer())
ventanaPrincipal.pushButtonHistorial.clicked.connect(lambda: ventanaPrincipal.btnAtras.show())
# Boton cambiar contraseña pulsado
ventanaPrincipal.pushButtonCambiarContrasena.clicked.connect(lambda: cambiarContraseña())
ventanaPrincipal.pushButtonCambiarContrasena.clicked.connect(lambda: quitarErrores())
ventanaPrincipal.pushButtonCambiarContrasena.clicked.connect(lambda: vaciarLineEdits())
ventanaPrincipal.pushButtonCambiarContrasena.clicked.connect(lambda: ventanaPrincipal.btnAtras.show())
ventanaPrincipal.btnCambiarContrasena.clicked.connect(lambda: cambiarContraseñaScript())
ventanaPrincipal.lineEditContrasenaActual.textChanged.connect(lambda: quitarErrores())
ventanaPrincipal.lineEditNuevaContrasena.textChanged.connect(lambda: quitarErrores())
ventanaPrincipal.lineEditRepetirContrasena.textChanged.connect(lambda: quitarErrores())
# Boton transferir pulsado
ventanaPrincipal.pushButtonTransferir.clicked.connect(lambda: transferirDinero())
ventanaPrincipal.pushButtonTransferir.clicked.connect(lambda: vaciarLineEdits())
ventanaPrincipal.pushButtonTransferir.clicked.connect(lambda: ventanaPrincipal.btnAtras.show())
# Boton cerrar sesion pulsado
ventanaPrincipal.btnCerrarSesion.clicked.connect(lambda: cerrarSesion())
ventanaPrincipal.pushButtonCerrarSesion.clicked.connect(lambda: cerrarSesion())
ventanaPrincipal.btnCerrarSesion_2.clicked.connect(lambda: cerrarSesion())

# Boton cambiar nombre de usuario pulsado
ventanaPrincipal.pushButtonCambiarUsuario.clicked.connect(lambda: animacionFadeUnfade(ventanaPrincipal.cambiarNombreUsuario))
ventanaPrincipal.pushButtonCambiarUsuario.clicked.connect(lambda: vaciarLineEdits())
ventanaPrincipal.pushButtonCambiarUsuario.clicked.connect(lambda: ventanaPrincipal.labelErrorUsuario.hide())
ventanaPrincipal.pushButtonCambiarUsuario.clicked.connect(lambda: ventanaPrincipal.btnAtras.show())
ventanaPrincipal.btnCambiarUsuario.clicked.connect(lambda: cambiarNombreUsuario())
ventanaPrincipal.lineEditNombreUsuario.textChanged.connect(lambda: quitarErrores())
# Boton eliminar cuenta pulsado
ventanaPrincipal.pushButtonEliminarCuenta.clicked.connect(lambda: animacionFadeUnfade(ventanaPrincipal.asegurarEliminarCuenta))
ventanaPrincipal.pushButtonEliminarCuenta.clicked.connect(lambda: ventanaPrincipal.btnAtras.show())
# CheckBox pulsado
ventanaPrincipal.checkBox_Contrasena.clicked.connect(lambda: comprobadorCheckBox3())
# Aceptar pulsado
ventanaPrincipal.btnAceptar.clicked.connect(lambda: animacionFadeUnfade(ventanaPrincipal.tuCuenta))
# Boton eliminar cuenta pulsado
ventanaPrincipal.btnEliminar.clicked.connect(lambda: eliminarCuenta())
# Acciones dinero ingresar
ventanaPrincipal.pushButton10.clicked.connect(lambda: ingresarDineroScript(10))
ventanaPrincipal.pushButton50.clicked.connect(lambda: ingresarDineroScript(50))
ventanaPrincipal.pushButton100.clicked.connect(lambda: ingresarDineroScript(100))
ventanaPrincipal.pushButton500.clicked.connect(lambda: ingresarDineroScript(500))
ventanaPrincipal.pushButton1000.clicked.connect(lambda: ingresarDineroScript(1000))
ventanaPrincipal.pushButton10000.clicked.connect(lambda: ingresarDineroScript(10000))
ventanaPrincipal.pushButtonIngresar_2.clicked.connect(lambda: ingresarDineroCustomScript())
# Acciones sacar dinero
ventanaPrincipal.pushButton10_2.clicked.connect(lambda: comprobadorDinero(10))
ventanaPrincipal.pushButton50_2.clicked.connect(lambda: comprobadorDinero(50))
ventanaPrincipal.pushButton100_2.clicked.connect(lambda: comprobadorDinero(100))
ventanaPrincipal.pushButton500_2.clicked.connect(lambda: comprobadorDinero(500))
ventanaPrincipal.pushButton1000_2.clicked.connect(lambda: comprobadorDinero(1000))
ventanaPrincipal.pushButton10000_2.clicked.connect(lambda: comprobadorDinero(10000))
ventanaPrincipal.pushButtonSacar.clicked.connect(lambda: comprobadorDineroCustom())
ventanaPrincipal.lineEdit_3.textChanged.connect(lambda: quitarErrores())

# Ejecutar app
splashScreen()

app.exec()
