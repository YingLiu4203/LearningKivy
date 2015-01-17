# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class DemoLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(DemoLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'

        click_button = Button(text="Click Me")
        click_button.size_hint_y = None
        click_button.height = '60dp'
        click_button.bind(on_press=self.on_button_press)
        self.add_widget(click_button)

        output_label = TextInput(text="Event Output")
        self.add_widget(output_label)

    def on_button_press(self, widget):
        print 'in handler'
        message = "Button Information \n"

        message += "Events: \n"
        button_events = widget.events()
        events_str = ', '.join(button_events)
        message += events_str + "\n"

        message += "\nProperties: \n"
        button_properties = widget.properties()
        properties_str = ', '.join(button_properties)
        message += properties_str + "\n"

        self.children[0].text = message


class EventDemoApp(App):
    def build(self):
        return DemoLayout()

if __name__ == '__main__':
    EventDemoApp().run()
