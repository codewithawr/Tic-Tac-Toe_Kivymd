from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.snackbar import BaseSnackbar
from kivymd.uix.label import MDLabel
from kivymd.uix.snackbar import Snackbar

from kivy.properties import StringProperty, NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import dp
from kivy.core.window import Window
from kivy.lang import Builder

import random


class Content(BoxLayout):
    pass


class CustomSnackbar(BaseSnackbar):
    text = StringProperty(None)
    icon = StringProperty(None)
    font_size = NumericProperty("15sp")

class main_app(MDApp):
    dialog = None
    option = ['X','O']
    player_choise = ''
    computer_choise = ''
    player_velu = 0
    computer_velu = 0
    round_count = 1
    def build(self):
        return Builder.load_file('main.kv')

    def on_start(self):
        all_butns = self.root.ids.main_play.children
        self.ttt_buttons = []
        self.ttt_buttons_taken = []
        
        for i in range(len(all_butns)):
            self.ttt_buttons.append(all_butns[-i-1])
            self.ttt_buttons_taken.append(all_butns[-i-1])


        if not self.dialog:
            self.dialog = MDDialog(
                title="Chose your Simbol:",
                type="custom",
                content_cls=Content()
            )
        self.dialog.open()
        # self.root.ids.Player_count.font_style = "H4"
        # self.root.ids.computer_count.font_style = "H4"

    def save_slaction(self, choise):
        self.option = ['X','O']
        self.player_choise = choise
        self.dialog.dismiss()
        self.option.remove(choise)
        self.computer_choise=self.option[0]

        self.root.ids.Player_count.text = self.player_choise+'/'+str(self.player_velu)
        self.root.ids.computer_count.text = self.computer_choise+'/'+str(+self.computer_velu)
    

    def cleare(self, obj, for_):
        self.snackbar.dismiss()
        if for_ == 'Mach':
            self.round_count = 1
            all_butns = self.root.ids.main_play.children
            
            self.ttt_buttons = []
            self.ttt_buttons_taken = []
            
            for i in range(len(all_butns)):
                self.ttt_buttons.append(all_butns[-i-1])
                self.ttt_buttons_taken.append(all_butns[-i-1])

            if self.player_velu > self.computer_velu:
                who_won = f'YOU({self.player_choise})'

            elif self.computer_velu > self.player_velu:
                who_won = self.computer_choise
            
            elif self.computer_velu == self.player_velu:
                who_won = 'no one'
            
            if self.dialog:
                self.dialog = MDDialog(
                    title=f"{who_won} won the match Chose your Simbol for next:",
                    type="custom",
                    content_cls=Content()
                )
            self.dialog.open()

            self.player_velu = 0
            self.computer_velu = 0


        for i in self.ttt_buttons:
            i.text = ''
        self.ttt_buttons_taken == self.ttt_buttons
        all_butns = self.root.ids.main_play.children
        self.ttt_buttons = []
        self.ttt_buttons_taken = []
        
        for i in range(len(all_butns)):
            self.ttt_buttons.append(all_butns[-i-1])
            self.ttt_buttons_taken.append(all_butns[-i-1])



    def check_lind(self):
        self.k=0
        def win(who):
            self.k=self.k+1
            if self.k == 1:
                if who == self.player_choise:
                    self.player_velu = self.player_velu+1
                    self.root.ids.Player_count.text = self.player_choise+'/'+str(self.player_velu)
                elif who == self.computer_choise:
                    self.computer_velu = self.computer_velu+1
                    self.root.ids.computer_count.text = self.computer_choise+'/'+str(self.computer_velu)
                
                if self.round_count <= 2:
                    self.snackbar = CustomSnackbar(
                        text=f"{who} was Won",
                        icon="information",
                        snackbar_x="10dp",
                        snackbar_y="10dp",
                        auto_dismiss=False,
                        bg_color=(0, 0, 1, .8),
                        buttons=[MDFlatButton(text="Next Round", text_color=(1, 1, 1, 1), on_release = lambda x: self.cleare(x, 'Round'))]
                    )
                    self.snackbar.size_hint_x = (
                        Window.width - (self.snackbar.snackbar_x * 2)
                    ) / Window.width
                    self.snackbar.open()
                elif self.round_count == 3:
                    self.snackbar = CustomSnackbar(
                        text=f"{who} was Won for next match",
                        icon="information",
                        snackbar_x="10dp",
                        snackbar_y="10dp",
                        auto_dismiss=False,
                        bg_color=(0, 0, 1, .8),
                        buttons=[MDFlatButton(text="Next Mach", text_color=(1, 1, 1, 1), on_release = lambda x: self.cleare(x, 'Mach'))]
                    )
                    self.snackbar.size_hint_x = (
                        Window.width - (self.snackbar.snackbar_x * 2)
                    ) / Window.width
                    self.snackbar.open()

                self.round_count = self.round_count+1
                


        for i in range(len(self.ttt_buttons_taken)):
            if i == 0:
                if self.ttt_buttons_taken[i] == self.ttt_buttons_taken[i+1] and self.ttt_buttons_taken[i] == self.ttt_buttons_taken[i+2]:
                    win(self.ttt_buttons_taken[i])
                    return True

                if self.ttt_buttons_taken[i] == self.ttt_buttons_taken[i+3] and self.ttt_buttons_taken[i] == self.ttt_buttons_taken[i+6]:
                    win(self.ttt_buttons_taken[i])
                    return True

                if self.ttt_buttons_taken[i] == self.ttt_buttons_taken[i+4] and self.ttt_buttons_taken[i] == self.ttt_buttons_taken[i+8]:
                    win(self.ttt_buttons_taken[i])
                    return True



            elif i == 1:
                if self.ttt_buttons_taken[i] == self.ttt_buttons_taken[i+3] and self.ttt_buttons_taken[i] == self.ttt_buttons_taken[i+6]:
                    win(self.ttt_buttons_taken[i])
                    return True


            elif i == 2:
                if self.ttt_buttons_taken[i] == self.ttt_buttons_taken[i+2] and self.ttt_buttons_taken[i] == self.ttt_buttons_taken[i+4]:
                    win(self.ttt_buttons_taken[i])
                    return True
                    
                if self.ttt_buttons_taken[i] == self.ttt_buttons_taken[i+3] and self.ttt_buttons_taken[i] == self.ttt_buttons_taken[i+6]:
                    win(self.ttt_buttons_taken[i])
                    return True
                    


            elif i == 3:
                if self.ttt_buttons_taken[i] == self.ttt_buttons_taken[i+1] and self.ttt_buttons_taken[i] == self.ttt_buttons_taken[i+2]:
                    win(self.ttt_buttons_taken[i])
                    return True


            elif i == 6:
                if self.ttt_buttons_taken[i] == self.ttt_buttons_taken[i+1] and self.ttt_buttons_taken[i] == self.ttt_buttons_taken[i+2]:
                    win(self.ttt_buttons_taken[i])
                    return True

            else:
                uko=[]
                for j in self.ttt_buttons_taken:
                    if j == self.computer_choise or j == self.player_choise:
                        uko.append(True)
                if len(uko) >=9:
                    win("no one")

        return False

    def pressed(self,button):
        for i in range(len(self.ttt_buttons_taken)):
            if self.ttt_buttons_taken[i] == button:
                self.ttt_buttons_taken[i] = self.player_choise
                if button.text == '':
                    button.text = self.player_choise

                if self.check_lind() == False:
                    self.computer_tern()

    def computer_tern(self):
        self.p = 10
        self.c = 10
        def inty(wher, from_):
            if from_ == self.computer_choise:
                self.c = wher
                # self.ttt_buttons[wher].text = self.computer_choise
                # self.ttt_buttons_taken[wher] = self.computer_choise
                # self.check_lind()
            elif from_ == self.player_choise:
                self.p = wher

        for k,j in enumerate(self.ttt_buttons_taken):
            if k == 0:
                if self.ttt_buttons_taken[k] == self.ttt_buttons_taken[k+1] and self.ttt_buttons[k+2].text == '':
                    inty(k+2,j)
                    
            
                elif self.ttt_buttons_taken[k] == self.ttt_buttons_taken[k+2] and self.ttt_buttons[k+1].text == '':
                    inty(k+1,j)
                    
            

                elif self.ttt_buttons_taken[k] == self.ttt_buttons_taken[k+3] and self.ttt_buttons[k+6].text == '':
                    inty(k+6,j)
                    
            
                elif self.ttt_buttons_taken[k] == self.ttt_buttons_taken[k+6] and self.ttt_buttons[k+3].text == '':
                    inty(k+3,j)
                    


                elif self.ttt_buttons_taken[k] == self.ttt_buttons_taken[k+4] and self.ttt_buttons[k+8].text == '':
                    inty(k+8,j)
                
                elif self.ttt_buttons_taken[k] == self.ttt_buttons_taken[k+8] and self.ttt_buttons[k+4].text == '':
                    inty(k+4,j)
                    
            
            elif k == 1:
                if self.ttt_buttons_taken[k] == self.ttt_buttons_taken[k+3] and self.ttt_buttons[k+6].text == '':
                    inty(k+6,j)
                    
            
                elif self.ttt_buttons_taken[k] == self.ttt_buttons_taken[k+6] and self.ttt_buttons[k+3].text == '':
                    inty(k+3,j)
                    

            elif k == 2:
                if self.ttt_buttons_taken[k] == self.ttt_buttons_taken[k-1] and self.ttt_buttons[k-2].text == '':
                    inty(k-2,j)
                    
            
                elif self.ttt_buttons_taken[k] == self.ttt_buttons_taken[k-2] and self.ttt_buttons[k-1].text == '':
                    inty(k-1,j)
                    
            

                elif self.ttt_buttons_taken[k] == self.ttt_buttons_taken[k+2] and self.ttt_buttons[k+4].text == '':
                    inty(k+4,j)
                    
            
                elif self.ttt_buttons_taken[k] == self.ttt_buttons_taken[k+4] and self.ttt_buttons[k+2].text == '':
                    inty(k+2,j)
                    


                elif self.ttt_buttons_taken[k] == self.ttt_buttons_taken[k+3] and self.ttt_buttons[k+6].text == '':
                    inty(k+6,j)
                    
                
                elif self.ttt_buttons_taken[k] == self.ttt_buttons_taken[k+6] and self.ttt_buttons[k+3].text == '':
                    inty(k+3,j)
                    
            
            elif k == 3:
                if self.ttt_buttons_taken[k] == self.ttt_buttons_taken[k+1] and self.ttt_buttons[k+2].text == '':
                    inty(k+2,j)
                    
            
                elif self.ttt_buttons_taken[k] == self.ttt_buttons_taken[k+2] and self.ttt_buttons[k+1].text == '':
                    inty(k+1,j)
                    
            
            elif k == 5:
                if self.ttt_buttons_taken[k] == self.ttt_buttons_taken[k-1] and self.ttt_buttons[k-2].text == '':
                    inty(k-2,j)
                    
            
                elif self.ttt_buttons_taken[k] == self.ttt_buttons_taken[k-2] and self.ttt_buttons[k-1].text == '':
                    inty(k-1,j)
                    
            
            elif k == 6:
                if self.ttt_buttons_taken[k] == self.ttt_buttons_taken[k-3] and self.ttt_buttons[k-6].text == '':
                    inty(k-6,j)
                    
            
                elif self.ttt_buttons_taken[k] == self.ttt_buttons_taken[k-6] and self.ttt_buttons[k-3].text == '':
                    inty(k-3,j)
                    
            

                elif self.ttt_buttons_taken[k] == self.ttt_buttons_taken[k-2] and self.ttt_buttons[k-4].text == '':
                    inty(k-4,j)
                    
            
                elif self.ttt_buttons_taken[k] == self.ttt_buttons_taken[k-4] and self.ttt_buttons[k-2].text == '':
                    inty(k-2,j)
                    


                elif self.ttt_buttons_taken[k] == self.ttt_buttons_taken[k+1] and self.ttt_buttons[k+2].text == '':
                    inty(k+2,j)
                    
                
                elif self.ttt_buttons_taken[k] == self.ttt_buttons_taken[k+2] and self.ttt_buttons[k+1].text == '':
                    inty(k+1,j)
                    
            
            elif k == 7:
                if self.ttt_buttons_taken[k] == self.ttt_buttons_taken[k-3] and self.ttt_buttons[k-6].text == '':
                    inty(k-6,j)
                    
            
                elif self.ttt_buttons_taken[k] == self.ttt_buttons_taken[k-6] and self.ttt_buttons[k-3].text == '':
                    inty(k-3,j)
                    
            
            elif k == 8:
                if self.ttt_buttons_taken[k] == self.ttt_buttons_taken[k-3] and self.ttt_buttons[k-6].text == '':
                    inty(k-6,j)
                    
            
                elif self.ttt_buttons_taken[k] == self.ttt_buttons_taken[k-6] and self.ttt_buttons[k-3].text == '':
                    inty(k-3,j)
                    
            

                elif self.ttt_buttons_taken[k] == self.ttt_buttons_taken[k-4] and self.ttt_buttons[k-8].text == '':
                    inty(k-8,j)
                    
            
                elif self.ttt_buttons_taken[k] == self.ttt_buttons_taken[k-8] and self.ttt_buttons[k-4].text == '':
                    inty(k-4,j)
                    


                elif self.ttt_buttons_taken[k] == self.ttt_buttons_taken[k-1] and self.ttt_buttons[k-2].text == '':
                    inty(k-2,j)
                    
                
                elif self.ttt_buttons_taken[k] == self.ttt_buttons_taken[k-2] and self.ttt_buttons[k-1].text == '':
                    inty(k-1,j)
        if self.c != 10:
            self.ttt_buttons[self.c].text = self.computer_choise
            self.ttt_buttons_taken[self.c] = self.computer_choise
            self.check_lind()
            return
        elif self.c == 10 and self.p != 10:
            self.ttt_buttons[self.p].text = self.computer_choise
            self.ttt_buttons_taken[self.p] = self.computer_choise
            self.check_lind()
            return

        for i in range(8):
            h = random.choice(self.ttt_buttons_taken)
            if h != self.computer_choise and h != self.player_choise:
                h.text=self.computer_choise
                for i in range(len(self.ttt_buttons_taken)):
                    if self.ttt_buttons_taken[i] == h:
                        self.ttt_buttons_taken[i] = self.computer_choise
                
                self.check_lind()
                return

main_app().run()
