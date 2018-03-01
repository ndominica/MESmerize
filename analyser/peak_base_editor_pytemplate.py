# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'peak_base_editor_pytemplate.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 612)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.graphicsView = PlotWidget(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout_2.addWidget(self.graphicsView, 0, 0, 1, 5)
        self.listwIndices = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listwIndices.sizePolicy().hasHeightForWidth())
        self.listwIndices.setSizePolicy(sizePolicy)
        self.listwIndices.setMinimumSize(QtCore.QSize(0, 33))
        self.listwIndices.setMaximumSize(QtCore.QSize(16777215, 33))
        self.listwIndices.setProperty("showDropIndicator", False)
        self.listwIndices.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.listwIndices.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listwIndices.setFlow(QtWidgets.QListView.LeftToRight)
        self.listwIndices.setObjectName("listwIndices")
        self.gridLayout_2.addWidget(self.listwIndices, 1, 0, 1, 2)
        self.btnPrev = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnPrev.sizePolicy().hasHeightForWidth())
        self.btnPrev.setSizePolicy(sizePolicy)
        self.btnPrev.setMinimumSize(QtCore.QSize(0, 33))
        self.btnPrev.setMaximumSize(QtCore.QSize(71, 33))
        self.btnPrev.setObjectName("btnPrev")
        self.gridLayout_2.addWidget(self.btnPrev, 1, 2, 1, 1)
        self.btnNext = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnNext.sizePolicy().hasHeightForWidth())
        self.btnNext.setSizePolicy(sizePolicy)
        self.btnNext.setMinimumSize(QtCore.QSize(0, 33))
        self.btnNext.setMaximumSize(QtCore.QSize(71, 33))
        self.btnNext.setObjectName("btnNext")
        self.gridLayout_2.addWidget(self.btnNext, 1, 3, 1, 1)
        self.btnSave = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSave.sizePolicy().hasHeightForWidth())
        self.btnSave.setSizePolicy(sizePolicy)
        self.btnSave.setMinimumSize(QtCore.QSize(0, 33))
        self.btnSave.setMaximumSize(QtCore.QSize(71, 33))
        self.btnSave.setObjectName("btnSave")
        self.gridLayout_2.addWidget(self.btnSave, 1, 4, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.spinBoxAmp = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.spinBoxAmp.setDecimals(4)
        self.spinBoxAmp.setMaximum(10000000.0)
        self.spinBoxAmp.setSingleStep(0.1)
        self.spinBoxAmp.setObjectName("spinBoxAmp")
        self.verticalLayout.addWidget(self.spinBoxAmp)
        self.spinBoxSlope = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.spinBoxSlope.setDecimals(4)
        self.spinBoxSlope.setMaximum(10000000.0)
        self.spinBoxSlope.setSingleStep(0.1)
        self.spinBoxSlope.setObjectName("spinBoxSlope")
        self.verticalLayout.addWidget(self.spinBoxSlope)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.gridLayout_2.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.sliderDotSize = QtWidgets.QSlider(self.centralwidget)
        self.sliderDotSize.setMinimum(1)
        self.sliderDotSize.setMaximum(50)
        self.sliderDotSize.setProperty("value", 10)
        self.sliderDotSize.setOrientation(QtCore.Qt.Horizontal)
        self.sliderDotSize.setObjectName("sliderDotSize")
        self.gridLayout.addWidget(self.sliderDotSize, 1, 0, 1, 3)
        self.gridLayout_2.addLayout(self.gridLayout, 2, 1, 1, 1)
        self.btnPlot = QtWidgets.QPushButton(self.centralwidget)
        self.btnPlot.setCheckable(True)
        self.btnPlot.setChecked(True)
        self.btnPlot.setObjectName("btnPlot")
        self.gridLayout_2.addWidget(self.btnPlot, 2, 2, 1, 1)
        self.btnDone = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnDone.sizePolicy().hasHeightForWidth())
        self.btnDone.setSizePolicy(sizePolicy)
        self.btnDone.setMinimumSize(QtCore.QSize(71, 33))
        self.btnDone.setMaximumSize(QtCore.QSize(71, 33))
        self.btnDone.setObjectName("btnDone")
        self.gridLayout_2.addWidget(self.btnDone, 2, 4, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionUndo = QtWidgets.QAction(MainWindow)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(MainWindow)
        self.actionRedo.setObjectName("actionRedo")
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        self.sliderDotSize.valueChanged['int'].connect(self.label_4.setNum)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnPrev.setText(_translate("MainWindow", "Previous"))
        self.btnNext.setText(_translate("MainWindow", "Next"))
        self.btnSave.setText(_translate("MainWindow", "Save"))
        self.label.setText(_translate("MainWindow", "Amplitude Threshold:"))
        self.label_2.setText(_translate("MainWindow", "Slope Threshold:"))
        self.label_3.setText(_translate("MainWindow", "Dot Size:"))
        self.label_4.setText(_translate("MainWindow", "10"))
        self.btnPlot.setText(_translate("MainWindow", "Plot!"))
        self.btnDone.setText(_translate("MainWindow", "Done"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionRedo.setText(_translate("MainWindow", "Redo"))

from pyqtgraphCore import PlotWidget
