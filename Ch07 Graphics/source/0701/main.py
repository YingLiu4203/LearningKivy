# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics.vertex_instructions import Rectangle, Line
from kivy.graphics import Color


class MyWidget(Widget):
    def __init__(self, **kwargs):
        super(MyWidget, self).__init__(**kwargs)
        with self.canvas:
            # Color(1, 0, 0, .5, mode='rgba')
            self.rect = Rectangle(pos=self.pos, size=self.size)
            Color(0, 1, 0, .5, mode='rgba')
            Line(points=(10, 10, 200, 200, 300, 300))

            # lets draw a semi-transparent red square

            #Rectangle(pos=self.pos, size=self.size)

        self.bind(pos=self.update_rect)
        self.bind(size=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size


class KvDemoApp(App):
    def build(self):
        return MyWidget()


if __name__ == '__main__':
    KvDemoApp().run()

