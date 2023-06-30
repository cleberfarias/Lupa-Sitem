from PySide6 import QtCore
from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox, QTableWidgetItem)
from projetolupa_ui import Ui_MainWindow
import sys
from ui_funtions import *
from database import Data_base

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Lupa - Sistema de cadastro de Objetos")
        appIcon = QIcon(u"")
        self.setWindowIcon(appIcon)

        #############################################################################################################
        # Toggle button
        self.btn_toggle.clicked.connect(self.leftMenu)
        #############################################################################################################
        # Paginas do sistema

        self.btn_home.clicked.connect(lambda: self.Pages.setCurrentWidget(self.page_home))
        self.btn_cadastro.clicked.connect(lambda: self.Pages.setCurrentWidget(self.page_cadastro))
        self.btn_sobre.clicked.connect(lambda: self.Pages.setCurrentWidget(self.page_sobre))
        self.btn_contato.clicked.connect(lambda: self.Pages.setCurrentWidget(self.page_contato))
        #############################################################################################################
        ###########################################################################################################
        self.pushButton_6.clicked.connect(self.cadastrar_alunos)

    def leftMenu(self):
        width = self.left_menu.width()

        if width == 9:
            newWidth = 200
        else:
            newWidth = 9

        self.animation = QtCore.QPropertyAnimation(self.left_menu, b"maximumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    def consult_api(self):
        cpf = self.txt_cpf_contr.text()
        data_nascimento = "YYYY-MM-DD"  # Replace with the actual date of birth
        campos = consulta_cpf(cpf, data_nascimento)

        self.txt_nome.setText(campos[0])
        self.txt_logradouro.setText(campos[1])
        self.txt_complemento.setText(campos[2])
        self.txt_municipio.setText(campos[3])
        self.txt_contato.setText(campos[4])
        self.txt_email.setText(campos[5])
        self.txt_matricula.setText(campos[6])
        self.txt_curso.setText(campos[7])
        self.txt_UnidEscola.setText(campos[8])


    def cadastrar_alunos(self):
        db = Data_base()
        db.connect()
    
        fullDataSet = (
            self.txt_cpf.text(), self.txt_nome.text(), self.txt_logradouro.text(), self.txt_complemento.text(),
            self.txt_email.text(), self.txt_contato.text(), self.txt_matricula.text(), self.txt_municipio.text(),
            self.txt_curso.text(), self.txt_UnidEscola.text()
        )

        # CADASTRAR NO BANCO DE DADOS
        resp = db.register_company(fullDataSet)

        if resp == "OK":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Casdastro Realizado")
            msg.setText("Cadastro Realizado com sucesso")
            msg.exec()
            db.close_connection()
            return
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Erro")
            msg.setText("Erro ao cadastrar, verifique se as informações foram preenchidas corretamente!")
            msg.exec()
            db.close_connection()
            return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
