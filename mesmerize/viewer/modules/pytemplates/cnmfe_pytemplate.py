# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui_files/cnmfe_pytemplate.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DockWidget(object):
    def setupUi(self, DockWidget):
        DockWidget.setObjectName("DockWidget")
        DockWidget.setWindowModality(QtCore.Qt.NonModal)
        DockWidget.resize(499, 1053)
        DockWidget.setFloating(True)
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_19 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_19.setMinimumSize(QtCore.QSize(0, 0))
        self.label_19.setMaximumSize(QtCore.QSize(40, 16777215))
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_4.addWidget(self.label_19)
        self.comboBoxInput = QtWidgets.QComboBox(self.dockWidgetContents)
        self.comboBoxInput.setObjectName("comboBoxInput")
        self.comboBoxInput.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBoxInput)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.label_5 = QtWidgets.QLabel(self.dockWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_2 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.dockWidgetContents)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.spinBoxGSig = QtWidgets.QSpinBox(self.dockWidgetContents)
        self.spinBoxGSig.setMinimum(2)
        self.spinBoxGSig.setMaximum(998)
        self.spinBoxGSig.setSingleStep(2)
        self.spinBoxGSig.setProperty("value", 14)
        self.spinBoxGSig.setObjectName("spinBoxGSig")
        self.horizontalLayout.addWidget(self.spinBoxGSig)
        self.label_22 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout.addWidget(self.label_22)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_9 = QtWidgets.QLabel(self.dockWidgetContents)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_3.addWidget(self.label_9)
        self.lineEdCorrPNRName = QtWidgets.QLineEdit(self.dockWidgetContents)
        self.lineEdCorrPNRName.setObjectName("lineEdCorrPNRName")
        self.horizontalLayout_3.addWidget(self.lineEdCorrPNRName)
        self.btnAddToBatchCorrPNR = QtWidgets.QPushButton(self.dockWidgetContents)
        self.btnAddToBatchCorrPNR.setObjectName("btnAddToBatchCorrPNR")
        self.horizontalLayout_3.addWidget(self.btnAddToBatchCorrPNR)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.line_2 = QtWidgets.QFrame(self.dockWidgetContents)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.label_20 = QtWidgets.QLabel(self.dockWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.verticalLayout.addWidget(self.label_20)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lineEditAin = QtWidgets.QLineEdit(self.dockWidgetContents)
        self.lineEditAin.setObjectName("lineEditAin")
        self.horizontalLayout_2.addWidget(self.lineEditAin)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_7 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_8 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_6.addWidget(self.label_8)
        self.doubleSpinBoxMinCorr = QtWidgets.QDoubleSpinBox(self.dockWidgetContents)
        self.doubleSpinBoxMinCorr.setDecimals(3)
        self.doubleSpinBoxMinCorr.setMaximum(1.0)
        self.doubleSpinBoxMinCorr.setSingleStep(0.005)
        self.doubleSpinBoxMinCorr.setProperty("value", 0.89)
        self.doubleSpinBoxMinCorr.setObjectName("doubleSpinBoxMinCorr")
        self.horizontalLayout_6.addWidget(self.doubleSpinBoxMinCorr)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.label_11 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_11.setObjectName("label_11")
        self.verticalLayout.addWidget(self.label_11)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_10 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_7.addWidget(self.label_10)
        self.spinBoxMinPNR = QtWidgets.QSpinBox(self.dockWidgetContents)
        self.spinBoxMinPNR.setMaximum(999)
        self.spinBoxMinPNR.setProperty("value", 4)
        self.spinBoxMinPNR.setObjectName("spinBoxMinPNR")
        self.horizontalLayout_7.addWidget(self.spinBoxMinPNR)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.label_13 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_13.setObjectName("label_13")
        self.verticalLayout.addWidget(self.label_13)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_12 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_8.addWidget(self.label_12)
        self.spinBoxMinSNR = QtWidgets.QSpinBox(self.dockWidgetContents)
        self.spinBoxMinSNR.setProperty("value", 1)
        self.spinBoxMinSNR.setObjectName("spinBoxMinSNR")
        self.horizontalLayout_8.addWidget(self.spinBoxMinSNR)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.label_14 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_14.setObjectName("label_14")
        self.verticalLayout.addWidget(self.label_14)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_15 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_9.addWidget(self.label_15)
        self.doubleSpinBoxRValuesMin = QtWidgets.QDoubleSpinBox(self.dockWidgetContents)
        self.doubleSpinBoxRValuesMin.setMaximum(1.0)
        self.doubleSpinBoxRValuesMin.setSingleStep(0.025)
        self.doubleSpinBoxRValuesMin.setProperty("value", 0.7)
        self.doubleSpinBoxRValuesMin.setObjectName("doubleSpinBoxRValuesMin")
        self.horizontalLayout_9.addWidget(self.doubleSpinBoxRValuesMin)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.label_17 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_17.setObjectName("label_17")
        self.verticalLayout.addWidget(self.label_17)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_16 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_10.addWidget(self.label_16)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.dockWidgetContents)
        self.doubleSpinBox.setMinimum(0.1)
        self.doubleSpinBox.setSingleStep(0.5)
        self.doubleSpinBox.setProperty("value", 4.0)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.horizontalLayout_10.addWidget(self.doubleSpinBox)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.label_24 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_24.setObjectName("label_24")
        self.verticalLayout.addWidget(self.label_24)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_21 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_13.addWidget(self.label_21)
        self.spinBoxRf = QtWidgets.QSpinBox(self.dockWidgetContents)
        self.spinBoxRf.setMaximum(999)
        self.spinBoxRf.setProperty("value", 50)
        self.spinBoxRf.setObjectName("spinBoxRf")
        self.horizontalLayout_13.addWidget(self.spinBoxRf)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout_13)
        self.label_25 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_25.setObjectName("label_25")
        self.verticalLayout.addWidget(self.label_25)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_26 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_26.setObjectName("label_26")
        self.horizontalLayout_18.addWidget(self.label_26)
        self.spinBoxOverlap = QtWidgets.QSpinBox(self.dockWidgetContents)
        self.spinBoxOverlap.setMaximum(999)
        self.spinBoxOverlap.setProperty("value", 30)
        self.spinBoxOverlap.setObjectName("spinBoxOverlap")
        self.horizontalLayout_18.addWidget(self.spinBoxOverlap)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem8)
        self.verticalLayout.addLayout(self.horizontalLayout_18)
        self.label_28 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_28.setObjectName("label_28")
        self.verticalLayout.addWidget(self.label_28)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_27 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_27.setObjectName("label_27")
        self.horizontalLayout_19.addWidget(self.label_27)
        self.spinBoxGnb = QtWidgets.QSpinBox(self.dockWidgetContents)
        self.spinBoxGnb.setMaximum(99)
        self.spinBoxGnb.setProperty("value", 10)
        self.spinBoxGnb.setObjectName("spinBoxGnb")
        self.horizontalLayout_19.addWidget(self.spinBoxGnb)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem9)
        self.verticalLayout.addLayout(self.horizontalLayout_19)
        self.label_30 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_30.setObjectName("label_30")
        self.verticalLayout.addWidget(self.label_30)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_29 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_29.setObjectName("label_29")
        self.horizontalLayout_20.addWidget(self.label_29)
        self.spinBoxNb_patch = QtWidgets.QSpinBox(self.dockWidgetContents)
        self.spinBoxNb_patch.setMinimum(1)
        self.spinBoxNb_patch.setProperty("value", 10)
        self.spinBoxNb_patch.setObjectName("spinBoxNb_patch")
        self.horizontalLayout_20.addWidget(self.spinBoxNb_patch)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem10)
        self.verticalLayout.addLayout(self.horizontalLayout_20)
        self.label_32 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_32.setObjectName("label_32")
        self.verticalLayout.addWidget(self.label_32)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.label_31 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_31.setObjectName("label_31")
        self.horizontalLayout_21.addWidget(self.label_31)
        self.spinBoxK = QtWidgets.QSpinBox(self.dockWidgetContents)
        self.spinBoxK.setMinimum(1)
        self.spinBoxK.setProperty("value", 10)
        self.spinBoxK.setObjectName("spinBoxK")
        self.horizontalLayout_21.addWidget(self.spinBoxK)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem11)
        self.verticalLayout.addLayout(self.horizontalLayout_21)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_18 = QtWidgets.QLabel(self.dockWidgetContents)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_11.addWidget(self.label_18)
        self.lineEdName = QtWidgets.QLineEdit(self.dockWidgetContents)
        self.lineEdName.setObjectName("lineEdName")
        self.horizontalLayout_11.addWidget(self.lineEdName)
        self.btnAddToBatchCNMFE = QtWidgets.QPushButton(self.dockWidgetContents)
        self.btnAddToBatchCNMFE.setObjectName("btnAddToBatchCNMFE")
        self.horizontalLayout_11.addWidget(self.btnAddToBatchCNMFE)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem12)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.btnExport = QtWidgets.QPushButton(self.dockWidgetContents)
        self.btnExport.setObjectName("btnExport")
        self.horizontalLayout_12.addWidget(self.btnExport)
        self.btnImport = QtWidgets.QPushButton(self.dockWidgetContents)
        self.btnImport.setObjectName("btnImport")
        self.horizontalLayout_12.addWidget(self.btnImport)
        self.verticalLayout.addLayout(self.horizontalLayout_12)
        DockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidget)
        self.lineEdName.returnPressed.connect(self.btnAddToBatchCNMFE.click)
        QtCore.QMetaObject.connectSlotsByName(DockWidget)
        DockWidget.setTabOrder(self.comboBoxInput, self.spinBoxGSig)
        DockWidget.setTabOrder(self.spinBoxGSig, self.lineEdCorrPNRName)
        DockWidget.setTabOrder(self.lineEdCorrPNRName, self.btnAddToBatchCorrPNR)
        DockWidget.setTabOrder(self.btnAddToBatchCorrPNR, self.doubleSpinBoxMinCorr)
        DockWidget.setTabOrder(self.doubleSpinBoxMinCorr, self.spinBoxMinPNR)
        DockWidget.setTabOrder(self.spinBoxMinPNR, self.spinBoxMinSNR)
        DockWidget.setTabOrder(self.spinBoxMinSNR, self.doubleSpinBoxRValuesMin)
        DockWidget.setTabOrder(self.doubleSpinBoxRValuesMin, self.spinBoxRf)
        DockWidget.setTabOrder(self.spinBoxRf, self.spinBoxOverlap)
        DockWidget.setTabOrder(self.spinBoxOverlap, self.spinBoxGnb)
        DockWidget.setTabOrder(self.spinBoxGnb, self.spinBoxNb_patch)
        DockWidget.setTabOrder(self.spinBoxNb_patch, self.spinBoxK)
        DockWidget.setTabOrder(self.spinBoxK, self.lineEdName)
        DockWidget.setTabOrder(self.lineEdName, self.btnAddToBatchCNMFE)
        DockWidget.setTabOrder(self.btnAddToBatchCNMFE, self.btnExport)
        DockWidget.setTabOrder(self.btnExport, self.btnImport)

    def retranslateUi(self, DockWidget):
        _translate = QtCore.QCoreApplication.translate
        DockWidget.setWindowTitle(_translate("DockWidget", "&CNMF-E"))
        self.label_19.setText(_translate("DockWidget", "Input:"))
        self.comboBoxInput.setItemText(0, _translate("DockWidget", "Current Work Environment"))
        self.label_5.setToolTip(_translate("DockWidget", "Compute some summary images (correlation and peak to noise ratio)"))
        self.label_5.setText(_translate("DockWidget", "Inspect Correlation and PNR"))
        self.label_2.setText(_translate("DockWidget", "gaussian width of a 2D gaussian kernel, which approximates a neuron\n"
"3 times less than the average diamters of a neuron (pixels)"))
        self.label.setText(_translate("DockWidget", "gSig:"))
        self.label_22.setText(_translate("DockWidget", "Must be an even number"))
        self.label_9.setText(_translate("DockWidget", "Stop here:"))
        self.lineEdCorrPNRName.setPlaceholderText(_translate("DockWidget", "Enter name"))
        self.btnAddToBatchCorrPNR.setText(_translate("DockWidget", "Add to batch"))
        self.label_20.setText(_translate("DockWidget", "CNMF-E"))
        self.label_3.setText(_translate("DockWidget", "Ain:"))
        self.label_7.setText(_translate("DockWidget", "Minimum correlation of peak"))
        self.label_8.setText(_translate("DockWidget", "min_corr:"))
        self.label_11.setText(_translate("DockWidget", "Minimum peak to noise ratio"))
        self.label_10.setText(_translate("DockWidget", "min_pnr:"))
        self.label_13.setText(_translate("DockWidget", "Adaptive way to set threshold on the transient size"))
        self.label_12.setText(_translate("DockWidget", "min_SNR:"))
        self.label_14.setText(_translate("DockWidget", "Threshold on space consistency \n"
"If lower more components will be accepted, potentially with worse quality"))
        self.label_15.setText(_translate("DockWidget", "r_values_min:"))
        self.label_17.setText(_translate("DockWidget", "Average decay time of calcium spikes (seconds)"))
        self.label_16.setText(_translate("DockWidget", "decay_time:"))
        self.label_24.setText(_translate("DockWidget", "Half size of patch"))
        self.label_21.setText(_translate("DockWidget", "rf:"))
        self.label_25.setText(_translate("DockWidget", "Overlap of patches (at least 4 times the size of a neuron/cell)"))
        self.label_26.setText(_translate("DockWidget", "overlap:"))
        self.label_28.setText(_translate("DockWidget", "Global number of background components"))
        self.label_27.setText(_translate("DockWidget", "gnb:"))
        self.label_30.setText(_translate("DockWidget", "Background components per patch"))
        self.label_29.setText(_translate("DockWidget", "nb_patch:"))
        self.label_32.setText(_translate("DockWidget", "Number of neurons/cell per patch"))
        self.label_31.setText(_translate("DockWidget", "k:"))
        self.label_18.setText(_translate("DockWidget", "Perform CNMF-E:"))
        self.lineEdName.setPlaceholderText(_translate("DockWidget", "Enter name"))
        self.btnAddToBatchCNMFE.setText(_translate("DockWidget", "Add to batch"))
        self.btnExport.setText(_translate("DockWidget", "Export Parameters"))
        self.btnImport.setText(_translate("DockWidget", "Import Parameters"))

