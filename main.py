from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen,ScreenManager
import json
from datetime import datetime

Builder.load_file('design.kv')

class LoginScreen(Screen):
    def sign_up(self):
        self.manager.transition.direction='left'
        self.manager.current="signup_screen"
    def forgot(self):
        self.manager.transition.direction='right'
        self.manager.current="forgot_password"        
    def log_in(self,uname,pwrd):
        with open("user_detail.json") as file:
            user=json.load(file)
        if uname in user and user[uname]['password']==pwrd:
            self.manager.transition.direction='left'
            self.manager.current="log_in_success"
        else:
            self.ids.log_err.text="Неверный логин или пароль"

class RootWidget(ScreenManager):
    pass

class SignUpScreen(Screen):
    def back(self):
        self.manager.transition.direction='right'
        self.manager.current="login_screen"

    def add_user(self,fname,lname,uname,pwrd):
        with open('user_detail.json') as file:
            user=json.load(file)

        user[uname]={'first_name':fname,'last_name':lname,'username':uname,'password':pwrd,
        'created':datetime.now().strftime('%Y-%m-%d %H-%M-%S')}  

        with open('user_detail.json','w') as file:
            json.dump(user,file)  

        self.manager.transition.direction='left'
        self.manager.current="sign_up_success"

class SignUpSuccessful(Screen):
    def back_to_login(self):
        self.manager.transition.direction='right'
        self.manager.current="login_screen"

class LoginSuccessful(Screen):
    def log_out(self):
        self.manager.transition.direction='right'
        self.manager.current="login_screen"

    def convert(self,amt,curr):
        val=0
        if curr=='U.S. Dollar (USD)':
            val=88.83
        elif curr=='European Euro (EUR)':
            val=96.92
        elif curr=='British Pound (GBP)':
            val=112.85
        elif curr=='Canadian Dollar (CAD)':
            val=67.06
        elif curr=='Japanese Yen (JPY)':
            val=0.62
        elif curr=='Swiss Franc (CHF)':
            val=99.28
        elif curr=='Australian/New Zealand Dollar':
            val=59.18
        try:
            amt=int(amt)
            inr=amt*val
            self.ids.currency.text=f'[b][u][font=times]INR : {inr}[/font][/u][/b]'
        except:
            self.ids.currency.text='Введите числовое значение в поле'

class ForgotPassword(Screen):
    def back_to_login(self):
        self.manager.transition.direction='left'
        self.manager.current="login_screen"  
    def find_password(self,uname):
        with open('user_detail.json') as file:
            user=json.load(file)
        if uname in user:
            self.ids.findpassword.text='Ваш пароль : '+user[uname]['password']
        else:
           self.ids.findpassword.text='Не можем найти ваш юзернейм'

class Currency(App): 
    def build(self):
        return RootWidget()

if __name__=="__main__":
    Currency().run()
