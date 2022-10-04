from telnetlib import STATUS
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDTopAppBar

################ Function ###############
class ConverterApp(MDApp):
    def flip(self):
        if self.state == 0:
            self.state = 1
            self.topappbar.title = 'Decimal To Binary'
            self.input.hint_text = 'Enter a decimal number'
        else:
            self.state = 0
            self.topappbar.title = 'Binary To Decimal'
            self.input.hint_text = 'Enter a binary number'
        
        self.converted.text = ''
        self.label.text = ''
        
    def clear(self, *args):
        self.input.text = ''
        self.converted.text = ''
        self.label.text = ''
        
    def convert(self, *args):
        # function to find the decimal / binary equivalent
        try:
            if '.' not in self.input.text:
                if self.state == 0:
                    val = str(int(self.input.text, 2))
                    self.label.text = 'in decimal is:'
                else:   
                    val = bin(int(self.input.text)) [2:]
                    self.label.text = 'in binary is:'
                self.converted.text = val
            else:
                whole, fract = self.input.text.split('.')
                
                if self.state == 0:
                    whole = int(whole, 2)
                    floating = 0
                    for idx, digit in enumerate(fract):
                        floating += int(digit)*2**(-(idx+1))
                    self.label.text = 'in decimal is:'
                    self.converted.text = str(whole + floating)
                else:
                    decimal_places = 10
                    whole = bin(int(whole))[2:]
                    fract = float('0.'+fract)
                    floating = []
                    for i in range(decimal_places):
                        if fract*2 < 1:
                            floating.append('0')
                            fract *= 2
                        elif fract*2 > 1:
                            floating.append('1')
                            fract = fract*2 - 1
                        elif fract*2 == 1.0:
                            floating.append('1')
                            break
                    self.label.text = 'in binary is:'
                    self.converted.text = whole + '.' + ''.join(floating)
        except ValueError:
            # if the user-provide value is invalid
            self.converted.text = ''
            if self.state == 0:
                # binary to decimal
                self.label.text = 'please enter a valid binary number'
            else:
                # decimal to binary
                self.label.text = 'please enter a valid decimal number'
                
################ Layout ###############
    def build(self):
        self.state = 0
        self.theme_cls.theme_style = "Dark"
        #self.theme_cls.accent_palette = "Red"
        self.theme_cls.primary_palette = 'Amber'
        screen = MDScreen()
        
        # ['Red', 'Pink', 'Purple', 'DeepPurple', 'Indigo', 'Blue', 'LightBlue', 
        # 'Cyan', 'Teal', 'Green', 'LightGreen', 'Lime', 'Yellow', 'Amber', 
        # 'Orange', 'DeepOrange', 'Brown', 'Gray', 'BlueGray']
        
        # TopAppBar
        self.topappbar = MDTopAppBar(
            title='Binary To Decimal',
            pos_hint= {'top': 1},
            
            right_action_items = [
            ['rotate-3d-variant', lambda x: self.flip()]])
           
        screen.add_widget(self.topappbar)
        
        # Logo
        self.image = Image(
            source= 'logo.png',
            pos_hint= {'center_x': 0.5,'center_y': 0.7},
           
        )
        screen.add_widget(self.image)
        
        # Input field
        self.input = MDTextField(
            text='',
            hint_text= "Enter a binary number",
            halign='center',
            helper_text_mode= "on_focus",
            size_hint= (0.8, 1),
            
            pos_hint= {'center_x': 0.5,'center_y': 0.5},
            font_size= 25
        )
        screen.add_widget(self.input)
    
        # Label
        self.label = MDLabel(
            halign='center',
            pos_hint= {'center_x': 0.5,'center_y': 0.35},
            
            theme_text_color = 'Secondary'
        )
        screen.add_widget(self.label)
        
        self.converted = MDLabel(
            halign='center',
            pos_hint= {'center_x': 0.5,'center_y': 0.3},
            theme_text_color = 'Primary',
            font_style = 'H5'
        )
        screen.add_widget(self.converted)
        
        # 'convert' button
        self.button_converted = MDFillRoundFlatButton(
            text= 'C O N V E R T',
            font_size=17,
            pos_hint= {'center_x': 0.4,'center_y': 0.15},
           
            on_press= self.convert
        )
        screen.add_widget(self.button_converted)
        
        # 'clear' button
        self.button_cleared = MDFillRoundFlatButton(
            text= 'C L E A R',
            font_size=17,
            pos_hint= {'center_x': 0.6,'center_y': 0.15},
            on_press= self.clear
        )
        screen.add_widget(self.button_cleared)
        
        return screen

ConverterApp().run()