from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen,ScreenManager
Builder.load_file('core.ky')

class Login(Screen):
    pass

class RootWidget(ScreenManager):
    pass

class Currency(App):
    def build(self):
        return RootWidget()

if __name__=="__main__":
    Currency().run()
