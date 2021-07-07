from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen,ScreenManager
Builder.load_file('design.kv')

class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current="signup_screen"

class RootWidget(ScreenManager):
    pass

class SignUpScreen(Screen):
    def back(self):
        self.manager.current="login_screen"

class Currency(App):
    def build(self):
        return RootWidget()

if __name__=="__main__":
    Currency().run()
