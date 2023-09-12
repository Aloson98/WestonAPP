from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix import boxlayout, floatlayout, button, label
from kivy.graphics import Color
from kivy.uix.image import Image


class CircularButton(button.ButtonBehavior, label.Label):
    def add_list(self):
        print('add list button clicked')


class IndexWidget(Widget):
    pass


class RegisterWidget(Widget):
    def __init__(self, **kwargs):
        super(RegisterWidget, self).__init__(**kwargs)
        #self.ward_name.text = 'ward name'
    
    def create(self):
        name = self.username.text
        
        if name != 'username':
            print(f'thank you {name} for registering, hope you are going to enjoy the AI')
        else:
            print(ValueError('please enter your username'))
    
    def sign_in(self):
        print('Now redirect you to the sign in page')
        self.manager.current = ''


class ThankWidget(Widget):
    pass


class LoginWidget(Widget):
    def __init__(self, **kwargs):
        super(LoginWidget, self).__init__(**kwargs)


class HomeWidget(Widget):
    pass


class EmptyMembersWidget(Widget):
    def __init__(self, **kwargs):
        super(EmptyMembersWidget, self).__init__(**kwargs)
    
    def add_list(self):
        print('add list button clicked')


class AddWidget(Widget):
    def __init__(self, **kwargs):
        super(AddWidget, self).__init__(**kwargs)
    
    def adding_list(self):
        name = label.Label(text='[color=#000afa]aloson[/color]', size_hint=(0.5,0.5), font_size='18sp', markup=True)
        self.name_list.add_widget(name)
        img = Image(source='./Delete_icon.png', size=(0.5, 0.5))
        self.name_list.add_widget(img)
        
        
        print('name added')

class Roster2App(App):
    def build(self):
        return AddWidget()

Roster2App().run()