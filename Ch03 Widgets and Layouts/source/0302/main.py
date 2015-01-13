# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label


class HelloWorldApp(App):
    def build(self):
        layout = GridLayout(cols=2)
        hello_label = Label(text="Hello World2")
        best_label = Label(text="Best Regards")
        layout.add_widget(hello_label)
        layout.add_widget(best_label)
        return layout

if __name__ == '__main__':
    HelloWorldApp().run()
