# -*- coding: utf-8 -*-

# code copied from http://kivy.org/docs/guide/events.html

from kivy.app import App
from kivy.clock import Clock
from kivy.uix.widget import Widget


class MyWidget(Widget):
    def __init__(self, **kwargs):
        super(MyWidget, self).__init__(**kwargs)
        self.register_event_type('on_custom_event')

    def trigger_custom_event(self, *args):
        self.dispatch('on_custom_event', 'test message')

    def on_custom_event(self, *args):
        pass


def on_custom_callback(*args):
    print 'my on_custom_event is called with {}'.format(args)


class HelloWorldApp(App):
    def build(self):
        w = MyWidget()
        w.bind(on_custom_event=on_custom_callback)
        Clock.schedule_once(w.trigger_custom_event, 3)

        return w


if __name__ == '__main__':

    HelloWorldApp().run()
