# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty, NumericProperty


class CustomBtn(Widget):
    pressed = ListProperty([0, 0])
    demo_prop = NumericProperty(0)

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.pressed = touch.pos
            return True
        return super(CustomBtn, self).on_touch_down(touch)

    def on_pressed(self, instance, pos):
        print 'pressed at {pos}'.format(pos=pos)

    def on_demo_prop(self, instance, value):
        print 'on_demo_prop value changed to {}'.format(value)

class RootWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        self.add_widget(Button(text='btn 1'))
        cb = CustomBtn()
        cb.bind(pressed=self.btn_pressed)
        cb.bind(demo_prop=self.demo_changed)
        self.add_widget(cb)
        self.cb = cb
        self.add_widget(Button(text='btn 2'))

    def btn_pressed(self, instance, pos):
        print 'pos: printed from root widget: {pos}'.format(pos=pos)
        self.cb.demo_prop += 1

    def demo_changed(self, instance, value):
        print 'demo changed to {}'.format(value)


class EventDemoApp(App):
    def build(self):
        return RootWidget()

if __name__ == '__main__':
    EventDemoApp().run()
