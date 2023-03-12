import random

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FallOutTransition, SlideTransition
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen

Builder.load_string('''
<MenuScreen>:
    BoxLayout:
        Button:
            text: 'Go to other screen'
            on_release: root.manager.current = 'other'
<OtherScreen>:
    BoxLayout:
        Button:
            text: 'Go to menu screen'
            on_press: app.change_transition('fallout','left')
            on_release: root.manager.current = 'menu'
''')


class MenuScreen(Screen):
    pass


class OtherScreen(Screen):
    pass


class MyApp(App):
    def __init__(self, screen_manager, **kwargs):
        self.screen_manager = screen_manager
        super(MyApp, self).__init__(**kwargs)

    def build(self):
        return self.screen_manager

    def change_transition(self, transition, direction=None):
        if transition == "fallout":
            self.screen_manager.transition = FallOutTransition()
        if transition == "slide":
            if direction is None:
                directions = ["left", "right"]
                direction = directions[random.randrange(0, 2)]
                self.screen_manager.transition = SlideTransition(direction=direction)
            else:
                self.screen_manager.transition = SlideTransition(direction=direction)


class MyScreen(Screen):
    def add_button(self, on_release):
        button = Button(text="to other")
        button.bind(on_release=self.to_other)
        self.add_widget(button)
        button.size_hint = (0.5, 0.25)
        button.pos_hint = {'center_x': 0.5, 'center_y': 0.5}

    def to_other(self, *args):
        App.get_running_app().change_transition("slide")
        self.parent.current = 'other'


if __name__ == '__main__':
    sm = ScreenManager()
    sm.add_widget(OtherScreen(name='other'))

    def set_other():
        sm.current = 'other'

    my_screen = MyScreen(name='menu')
    my_screen.add_button(set_other())
    # sm.add_widget(OtherScreen(name='other'))
    sm.add_widget(my_screen)
    sm.current = 'other'
    MyApp(sm).run()
