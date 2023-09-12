from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import Color
from kivy.uix.floatlayout import FloatLayout
import requests
import json


#my custom layouts for code re-use


class IndexScreen(Screen):
    def __init__(self, **kw):
        super(IndexScreen, self).__init__(**kw)
    
    def starting_page(self):
        self.manager.current = 'register'


class RegisterScreen(Screen):
    def __init__(self, **kw):
        super(RegisterScreen, self).__init__(**kw)
    
    def create(self):
        name = self.username.text
        ward = self.ward_name.text
        password = self.password.text
        password2 = self.password2.text
        
        credentials = {}
        
        if name:
            credentials['username'] = name
        else:
            print(ValueError('please enter your username'))
            
        if ward:
            credentials['ward'] = ward
        else:
            print(ValueError('please enter correct ward name'))
        
        if password:
            if password == password2:
                credentials['password'] = password
                req = requests.post('http://127.0.0.1:8000/roster/registration/', json=credentials)
                if req.status_code == 201:
                    self.manager.current = 'thank'
            else:
                print(ValueError('unmatch password'))
        else:
            print(ValueError('password cannot be null'))
        
    def sign_in(self):
        print('Now redirect you to the sign in page')
        self.manager.current = 'login'


class ThankScreen(Screen):
    def __init__(self, **kw):
        super(ThankScreen, self).__init__(**kw)
    
    def back(self):
        self.manager.current = 'login'

class SettingsScreen(Screen):
    pass


class LoginScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
    
    def sign_up(self):
        self.manager.current = 'register'
    
    def sign_in(self):
        username = self.username.text
        password = self.password.text
        
        credentials = {}
        if username and password:
            credentials['username'] = username
            credentials['password'] = password
            req = requests.post('http://127.0.0.1:8000/roster/login/', json=credentials)
            if req.status_code == 200:
                self.manager.current = 'home'
        else:
            if not username:
                self.username_error.text = 'required'
            else:
                self.username_error.text = ''
            if not password:
                self.password_error.text = 'required'


class HomeScreen(Screen):
    pass


class RosterApp(App):
    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        sm.add_widget(IndexScreen(name='index'))
        sm.add_widget(SettingsScreen(name='settings'))
        sm.add_widget(RegisterScreen(name='register'))
        sm.add_widget(ThankScreen(name='thank'))
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(HomeScreen(name='home'))
        return sm

if __name__ == '__main__':
    RosterApp().run()