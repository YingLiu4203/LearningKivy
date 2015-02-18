from kivy.app import App
from kivy.factory import Factory
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

class MyFirstWidget(BoxLayout):

    txt_inpt = ObjectProperty(None)

    def check_status(self, btn):
        print('button state is: {state}'.format(state=btn.state))
        print('text input text is: {txt}'.format(txt=self.txt_inpt))


class KvDemoApp(App):
    def build(self):
        return MyFirstWidget()


if __name__ == '__main__':
    KvDemoApp().run()
