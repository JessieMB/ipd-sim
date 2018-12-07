# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'faq.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(978, 676)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        Dialog.setPalette(palette)
        self.label_32 = QtWidgets.QLabel(Dialog)
        self.label_32.setGeometry(QtCore.QRect(20, 10, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.line_9 = QtWidgets.QFrame(Dialog)
        self.line_9.setGeometry(QtCore.QRect(340, 690, 251, 20))
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.label_40 = QtWidgets.QLabel(Dialog)
        self.label_40.setGeometry(QtCore.QRect(340, 670, 261, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_40.setFont(font)
        self.label_40.setObjectName("label_40")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(20, 50, 281, 121))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_2.setGeometry(QtCore.QRect(20, 210, 281, 121))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label_33 = QtWidgets.QLabel(Dialog)
        self.label_33.setGeometry(QtCore.QRect(20, 170, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_33.setFont(font)
        self.label_33.setObjectName("label_33")
        self.textBrowser_3 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_3.setGeometry(QtCore.QRect(20, 370, 281, 121))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.label_34 = QtWidgets.QLabel(Dialog)
        self.label_34.setGeometry(QtCore.QRect(20, 330, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.label_34.setFont(font)
        self.label_34.setObjectName("label_34")
        self.textBrowser_4 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_4.setGeometry(QtCore.QRect(320, 50, 281, 121))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.label_35 = QtWidgets.QLabel(Dialog)
        self.label_35.setGeometry(QtCore.QRect(320, 10, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_35.setFont(font)
        self.label_35.setObjectName("label_35")
        self.textBrowser_5 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_5.setGeometry(QtCore.QRect(620, 50, 281, 121))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.textBrowser_5.setFont(font)
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.label_36 = QtWidgets.QLabel(Dialog)
        self.label_36.setGeometry(QtCore.QRect(620, 10, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_36.setFont(font)
        self.label_36.setObjectName("label_36")
        self.textBrowser_6 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_6.setGeometry(QtCore.QRect(20, 530, 281, 101))
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.label_37 = QtWidgets.QLabel(Dialog)
        self.label_37.setGeometry(QtCore.QRect(20, 490, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_37.setFont(font)
        self.label_37.setObjectName("label_37")
        self.textBrowser_7 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_7.setGeometry(QtCore.QRect(320, 220, 281, 121))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.textBrowser_7.setFont(font)
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.label_38 = QtWidgets.QLabel(Dialog)
        self.label_38.setGeometry(QtCore.QRect(320, 180, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_38.setFont(font)
        self.label_38.setObjectName("label_38")
        self.textBrowser_8 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_8.setGeometry(QtCore.QRect(620, 220, 281, 121))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.textBrowser_8.setFont(font)
        self.textBrowser_8.setObjectName("textBrowser_8")
        self.label_41 = QtWidgets.QLabel(Dialog)
        self.label_41.setGeometry(QtCore.QRect(620, 180, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_41.setFont(font)
        self.label_41.setObjectName("label_41")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(740, 410, 156, 23))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_32.setText(_translate("Dialog", "What is the Prisoner\'s Dilemma?"))
        self.label_40.setText(_translate("Dialog", "correctly."))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; color:#111111; background-color:#ffffff;\">The prisoner’s dilemma, one of the most famous game theories,</span><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; color:#111111;\"> basically provides a framework for understanding how to strike a balance between cooperation and competition, and is a very useful tool for strategic decision-making. </span><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; color:#111111; background-color:#ffffff;\">As a result, it finds application in diverse areas ranging from business, finance, economics and political science to philosophy, psychology, biology and sociology.</span></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; color:#111111; background-color:#ffffff;\">Two suspects have been apprehended for a crime and are now in separate rooms in a police station, with no means of communicating with each other. The prosecutor has separately told them the following:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; color:#111111;\">If you confess and agree to testify against the other suspect, who does not confess, the charges against you will be dropped and you will get off for free.If you do not confess but the other suspect does, you will be convicted and the prosecution will seek the maximum sentence of three years.If both of you confess, you will both be sentenced to two years in prison.If neither of you confess, you will both be charged with misdemeanors and will be sentenced to one year in prison.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; color:#111111; background-color:#ffffff;\">What should the suspects do? This is the essence of the prisoner’s dilemma.</span></p></body></html>"))
        self.label_33.setText(_translate("Dialog", "How does it work?"))
        self.textBrowser_3.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; color:#111111; background-color:#ffffff;\">Let’s begin by constructing a payoff matrix as shown in the table below. The “payoff” here is shown in terms of the length of a prison sentence (as symbolized by the negative sign; the higher the number the better). The terms “cooperate” and “defect” refer to the suspects cooperating with each other (as for example, if neither of them confesses) or defecting (i.e. not cooperating with the other player, which is the case where one suspect confesses, but the other does not). The first numeral in cells (a) through (d) shows the payoff for Suspect A, while the second numeral shows it for Suspect B.</span></p></body></html>"))
        self.label_34.setText(_translate("Dialog", "What\'s the smartest way to play?"))
        self.textBrowser_4.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; color:#111111; background-color:#ffffff;\">A classic example of prisoner’s dilemma in the real world is encountered when two competitors are battling it out in the marketplace. Many sectors of the economy have two main rivals. In the U.S., for example, the fierce rivalry between Coca-Cola </span><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; color:#111111;\">and PepsiCo in soft drinks, and Home Depot versus Lowe\'s in building supplies, has given rise to numerous case studies in business schools. Other fierce rivalries include Starbucks versus Tim Horton’s in Canada, and Apple versus Samsung in the global mobile phone sector.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; color:#111111; background-color:#ffffff;\">Consider the case of Coca-Cola versus PepsiCo, and assume the former is thinking of cutting the price of its iconic soda. If it does so, Pepsi may have no choice but to follow suit for its cola to retain its market share</span><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; color:#111111;\">. This may result in a significant drop in profits for both companies. A price drop by either company may therefore be construed as defecting, since it breaks an implicit agreement to keep prices high and maximize profits. Thus, if Coca-Cola drops its price but Pepsi continues to keep prices high, the former is defecting while the latter is cooperating (by sticking to the spirit of the implicit agreement). In this scenario, Coca-Cola may win market share and earn incremental profits by selling more colas.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; font-weight:600; color:#362f2d; background-color:#ffffff;\">Payoff Matrix</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; color:#111111; background-color:#ffffff;\">Let’s assume that the incremental profits that accrue to Coca-Cola and Pepsi are as follows: </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; color:#111111; background-color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; color:#111111;\">If both keep prices high, profits for each company increase by $500 million (because of normal growth in demand). If one drops prices (i.e. defects) but the other does not (cooperates), profits increase by $750 million for the former because of greater market share, and are unchanged for the latter.If both companies reduce prices, the increase in soft drink consumption offsets the lower price, and profits for each company increase by $250 million.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; color:#111111; background-color:#ffffff;\">The payoff matrix looks like this (the numbers represent incremental dollar profits in hundreds of millions):</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; color:#111111; background-color:#ffffff;\"><br /></p>\n"
"<table border=\"1\" style=\" margin-top:0px; margin-bottom:30px; margin-left:0px; margin-right:0px;\" cellspacing=\"0\" cellpadding=\"0\" bgcolor=\"#ffffff\">\n"
"<tr>\n"
"<td colspan=\"2\" rowspan=\"2\">\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; font-weight:600; color:#111111;\">Coca-Cola vs. PepsiCo –</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; font-weight:600; color:#111111;\">Payoff Matrix</span></p></td>\n"
"<td colspan=\"2\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; font-weight:600; color:#111111;\">PepsiCo</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; font-weight:600; color:#111111;\">Cooperate</span></p></td>\n"
"<td>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; font-weight:600; color:#111111;\">Defect</span></p></td></tr>\n"
"<tr>\n"
"<td rowspan=\"2\">\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; font-weight:600; color:#111111;\">Coca-Cola</span></p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; font-weight:600; color:#111111;\">Cooperate</span></p></td>\n"
"<td>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; color:#111111;\">500, 500</span></p></td>\n"
"<td>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; color:#111111;\">0, 750</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; font-weight:600; color:#111111;\">Defect</span></p></td>\n"
"<td>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; color:#111111;\">750, 0</span></p></td>\n"
"<td>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; color:#111111;\">250, 250</span></p></td></tr></table>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; color:#111111; background-color:#ffffff;\">Other oft-cited prisoner’s dilemma examples are in areas such as new product/technology development or advertising and marketing expenditures by companies.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; color:#111111; background-color:#ffffff;\">For example, if two firms have an implicit agreement to leave advertising budgets unchanged in a given year, their</span><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; color:#111111;\"> net income may stay at relatively high levels. But if one defects and raises its advertising budget, it may earn greater profits at the expense of the other company, as higher sales offset the increased advertising expenses. However, if both companies boost their advertising budgets, the increased advertising efforts may offset each other and prove ineffective, resulting in lower profits (due to the higher ad expenses) than would have been the case if the ad budgets were left unchanged.</span></p>\n"
"<p style=\" margin-top:3px; margin-bottom:3px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; font-weight:600; color:#362f2d; background-color:#ffffff;\">Applications to the Economy</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; color:#111111; background-color:#ffffff;\">The U.S. debt deadlock between the Democrats and Republicans that springs up from time to time is a classic example of a prisoner’s dilemma.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; color:#111111; background-color:#ffffff;\">Let’s say the utility or benefit of resolving the U.S. debt issue would be electoral gains for the parties in the next election. Cooperation in this instance refers to the willingness of both parties to work to maintain the status quo with regard to the spiraling US budget deficit.</span><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; color:#111111;\"> Defecting implies backing away from this implicit agreement and taking the steps required to bring the deficit under control.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; color:#111111; background-color:#ffffff;\">If both parties cooperate and keep the economy running smoothly, some electoral gains are assured. But if Party A tries to resolve the debt issue in a proactive manner, while Party B does not cooperate, this recalcitrance may cost B votes in the next election, which may go to A. However, if both parties back away from cooperation and play hardball in an attempt to resolve the debt issue, the consequent economic turmoil (sliding markets, a possible credit downgrade, government shutdown</span><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; color:#111111;\">, etc.) may result in lower electoral gains for both parties.</span></p>\n"
"<p style=\" margin-top:3px; margin-bottom:3px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; font-weight:600; color:#362f2d; background-color:#ffffff;\">How Can You Use It?</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; color:#111111; background-color:#ffffff;\">The prisoner’s dilemma can be used to aid decision-making in a number of areas in one’s personal life, such as buying a car, salary negotiations and so on.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; color:#111111; background-color:#ffffff;\">For example, assume you are</span><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; color:#111111;\"> in the market for a new car, and you walk into a car dealership. The utility or payoff in this case is a non-numerical attribute, i.e. satisfaction with the deal. You want to get the best possible deal in terms of price, car features, etc. while the car salesman wants to get the highest possible price to maximize his commission.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; color:#111111; background-color:#ffffff;\">Cooperation in this context means no haggling; you walk in, pay the sticker price (much to the salesman’s delight) and leave with a new car. On the other hand, defecting means bargaining; you want a lower price, while the salesman wants a higher price. Assigning numerical values to the levels of satisfaction, where 10 means fully satisfied with the deal and 0 implies no satisfaction, the payoff matrix is as shown below:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; color:#111111; background-color:#ffffff;\"><br /></p>\n"
"<table border=\"1\" style=\" margin-top:0px; margin-bottom:30px; margin-left:0px; margin-right:0px;\" cellspacing=\"0\" cellpadding=\"0\" bgcolor=\"#ffffff\">\n"
"<tr>\n"
"<td colspan=\"2\" rowspan=\"2\">\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; font-weight:600; color:#111111;\">Car Buyer  vs. Salesman –</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; font-weight:600; color:#111111;\">Payoff Matrix</span></p></td>\n"
"<td colspan=\"2\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; font-weight:600; color:#111111;\">Salesman</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; font-weight:600; color:#111111;\">Cooperate</span></p></td>\n"
"<td>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; font-weight:600; color:#111111;\">Defect</span></p></td></tr>\n"
"<tr>\n"
"<td rowspan=\"2\">\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; font-weight:600; color:#111111;\">Buyer</span></p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; font-weight:600; color:#111111;\">Cooperate</span></p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; color:#111111;\">(a) 7, 7</span></p></td>\n"
"<td>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; color:#111111;\">(c) 0,10</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; font-weight:600; color:#111111;\">Defect</span></p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; color:#111111;\">(b) 10, 0</span></p></td>\n"
"<td>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; color:#111111;\">(d) 3, 3</span></p></td></tr></table>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; color:#111111; background-color:#ffffff;\">What does this matrix tell us? If you</span><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; color:#111111;\"> drive a hard bargain and get a substantial reduction in the car price, you are likely to be fully satisfied with the deal, but the salesman is likely to be unsatisfied because of the loss of commission (as can be seen in cell b). Conversely, if the salesman sticks to his guns and does not budge on price, you are likely to be unsatisfied with the deal while the salesman would be fully satisfied (cell c).</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; color:#111111; background-color:#ffffff;\">Your satisfaction level may be less if you simply walked in and paid full sticker price (cell a). The salesman in this situation is also likely to be less than fully satisfied, since your willingness to pay full price may leave him wondering if he could have “steered” you to a more expensive model, or added some more bells and whistles to gain more</span><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; color:#111111;\"> commission.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; color:#111111; background-color:#ffffff;\">Cell (d) shows a much lower degree of satisfaction for both buyer and seller, since prolonged haggling may have eventually led to a reluctant compromise on the price paid for the car.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; color:#111111; background-color:#ffffff;\">Likewise, with salary negotiations</span><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; color:#111111;\">, you may be ill-advised to take the first offer that a potential employer makes to you (assuming you know that you’re worth more).</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; color:#111111; background-color:#ffffff;\">Cooperating by taking the first offer may seem like an easy solution in a difficult</span><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; color:#111111;\"> job market, but it may result in you leaving some money on the table. Defecting (i.e. negotiating) for a higher salary may indeed fetch you a fatter pay package; conversely, if the employer is not willing to pay more, you may be dissatisfied with the final offer.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; color:#111111; background-color:#ffffff;\">Hopefully, the salary negotiations do not turn acrimonious, since that may result in a lower level of satisfaction for you and the employer. The buyer-salesman payoff matrix shown earlier can be easily extended to show the satisfaction level for the job seeker versus employer.</span></p>\n"
"<p style=\" margin-top:3px; margin-bottom:3px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; font-weight:600; color:#362f2d; background-color:#ffffff;\">The Bottom Line</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; color:#111111; background-color:#ffffff;\">The prisoner’s dilemma shows us that mere cooperation is not always in one’s best interests. In fact, when shopping for a big-ticket item such as a car, bargaining is the preferred course of action from the consumers\' point of view. Otherwise, the car dealership may adopt a policy of inflexibility in price negotiations, maximizing its profits but resulting in consumers overpaying for their vehicles.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; color:#111111; background-color:#ffffff;\">Understanding the relative payoffs of cooperating versus defecting may stimulate you to engage in significant price negotiations before you make a big purchase.</span></p></body></html>"))
        self.label_35.setText(_translate("Dialog", "What \"real world\" applications?"))
        self.textBrowser_5.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; color:#111111; background-color:#ffffff;\">The iterated prisoner\'s dilemma is an extension of the general form except the game is repeatedly played by the same participants. An iterated prisoner\'s dilemma differs from the original concept of a prisoner\'s dilemma because participants can learn about the behavioral tendencies of their counterparty.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; color:#111111;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; color:#111111; background-color:#ffffff;\">Since the game is repeated, one individual can formulate a strategy that does not follow the regular logical convention of an isolated round.The iterated prisoner\'s dilemma game is fundamental to many theories of human cooperation and trust. Based on the assumption that the game can model transactions between two people requiring trust, cooperative behavior in populations may be modeled by a multi-player, iterated, version of the game.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; color:#111111; background-color:#ffffff;\">The theory behind the game has captivated many scholars over the years. More recently, organizational design researchers have used the game to model corporate strategies. The prisoner\'s dilemma is also now commonplace for game theories becoming popular with investment strategist. Globalization</span><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; color:#111111;\"> and integrated trade have further driven demand for financial and operational models that can describe geopolitical issues.</span></p>\n"
"<p style=\" margin-top:3px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; font-weight:600; color:#362f2d; background-color:#ffffff;\">Example of the Iterated Prisoner\'s Dilemma Game</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:3px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; font-weight:600; color:#362f2d; background-color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; color:#111111; background-color:#ffffff;\">For example, you and a colleague, are in jail and suspected of committing a crime. You are isolated from each other and do not know how the other will respond to questioning. The police invite both of you to implicate the other in the crime (defect). What happens depends on what both of you do, but neither of you know how the other will respond. If your colleague betrays you (yields to the temptation to defect) while you remain silent, then you receive the longest jail term while your colleague gets off free (and visa versa). If you both choose to cooperate with each other (not the police) by remaining silent, there is insufficient evidence to convict both of you, so you are both given a light sentence for a lesser crime. If both of you decide to defect, then you have condemned each other to slightly reduced but still heavy sentences.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; color:#111111; background-color:#ffffff;\">The payoff in this game is a reduction in prison sentencing of very good, fairly good, fairly bad or very bad, which is translated into a point score system as follows:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; color:#111111; background-color:#ffffff;\"><br /></p>\n"
"<table border=\"1\" style=\" margin-top:0px; margin-bottom:30px; margin-left:0px; margin-right:0px;\" cellspacing=\"1\" cellpadding=\"1\" bgcolor=\"#ffffff\">\n"
"<tr>\n"
"<td colspan=\"2\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; font-weight:600; color:#111111;\"> </span></p></td>\n"
"<td colspan=\"2\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; font-weight:600; color:#111111;\">What your colleague does</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"2\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; font-style:italic; color:#111111;\">This table shows payoffs to you for various outcomes.</span></p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; color:#111111;\">Co-operate</span></p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; color:#111111;\">Defect</span></p></td></tr>\n"
"<tr>\n"
"<td rowspan=\"2\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; color:#111111;\">What you do</span></p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; color:#111111;\">Co-operate</span></p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; color:#111111;\">Fairly good.<br />REWARD<br />for mutual co-operation.<br />3 points</span></p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; color:#111111;\">Very bad.<br />SUCKER\'S PAYOFF.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; color:#111111;\">0 points</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; color:#111111;\">Defect</span></p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; color:#111111;\">Very good.<br />TEMPTATION<br />to defect.<br />5 points</span></p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Source Sans Pro,sans-serif\'; font-size:8pt; color:#111111;\">Fairly bad.<br />PUNISHMENT<br />for mutual defection.<br />1 point</span></p></td></tr></table>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">The game is played iteratively for a number of rounds until it is ended (as if you are repeatedly interrogated for separate crimes). The scores from each round are accumulated, so the object is to optimize the point score before reaching game over. Game over is determined randomly anywhere between 1 and 100 rounds. At the end of the game, the scores are translated into percentages of the best possible scores.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><br /></p></body></html>"))
        self.label_36.setText(_translate("Dialog", "What\'s an Iterated Prisoner\'s Dilemma?"))
        self.textBrowser_6.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-size:8pt; background-color:#ffffff;\">In both isolated matches as well as iterated prisoner\'s dilemma tournaments, the incentives and disincentives largely dictate the success of a given strategy. For example, you can change the parameters within the payoff matrix to turn the game into Chicken instead, where you and an opponent try to scare each other into swerving while driving headfirst into one another. If you don\'t swerve, you get to be the &quot;brave&quot; one and your opponent suffers embarrassment, but if neither of you swerve, you surely crash and risk fatal injury, resulting in a catastrophic loss for each player.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt; background-color:#ffffff;\"><br /></p>\n"
"<table border=\"1\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;\" cellspacing=\"0\" cellpadding=\"4\" bgcolor=\"#bacdd8\">\n"
"<tr>\n"
"<td>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-weight:600; color:#3a3a3a;\"><br /></span></p></td>\n"
"<td>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-weight:600; color:#3a3a3a;\">Swerve</span></p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-weight:600; color:#3a3a3a;\">Continue Straight</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-weight:600; color:#3a3a3a;\">Swerve</span></p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; color:#3a3a3a;\">0, 0</span></p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; color:#3a3a3a;\">-1, +1</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-weight:600; color:#3a3a3a;\">Continue Straight</span></p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; color:#3a3a3a;\">+1, -1</span></p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; color:#3a3a3a;\">-100, -100</span></p></td></tr></table>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-size:8pt; font-weight:600; background-color:#ffffff;\">For a game to be considered a &quot;Prisoner\'s Dilemma&quot;, the following metrics must be accounted for in the payoff matrix :</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-size:8pt; background-color:#ffffff;\">Temptation &gt; Reward &gt; Punishment &gt; Sucker</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:9px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'sans-serif\'; font-size:8pt; font-weight:600; color:#222222;\">Prisoner\'s dilemma payoff matrix</span></p>\n"
"<table border=\"0\" style=\" float: right; margin-top:0px; margin-bottom:9px; margin-left:9px; margin-right:0px;\" cellspacing=\"2\" cellpadding=\"0\" bgcolor=\"#f8f9fa\">\n"
"<tr>\n"
"<td style=\" padding-left:5; padding-right:5; padding-top:3; padding-bottom:3;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:26px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:1%;\"><span style=\" font-family:\'sans-serif\'; font-size:8pt; font-weight:600; color:#222222;\">B</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:26px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'sans-serif\'; font-size:8pt; font-weight:600; color:#222222;\">A</span></p></td>\n"
"<td bgcolor=\"#eaecf0\" style=\" padding-left:5; padding-right:5; padding-top:3; padding-bottom:3;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'sans-serif\'; font-size:8pt; font-weight:600; color:#222222; background-color:#eaecf0;\">B stays</span><span style=\" font-family:\'sans-serif\'; font-size:8pt; font-weight:600; color:#222222;\"><br />silent</span></p></td>\n"
"<td bgcolor=\"#eaecf0\" style=\" padding-left:5; padding-right:5; padding-top:3; padding-bottom:3;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'sans-serif\'; font-size:8pt; font-weight:600; color:#222222; background-color:#eaecf0;\">B</span><span style=\" font-family:\'sans-serif\'; font-size:8pt; font-weight:600; color:#222222;\"><br />betrays</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#eaecf0\" style=\" padding-left:5; padding-right:5; padding-top:3; padding-bottom:3;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'sans-serif\'; font-size:8pt; font-weight:600; color:#222222; background-color:#eaecf0;\">A stays</span><span style=\" font-family:\'sans-serif\'; font-size:8pt; font-weight:600; color:#222222;\"><br />silent</span></p></td>\n"
"<td style=\" padding-left:5; padding-right:5; padding-top:3; padding-bottom:3;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:26px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">T,T</span></p></td>\n"
"<td style=\" padding-left:5; padding-right:5; padding-top:3; padding-bottom:3;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:26px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:1%;\"><span style=\" font-family:\'sans-serif\'; font-size:8pt; color:#222222;\">T</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:26px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">S,</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#eaecf0\" style=\" padding-left:5; padding-right:5; padding-top:3; padding-bottom:3;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'sans-serif\'; font-size:8pt; font-weight:600; color:#222222; background-color:#eaecf0;\">A</span><span style=\" font-family:\'sans-serif\'; font-size:8pt; font-weight:600; color:#222222;\"><br />betrays</span></p></td>\n"
"<td style=\" padding-left:5; padding-right:5; padding-top:3; padding-bottom:3;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:26px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">T,S</span></p></td>\n"
"<td style=\" padding-left:5; padding-right:5; padding-top:3; padding-bottom:3;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:26px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:1%;\"><span style=\" font-size:8pt;\">P</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:26px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">P,</span></p></td></tr></table>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Here are other games you can play with this simulator by changing the parameters.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Planning an Outing</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'sans-serif\'; font-size:8pt; color:#222222; background-color:#ffffff;\">In this game the players want to cooperate with each other, but they disagree about the best outcome for the game.</span></p>\n"
"<p style=\" margin-top:9px; margin-bottom:9px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'sans-serif\'; font-size:8pt; color:#222222; background-color:#ffffff;\">Two friends want to meet but disagree on the venue. One prefers to watching boxing while the other prefers ballet. However, if they show up at different sites, they will be unhappy without the other. We can model this game as a two player strategic game:</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'sans-serif\'; font-size:8pt; font-weight:600; color:#222222;\"><br /></p>\n"
"<table border=\"0\" style=\" margin-top:17px; margin-bottom:17px; margin-left:0px; margin-right:0px;\" align=\"center\" cellspacing=\"2\" cellpadding=\"0\" bgcolor=\"#f8f9fa\">\n"
"<tr>\n"
"<td colspan=\"2\" rowspan=\"2\" bgcolor=\"#c8d1b1\" style=\" padding-left:5; padding-right:5; padding-top:3; padding-bottom:3;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'sans-serif\'; font-size:8pt; font-weight:600; color:#222222;\">Game</span></p></td>\n"
"<td colspan=\"2\" bgcolor=\"#fcf3d3\" style=\" padding-left:5; padding-right:5; padding-top:3; padding-bottom:3;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'sans-serif\'; font-size:8pt; color:#222222; background-color:#fcf3d3;\">Player 2</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#ebe294\" style=\" padding-left:5; padding-right:5; padding-top:3; padding-bottom:3;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'sans-serif\'; font-size:8pt; color:#222222; background-color:#ebe294;\">Boxing</span></p></td>\n"
"<td bgcolor=\"#ebe294\" style=\" padding-left:5; padding-right:5; padding-top:3; padding-bottom:3;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'sans-serif\'; font-size:8pt; color:#222222; background-color:#ebe294;\">Ballet</span></p></td></tr>\n"
"<tr>\n"
"<td rowspan=\"2\" bgcolor=\"#fcf3d3\" style=\" padding-left:5; padding-right:5; padding-top:3; padding-bottom:3;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'sans-serif\'; font-size:8pt; color:#222222; background-color:#fcf3d3;\">Player 1</span></p></td>\n"
"<td bgcolor=\"#ebe294\" style=\" padding-left:5; padding-right:5; padding-top:3; padding-bottom:3;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'sans-serif\'; font-size:8pt; color:#222222; background-color:#ebe294;\">Boxing</span></p></td>\n"
"<td style=\" padding-left:5; padding-right:5; padding-top:3; padding-bottom:3;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'sans-serif\'; font-size:8pt; color:#222222;\">(2,1)</span></p></td>\n"
"<td style=\" padding-left:5; padding-right:5; padding-top:3; padding-bottom:3;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'sans-serif\'; font-size:8pt; color:#222222;\">(0,0)</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#ebe294\" style=\" padding-left:5; padding-right:5; padding-top:3; padding-bottom:3;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'sans-serif\'; font-size:8pt; color:#222222; background-color:#ebe294;\">Ballet</span></p></td>\n"
"<td style=\" padding-left:5; padding-right:5; padding-top:3; padding-bottom:3;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'sans-serif\'; font-size:8pt; color:#222222;\">(0,0)</span></p></td>\n"
"<td style=\" padding-left:5; padding-right:5; padding-top:3; padding-bottom:3;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'sans-serif\'; font-size:8pt; color:#222222;\">(1,2)</span></p></td></tr></table>\n"
"<p style=\" margin-top:9px; margin-bottom:9px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'sans-serif\'; font-size:8pt; color:#222222; background-color:#ffffff;\">The table clearly shows that the best choice for the two friends is to both play the same game since neither of them will be happy without the other. The only question left is which game to play.</span></p>\n"
"<p style=\" margin-top:9px; margin-bottom:9px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'sans-serif\'; font-size:8pt; color:#222222; background-color:#ffffff;\">This game is also known as</span><span style=\" font-family:\'sans-serif\'; font-size:8pt; color:#222222;\"> </span><span style=\" font-family:\'sans-serif\'; font-size:8pt; font-style:italic; color:#222222;\">Bach or Stravinsky</span><span style=\" font-family:\'sans-serif\'; font-size:8pt; color:#222222;\">.</span></p>\n"
"<p style=\" margin-top:9px; margin-bottom:9px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-size:8pt; font-weight:600;\">Matching Pennies</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'sans-serif\'; font-size:8pt; color:#222222; background-color:#ffffff;\">In this game we imagine two players, each with a penny. They independently choose a side of the coin and then simultaneously show the other the chosen side. If the sides match, then Player 1 gains Player 2\'s penny. If the sides differ, Player 2 wins Player 1\'s penny.</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'sans-serif\'; font-size:8pt; font-weight:600; color:#222222;\"><br /></p>\n"
"<table border=\"0\" style=\" margin-top:17px; margin-bottom:17px; margin-left:0px; margin-right:0px;\" align=\"center\" cellspacing=\"2\" cellpadding=\"0\" bgcolor=\"#f8f9fa\">\n"
"<tr>\n"
"<td colspan=\"2\" rowspan=\"2\" bgcolor=\"#c8d1b1\" style=\" padding-left:5; padding-right:5; padding-top:3; padding-bottom:3;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'sans-serif\'; font-size:8pt; font-weight:600; color:#222222;\">Matching Pennies</span></p></td>\n"
"<td colspan=\"2\" bgcolor=\"#fcf3d3\" style=\" padding-left:5; padding-right:5; padding-top:3; padding-bottom:3;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'sans-serif\'; font-size:8pt; color:#222222; background-color:#fcf3d3;\">Player 2</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#ebe294\" style=\" padding-left:5; padding-right:5; padding-top:3; padding-bottom:3;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'sans-serif\'; font-size:8pt; color:#222222; background-color:#ebe294;\">Heads</span></p></td>\n"
"<td bgcolor=\"#ebe294\" style=\" padding-left:5; padding-right:5; padding-top:3; padding-bottom:3;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'sans-serif\'; font-size:8pt; color:#222222; background-color:#ebe294;\">Tails</span></p></td></tr>\n"
"<tr>\n"
"<td rowspan=\"2\" bgcolor=\"#fcf3d3\" style=\" padding-left:5; padding-right:5; padding-top:3; padding-bottom:3;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'sans-serif\'; font-size:8pt; color:#222222; background-color:#fcf3d3;\">Player 1</span></p></td>\n"
"<td bgcolor=\"#ebe294\" style=\" padding-left:5; padding-right:5; padding-top:3; padding-bottom:3;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'sans-serif\'; font-size:8pt; color:#222222; background-color:#ebe294;\">Heads</span></p></td>\n"
"<td style=\" padding-left:5; padding-right:5; padding-top:3; padding-bottom:3;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'sans-serif\'; font-size:8pt; color:#222222;\">1, -1</span></p></td>\n"
"<td style=\" padding-left:5; padding-right:5; padding-top:3; padding-bottom:3;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'sans-serif\'; font-size:8pt; color:#222222;\">-1, 1</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#ebe294\" style=\" padding-left:5; padding-right:5; padding-top:3; padding-bottom:3;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'sans-serif\'; font-size:8pt; color:#222222; background-color:#ebe294;\">Tails</span></p></td>\n"
"<td style=\" padding-left:5; padding-right:5; padding-top:3; padding-bottom:3;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'sans-serif\'; font-size:8pt; color:#222222;\">-1, 1</span></p></td>\n"
"<td style=\" padding-left:5; padding-right:5; padding-top:3; padding-bottom:3;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'sans-serif\'; font-size:8pt; color:#222222;\">1, -1</span></p></td></tr></table>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">You can invent your own games and use this program to test how different strategies hold up!</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\"><br /></span></p></body></html>"))
        self.label_37.setText(_translate("Dialog", "How do parameters alter outcomes?"))
        self.textBrowser_7.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-weight:600;\">Summary</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; background-color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-size:8pt;\">This program allows you to choose from 10 different prisoner\'s dilemma strategies whose details can be found by clicking the &quot;Strategy&quot; button on the main menu. You can specify how many players you would like to include in your simulation by inputting your desired amount as an integer next to the given strategy. The program offers three different modes, which can be activated as needed by clicking the checkbox next to their names, near the bottom right. On the other side, you can choose your output settings, with population maps, various graphs, and a CSV file as options. Simply check whatever you\'d like to receive to analyze the data.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt; background-color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-weight:600;\">Modes</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; background-color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-size:8pt;\">The three simulation modes in this program are Round Robin Tournaments, Moran Processes, and Ecological Sustainability Processes. Results vary based upon player numbers, strategies, parameters, noise, and random seeds.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt; background-color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-size:8pt;\">In Tournament mode, the total number of players are divided in two pairs until no more pairs exist, then each pair competes for the specified number of turns. As players are eliminated, one strategy will win over time.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt; background-color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-size:8pt;\">A Moran Process is a population process simulating natural selection. Given an initial population of players, the population is iterated in rounds consisting of matches played between each pair of players, with the cumulative total scores recorded. A player is chosen to reproduce proportional to the player’s score in the round and a lower-scoring player is chosen at random to be replaced. The process proceeds in rounds until the population consists of a single player type. That type is declared the winner.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt; background-color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-size:8pt;\">In an Ecological Sustainability Tournament, the participant populations are evolved over a given number of time steps. This is done by determining strategy &quot;fitness&quot; and multiplying succesful strategies according to the given payoff matrix while inferior strategies doie off.</span></p></body></html>"))
        self.label_38.setText(_translate("Dialog", "How do I use this program?"))
        self.textBrowser_8.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"http://axelrod.readthedocs.io\"><span style=\" text-decoration: underline; color:#0000ff;\">axelrod.readthedocs.io</span></a></p></body></html>"))
        self.label_41.setText(_translate("Dialog", "Where do I learn more about the IPD?"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

