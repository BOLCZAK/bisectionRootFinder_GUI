# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'application.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 760, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.groupBoxFunkcje = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxFunkcje.setGeometry(QtCore.QRect(20, 80, 200, 130))
        self.groupBoxFunkcje.setObjectName("groupBoxFunkcje")
        self.radioButtonWielomian = QtWidgets.QRadioButton(self.groupBoxFunkcje)
        self.radioButtonWielomian.setGeometry(QtCore.QRect(10, 20, 82, 17))
        self.radioButtonWielomian.setObjectName("radioButtonWielomian")
        self.radioButtonTryg = QtWidgets.QRadioButton(self.groupBoxFunkcje)
        self.radioButtonTryg.setGeometry(QtCore.QRect(10, 60, 120, 17))
        self.radioButtonTryg.setObjectName("radioButtonTryg")
        self.radioButtonWyk = QtWidgets.QRadioButton(self.groupBoxFunkcje)
        self.radioButtonWyk.setGeometry(QtCore.QRect(10, 100, 120, 17))
        self.radioButtonWyk.setObjectName("radioButtonWyk")
        self.groupBoxMetoda = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxMetoda.setGeometry(QtCore.QRect(240, 80, 120, 130))
        self.groupBoxMetoda.setObjectName("groupBoxMetoda")
        self.radioButtonBisekcja = QtWidgets.QRadioButton(self.groupBoxMetoda)
        self.radioButtonBisekcja.setGeometry(QtCore.QRect(10, 20, 82, 17))
        self.radioButtonBisekcja.setObjectName("radioButtonBisekcja")
        self.radioButtonSieczne = QtWidgets.QRadioButton(self.groupBoxMetoda)
        self.radioButtonSieczne.setGeometry(QtCore.QRect(10, 60, 82, 17))
        self.radioButtonSieczne.setObjectName("radioButtonSieczne")
        self.groupBoxZakres = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxZakres.setGeometry(QtCore.QRect(380, 80, 120, 130))
        self.groupBoxZakres.setObjectName("groupBoxZakres")
        self.labelPoczatekZakres = QtWidgets.QLabel(self.groupBoxZakres)
        self.labelPoczatekZakres.setGeometry(QtCore.QRect(10, 20, 47, 13))
        self.labelPoczatekZakres.setObjectName("labelPoczatekZakres")
        self.labelKoniecZakres = QtWidgets.QLabel(self.groupBoxZakres)
        self.labelKoniecZakres.setGeometry(QtCore.QRect(10, 67, 47, 13))
        self.labelKoniecZakres.setObjectName("labelKoniecZakres")
        self.lineEditStart = QtWidgets.QLineEdit(self.groupBoxZakres)
        self.lineEditStart.setGeometry(QtCore.QRect(10, 40, 80, 20))
        self.lineEditStart.setText("")
        self.lineEditStart.setObjectName("lineEditStart")
        self.lineEditEnd = QtWidgets.QLineEdit(self.groupBoxZakres)
        self.lineEditEnd.setGeometry(QtCore.QRect(10, 87, 80, 20))
        self.lineEditEnd.setObjectName("lineEditEnd")
        self.groupBoxEpsilon = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxEpsilon.setGeometry(QtCore.QRect(660, 80, 120, 55))
        self.groupBoxEpsilon.setObjectName("groupBoxEpsilon")
        self.lineEditEpsilon = QtWidgets.QLineEdit(self.groupBoxEpsilon)
        self.lineEditEpsilon.setGeometry(QtCore.QRect(10, 20, 100, 20))
        self.lineEditEpsilon.setObjectName("lineEditEpsilon")
        self.groupBoxIteracje = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxIteracje.setGeometry(QtCore.QRect(660, 155, 120, 55))
        self.groupBoxIteracje.setObjectName("groupBoxIteracje")
        self.lineEditIteracje = QtWidgets.QLineEdit(self.groupBoxIteracje)
        self.lineEditIteracje.setGeometry(QtCore.QRect(10, 20, 100, 20))
        self.lineEditIteracje.setObjectName("lineEditIteracje")
        self.groupBoxStop = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxStop.setGeometry(QtCore.QRect(520, 80, 120, 130))
        self.groupBoxStop.setObjectName("groupBoxStop")
        self.radioButtonEpsilon = QtWidgets.QRadioButton(self.groupBoxStop)
        self.radioButtonEpsilon.setGeometry(QtCore.QRect(10, 30, 82, 17))
        self.radioButtonEpsilon.setObjectName("radioButtonEpsilon")
        self.radioButtonIteracje = QtWidgets.QRadioButton(self.groupBoxStop)
        self.radioButtonIteracje.setGeometry(QtCore.QRect(10, 90, 82, 17))
        self.radioButtonIteracje.setObjectName("radioButtonIteracje")
        self.groupBoxPodglad = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxPodglad.setGeometry(QtCore.QRect(20, 220, 200, 50))
        self.groupBoxPodglad.setObjectName("groupBoxPodglad")
        self.labelPodglad = QtWidgets.QLabel(self.groupBoxPodglad)
        self.labelPodglad.setGeometry(QtCore.QRect(10, 10, 180, 30))
        self.labelPodglad.setObjectName("labelPodglad")
        self.groupBoxChoices = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxChoices.setGeometry(QtCore.QRect(240, 220, 540, 50))
        self.groupBoxChoices.setObjectName("groupBoxChoices")
        self.labelChoices = QtWidgets.QLabel(self.groupBoxChoices)
        self.labelChoices.setGeometry(QtCore.QRect(10, 17, 520, 20))
        self.labelChoices.setObjectName("labelChoices")
        self.pushButtonCalculate = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonCalculate.setGeometry(QtCore.QRect(20, 280, 760, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButtonCalculate.setFont(font)
        self.pushButtonCalculate.setObjectName("pushButtonCalculate")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 340, 200, 200))
        self.groupBox.setObjectName("groupBox")
        self.labelZerowe = QtWidgets.QLabel(self.groupBox)
        self.labelZerowe.setGeometry(QtCore.QRect(10, 20, 80, 20))
        self.labelZerowe.setObjectName("labelZerowe")
        self.lineEditZerowe = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditZerowe.setEnabled(False)
        self.lineEditZerowe.setGeometry(QtCore.QRect(90, 20, 100, 20))
        self.lineEditZerowe.setText("")
        self.lineEditZerowe.setObjectName("lineEditZerowe")
        self.lineEditCzas = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditCzas.setEnabled(False)
        self.lineEditCzas.setGeometry(QtCore.QRect(90, 50, 100, 20))
        self.lineEditCzas.setObjectName("lineEditCzas")
        self.labelCzas = QtWidgets.QLabel(self.groupBox)
        self.labelCzas.setGeometry(QtCore.QRect(10, 50, 80, 20))
        self.labelCzas.setObjectName("labelCzas")
        self.labelIloscIteracji = QtWidgets.QLabel(self.groupBox)
        self.labelIloscIteracji.setGeometry(QtCore.QRect(10, 80, 80, 20))
        self.labelIloscIteracji.setObjectName("labelIloscIteracji")
        self.lineEditIloscIteracji = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditIloscIteracji.setEnabled(False)
        self.lineEditIloscIteracji.setGeometry(QtCore.QRect(90, 80, 100, 20))
        self.lineEditIloscIteracji.setObjectName("lineEditIloscIteracji")
        self.lineEditDokladnoscWynik = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditDokladnoscWynik.setEnabled(False)
        self.lineEditDokladnoscWynik.setGeometry(QtCore.QRect(90, 110, 100, 20))
        self.lineEditDokladnoscWynik.setObjectName("lineEditDokladnoscWynik")
        self.labelDokladnoscWynik = QtWidgets.QLabel(self.groupBox)
        self.labelDokladnoscWynik.setGeometry(QtCore.QRect(10, 110, 80, 20))
        self.labelDokladnoscWynik.setObjectName("labelDokladnoscWynik")
        self.pushButtonXValuesChange = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonXValuesChange.setGeometry(QtCore.QRect(10, 160, 180, 30))
        self.pushButtonXValuesChange.setObjectName("pushButtonXValuesChange")
        self.groupBoxchart = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxchart.setGeometry(QtCore.QRect(240, 340, 540, 200))
        self.groupBoxchart.setObjectName("groupBoxchart")
        self.labelGraph = QtWidgets.QLabel(self.groupBoxchart)
        self.labelGraph.setGeometry(QtCore.QRect(10, 20, 214, 160))
        self.labelGraph.setText("")
        self.labelGraph.setObjectName("labelGraph")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Witaj w programie do okre??lania miejsc zerowych, wybierz interesuj??ce ciebie opcje"))
        self.groupBoxFunkcje.setTitle(_translate("MainWindow", "Funkcje"))
        self.radioButtonWielomian.setText(_translate("MainWindow", "Wielomian"))
        self.radioButtonTryg.setText(_translate("MainWindow", "Trygonometryczna"))
        self.radioButtonWyk.setText(_translate("MainWindow", "Wyk??adnicza"))
        self.groupBoxMetoda.setTitle(_translate("MainWindow", "Metoda"))
        self.radioButtonBisekcja.setText(_translate("MainWindow", "Bisekcja"))
        self.radioButtonSieczne.setText(_translate("MainWindow", "Sieczne"))
        self.groupBoxZakres.setTitle(_translate("MainWindow", "Przedzia??"))
        self.labelPoczatekZakres.setText(_translate("MainWindow", "Pocz??tek"))
        self.labelKoniecZakres.setText(_translate("MainWindow", "Koniec"))
        self.lineEditStart.setPlaceholderText(_translate("MainWindow", "Pocz??tek"))
        self.lineEditEnd.setPlaceholderText(_translate("MainWindow", "Koniec"))
        self.groupBoxEpsilon.setTitle(_translate("MainWindow", "Dok??adno????"))
        self.lineEditEpsilon.setPlaceholderText(_translate("MainWindow", "Epsilon"))
        self.groupBoxIteracje.setTitle(_translate("MainWindow", "Ilo???? Iteracji"))
        self.lineEditIteracje.setPlaceholderText(_translate("MainWindow", "Iteracje"))
        self.groupBoxStop.setTitle(_translate("MainWindow", "Kryterium zatrzymania"))
        self.radioButtonEpsilon.setText(_translate("MainWindow", "Epsilon"))
        self.radioButtonIteracje.setText(_translate("MainWindow", "Liczba iteracji"))
        self.groupBoxPodglad.setTitle(_translate("MainWindow", "Podgl??d funkcji"))
        self.labelPodglad.setText(_translate("MainWindow", "Placeholder dla podgl??du"))
        self.groupBoxChoices.setTitle(_translate("MainWindow", "Wybrane ustawienia"))
        self.labelChoices.setText(_translate("MainWindow", "Placeholder dla wybranych ustawie??"))
        self.pushButtonCalculate.setText(_translate("MainWindow", "DO IT"))
        self.groupBox.setTitle(_translate("MainWindow", "Wyniki oblicze??"))
        self.labelZerowe.setText(_translate("MainWindow", "Miejsce zerowe:"))
        self.labelCzas.setText(_translate("MainWindow", "Czas [s]:"))
        self.labelIloscIteracji.setText(_translate("MainWindow", "Ilo???? iteracji:"))
        self.labelDokladnoscWynik.setText(_translate("MainWindow", "Dok??adno????:"))
        self.pushButtonXValuesChange.setText(_translate("MainWindow", "Poka?? zmiany warto??ci X"))
        self.groupBoxchart.setTitle(_translate("MainWindow", "Reprezentacja Graficzna"))
