# -*- coding: utf-8 -*-

# code copied from http://kivy.org/docs/guide/events.html

from kivy.app import App
from kivy.event import EventDispatcher


class MyEventDispatcher(EventDispatcher):
    def __init__(self, **kwargs):
        self.register_event_type('on_test')
        super(MyEventDispatcher, self).__init__(**kwargs)

    def on_test(self, *args):
        pass


def my_callback(value, *args):
    print "Hello, I got an event!", args


class HelloWorldApp(App):
    pass

if __name__ == '__main__':

    ev = MyEventDispatcher()
    ev.bind(on_test=my_callback)
    ev.dispatch('on_test', 'test_message')

    HelloWorldApp().run()
