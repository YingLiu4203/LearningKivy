from kivy.app import  App
from kivy.uix.boxlayout import BoxLayout


class MyWidget(BoxLayout):
    pass


class KvDemoApp(App):
    def build(self):
        return MyWidget()


if __name__ == '__main__':
    KvDemoApp().run()
