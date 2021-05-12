# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'application.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
import numpy as np
import cv2
import application
import time as tm


def licz_iter(funkcja, przedzial, nazwa, *args, **kwargs):
    if 'bisekcja' in args:
        print('=============BISEKCJA=============')
        nowy_x = lambda a,b: (a + b) / 2
    elif 'sieczne' in args:
        print('=============SIECZNE=============')
        nowy_x = lambda a,b: a + (funkcja(a) * ((b - a) / (funkcja(a)-funkcja(b))))
    a, b = przedzial
    i = 0
    ilosc_iteracji = 0
    if 'iter' in kwargs.keys():
        poczatek = tm.perf_counter()
        print('ITERACYJNIE')
        while i<kwargs['iter']:
            # print(abs(a-b))
            if funkcja(a)*funkcja(b)<0:
                x = nowy_x(a, b)
                if funkcja(x)==0:
                    print(f'{x} jest miejscem zerowym funkcji')
                else:
                    if funkcja(a)*funkcja(x)<0:
                        a, b = a, x
                        print(x)
                    else:
                        a, b = x, b
                        print(x)
                MyQtApp.wynik.append(x)
            else:
                print('Na podanym przedziale funkcja nie ma miejsc zerowych !!!')
            i+=1
        print('Przekroczono maksymalną zadaną ilość iteracji')
        MyQtApp.ilosc_iteracji = i
        koniec = tm.perf_counter()
        MyQtApp.czas = koniec - poczatek
        print(f"KONIEC X = {x}")
        print(f"KONIEC F(x) = {funkcja(x)}")
        print(f"CZAS WYKONANIA = {koniec-poczatek}")
    elif 'eps' in kwargs.keys():
        poczatek = tm.perf_counter()
        print('EPSILONOWO')
        # print('ABS = ', abs(a-b))
        x1 = a
        x2 = b
        x=a
        while not abs(x1-x2)<kwargs['eps']:
            print('ABS = ', abs(a-b))
            if funkcja(a)*funkcja(b)<0:
                print(f"POPRZEDNI X = {x1}")
                x1 = x
                x = nowy_x(a, b)
                print(f"NASTĘPNY X = {x2}")
                x2 = x
                if funkcja(x)==0:
                    print(f'{x} jest miejscem zerowym funkcji')
                else:
                    if funkcja(a)*funkcja(x)<0:
                        print('A = ', a, "\tB = ", b)
                        a, b = a, x
                        print(x)
                    else:
                        print('A = ', a, "\tB = ", b)
                        a, b = x, b
                        print(x)
                MyQtApp.wynik.append(x)
            else:
                print('Na podanym przedziale funkcja nie ma miejsc zerowych !!!')
            ilosc_iteracji+=1
        else:
            print('Osiągnięto zamierzoną dokładność')
        MyQtApp.ilosc_iteracji = ilosc_iteracji
        koniec = tm.perf_counter()
        MyQtApp.czas = koniec-poczatek
        print(f"KONIEC X = {x}")
        print(f"KONIEC F(x) = {funkcja(x)}")
        print(f"CZAS WYKONANIA = {koniec-poczatek}")
    # print(a, b, 'DZIALA', f'{x} = X')

    x_values = np.linspace(przedzial[0], przedzial[1], num=100)
    y_values = [funkcja(x) for x in x_values]

    plt.figure(1)
    plt.plot(x_values, y_values)
    try:
        plt.scatter(x, funkcja(x), c='red')
    except NameError:
        pass
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title(nazwa)
    plt.grid()
    plt.savefig('graphs/graph.png')
    # plt.show()
    img = cv2.imread('graphs/graph.png')
    img = cv2.resize(img, (0, 0), fx=(1 / 3), fy=(1 / 3))
    cv2.imwrite('graphs/img.png', img)


def plotGraph(funkcja ,przedzial, nazwa):
    x_values = np.linspace(przedzial[0], przedzial[1], num=100)
    y_values = [funkcja(x) for x in x_values]

    plt.figure(2)
    plt.plot(x_values, y_values)
    try:
        plt.scatter(MyQtApp.wynik[-1], funkcja(MyQtApp.wynik[-1]), c='red')
    except NameError:
        pass
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title(nazwa)
    plt.grid()
    plt.show()

def plot_x_change(x_values):
    xaxis = [x for x in range(len(x_values))]
    plt.figure(3)
    plt.plot(xaxis, x_values, c='purple')
    plt.hlines(MyQtApp.wynik[-1], xaxis[0], xaxis[-1], colors='green', linestyles='dashed')
    plt.title('X values change')
    plt.xlabel("Iteration")
    plt.ylabel('Values of X')
    plt.grid()
    plt.show()

def clickable(widget):
    class Filter(QtCore.QObject):

        clicked = QtCore.pyqtSignal()

        def eventFilter(self, obj, event):

            if obj == widget:
                if event.type() == QtCore.QEvent.MouseButtonRelease:
                    if obj.rect().contains(event.pos()):
                        self.clicked.emit()
                        # The developer can opt for .emit(obj) to get the object within the slot.
                        return True

            return False

    filter = Filter(widget)
    widget.installEventFilter(filter)
    return filter.clicked


class MyQtApp(application.Ui_MainWindow, QtWidgets.QMainWindow):

    wynik = []
    czas = 0
    ilosc_iteracji = 0

    def __init__(self):
        super(MyQtApp, self).__init__()
        self.setupUi(self)

        self.radioButtonWielomian.clicked.connect(self.wyborFunkcji)
        self.radioButtonTryg.clicked.connect(self.wyborFunkcji)
        self.radioButtonWyk.clicked.connect(self.wyborFunkcji)

        self.pushButtonCalculate.clicked.connect(self.ustawienia)

        # self.labelGraph.mouseDoubleClickEvent.connect(plotGraph(self.usedFunction, self.usedSection, 'test'))
        clickable(self.labelGraph).connect(self.labelPlot)
        self.pushButtonXValuesChange.clicked.connect(self.showXValuesChange)



    def wyborFunkcji(self):
        if self.radioButtonWielomian.isChecked():
            # self.labelPodglad.setText('5x^3+4x^2-4x-7')
            self.labelPodglad.setText('')
            self.labelPodglad.setStyleSheet('background-image: url("assets/wielomian_1.png")')
        if self.radioButtonTryg.isChecked():
            # self.labelPodglad.setText('sin(x)^2-cos(x)+3x-7')
            self.labelPodglad.setText('')
            self.labelPodglad.setStyleSheet('background-image: url("assets/trygonometryczna_1.png")')
        if self.radioButtonWyk.isChecked():
            # self.labelPodglad.setText('5^x-4')
            self.labelPodglad.setText('')
            self.labelPodglad.setStyleSheet('background-image: url("assets/wykladnicza_1.png")')

    def ustawienia(self):
        MyQtApp.wynik = []
        if (self.radioButtonWielomian.isChecked() or self.radioButtonTryg.isChecked() or self.radioButtonWyk.isChecked()) and (self.radioButtonBisekcja.isChecked() or self.radioButtonSieczne.isChecked()) and self.lineEditStart.text()!='' and self.lineEditEnd.text()!='' and (self.radioButtonEpsilon.isChecked() or self.radioButtonIteracje.isChecked()) and (self.lineEditEpsilon.text()!='' or self.lineEditIteracje.text()!=''):
            radiofunc = [self.radioButtonWielomian, self.radioButtonWyk, self.radioButtonTryg]
            funkcja = ''
            metoda = ''
            kryterium = ''
            przedzial = (float(self.lineEditStart.text()), float(self.lineEditEnd.text()))
            if self.radioButtonEpsilon.isChecked():
                kryterium = 'Epsilon'
                epsilon = float(self.lineEditEpsilon.text())
            elif self.radioButtonIteracje.isChecked():
                kryterium = 'Iteracje'
                iteracje = int(self.lineEditIteracje.text())
            self.usedSection = przedzial
            for x in radiofunc:
                if x.isChecked():
                    funkcja = x.text()
            if self.radioButtonBisekcja.isChecked():
                metoda = 'Bisekcja'
            elif self.radioButtonSieczne.isChecked():
                metoda = 'Sieczne'

            # if self.radioButtonEpsilon.isChecked():
            #     kryterium = 'Epsilon'
            # elif self.radioButtonIteracje.isChecked():
            #     kryterium = 'Iteracje'

            if kryterium == 'Epsilon':
                self.labelChoices.setText(f'{funkcja}, {metoda}, {self.lineEditStart.text()}, {self.lineEditEnd.text()}, {kryterium}, {self.lineEditEpsilon.text()}')
            else:
                self.labelChoices.setText(f'{funkcja}, {metoda}, {self.lineEditStart.text()}, {self.lineEditEnd.text()}, {kryterium}, {self.lineEditIteracje.text()}')
            if kryterium == 'Epsilon':
                if funkcja=='Wielomian':
                    self.usedFunction = self.wielomian
                    if metoda == 'Sieczne':
                        licz_iter(self.wielomian, przedzial, 'test', 'sieczne', eps=epsilon)
                    else:
                        licz_iter(self.wielomian, przedzial, 'test', 'bisekcja', eps=epsilon)
                elif funkcja=='Trygonometryczna':
                    self.usedFunction = self.trygonometryczna
                    if metoda == 'Sieczne':
                        licz_iter(self.trygonometryczna, przedzial, 'test', 'sieczne', eps=epsilon)
                    else:
                        licz_iter(self.trygonometryczna, przedzial, 'test', 'bisekcja', eps=epsilon)
                else:
                    self.usedFunction = self.wykladnicza
                    if metoda == 'Sieczne':
                        licz_iter(self.wykladnicza, przedzial, 'test', 'sieczne', eps=epsilon)
                    else:
                        licz_iter(self.wykladnicza, przedzial, 'test', 'bisekcja', eps=epsilon)
                print(MyQtApp.wynik)
                self.lineEditZerowe.setText(str(MyQtApp.wynik[-1])[0:8])
                self.lineEditCzas.setText(str(MyQtApp.czas)[0:12])
                self.lineEditIloscIteracji.setText(str(MyQtApp.ilosc_iteracji))
                self.lineEditDokladnoscWynik.setText("{:.10f}".format(abs(MyQtApp.wynik[-2] - MyQtApp.wynik[-1]))[0:12])
                self.labelGraph.setStyleSheet("""
                    background: url("graphs/img.png") no-repeat center;
                    background-size: contain;
                """)
            else:
                if funkcja == 'Wielomian':
                    self.usedFunction = self.wielomian
                    if metoda == 'Sieczne':
                        licz_iter(self.wielomian, przedzial, 'test', 'sieczne', iter=iteracje)
                    else:
                        licz_iter(self.wielomian, przedzial, 'test', 'bisekcja', iter=iteracje)
                elif funkcja == 'Trygonometryczna':
                    self.usedFunction = self.trygonometryczna
                    if metoda == 'Sieczne':
                        licz_iter(self.trygonometryczna, przedzial, 'test', 'sieczne', iter=iteracje)
                    else:
                        licz_iter(self.trygonometryczna, przedzial, 'test', 'bisekcja', iter=iteracje)
                else:
                    self.usedFunction = self.wykladnicza
                    if metoda == 'Sieczne':
                        licz_iter(self.wykladnicza, przedzial, 'test', 'sieczne', iter=iteracje)
                    else:
                        licz_iter(self.wykladnicza, przedzial, 'test', 'bisekcja', iter=iteracje)
                print(MyQtApp.wynik)
                self.lineEditZerowe.setText(str(MyQtApp.wynik[-1])[0:8])
                self.lineEditCzas.setText(str(MyQtApp.czas)[0:12])
                self.lineEditIloscIteracji.setText(str(MyQtApp.ilosc_iteracji))
                self.lineEditDokladnoscWynik.setText("{:.10f}".format(abs(MyQtApp.wynik[-2] - MyQtApp.wynik[-1]))[0:12])
                self.labelGraph.setStyleSheet("""
                    background: url("graphs/img.png") no-repeat center;
                    background-size: contain;
                """)

    def showXValuesChange(self):
        plot_x_change(MyQtApp.wynik)

    def labelPlot(self):
        plotGraph(self.usedFunction, self.usedSection, 'test')

    def wielomian(self, x):
        return 5 * x ** 3 + 4 * x ** 2 - 4 * x - 7

    def trygonometryczna(self, x):
        return np.sin(x) * np.sin(x) - np.cos(x) + 3 * x - 7

    def wykladnicza(self, x):
        return 2 ** x -7


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    with open('style.css', 'r') as f:
        app.setStyleSheet(f.read())
    ui = MyQtApp()
    ui.show()
    sys.exit(app.exec_())