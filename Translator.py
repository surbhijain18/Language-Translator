# -*- coding: utf-8 -*-


#!/usr/bin/env python
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication, QWidget, QToolTip, QPushButton, QMessageBox)
from PyQt5.QtCore import QUrl
import webbrowser
import http.client, urllib.parse
from PyQt5.QtGui import QDesktopServices

class Ui_HCI(object):
    def setupUi(self, HCI):
        HCI.setObjectName("HCI")
        HCI.resize(1187, 837)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        HCI.setFont(font)
        self.centralwidget = QtWidgets.QWidget(HCI)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(30, 230, 411, 381))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        data = self.textEdit.toPlainText()
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setReadOnly(True)
        self.textEdit_2.setGeometry(QtCore.QRect(740, 230, 411, 381))
        self.textEdit_2.setObjectName("textEdit_2")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(20, 760, 225, 48))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.commandLinkButton_2 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_2.setGeometry(QtCore.QRect(930, 750, 225, 48))
        self.commandLinkButton_2.setObjectName("commandLinkButton_2")
        self.commandLinkButton_3 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_3.setGeometry(QtCore.QRect(510, 380, 151, 48))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.commandLinkButton_3.setFont(font)
        self.commandLinkButton_3.setObjectName("commandLinkButton_3")
        '''self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(30, 140, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")'''
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(740, 140, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setObjectName("comboBox_3")
        languages = ['Afrikaans','Arabic','Bangla','Bosnian','Bulgarian','Cantonese', 'Catalan', 'Chinese Simplified', 'Chinese Traditional','Croatian', 'Czech','Danish','Dutch','English','Estonian','Fijian','Filipino','Finnish','French','German','Greek',
        'Haitian Creole','Hebrew','Hindi','Hmong Daw','Hungarian','Indonesian','Italian','Japanese','Kiswahili','Klingon','Klingon (plqaD)','Korean','Latvian','Lithuanian','Malagasy'
        ,'Malay','Maltese','Norwegian','Persian','Polish','Portuguese','Queretaro Otomi','Romanian','Russian','Samoan','Serbian (Cyrillic)','Serbian (Latin)','Slovak','Slovenian','Spanish'
        ,'Swedish','Tahitian','Tamil','Thai','Tongan','Turkish','Ukrainian','Urdu','Vietnamese','Welsh','Yucatec Maya']
        self.comboBox_3.addItems(languages)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(460, 10, 291, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        HCI.setCentralWidget(self.centralwidget)

        self.retranslateUi(HCI,data)
        QtCore.QMetaObject.connectSlotsByName(HCI)

    def printfunc(self ):
        subscriptionKey = 'SUBSCRIPTION KEY'

        host = 'api.microsofttranslator.com'
        path = '/V2/Http.svc/Translate'

        test = str(self.comboBox_3.currentText())

        target = self.languagesel(test)
        if (target == 'error'):
    
            target = self.languagesel(test)
        else:
            text = self.textEdit.toPlainText()
            params = '?to=' + target + '&text=' + urllib.parse.quote(text)
            headers = {'Ocp-Apim-Subscription-Key': subscriptionKey}
            conn = http.client.HTTPSConnection(host)
            conn.request ("GET", path + params, None, headers)
            response = conn.getresponse ()
            result = response.read()
            result = result [68 : len(result)-9]
            self.textEdit_2.setText(result.decode("utf-8"))

    def retranslateUi(self, HCI,data):
        _translate = QtCore.QCoreApplication.translate
        HCI.setWindowTitle(_translate("HCI", "HCI"))
        self.commandLinkButton.setText(_translate("HCI", "Report Error"))
        self.commandLinkButton.clicked.connect(lambda: webbrowser.open('https://ufl.qualtrics.com/jfe/form/SV_eONVoLWuM7cjqNn'))
        self.commandLinkButton_2.setText(_translate("HCI", "Complete Interaction"))
        self.commandLinkButton_2.clicked.connect(lambda: webbrowser.open('https://ufl.qualtrics.com/jfe/form/SV_9uY6i1QKmNNw5O5'))
        self.commandLinkButton_3.setText(_translate("HCI", "TRANSLATE"))
        self.commandLinkButton_3.clicked.connect(self.printfunc)
        self.comboBox_3.setItemText(0, _translate("HCI", "Translate to"))

        self.label.setText(_translate("HCI", "TRANSLATOR"))

    def languagesel(self, lang):

        if lang == 'Afrikaans':
            return 'af'
        elif lang == 'Arabic':
            return 'ar'
        elif lang == 'Bangla':
            return 'bn'
        elif lang == 'Bosnian':
            return 'bs'
        elif lang == 'Bulgarian':
            return 'bg'
        elif lang == 'Cantonese':
            return 'yue'
        elif lang == 'Catalan':
            return 'ca'
        elif lang == 'Chinese Traditional':
            return 'zh-Hant'
        elif lang == 'Chinese Simplified':
            return 'zh-Hans'
        elif lang == 'Croatian':
            return 'hr'
        elif lang == 'Czech':
            return 'cs'
        elif lang == 'Danish':
            return 'da'
        elif lang == 'Dutch':
            return 'nl'
        elif lang == 'English':
            return 'en'
        elif lang == 'Estonian':
            return 'et'
        elif lang == 'Fijian':
            return 'fj'
        elif lang == 'Filipino':
            return 'fil'
        elif lang == 'Finnish':
            return 'fi'
        elif lang == 'French':
            return 'fr'
        elif lang == 'German':
            return 'de'
        elif lang == 'Greek':
            return 'el'
        elif lang == 'Haitian Creole':
            return 'ht'
        elif lang == 'Hebrew':
            return 'he'
        elif lang == 'Hindi':
            return 'hi'
        elif lang == 'Hmong Daw':
            return 'mww'
        elif lang == 'Hungarian':
            return 'hu'
        elif lang == 'Indonesian':
            return 'id'
        elif lang == 'Italian':
            return 'it'
        elif lang == 'Japanese':
            return 'ja'
        elif lang == 'Kiswahili':
            return 'sw'
        elif lang == 'Klingon (plqaD)':
            return 'tlh-Qaak'
        elif lang == 'Klingon':
            return 'tlh'
        elif lang == 'Korean':
            return 'ko'
        elif lang == 'Latvian':
            return 'lv'
        elif lang == 'Lithuanian':
            return 'lt'
        elif lang == 'Malagasy':
            return 'mg'
        elif lang == 'Malay':
            return 'ms'
        elif lang == 'Maltese':
            return 'mt'
        elif lang == 'Norwegian':
            return 'nb'
        elif lang == 'Persian':
            return 'fa'
        elif lang == 'Polish':
            return 'pl'
        elif lang == 'Portuguese':
            return 'pt'
        elif lang == 'Queretaro Otomi':
            return 'otq'
        elif lang == 'Romanian':
            return 'ro'
        elif lang == 'Russian':
            return 'ru'
        elif lang == 'Samoan':
            return 'sm'
        elif lang == 'Serbian (Cyrillic)':
            return 'sr-Cyrl'
        elif lang == 'Serbian (Latin)':
            return 'sr-Latn'
        elif lang == 'Slovak':
            return 'sk'
        elif lang == 'Slovenian':
            return 'sl'
        elif lang == 'Spanish':
            return 'es'
        elif lang == 'Swedish':
            return 'sv'
        elif lang == 'Tahitian':
            return 'ty'
        elif lang == 'Tamil':
            return 'ta'
        elif lang == 'Thai':
            return 'th'
        elif lang == 'Tongan':
            return 'to'
        elif lang == 'Turkish':
            return 'tr'
        elif lang == 'Ukrainian':
            return 'uk'
        elif lang == 'Urdu':
            return 'ur'
        elif lang == 'Vietnamese':
            return 'vi'
        elif lang == 'Welsh':
            return 'cy'
        elif lang == 'Yucatec Maya':
            return 'yua'
        elif lang == 'Translate to':
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Please select a language to proceed with translation!")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.setEscapeButton(QMessageBox.Close)
            msg.exec_()
            return 'error'



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HCI = QtWidgets.QMainWindow()
    ui = Ui_HCI()
    ui.setupUi(HCI)
    HCI.show()
    sys.exit(app.exec_())
