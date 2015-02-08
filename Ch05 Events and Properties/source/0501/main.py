# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.clock import Clock

count = 0
def my_callback(dt):
    global count
    count += 1
    if count == 10:
        print 'Last call of my callback, bye bye !'

        # schedule once in 10 seconds later
        # Clock.schedule_once(my_callback, 10)

        # cancel the schedule event
        return False

        # another method to unschedule
        # Clock.unschedule(my_callback)

        # trigger an event in the next frame
        # trigger = Clock.create_trigger(my_callback)
        # trigger()

    print 'My callback is called'


class HelloWorldApp(App):
    pass

if __name__ == '__main__':

    Clock.schedule_interval(my_callback, 1 / 30.0)

    HelloWorldApp().run()
