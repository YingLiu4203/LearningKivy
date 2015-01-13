# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button


class SizePositionApp(App):
    def build(self):
        root_widget = Widget()
        button_1 = Button(pos=(100, 100))
        button_2 = Button(pos=(100, 300))
        root_widget.add_widget(button_1)
        root_widget.add_widget(button_2)
        return root_widget


if __name__ == '__main__':
    SizePositionApp().run()
