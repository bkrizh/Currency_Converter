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
    def log_in(self,uname,pwrd):
        with open("user_detail.json") as file:
            user=json.load(file)
        if uname in user and user[uname]['password']==pwrd:
            self.manager.transition.direction='left'
            self.manager.current="log_in_success"
        else:
            self.ids.log_err.text="Wrong username or Password"

class RootWidget(ScreenManager):
    pass

class SignUpScreen(Screen):
    def back(self):
        self.manager.transition.direction='right'
        self.manager.current="login_screen"

    def add_user(self,uname,pwrd):
        with open('user_detail.json') as file:
            user=json.load(file)

        user[uname]={'username':uname,'password':pwrd,
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

class Currency(App):
    def build(self):
        return RootWidget()

if __name__=="__main__":
    Currency().run()
