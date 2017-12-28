#!/usr/bin/env python
# -*- coding:utf-8 -*-

#--------------
# a simple graffiti tool for kindle pw1, pw2, pw3, kv, koa1, koa2，
# it is written in python 2.7
# n31WeLt@protonmail.com  2017,12.18
#--------------

import sys, os
from PySide.QtGui import QFont,QListWidgetItem,QWidget,qApp,QPushButton,QPlainTextEdit,QSpinBox,QSlider,QHBoxLayout,QVBoxLayout, QSpacerItem,QGraphicsScene,QGraphicsView,QPen,QColor,QBrush,QListWidget,QToolTip,QImage,QPixmap,QApplication
from PySide.QtCore import QSize,Qt,QRectF,QPoint,QTimer,QLineF


class N31_KGR(QWidget):         #kindle GRAFFITI
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        qApp.setStyleSheet("QWidget{background-color:White} QToolTip {font:Bold 6pt 'Sans';color:Black;background-color:White;border:3px solid grey;border-radius:5px;}QScrollBar::horizontal {height:50;background:gray;border:0px solid darkBlue;position:top;border:2px solid grey;border-radius:10px;} QScrollBar::vertical {width:96;background:gray;border:0px solid darkBlue;position:right;border:2px solid grey;border-radius:10px;} QScrollBar::handle:horizontal{min-width:160px;background-color:white;border:3px solid grey;position:top;border:2px solid grey;border-radius:10px;} QScrollBar::handle:vertical {min-height:50px;background-color:white;border:3px solid grey;position:right;border:2px solid grey;border-radius:10px;} QSpinBox{border:2px solid grey;border-radius:10px;} QPushButton{border:2px solid grey;border-radius:10px;} QPushButton:checked{background-color:rgb(62,62,62);color:rgb(255,255,255);}")
        self.prj_pth_txt_odn = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/') + '/pictures/'
        print "\n\n    Images path : " + self.prj_pth_txt_odn + '\n\n'
        if not os.path.isdir(self.prj_pth_txt_odn): os.mkdir(self.prj_pth_txt_odn)
        #----------------------------
        butn_w,butn_h=66,60      # for pw1, pw2
        #butn_w,butn_h=76,70     # for pw3, kv koa1
        #butn_w,butn_h=96,90     # for koa2

        self.reload_flg = 0
        wdt_font = QFont('Sans',6,QFont.Normal,0)
        self.crnt_file = 'n31_Kgr_pic.png'
        self.set_spin_box_vlaue_flag = 0

        self.butn_save = QPushButton('Save\nimage',  font=wdt_font,  minimumSize=QSize(butn_w+20,butn_h), maximumSize=QSize(butn_w+20,butn_h))
        self.butn_save_as = QPushButton('as',  font=wdt_font, checkable=1,  minimumSize=QSize(butn_w-20,butn_h-8), maximumSize=QSize(butn_w-20,butn_h-8))

        self.ptxedt_file_name_ipt=QPlainTextEdit(maximumSize=QSize(190, butn_h-8),font=QFont('Sans', 5, QFont.Bold, 0))
        self.ptxedt_file_name_ipt.setStyleSheet("border:2px  solid grey;border-radius:0px;")
        self.ptxedt_file_name_ipt.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ptxedt_file_name_ipt.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # self.spnx_nm_sufix=QSpinBox(prefix='0', frame=1, value=0, enabled=1, minimum=0, maximum=99, font=wdt_font, maximumSize=QSize(butn_w + 118, butn_h - 8))    # for pw3, kv, koa1
        # self.spnx_nm_sufix.setStyleSheet("QSpinBox { font:normal 1pt 'Sans'; border: 2px solid grey;border-radius:0px;padding-right:118px; background-color:rgb(176,176,176);} QSpinBox::up-button{subcontrol-position: right; right: 111px; width: 80px; height: 70px;} QSpinBox::down-button{subcontrol-position: right; width: 80px; height: 70px;} ")     # for pw3, kv, koa1

        # self.spnx_nm_sufix=QSpinBox(prefix='0', frame=1, value=0, enabled=1, minimum=0, maximum=99, font=wdt_font, maximumSize=QSize(butn_w + 105, butn_h - 20))   # for  koa2
        # self.spnx_nm_sufix.setStyleSheet("QSpinBox { font:normal 1pt 'Sans'; border: 2px solid grey;border-radius:0px;padding-right:105px; background-color:rgb(176,176,176);} QSpinBox::up-button{subcontrol-position: right; right: 111px; width: 80px; height: 70px;} QSpinBox::down-button{subcontrol-position: right; width: 80px; height: 70px;} ")     # for  koa2

        self.spnx_nm_sufix=QSpinBox(prefix='0', frame=1, value=0, enabled=1, minimum=0, maximum=99, font=wdt_font, maximumSize=QSize(butn_w + 80, butn_h - 8))       # for pw1, pw2
        self.spnx_nm_sufix.setStyleSheet("QSpinBox { font:normal 1pt 'Sans'; border: 2px solid grey;border-radius:0px;padding-right:40px; background-color:rgb(176,176,176);} QSpinBox::up-button{subcontrol-position: right; right: 40px; width: 40px; height: 70px;} QSpinBox::down-button{subcontrol-position: right; width: 40px; height: 70px;} ")         # for pw1, pw2

        self.butn_load = QPushButton('Load\nimage',  font=wdt_font,  minimumSize=QSize(butn_w+20,butn_h), maximumSize=QSize(butn_w+20,butn_h))
        #---
        # self.sld_brush_size=QSlider(Qt.Vertical, font=wdt_font, minimum=1, maximum=96,  value=36, singleStep=6, minimumSize=QSize(76, 440), maximumSize=QSize(76, 440))     # for pw3, kv, koa1
        # self.sld_brush_size.setStyleSheet("QSlider::groove:vertical { border:2px solid grey;height:436px;background:white;border:2px solid grey;border-radius:10px;} QSlider::handle:vertical { width:90px;height:60px;background-color:white;border:12px solid grey;border-radius:30px;}")     # for pw3, kv, koa1

        # self.sld_brush_size=QSlider(Qt.Vertical, font=wdt_font, minimum=1, maximum=96,  value=36, singleStep=6, minimumSize=QSize(76, 440), maximumSize=QSize(76, 440))     # for  koa2
        # self.sld_brush_size.setStyleSheet("QSlider::groove:vertical { border:2px solid grey;height:436px;background:white;border:2px solid grey;border-radius:10px;} QSlider::handle:vertical { width:90px;height:60px;background-color:white;border:12px solid grey;border-radius:30px;}")     # for  koa2

        self.sld_brush_size=QSlider(Qt.Vertical, font=wdt_font, minimum=1, maximum=96,  value=36, singleStep=6, minimumSize=QSize(66, 240), maximumSize=QSize(66, 240))
        self.sld_brush_size.setStyleSheet("QSlider::groove:vertical { border:2px solid grey;height:236px;background:white;border:2px solid grey;border-radius:10px;} QSlider::handle:vertical { width:90px;height:60px;background-color:white;border:12px solid grey;border-radius:30px;}")
        self.sld_brush_size.setInvertedAppearance(1)

        self.butn_adjust_brush = QPushButton(u'△', font=QFont('Sans',15,QFont.Normal,0), minimumSize=QSize(butn_w,butn_h-20), maximumSize=QSize(butn_w,butn_h))
        self.butn_brsh_1 = QPushButton('****\n****',  font=wdt_font, checkable=1,minimumSize=QSize(butn_w,butn_h), maximumSize=QSize(butn_w,butn_h))
        self.butn_brsh_2 = QPushButton(": : : :",  font=wdt_font,checkable=1,minimumSize=QSize(butn_w,butn_h), maximumSize=QSize(butn_w,butn_h))
        self.butn_brsh_3 = QPushButton('///',   font=wdt_font,checkable=1,minimumSize=QSize(butn_w,butn_h), maximumSize=QSize(butn_w,butn_h))
        self.butn_brsh_4 = QPushButton('| | |',  font=wdt_font,checkable=1,minimumSize=QSize(butn_w,butn_h), maximumSize=QSize(butn_w,butn_h))
        self.butn_brsh_5 = QPushButton('----\n----',  font=wdt_font, checkable=1,minimumSize=QSize(butn_w,butn_h), maximumSize=QSize(butn_w,butn_h))
        self.butn_brsh_6 = QPushButton('xxxx', font=wdt_font,checkable=1, minimumSize=QSize(butn_w,butn_h), maximumSize=QSize(butn_w,butn_h) )

        self.butn_light = QPushButton('Grey\ncolor',  font=wdt_font, checkable=1,minimumSize=QSize(butn_w,butn_h-8), maximumSize=QSize(butn_w,butn_h-8))
        self.butn_dark = QPushButton('Dark\ncolor', font=wdt_font,  checkable=1,minimumSize=QSize(butn_w,butn_h-8), maximumSize=QSize(butn_w,butn_h-8))
        self.butn_dark.setChecked(1)
        self.butn_erase = QPushButton('Erase\nwhite', font=wdt_font, checkable=1,minimumSize=QSize(butn_w,butn_h-8), maximumSize=QSize(butn_w,butn_h-8))

        self.butn_undo = QPushButton('UnDo',font=wdt_font, minimumSize=QSize(butn_w,butn_h), maximumSize=QSize(butn_w,butn_h))

        self.butn_reset = QPushButton('ReseT',font=wdt_font, minimumSize=QSize(butn_w,butn_h), maximumSize=QSize(butn_w,butn_h))
        self.butn_quit = QPushButton('QUIT',  font=wdt_font,  minimumSize=QSize(butn_w,butn_h), maximumSize=QSize(butn_w,butn_h))
        #---
        lyt_hrznt_top_butn=QHBoxLayout()
        lyt_hrznt_top_butn.setContentsMargins(0,0,0,0)

        lyt_hrznt_top_butn.addWidget(self.butn_save)
        lyt_hrznt_top_butn.addItem(QSpacerItem(10,10))     #---
        lyt_hrznt_top_butn.addWidget(self.butn_save_as)
        lyt_hrznt_top_butn.addItem(QSpacerItem(10,10))     #---
        lyt_hrznt_top_butn.addWidget(self.ptxedt_file_name_ipt)
        lyt_hrznt_top_butn.addWidget(self.spnx_nm_sufix)
        lyt_hrznt_top_butn.addItem(QSpacerItem(10,10))     #---
        lyt_hrznt_top_butn.addWidget(self.butn_load)
        lyt_hrznt_top_butn.addItem(QSpacerItem(26,26))     #---
        lyt_hrznt_top_butn.addWidget(self.butn_light)
        lyt_hrznt_top_butn.addItem(QSpacerItem(10,10))     #---
        lyt_hrznt_top_butn.addWidget(self.butn_dark)
        lyt_hrznt_top_butn.addItem(QSpacerItem(10,10))     #---
        lyt_hrznt_top_butn.addWidget(self.butn_erase)
        lyt_hrznt_top_butn.addItem(QSpacerItem(26,26))     #---
        lyt_hrznt_top_butn.addWidget(self.butn_undo)
        #---
        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene)
        self.scene.setSceneRect(QRectF(self.view.rect()))
        self.view.setStyleSheet(" QGraphicsView{border:1px solid grey;border-radius:0px;background-color:rgb(255,255,255);} ") # 2 , 10
        self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.penclr = QPen(QColor(0, 0, 0), self.sld_brush_size.value(), Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
        self.penclr.setBrush(QBrush(Qt.SolidPattern))
        self.penclr.setStyle(Qt.SolidLine)
        self.view.setCacheMode(QGraphicsView.CacheBackground)
        self.view.setViewportUpdateMode(QGraphicsView.BoundingRectViewportUpdate)
        #---
        lyt_vtkl_brush = QVBoxLayout()
        lyt_vtkl_brush.setContentsMargins(9,0,0,0)   #8
        lyt_vtkl_brush.addWidget(self.sld_brush_size)
        lyt_vtkl_brush.addWidget(self.butn_adjust_brush)
        lyt_vtkl_brush.addItem(QSpacerItem(25,25))     #---
        lyt_vtkl_brush.addWidget(self.butn_brsh_1)
        lyt_vtkl_brush.addItem(QSpacerItem(10,10))     #---
        lyt_vtkl_brush.addWidget(self.butn_brsh_2)
        lyt_vtkl_brush.addItem(QSpacerItem(10,10))     #---
        lyt_vtkl_brush.addWidget(self.butn_brsh_3)
        lyt_vtkl_brush.addItem(QSpacerItem(10,10))     #---
        lyt_vtkl_brush.addWidget(self.butn_brsh_4)
        lyt_vtkl_brush.addItem(QSpacerItem(10,10))     #---
        lyt_vtkl_brush.addWidget(self.butn_brsh_5)
        lyt_vtkl_brush.addItem(QSpacerItem(10,10))     #---
        lyt_vtkl_brush.addWidget(self.butn_brsh_6)
        lyt_vtkl_brush.addItem(QSpacerItem(25,25))     #---
        lyt_vtkl_brush.addWidget(self.butn_reset)
        lyt_vtkl_brush.addItem(QSpacerItem(10,10))     #---
        lyt_vtkl_brush.addItem(QSpacerItem(10,10))     #---
        lyt_vtkl_brush.addItem(QSpacerItem(10,10))     #---
        lyt_vtkl_brush.addWidget(self.butn_quit)
        #---
        self.list_openlst=QListWidget(font=wdt_font,alternatingRowColors=1, gridSize=QSize(0,96), layoutDirection=Qt.RightToLeft)
        self.list_openlst.setFixedWidth(0)
        self.list_openlst.verticalScrollBar().setContextMenuPolicy(Qt.NoContextMenu)
        self.list_openlst.setStyleSheet("border:2px solid grey;border-radius:10px; alternate-background-color:rgb(255,255,255);selection-color:Mediumvioletred;selection-background-color:lightblue;background-color:rgb(236,236,236)")

        lyt_hrzt_bottom = QHBoxLayout()
        lyt_hrzt_bottom.setContentsMargins(0,0,0,0)
        lyt_hrzt_bottom.addWidget(self.list_openlst)
        lyt_hrzt_bottom.addWidget(self.view)
        lyt_hrzt_bottom.addItem(lyt_vtkl_brush)
        #---
        lyt_vtkl_main = QVBoxLayout()
        lyt_vtkl_main.setContentsMargins(10,5,10,10)
        lyt_vtkl_main.addItem(lyt_hrznt_top_butn)
        lyt_vtkl_main.addItem(lyt_hrzt_bottom)
        #----------------------------
        self.setLayout(lyt_vtkl_main)
        #----------------------------
        self.butn_reset.clicked.connect(self.reset_draw)
        self.butn_brsh_1.clicked.connect(lambda : self.change_brush_type('1'))
        self.butn_brsh_2.clicked.connect(lambda : self.change_brush_type('2'))
        self.butn_brsh_3.clicked.connect(lambda : self.change_brush_type('3'))
        self.butn_brsh_4.clicked.connect(lambda : self.change_brush_type('4'))
        self.butn_brsh_5.clicked.connect(lambda : self.change_brush_type('5'))
        self.butn_brsh_6.clicked.connect(lambda : self.change_brush_type('6'))

        self.butn_light.clicked.connect(lambda : self.change_color('lgh'))
        self.butn_dark.clicked.connect(lambda : self.change_color('drk'))
        self.butn_erase.clicked.connect(lambda : self.change_color('era'))

        self.butn_undo.clicked.connect(self.butn_undo_clicked)
        self.butn_save.clicked.connect(self.butn_save_clicked)
        self.butn_save_as.clicked.connect(self.butn_save_as_clicked)
        self.butn_load.clicked.connect(self.load_butn_clicked)
        self.list_openlst.itemPressed.connect(self.item_in_load_file_list_actived)
        self.butn_quit.clicked.connect(self.butn_quit_clicked)
        #------------------------------------------
        self.scene.mouseMoveEvent = self.draw_point
        #------------------------------------------
        self.sld_brush_size.sliderReleased.connect(self.brush_size_value_changed)
        self.butn_adjust_brush.clicked.connect(self.butn_adjust_brush_clicked)
        self.spnx_nm_sufix.valueChanged.connect(self.spnx_naming_sufix_value_changed)
        self.ptxedt_file_name_ipt.setPlainText(self.crnt_file.split('/')[-1])
        self.butn_save_as.setChecked(1)

    def butn_quit_clicked(self):
        if self.butn_save_as.isChecked():
            QTimer.singleShot(500,lambda:QToolTip.showText(QPoint(8,40),u"* n31_Kgr will quit in 18 seconds, uncheck 'as' button to prevent this popup window\n\
______________________\n\n\
Quick Start :  n31_Kgr v0.1 ( Kindle Graffiti )\n\n\
1. Click buttons on the right panel to change brush style:  '| | |',  '///'  etc.\n\n\
2. Click buttons on the top panel to change brush color: 'Grey color', 'Dark color'.\n\n\
3. Slide grey ring vertically on the right pannel to change brush size. \n\n\
4. When 'as' button is checked, 'save' button function switch to save as mode.\n\
    Click the arrow button to change file names.    ( ↑ prevent overwrite ↑ )\n\n\
5. When 'as' button is unchecked, save file directly.    ( allow overwrite )\n\n\
6. Images file path is ( open and save ) : /mnt/us/extensions/n31_Kgr/bin/pictures/\n\n\n\
* n31_Kgr will quit in 18 seconds.( uncheck 'as' button to prevent this popup window )\n\n\
  More info about n31_Kgr : N31WeLt@protonmail.com  2017,12.18 D ."))
            QTimer.singleShot(18000,lambda:app.quit())
        else : app.quit()

    def reset_draw(self):
        self.scene.clear()
        # os.popen("xrefresh")      #for koa2
        # QTimer.singleShot(1200,lambda:os.popen("xrefresh"))       #for koa2
        self.crnt_file = 'n31_Kgr_pic.png'
        self.ptxedt_file_name_ipt.setPlainText(self.crnt_file.split('/')[-1])
        self.butn_save_as.setChecked(1)
        self.spnx_nm_sufix.setEnabled(1)
        self.sld_brush_size.setValue(3)
        self.penclr.setWidth( self.sld_brush_size.value() )

    def load_butn_clicked(self):
        self.fill_load_files_list()
        if self.list_openlst.width()>2 :
            self.list_openlst.setFixedWidth(0)
            self.butn_load.setText('Load\nimage')
            self.view.setEnabled(1)
            self.butn_save.setEnabled(1)
            if self.crnt_file and self.reload_flg==1:
                QTimer.singleShot(10,lambda:self.scene.clear())
                QTimer.singleShot(100,lambda:self.load_image(self.crnt_file,'int'))
        else :
            self.list_openlst.setFixedWidth(270)
            self.butn_load.setText('Slide')
            self.view.setEnabled(0)
            self.butn_save.setEnabled(0)

    def fill_load_files_list(self):
        self.list_openlst.clear()
        file_formt_set = set( ('.jpg', '.tif', '.png', '.bmp', '.xpm', '.tga') )
        for ff in os.listdir(self.prj_pth_txt_odn):
            if os.path.isfile(self.prj_pth_txt_odn+ff) and ff[-4:].lower() in file_formt_set:
                crt_itm=QListWidgetItem(ff.decode('utf8'))
                crt_itm.setSizeHint(QSize(180,80))
                self.list_openlst.addItem(crt_itm)

    def item_in_load_file_list_actived(self):
        self.crnt_file=str(self.prj_pth_txt_odn + self.list_openlst.currentItem().text()).decode('utf-8')
        self.load_image(self.crnt_file, 'ext')

    def load_image(self, ipt_pth, typ):
        self.scene.clear()
        dsp_image = QImage(ipt_pth)
        self.scene.addPixmap(QPixmap.fromImage(dsp_image))
        tmp_rect = QRectF(0,0,1,1)
        self.scene.setSceneRect(QRectF(self.view.rect().x()+1 ,self.view.rect().x()+1  ,self.view.rect().width() ,self.view.rect().height() ))
        self.scene.update()

        self.reload_flg=1 if typ=='ext' else 0
        self.ptxedt_file_name_ipt.setPlainText(self.crnt_file.split('/')[-1])
        self.spnx_nm_sufix.setEnabled(1) if self.butn_save_as.isChecked() else self.spnx_nm_sufix.setEnabled(0)

    def butn_save_as_clicked(self):
        self.spnx_nm_sufix.setValue(0)
        self.spnx_nm_sufix.setEnabled(1) if self.butn_save_as.isChecked() else self.spnx_nm_sufix.setEnabled(0)
        self.set_spin_box_vlaue_flag = 1
        self.ptxedt_file_name_ipt.setPlainText(self.crnt_file.split('/')[-1])

    def butn_save_clicked(self):
        tips_pp = self.mapToGlobal(self.butn_save.pos()) - QPoint(2, 75)
        opt_nm = str(self.ptxedt_file_name_ipt.toPlainText())
        if not opt_nm :
            QTimer.singleShot(100, lambda:QToolTip.showText(tips_pp, 'please set a file name to save.'))
            return
        opt_pth = self.prj_pth_txt_odn + opt_nm
        if self.butn_save_as.isChecked() and os.path.isfile(opt_pth):
            QTimer.singleShot(10, lambda:QToolTip.showText(tips_pp, "file is exist, please change a name to save, or uncheck 'as' button to overwrite the file."))
            return
        crnt_pixmap = QPixmap.grabWidget(self.view,x=0, y=0, width= self.view.width()-3, height = self.view.height()-3)   #crop border line
        crnt_pixmap.save(opt_pth, format='png')
        QTimer.singleShot(10, lambda:QToolTip.showText(tips_pp, 'file saved successfully.'))
        self.crnt_file=opt_pth

    def spnx_naming_sufix_value_changed(self):
        self.ptxedt_file_name_ipt.setFocus()
        self.spnx_nm_sufix.setPrefix('0') if self.spnx_nm_sufix.value() < 10 else self.spnx_nm_sufix.setPrefix('')
        if '.' in self.crnt_file :
            crnt_nmb = self.crnt_file.split('/')[-1].split('.')[-2][-2:]        #get current file name sufix
            if crnt_nmb.isdigit():      #if file sufix is digital
                if self.set_spin_box_vlaue_flag == 1:
                    self.spnx_nm_sufix.setValue(int(crnt_nmb) + 1)
                    self.set_spin_box_vlaue_flag = 0
                new_img_nm = '.'.join(self.crnt_file.split('/')[-1].split('.')[:-1])[:-2] + str(self.spnx_nm_sufix.text()) + '.png'
            else :
                new_img_nm = '.'.join(self.crnt_file.split('/')[-1].split('.')[:-1]) + '_' + str(self.spnx_nm_sufix.text()) + '.png'
        else :  new_img_nm = self.crnt_file.split('/')[-1] + '_' + str(self.spnx_nm_sufix.text()) + '.png'

        self.ptxedt_file_name_ipt.setPlainText(new_img_nm)
        tips_pp = self.mapToGlobal(self.butn_save.pos()) - QPoint(2, 75)
        if os.path.isfile( self.prj_pth_txt_odn + new_img_nm) : QTimer.singleShot(150, lambda:QToolTip.showText(tips_pp, 'this file name is exists in project folder.'))           #print ('this file name is exists in project folder.')        # if not os.path.isfile( self.prj_pth_txt_odn + new_img_nm) : print ('file name is ok.')
        # else :      QTimer.singleShot(10, lambda:QToolTip.showText(tips_pp, 'the file name is valid.'))

    def change_brush_type(self, typ):
        color_butn_lst = ( self.butn_light,self.butn_dark,self.butn_erase)
        for cc in color_butn_lst : cc.setChecked(0)

        butn_dic = { '1':self.butn_brsh_1 ,'2':self.butn_brsh_2 ,'3':self.butn_brsh_3 ,'4':self.butn_brsh_4 ,'5':self.butn_brsh_5, '6':self.butn_brsh_6 }
        for kk, vv in butn_dic.iteritems() : vv.setChecked(0) if kk != typ else vv.setChecked(1)

        brsh_dic = { '1':Qt.Dense5Pattern ,'2':Qt.Dense6Pattern, '3':Qt.BDiagPattern ,'4':Qt.VerPattern ,'5':Qt.HorPattern,'6':Qt.DiagCrossPattern }
        self.penclr.setBrush(QBrush(brsh_dic[typ]))
        self.penclr.setWidth(self.sld_brush_size.value())

    def change_color(self, typ):
        brush_butn_lst = (  self.butn_brsh_1 , self.butn_brsh_2 , self.butn_brsh_3 , self.butn_brsh_4 , self.butn_brsh_5 , self.butn_brsh_6 )
        for bb in brush_butn_lst : bb.setChecked(0)

        butn_dic = { 'lgh':self.butn_light,'drk':self.butn_dark, 'era':self.butn_erase }
        for kk, vv in butn_dic.iteritems() : vv.setChecked(0) if kk != typ else vv.setChecked(1)

        clor_dic = { 'lgh':QColor(190, 190, 190),'drk':QColor(0, 0, 0), 'era':QColor(255, 255, 255)}
        self.penclr.setColor(clor_dic[typ])
        self.penclr.setWidth(self.sld_brush_size.value() * 5) if typ == 'era' else self.penclr.setWidth(self.sld_brush_size.value())

    def brush_size_value_changed(self):
         self.penclr.setWidth(self.sld_brush_size.value() * 5) if self.butn_erase.isChecked() else self.penclr.setWidth(self.sld_brush_size.value())
         pp = self.mapToGlobal(self.sld_brush_size.pos()) - QPoint(47, 17)
         QTimer.singleShot(10, lambda:QToolTip.showText(pp, str(self.sld_brush_size.value())))

    def butn_adjust_brush_clicked(self):
        if self.sld_brush_size.value() < 2 : return
        self.sld_brush_size.setValue( self.sld_brush_size.value() - 1 )
        self.penclr.setWidth( self.sld_brush_size.value() )
        pp = self.mapToGlobal(self.sld_brush_size.pos()) - QPoint(47, 17)
        QTimer.singleShot(10, lambda:QToolTip.showText(pp, str(self.sld_brush_size.value())))

    def butn_undo_clicked(self):
        for idx , ii in enumerate(self.scene.items()) :
            if len(self.scene.items())< 2 or idx >12  :return       #to keep background layer
            self.scene.removeItem(ii)

    def draw_point(self, event):
        self.scene.addLine(QLineF( event.scenePos(), event.lastScenePos() ), self.penclr)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    screen_rect=app.desktop().screenGeometry()
    #if screen_rect.width() >= 1072 and screen_rect.height() == 1448:   #for pw3, kv koa1
    #if screen_rect.width() >=1264 and screen_rect.height()==1680:      #for koa2
    if 1==1: #screen_rect.width() >= 758 and screen_rect.height() == 1024:     #for pw1, pw2
        MainWindow = N31_KGR()
        MainWindow.setWindowTitle('L:A_N:application_ID:PySide')
        MainWindow.setWindowFlags(Qt.FramelessWindowHint)
        #MainWindow.setFixedSize(1072, 1392)                            #for pw3, kv koa1
        #MainWindow.setFixedSize(1264, 1608)                            #for koa2
        MainWindow.setFixedSize(758, 980)                               #for pw1, pw2
        MainWindow.show()
        sys.exit(app.exec_()
