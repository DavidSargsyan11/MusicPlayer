# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'beta_2.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(969, 557)
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/favicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QtCore.QSize(50, 50))
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 951, 441))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(16)
        self.tabWidget.setFont(font)
        self.tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tabWidget.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.tabWidget.setAcceptDrops(False)
        self.tabWidget.setWhatsThis("")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.dial = QtWidgets.QDial(self.tab_1)
        self.dial.setGeometry(QtCore.QRect(170, 430, 50, 64))
        self.dial.setObjectName("dial")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.tab_1)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(-1, 9, 951, 401))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label.setMaximumSize(QtCore.QSize(45, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setScaledContents(False)
        self.label.setWordWrap(False)
        self.label.setOpenExternalLinks(False)
        self.label.setTextInteractionFlags(QtCore.Qt.TextEditable)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 4, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(610, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 6, 1, 1)
        self.cmbSort = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbSort.sizePolicy().hasHeightForWidth())
        self.cmbSort.setSizePolicy(sizePolicy)
        self.cmbSort.setMaximumSize(QtCore.QSize(100, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cmbSort.setFont(font)
        self.cmbSort.setEditable(True)
        self.cmbSort.setCurrentText("")
        self.cmbSort.setDuplicatesEnabled(False)
        self.cmbSort.setFrame(True)
        self.cmbSort.setModelColumn(0)
        self.cmbSort.setObjectName("cmbSort")
        self.gridLayout.addWidget(self.cmbSort, 1, 5, 1, 1)
        self.btnImport = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btnImport.setMaximumSize(QtCore.QSize(100, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnImport.setFont(font)
        self.btnImport.setAutoDefault(False)
        self.btnImport.setDefault(False)
        self.btnImport.setFlat(False)
        self.btnImport.setObjectName("btnImport")
        self.gridLayout.addWidget(self.btnImport, 1, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(30, 10, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 3, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.playList = QtWidgets.QListWidget(self.gridLayoutWidget_2)
        self.playList.setDragEnabled(False)
        self.playList.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.playList.setAlternatingRowColors(False)
        self.playList.setViewMode(QtWidgets.QListView.ListMode)
        self.playList.setModelColumn(0)
        self.playList.setUniformItemSizes(False)
        self.playList.setObjectName("playList")
        self.gridLayout_2.addWidget(self.playList, 2, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 3, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout_2.addItem(spacerItem3, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.recentList = QtWidgets.QListWidget(self.tab_2)
        self.recentList.setGeometry(QtCore.QRect(0, 30, 951, 401))
        self.recentList.setObjectName("recentList")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_2 = QtWidgets.QLabel(self.tab_3)
        self.label_2.setGeometry(QtCore.QRect(300, 150, 321, 91))
        font = QtGui.QFont()
        font.setPointSize(72)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.tabWidget.addTab(self.tab_3, "")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(-10, 440, 981, 61))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(820, 520, 121, 22))
        self.horizontalSlider.setMouseTracking(False)
        self.horizontalSlider.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.horizontalSlider.setAutoFillBackground(False)
        self.horizontalSlider.setStyleSheet("QSlider::groove:horizontal {\n"
"border: 1px solid #bbb;\n"
"background: white;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
"    stop: 0 #66e, stop: 1 #bbf);\n"
"background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,\n"
"    stop: 0 #bbf, stop: 1 #55f);\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: #fff;\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #eee, stop:1 #ccc);\n"
"border: 1px solid #777;\n"
"width: 13px;\n"
"margin-top: -2px;\n"
"margin-bottom: -2px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #fff, stop:1 #ddd);\n"
"border: 1px solid #444;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"background: #bbb;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal:disabled {\n"
"background: #eee;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"background: #eee;\n"
"border: 1px solid #aaa;\n"
"border-radius: 4px;\n"
"}")
        self.horizontalSlider.setMaximum(99)
        self.horizontalSlider.setTracking(True)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setInvertedAppearance(False)
        self.horizontalSlider.setInvertedControls(False)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.btnSound = QtWidgets.QPushButton(self.centralwidget)
        self.btnSound.setGeometry(QtCore.QRect(780, 520, 31, 23))
        self.btnSound.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btnSound.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Icons/speaker_bold_convert-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap("Icons/d.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btnSound.setIcon(icon1)
        self.btnSound.setCheckable(True)
        self.btnSound.setChecked(False)
        self.btnSound.setAutoRepeat(False)
        self.btnSound.setAutoDefault(False)
        self.btnSound.setDefault(False)
        self.btnSound.setFlat(True)
        self.btnSound.setObjectName("btnSound")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(380, 510, 155, 45))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnPrev = QtWidgets.QPushButton(self.layoutWidget)
        self.btnPrev.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Icons/icons8-go-back-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPrev.setIcon(icon2)
        self.btnPrev.setIconSize(QtCore.QSize(35, 35))
        self.btnPrev.setFlat(True)
        self.btnPrev.setObjectName("btnPrev")
        self.horizontalLayout.addWidget(self.btnPrev)
        self.btnPlay = QtWidgets.QPushButton(self.layoutWidget)
        self.btnPlay.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(26)
        self.btnPlay.setFont(font)
        self.btnPlay.setWhatsThis("")
        self.btnPlay.setAutoFillBackground(False)
        self.btnPlay.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Icons/icons8-play-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon3.addPixmap(QtGui.QPixmap("Icons/icons8-pause-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btnPlay.setIcon(icon3)
        self.btnPlay.setIconSize(QtCore.QSize(35, 35))
        self.btnPlay.setCheckable(True)
        self.btnPlay.setChecked(False)
        self.btnPlay.setAutoRepeat(False)
        self.btnPlay.setAutoExclusive(False)
        self.btnPlay.setAutoDefault(False)
        self.btnPlay.setDefault(False)
        self.btnPlay.setFlat(True)
        self.btnPlay.setObjectName("btnPlay")
        self.horizontalLayout.addWidget(self.btnPlay)
        self.btnNext = QtWidgets.QPushButton(self.layoutWidget)
        self.btnNext.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Icons/icons8-circled-right-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnNext.setIcon(icon4)
        self.btnNext.setIconSize(QtCore.QSize(35, 35))
        self.btnNext.setFlat(True)
        self.btnNext.setObjectName("btnNext")
        self.horizontalLayout.addWidget(self.btnNext)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 480, 941, 34))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.muzStart = QtWidgets.QLabel(self.layoutWidget1)
        self.muzStart.setObjectName("muzStart")
        self.horizontalLayout_2.addWidget(self.muzStart)
        self.timeOfMusic = QtWidgets.QSlider(self.layoutWidget1)
        self.timeOfMusic.setMouseTracking(False)
        self.timeOfMusic.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.timeOfMusic.setAutoFillBackground(False)
        self.timeOfMusic.setStyleSheet("QSlider::groove:horizontal {\n"
"border: 1px solid #bbb;\n"
"background: white;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
"    stop: 0 #66e, stop: 1 #bbf);\n"
"background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,\n"
"    stop: 0 #bbf, stop: 1 #55f);\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: #fff;\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #eee, stop:1 #ccc);\n"
"border: 1px solid #777;\n"
"width: 13px;\n"
"margin-top: -2px;\n"
"margin-bottom: -2px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #fff, stop:1 #ddd);\n"
"border: 1px solid #444;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"background: #bbb;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal:disabled {\n"
"background: #eee;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"background: #eee;\n"
"border: 1px solid #aaa;\n"
"border-radius: 4px;\n"
"}")
        self.timeOfMusic.setMaximum(99)
        self.timeOfMusic.setProperty("value", 0)
        self.timeOfMusic.setSliderPosition(0)
        self.timeOfMusic.setTracking(True)
        self.timeOfMusic.setOrientation(QtCore.Qt.Horizontal)
        self.timeOfMusic.setInvertedControls(False)
        self.timeOfMusic.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.timeOfMusic.setObjectName("timeOfMusic")
        self.horizontalLayout_2.addWidget(self.timeOfMusic)
        self.muzEnd = QtWidgets.QLabel(self.layoutWidget1)
        self.muzEnd.setObjectName("muzEnd")
        self.horizontalLayout_2.addWidget(self.muzEnd)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.cmbSort.setCurrentIndex(-1)
        self.playList.setCurrentRow(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ZeroTwo"))
        self.label.setText(_translate("MainWindow", "Sort by:"))
        self.btnImport.setText(_translate("MainWindow", " Import Music"))
        self.playList.setSortingEnabled(True)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "Music"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Recent Plays"))
        self.label_2.setText(_translate("MainWindow", "Closed"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Albums"))
        self.muzStart.setText(_translate("MainWindow", "0:00"))
        self.muzEnd.setText(_translate("MainWindow", "0:00"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
