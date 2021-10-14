import sys
# Импортируем наш интерфейс из файла
from bus2 import *
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem as QWT
from  PyQt5.QtWidgets import QMessageBox
import os
from PyQt5 import QtPrintSupport, QtCore
import dialogvoditel
import dialogauto
import dialogmarshrut
import dialogflight
import socket
import dialogr

import time

import traceback
HOST='localhost'
#HOST = '192.168.43.230'  
PORT = 12344      

def log_uncaught_exceptions(ex_cls, ex, tb):
    text = '{}: {}:\n'.format(ex_cls.__name__, ex)
    text += ''.join(traceback.format_tb(tb))
    print(text)
    sys.exit()
sys.excepthook = log_uncaught_exceptions

class Dialogvoditel(QtWidgets.QDialog, dialogvoditel.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)       
class Dialogauto(QtWidgets.QDialog, dialogauto.Ui_Dialog_Auto):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
class Dialogmarshrut(QtWidgets.QDialog, dialogmarshrut.Ui_Dialog_Marshrut):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
class Dialogflight(QtWidgets.QDialog, dialogflight.Ui_Dialog_Flight):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
class Dialogr(QtWidgets.QDialog, dialogr.Ui_Dialog_r):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.dialogvoditell=Dialogvoditel()
        self.dialogautoo=Dialogauto()
        self.dialogmarshrutt=Dialogmarshrut()
        self.dialogflightt=Dialogflight()
        self.dialogrr=Dialogr()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_4.clicked.connect(lambda:self.output(0,0))
        self.ui.pushButton_2.clicked.connect(lambda: self.output(1,1))
        self.ui.pushButton_3.clicked.connect(lambda: self.output(2,2))
        self.ui.pushButton_5.clicked.connect(self.request)
        self.ui.pushButton.clicked.connect(lambda:self.output(2,3))
        self.ui.action_7.triggered.connect(lambda: self.setenabledf(1))
        self.ui.action_8.triggered.connect(lambda: self.setenabledt(0))
        self.ui.tabWidget.currentChanged.connect(self.pri)
        
        self.ui.action_3.triggered.connect(self.prog)
        self.ui.action_4.triggered.connect(self.avtor)
      
        self.ui.action_6.triggered.connect(self.ex)
        self.dialogvoditell.buttonBox.accepted.connect(self.upd)
        self.dialogautoo.buttonBox.accepted.connect(self.upd)
        self.dialogmarshrutt.buttonBox.accepted.connect(self.upd)
        self.dialogflightt.buttonBox.accepted.connect(self.upd)
      
        self.ui.pushButton.setEnabled(False)
        self.ui.pushButton_3.setEnabled(False)
        self.ui.pushButton_2.setEnabled(False)

        self.kk=1
       
    def dialogvoditel(self):
        if self.yy==3:#если добавление - блокируем спинбокс
                self.dialogvoditell.spinBox.setEnabled(False)
                self.dialogautoo.spinBox.setEnabled(False)
                self.dialogmarshrutt.spinBox_2.setEnabled(False)
                self.dialogflightt.spinBox.setEnabled(False)
        if self.yy==2:#если изменение - спинбокс активен
                self.dialogvoditell.spinBox.setEnabled(True)
                self.dialogautoo.spinBox.setEnabled(True)
                self.dialogmarshrutt.spinBox_2.setEnabled(True)
                self.dialogflightt.spinBox.setEnabled(True)       
        if self.nTub==0:
            self.dialogvoditell.show()
            self.kk=0
        if self.nTub==1:
            self.dialogautoo.show()
            self.kk=0
        if self.nTub==2:
            self.dialogmarshrutt.show()
            self.kk=0
        if self.nTub==3:
            self.dialogflightt.show()
            self.kk=0

    def ex(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(bytes('close','utf-8'))
            s.close()
        self.close()

    def prog(self):
        os.startfile("instruct.txt")
    def avtor(self):
        QMessageBox.about(self,"Об авторе ","Распопова М.В, курсант 431 группы ТАТК - филиала МГТУ ГА.")
    def pri(self):
        
        self.ui.stackedWidget_2.setCurrentIndex(0)
        if self.ui.tabWidget.currentIndex()==4:
            self.ui.stackedWidget_2.setCurrentIndex(1)
    def setenabledt(self,x):
        pas=open("password.txt","r+",encoding="utf-8")
        password=pas.readline()
        if password=="":
            txt,oks=QtWidgets.QInputDialog.getText(self,'Пароль','Придумайте пароль')
            pas.write(txt)
            if oks:
                self.ui.pushButton.setEnabled(True)
                self.ui.pushButton_3.setEnabled(True)
                self.ui.pushButton_2.setEnabled(True)
        else:
            txt,oks=QtWidgets.QInputDialog.getText(self,'Пароль','Введите пароль')
            if oks:
                if txt==password:
                    self.ui.pushButton.setEnabled(True)
                    self.ui.pushButton_3.setEnabled(True)
                    self.ui.pushButton_2.setEnabled(True)
                else:
                    QMessageBox.about(self,"Неверный пароль ","Неверный пароль.")
    def setenabledf(self,x):
        self.ui.pushButton.setEnabled(False)
        self.ui.pushButton_3.setEnabled(False)
        self.ui.pushButton_2.setEnabled(False) 
    def request(self):       
       
            
        self.currText = self.ui.listWidget.currentRow()        
        try:
            
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((HOST, PORT))
                if self.currText==0:                    
                    txt,oks=QtWidgets.QInputDialog.getText(self,'Запрос 1','Количество мест >?')
                    if oks:
                        self.ui.statusbar.showMessage("Вывести машины, у которых количество мест >"+str(txt))
                        s.sendall(bytes(f'SELECT *FROM Автомашины WHERE ЧислоМест>{int(txt)}','utf-8'))
                        k = s.recv(18384).decode(encoding='utf-8')
                        k = eval(k)
                        
                           
                if self.currText==1:
                    txt,oks=QtWidgets.QInputDialog.getText(self,'Запрос 2','Стаж работы >?') 
                    if oks:
                        
                        self.ui.statusbar.showMessage("Вывести водителей , стаж которых >"+str(txt))
                        s.sendall(bytes(f'SELECT *FROM Водитель WHERE СтажРаботы>{int(txt)}','utf-8'))
                        k = s.recv(18384).decode(encoding='utf-8')
                        k = eval(k)
                              
                if self.currText==2:
                    txt,oks=QtWidgets.QInputDialog.getText(self,'Запрос 3','Введите дату (ДД-ММ-ГГГГ)')                
                    if oks:
                        self.ui.statusbar.showMessage("Вывести все номера рейсов за "+str(txt))
                        s.sendall(bytes(f'SELECT * FROM Рейс WHERE Дата="{txt}"','utf-8'))
                        k = s.recv(18384).decode(encoding='utf-8')
                        k = eval(k)
                if self.currText==3:
                    txt,oks=QtWidgets.QInputDialog.getText(self,'Запрос 4','Марка машины')
                    if oks:
                        self.ui.statusbar.showMessage("Вывести номер рейса , на котором была машина с маркой   "+str(txt))
                        s.sendall(bytes(f'SELECT Рейс.НомерРейса from Рейс , Автомашины WHERE Автомашины.МаркаМашины="{txt}" and Рейс.КодМашины=Автомашины.КодМашины"','utf-8')) 
                        k = s.recv(18384).decode(encoding='utf-8')
                        k = eval(k)
                if self.currText==4:
                    txt,oks=QtWidgets.QInputDialog.getText(self,'Запрос 5','Введите дату (ДД-ММ-ГГГГ)')
                    if oks:
                        self.ui.statusbar.showMessage("Вывести водителей , которые совершили рейс  "+str(txt))
                        s.sendall(bytes(f'SELECT Водитель.ТабельныйНомерВодителя,Водитель.ФИО,Водитель.ДатаРождения,Водитель.СтажРаботы FROM Водитель,Рейс WHERE Водитель.ТабельныйНомерВодителя=Рейс.ТабельныйНомерВодителя and Рейс.Дата="{txt}"','utf-8'))     
                        k = s.recv(18384).decode(encoding='utf-8')
                        k = eval(k)
                if self.currText==5:
                    txt,oks=QtWidgets.QInputDialog.getText(self,'Запрос 6','Номер маршрута >')
                    if oks:
                        self.ui.statusbar.showMessage("Вывести водителя , который совершал рейс по маршруту - "+str(txt))
                        s.sendall(bytes(f'SELECT Водитель.ТабельныйНомерВодителя,Водитель.ФИО,Водитель.ДатаРождения,Водитель.СтажРаботы FROM Водитель,Рейс WHERE Рейс.КодМаршрута={txt} and Водитель.ТабельныйНомерВодителя=Рейс.ТабельныйНомерВодителя"','utf-8')) 
                        k = s.recv(18384).decode(encoding='utf-8')
                        k = eval(k)
                if self.currText==6:
                    txt,oks=QtWidgets.QInputDialog.getText(self,'Запрос 7','Расстояние >')                
                    if oks:
                        self.ui.statusbar.showMessage("Вывести маршрут, расстояние которого  >"+str(txt))
                        s.sendall(bytes(f'SELECT * FROM  Маршрут WHERE Маршрут.Расстояние>{txt}','utf-8'))
                        k = s.recv(18384).decode(encoding='utf-8')
                        k = eval(k)
                if self.currText==7:
                    txt,oks=QtWidgets.QInputDialog.getText(self,'Запрос 8','Введите дату (ДД-ММ-ГГГГ)')                
                    if oks:
                        self.ui.statusbar.showMessage("Вывести машины, которые  совершили рейс  "+str(txt))
                        s.sendall(bytes(f'SELECT Автомашины.КодМашины, Автомашины.МаркаМашины, Автомашины.ЧислоМест, Автомашины.РасходТоплива , Рейс.Дата from Автомашины, Рейс WHERE Рейс.Дата="{txt}"','utf-8'))
                        k = s.recv(18384).decode(encoding='utf-8')
                        k = eval(k)
                if self.currText==8:
                    txt,oks=QtWidgets.QInputDialog.getText(self,'Запрос 9','Расход топлива >')
                    if oks:
                        self.ui.statusbar.showMessage("Сколько машин, у которых расход топлива >"+str(txt))
                        s.sendall(bytes(f'SELECT COUNT(*)  FROM Автомашины WHERE РасходТоплива >{txt}','utf-8'))
                        k = s.recv(18384).decode(encoding='utf-8')
                        k = eval(k)
                if self.currText==9:
                    txt,oks=QtWidgets.QInputDialog.getText(self,'Запрос 10','Цена билета')
                    if oks:
                        self.ui.statusbar.showMessage("Вывести запись рейсов, цена билета которых >"+str(txt))
                        s.sendall(bytes(f'SELECT * FROM Рейс WHERE ЦенаБилета>{txt}','utf-8'))
                        k = s.recv(18384).decode(encoding='utf-8')
                        k = eval(k)

                if self.currText==10:
                    txt,oks=QtWidgets.QInputDialog.getText(self,'Запрос 11','Номер водителя')
                    if oks:
                        self.ui.statusbar.showMessage("Вывести водителя по номеру >"+str(txt))
                        s.sendall(bytes(f'SELECT *from Водитель WHERE ТабельныйНомерВодителя={txt}','utf-8'))
                        k = s.recv(18384).decode(encoding='utf-8')
                        k = eval(k)
                if self.currText==11:
                    txt,oks=QtWidgets.QInputDialog.getText(self,'Запрос 12','Код машины')
                    if oks:
                        self.ui.statusbar.showMessage("Вывести Автомашину по номеру >"+str(txt))
                        s.sendall(bytes(f'SELECT *from Автомашины WHERE КодМашины={txt}','utf-8'))
                        k = s.recv(18384).decode(encoding='utf-8')
                        k = eval(k)
                if self.currText==12:
                    txt,oks=QtWidgets.QInputDialog.getText(self,'Запрос 13','Код маршрута')
                    if oks:
                        self.ui.statusbar.showMessage("Вывести Маршрут по номеру >"+str(txt))
                        s.sendall(bytes(f'SELECT *from Маршрут WHERE КодМаршрута={txt}','utf-8'))
                        k = s.recv(18384).decode(encoding='utf-8')
                        k = eval(k)
                if self.currText==13:
                    txt,oks=QtWidgets.QInputDialog.getText(self,'Запрос 14','Номер рейса')
                    if oks:
                        self.ui.statusbar.showMessage("Вывести Рейс по номеру >"+str(txt))
                        s.sendall(bytes(f'SELECT *from Рейс WHERE НомерРейса={txt}','utf-8'))
                        k = s.recv(18384).decode(encoding='utf-8')
                        k = eval(k)
                try:
                    
                    
                    print(k)
                    if k==1:
                        pass
                    else:
                        self.insTb(k,self.ui.tableWidget)
                   
                except:
                    
                    QMessageBox.critical(self,"Ошибка ","нет данных")
                    
                s.close()
                
            
        except:
            pass
        
    def adds(self):
        connection = sqlite3.connect('bus.db')
        cursor = connection.cursor()
        stolb=0
        up=[]
        upp=[]
     
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((HOST, PORT))
                
                if self.nTub==0:#если первая таблица
                    
                    for i in range(self.colum):#по количеству столбцов в таблице
                        up.append(self.dialogvoditell.tableWidget.item(0,stolb).text())#считывание значений 
                        stolb+=1
                    for i in up:
                        if i.isdigit():
                            
                            upp.append(int(i))
                        else:
                            upp.append(i)
                    
                    try:
                        valid_date = time.strptime(upp[2], '%m-%d-%Y')
                        cr=1
                    except ValueError:
                        cr=0
                    
                    if type(upp[0])==int and type(upp[1])==str and type(upp[3])==int and cr==1 :
                        
                        up=tuple(upp)

                        s.sendall(bytes(f'INSERT INTO Водитель VALUES{up}','utf-8'))
                        
                    else:
                        QMessageBox.critical(self,"Ошибка ","Запись некорректна") 
                if self.nTub==1:
                    for i in range(self.colum):
                        up.append(self.dialogautoo.tableWidget.item(0,stolb).text())
                        stolb+=1
                    for i in up:
                        if i.isdigit():
                        
                            upp.append(int(i))
                        else:
                            upp.append(i)
                
                    
                    if type(upp[0])==int and type(upp[1])==str and type(upp[2])==int and type(upp[3])==int:
                        up=tuple(up)
                        s.sendall(bytes(f'INSERT INTO Автомашины VALUES{up}','utf-8'))
                        
                    else:
                        QMessageBox.critical(self,"Ошибка ","Запись некорректна") 
                if self.nTub==2:
                    
                    for i in range(self.colum):
                        up.append(self.dialogmarshrutt.tableWidget_2.item(0,stolb).text())
                        stolb+=1
                    for i in up:
                        if i.isdigit():
                            
                            upp.append(int(i))
                        else:
                            upp.append(i)
                    
                    if type(upp[0])==int and type(upp[1])==str and type(upp[2])==str and type(upp[3])==int:
                        up=tuple(up)
                        s.sendall(bytes(f'INSERT INTO Маршрут VALUES{up}','utf-8'))
                        
                    else:
                        QMessageBox.critical(self,"Ошибка ","Запись некорректна")
                if self.nTub==3:
                    stolb=4
                    
                    for i in range(1):
                        up.append(self.dialogflightt.tableWidget_4.item(0,0).text())
                        
                        
                    up.insert(1,self.combobox1.currentText())
                    up.insert(2,self.combobox2.currentText())
                    up.insert(3,self.combobox3.currentText())    

                    for i in range(4):
                        up.append(self.dialogflightt.tableWidget_4.item(0,stolb).text())
                        stolb+=1
                    
                    for i in up:
                        if i.isdigit():
            
                            upp.append(int(i))
                        else:
                            upp.append(i)
                    
                   
                    try:
                        valid_date = time.strptime(upp[6], '%m-%d-%Y')
                        valid_date1 = time.strptime(upp[5], '%H:%M')
                        valid_date2 = time.strptime(upp[4], '%H:%M')
                      
                        cr=1
                        
                    except ValueError:
                        cr=0
                    
                    if type(upp[0])==int and cr==1 and type(upp[7])==int:
                        up=tuple(up)     
                        s.sendall(bytes(f'INSERT INTO Рейс VALUES{up}','utf-8'))
                    else:
                        QMessageBox.critical(self,"Ошибка ","Запись некорректна")
                        
                s.close()        

               
                x=0
                y=0
                self.kk=1
                self.output(x,y)
        except:
            QMessageBox.critical(self,"Ошибка ","Запись некорректна") 
    def upd(self):
        if self.yy==3:#добавление
            self.adds()      
        if self.yy==2:
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect((HOST, PORT))
                    up=[]
                    upp=[]
                    stolb=0
                    if self.nTub==0:
                        for i in range(self.colum):#по количеству столбцов в таблице
                            up.append(self.dialogvoditell.tableWidget.item(0,stolb).text())#считывание значений 
                            stolb+=1
                        
                        for i in up:
                            if i.isdigit():
                                
                                upp.append(int(i))
                            else:
                                upp.append(i)
                       
                        try:
                            valid_date = time.strptime(upp[2], '%m-%d-%Y')
                            cr=1
                        except ValueError:
                            cr=0
                        
                        if type(upp[0])==int and type(upp[1])==str and type(upp[3])==int and cr==1 :
                            up=tuple(up)
                            number=int(self.dialogvoditell.spinBox.text())
                            idd = self.ui.tableWidget_1.item(number- 1, 0).text()
                            
                            s.sendall(bytes(f'UPDATE Водитель SET ТабельныйНомерВодителя = {up[0]}, ФИО = "{up[1]}", ДатаРождения ="{up[2]}", СтажРаботы = {up[3]} WHERE ТабельныйНомерВодителя= {idd}','utf-8'))
                            
                        else:
                            QMessageBox.critical(self,"Ошибка ","Запись некорректна")
                    if self.nTub==1:
                        for i in range(self.colum):#по количеству столбцов в таблице
                            up.append(self.dialogautoo.tableWidget.item(0,stolb).text())#считывание значений 
                            stolb+=1
                        for i in up:
                            if i.isdigit():
                             
                                upp.append(int(i))
                            else:
                                upp.append(i)
                    
                    
                        if type(upp[0])==int and type(upp[1])==str and type(upp[2])==int and type(upp[3])==int:
                            up=tuple(up)
                            number=int( self.dialogautoo.spinBox.text())
                            idd = self.ui.tableWidget_2.item(number- 1, 0).text()
                            
                            s.sendall(bytes(f'UPDATE Автомашины SET КодМашины = {up[0]}, МаркаМашины = "{up[1]}", ЧислоМест = {up[2]}, РасходТоплива = {up[3]} WHERE КодМашины= {idd}','utf-8') )
                        else:
                            QMessageBox.critical(self,"Ошибка ","Запись некорректна")
                    if self.nTub==2:
                        for i in range(self.colum):#по количеству столбцов в таблице
                            up.append(self.dialogmarshrutt.tableWidget_2.item(0,stolb).text())#считывание значений 
                            stolb+=1
                        for i in up:
                            if i.isdigit():
                                
                                upp.append(int(i))
                            else:
                                upp.append(i)
                        
                        if type(upp[0])==int and type(upp[1])==str and type(upp[2])==str and type(upp[3])==int:
                            up=tuple(up)
                            number=int(self.dialogmarshrutt.spinBox_2.text())
                            idd = self.ui.tableWidget_3.item(number- 1, 0).text()
                            s.sendall(bytes(f'UPDATE Маршрут SET КодМаршрута = {up[0]}, ПунктОтправления = "{up[1]}", ПунктНазначения = "{up[2]}", Расстояние = {up[3]} WHERE КодМаршрута= {idd}' ,'utf-8') )
                        else:
                            QMessageBox.critical(self,"Ошибка ","Запись некорректна")
                    if self.nTub==3:
                        stolb=4
                        for i in range(1):
                            up.append(self.dialogflightt.tableWidget_4.item(0,0).text())
                        
                        
                        up.insert(1,self.combobox1.currentText())
                        up.insert(2,self.combobox2.currentText())
                        up.insert(3,self.combobox3.currentText())    

                        for i in range(4):
                            up.append(self.dialogflightt.tableWidget_4.item(0,stolb).text())
                            stolb+=1
                        for i in up:
                            if i.isdigit():
                
                                upp.append(int(i))
                            else:
                                upp.append(i)
                    
                   
                        try:
                            valid_date = time.strptime(upp[6], '%m-%d-%Y')
                            valid_date1 = time.strptime(upp[5], '%H:%M')
                            valid_date2 = time.strptime(upp[4], '%H:%M')
                          
                            cr=1
                            
                        except ValueError:
                            cr=0
                    
                        if type(upp[0])==int and cr==1 and type(upp[7])==int:
                            up=tuple(up)
                            
                            number=int(self.dialogflightt.spinBox.text())
                            idd = self.ui.tableWidget_4.item(number- 1, 0).text()
                           
                            d=f'UPDATE Рейс SET НомерРейса = {up[0]}, КодМаршрута = {up[1]}, ТабельныйНомерВодителя = {up[2]},КодМашины   = {up[3]},ВремяОтправления= "{up[4]}",ВремяПрибытия = "{up[5]}",Дата = "{up[6]}",ЦенаБилета = {up[7]} WHERE НомерРейса= {idd}'
                           
                            s.sendall(bytes(f'UPDATE Рейс SET НомерРейса = {up[0]}, КодМаршрута = {up[1]}, ТабельныйНомерВодителя = {up[2]},КодМашины   = {up[3]},ВремяОтправления= "{up[4]}",ВремяПрибытия = "{up[5]}",Дата = "{up[6]}",ЦенаБилета = {up[7]} WHERE НомерРейса= {idd}','utf-8') )
                        else:
                            QMessageBox.critical(self,"Ошибка ","Запись некорректна")
                            
                    s.close()
                    x=0
                    y=0
                    self.kk=1
                    self.output(x,y)
            except:
                QMessageBox.critical(self,"Ошибка ","Запись некорректна") 
    def delete(self):
        try:
            txt,oks=QtWidgets.QInputDialog.getText(self,'Удалить','Введите номер строки')
            if oks:
                 with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect((HOST, PORT))
                    
                    if self.nTub==0:
                        s.sendall(bytes(f'DELETE FROM Водитель WHERE ТабельныйНомерВодителя={self.ui.tableWidget_1.item(int(txt)-1, 0).text()}','utf-8'))
                       
                    if self.nTub==1:
                         s.sendall(bytes(f'DELETE FROM Автомашины WHERE КодМашины={self.ui.tableWidget_2.item(int(txt)-1, 0).text()}','utf-8'))
                        
                    if self.nTub==2:
                        s.sendall(bytes(f'DELETE FROM Маршрут WHERE КодМаршрута={self.ui.tableWidget_3.item(int(txt)-1, 0).text()}','utf-8'))
                        
                    if self.nTub==3:
                        s.sendall(bytes(f'DELETE FROM Рейс WHERE НомерРейса={self.ui.tableWidget_4.item(int(txt)-1, 0).text()}','utf-8'))
                        
        except:
            QMessageBox.critical(self,"Ошибка ","Запись не найдена")
            
    def output(self,x,y):#вывод данных
   
        self.nTub= self.ui.tabWidget.currentIndex()
        self.yy=y
            
        if x==1:#удаление
            self.delete()
            self.kk=1
        if x==2:#добавление/изменение
                
            self.dialogvoditel()
                
        
        if self.kk!=0:
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect((HOST, PORT))
                    
                    if self.nTub ==0:
                     
                        msg='SELECT * FROM Водитель'
                        s.sendall(bytes(msg,'utf-8'))
                        
                               
                    if self.nTub==1:
                        s.sendall(bytes('SELECT * FROM Автомашины', 'utf-8'))
                              
                    if self.nTub==2:
                        s.sendall(bytes('SELECT * FROM Маршрут', 'utf-8'))
                                
                    if self.nTub==3:
                        s.sendall(bytes('SELECT * FROM Рейс', 'utf-8'))
                     
                    
                    k = s.recv(18384).decode(encoding='utf-8')
                             
                    k = eval(k)
                               
                    s.close()
                    self.colum=len(k[0])#количество столбцов
                    yyy = eval('self.ui.tableWidget_' + str(int(self.nTub)+1))
                    self.sav=eval('self.ui.tableWidget_' + str(int(self.nTub)+1))#для сохранения
                    self.insTb(k,yyy)
                           
                    self.kk=1
            except:
                QMessageBox.critical(self,"Ошибка ","Сервер не запущен")
         
        
    def insTb(self,k,tbl):
        
        tbl.setRowCount(len(k))
        tbl.setColumnCount(len(k[0]))
        print(len(k[0]))
        for j in range(len(k)):
            for i in range(len(k[0])):
                inf=QWT(str(k[j][i]))
                inf.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                tbl.setItem(j, i, inf)    
        if  self.ui.tabWidget.currentIndex()==4:
            
            currtext = self.ui.listWidget.currentRow()
            if currtext==0:
                 self.ui.tableWidget.setHorizontalHeaderLabels(('КодМашины','МаркаМашины','ЧислоМест','РасходТоплива'))
            elif currtext==1 or currtext==4 or currtext==5 or currtext==10:
                self.ui.tableWidget.setHorizontalHeaderLabels(('НомерВодителя','ФИО','ДатаРождения','СтажРаботы'))
            elif currtext==2 or currtext==9 or currtext==13:       
                self.ui.tableWidget.setHorizontalHeaderLabels(('НомерРейса','КодМаршрута','НомерВодителя','КодМашины','ВремяОтправления','ВремяПрибытия','Дата','ЦенаБилета'))
            elif currtext==6 or currtext==12:
                self.ui.tableWidget.setHorizontalHeaderLabels(('КодМаршрута','ПунктОтправления','ПунктНазначения','Расстояние'))
            elif currtext==3:
                
                self.ui.tableWidget.setHorizontalHeaderLabels(('НомерРейса','','',''))
            elif currtext==7 or currtext==11:
                self.ui.tableWidget.setHorizontalHeaderLabels(('КодМашины','МаркаМашины','ЧислоМест','РасходТоплива','Дата'))
            elif currtext==8:
             
                self.ui.tableWidget.setHorizontalHeaderLabels(('Количество','','',''))
                
            
        
        self.combobox1=QtWidgets.QComboBox()
        self.combobox2=QtWidgets.QComboBox()
        self.combobox3=QtWidgets.QComboBox()
        
        for i in range (self.ui.tableWidget_3.rowCount()):
            idi=self.ui.tableWidget_3.item(i,0).text()
            self.combobox1.addItem(idi)
        for i in range (self.ui.tableWidget_1.rowCount()):
            idi=self.ui.tableWidget_1.item(i,0).text()
            self.combobox2.addItem(idi)
        for i in range (self.ui.tableWidget_2.rowCount()):
            idi=self.ui.tableWidget_2.item(i,0).text()
            self.combobox3.addItem(idi)
        
        self.dialogflightt.tableWidget_4.setCellWidget(0,1,self.combobox1)
        self.dialogflightt.tableWidget_4.setCellWidget(0,2,self.combobox2)
        self.dialogflightt.tableWidget_4.setCellWidget(0,3,self.combobox3)
if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
   

    
