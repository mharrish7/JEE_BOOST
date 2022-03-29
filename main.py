from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.button import MDRectangleFlatButton,MDRaisedButton
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.label import MDLabel
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.screen import MDScreen

from random import randint
from kivy.uix.image import Image
from kivmob import KivMob, TestIds
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivy.core.window import Window

Window.size = (320,600)


import questions as jq
import Aquestions as ajq
na = 0
q = 0
aq = 0
mark = 0
ma = 1
mb = 1
mc = 1
md = 1
accuracy = '____'
no = 1

def aqchange(arg=''):
    global aq
    ran = randint(1,ajq.na)
    aq = ajq.aq[ran-1]
    return aq
aq = aqchange()



cardt = """
MDCard:
    orientation : 'vertical'
    size_hint_y : None
    height : dp(120)
    md_bg_color : 0,153/255,1,1
    radius : dp(15)
    
    
"""



def qchange(arg=''):
    global q
    ran = randint(1,jq.n)
    q = jq.q[ran-1]
    return q 
q = qchange()

class Menu(MDScreen):
    pass

class Pratice(MDScreen):
    pass

class Answer(MDScreen):
    pass

class Archive(MDScreen):
    pass

class jee(MDApp):
    def backarc(self):
        self.sm.transition.direction = 'right'
        self.sm.current = 'menu'
    def nextaqf(self,arg):
        self.aq = self.aqchange()
        print(self.aq)
        self.archiveq.source = self.aq[0]
        
        
    def archivef(self,arg):
        self.sm.transition.direction = 'left'
        self.sm.current = 'archive'
        
    def backpra(self):
        self.sm.transition.direction = 'right'
        self.sm.current = 'menu'

        
    def dailypraf(self,arg):
        self.sm.transition.direction = 'left'

        self.sm.current = 'pratice'

    def nextqf(self,arg):
        self.no = self.no +1

        self.q = self.qchange()
        self.question.source=self.q[0]
        self.optionA.text='A. '+self.q[1]
        self.optionB.text='B. '+self.q[2]
        self.optionC.text='C. '+self.q[3]
        self.optionD.text='D. '+self.q[4]
        self.nextq.disabled = True
        self.optionA.text_color = (0,0,1,1)
        self.optionB.text_color = (0,0,1,1)
        self.optionC.text_color = (0,0,1,1)
        self.optionD.text_color = (0,0,1,1)
        self.ansbut.disabled = True
        self.anslabel.source = self.q[6]
        if self.ma == 0 or self.mb == 0 or self.mc == 0 or self.md ==0:
            pass
        else:
            self.mark = self.mark + 1
        self.accuracy = str((self.mark*100)//(self.no-1))
        self.accuracytxt.text = 'ACCURACY : '+self.accuracy + ' %'
        if int(self.accuracy) <= 40:
            self.accuracytxt.color = (1,0,0,1)
        elif int(self.accuracy) >40 and int(self.accuracy) <= 70:
            self.accuracytxt.color = (0.5,0.75,0,1)
        elif int(self.accuracy) >70:
            self.accuracytxt.color = (0,1,0,1)


        self.ma = 1
        self.mb = 1
        self.mc = 1
        self.md = 1
    

    def backans(self):
        self.sm.current = 'pratice'
        self.sm.transition.direction = 'right'
    def ansscreenf(self,arg):
        self.sm.current = 'answer'
        self.sm.transition.direction = 'left'
    def optionaf(self,arg):
        if q[5] == 'A':
            self.optionA.text_color = (0,1,0,1)
            self.nextq.disabled = False
            self.ansbut.disabled = False
            self.ma = 1


        else:
            self.optionA.text_color = (1,0,0,1)
            self.ansbut.disabled = False
            self.ma = 0

    def optionbf(self,arg):
        if q[5] == 'B':
            self.optionB.text_color = (0,1,0,1)
            self.nextq.disabled = False
            self.ansbut.disabled = False
            self.mb = 1

            
        else:
            self.optionB.text_color = (1,0,0,1)
            self.ansbut.disabled = False
            self.mb = 0

    def optioncf(self,arg):
        if q[5] == 'C':
            self.optionC.text_color = (0,1,0,1)
            self.nextq.disabled = False
            self.ansbut.disabled = False
            self.mc = 1


        else:
            self.optionC.text_color = (1,0,0,1)
            self.ansbut.disabled = False
            self.mc = 0


    def optiondf(self,arg):
        if q[5] == 'D':
            self.optionD.text_color = (0,1,0,1)
            self.nextq.disabled = False
            self.ansbut.disabled = False
            self.md = 1


        else:
            self.optionD.text_color = (1,0,0,1)
            self.ansbut.disabled = False
            self.md = 0


    #MAIN FUNCTION

    #!!!!!!!!!!!!!!!!!!!!!!!!
    def build(self):
        #variables
        global q,qchange,mark,ma,mb,mc,md,accuracy,no,na,aq,aqchange
        self.aqchange = aqchange
        self.na = na
        self.aq = aq
        self.q = q
        self.qchange = qchange
        self.mark = mark
        self.ma = ma
        self.mb = mb
        self.mc = mc
        self.md = md
        self.accuracy = accuracy
        self.no = no

        #screens
        self.sm = ScreenManager()
        menu = Menu(name ='menu')
        menu.md_bg_color = 0,102/255,1,1
        pratice = Pratice(name = 'pratice')
        answer = Answer(name = 'answer')
        archive = Archive(name = 'archive')
    
        
        self.sm.add_widget(menu)
        self.sm.add_widget(pratice)
        self.sm.add_widget(answer)
        self.sm.add_widget(archive)


        #menu widgets
        box1 = MDBoxLayout(orientation = 'vertical')
        
        grid1 = MDGridLayout(spacing = 15,cols =2 , size_hint = (0.85,0.75),pos_hint = {'center_x':0.5,'center_y':0.5})
        card1 = Builder.load_string(cardt)
        card1.add_widget(MDLabel(text = 'DAILY PRATICE',halign = 'center', theme_text_color ="Secondary"))
        card1.add_widget(Image(source = 'target.png'))
        card1.add_widget(MDRaisedButton(text = 'GO',pos_hint = {'center_x':0.5,'center_y':0.5},on_press = self.dailypraf))
        card2 = Builder.load_string(cardt)

        #menu add widgets

        card2.add_widget(MDLabel(text = 'LEARN ARCHIVE',halign = 'center',theme_text_color ="Secondary"))
        card2.add_widget(Image(source = 'book.png'))
        card2.add_widget(MDRaisedButton(text = 'GO',pos_hint = {'center_x':0.5,'center_y':0.5},on_press = self.archivef))
        grid1.add_widget(card1)                 
        grid1.add_widget(card2)
        toolm = MDToolbar(title = 'MENU',pos_hint = {'top' : 1})
        toolm.md_bg_color = 0,102/255,1,1
        box1.add_widget(toolm)
        
        box1.add_widget(grid1)
        menu.add_widget(box1)
        
        
        

        #pratice widgets
        toolpra = MDToolbar(title = 'PRATICE',pos_hint = {'top' : 1})
        toolpra.left_action_items = [['arrow-left',lambda x : self.backpra()]]
        self.ansbut = MDRaisedButton(on_release = self.ansscreenf,text = 'ANSWER' ,pos_hint = {'center_x': 0.7 , 'center_y' : 0.2})

        self.nextq = MDRaisedButton(on_press = self.nextqf,text ='NEXT',pos_hint = {'center_x': 0.3 , 'center_y' : 0.2})
        self.nextq.disabled = True
        self.question = Image(source = self.q[0],size_hint_x = (0.9),size_hint_y = (0.4),pos_hint = {'center_x': 0.5 , 'center_y' : 0.7},)
        self.optionA = MDRectangleFlatButton(on_release = self.optionaf,text = 'A. '+self.q[1] ,pos_hint = {'center_x': 0.5, 'center_y' : 0.5})
        self.optionB = MDRectangleFlatButton(on_release = self.optionbf,text = 'B. '+self.q[2] ,pos_hint = {'center_x': 0.5 , 'center_y' : 0.43})
        self.optionC = MDRectangleFlatButton(on_release = self.optioncf,text = 'C. '+self.q[3] ,pos_hint = {'center_x': 0.5 , 'center_y' : 0.36})
        self.optionD = MDRectangleFlatButton(on_release = self.optiondf,text = 'D. '+self.q[4] ,pos_hint = {'center_x': 0.5 , 'center_y' : 0.29})
        self.question.padding_x = 20
        self.question.md_bg_color = (0,0,0,20/255)
        self.ansbut.disabled = True
        self.accuracytxt= MDLabel(font_style = 'Caption',text = 'ACCURACY : '+self.accuracy+ ' %',size_hint_x = (0.8),size_hint_y = (0.5),pos_hint = {'center_x': 0.5 , 'center_y' : 0.15})
        self.question.allow_stretch = True
        

        #pratice add widgets
        pratice.add_widget(toolpra)
        pratice.add_widget(self.question)
        pratice.add_widget(self.optionA)
        pratice.add_widget(self.optionB)
        pratice.add_widget(self.optionC)
        pratice.add_widget(self.optionD)
        pratice.add_widget(self.nextq)
        pratice.add_widget(self.ansbut)
        pratice.add_widget(self.accuracytxt)
        
        
        #answer widgets
        self.anslabel= Image(source = self.q[6],size_hint_x = 0.8,size_hint_y = 0.7,pos_hint = {'center_x': 0.5 , 'center_y' : 0.5})
        tool = MDToolbar(title = 'ANSWER',pos_hint = {'top' : 1})
        tool.left_action_items = [['arrow-left',lambda x : self.backans()]]
        self.anslabel.allow_stretch = True
        
        #answer add widgets
        answer.add_widget(self.anslabel)
        answer.add_widget(tool)

        #archive widgets
        artool = MDToolbar(title = 'ARCHIVE',pos_hint = {'top' : 1})
        artool.left_action_items = [['arrow-left',lambda x : self.backarc()]]

        self.archiveq = Image(source = self.aq[0],size_hint_x = (0.9),size_hint_y = (0.5),pos_hint = {'center_x': 0.5 , 'center_y' : 0.6})
        self.nextaq = MDRaisedButton(on_press = self.nextaqf,text ='NEXT',pos_hint = {'center_x': 0.5 , 'center_y' : 0.2})


        #archive add widgets
        archive.add_widget(self.archiveq)
        archive.add_widget(self.nextaq)
        archive.add_widget(artool)

        
        #ads
        self.ads = KivMob(TestIds.APP)
        self.ads.new_banner(TestIds.BANNER, top_pos=False)
        self.ads.request_banner()
        self.ads.show_banner()
        self.ads.new_interstitial(TestIds.INTERSTITIAL)
        self.ads.request_interstitial()
        
        return self.sm


jee().run()





    
