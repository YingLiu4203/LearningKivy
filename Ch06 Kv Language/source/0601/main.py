from kivy.app import App
from kivy.factory import Factory


class KvDemoApp(App):
    def build(self):
        my_widget = Factory.MyWidget()
        return my_widget


if __name__ == '__main__':
    KvDemoApp().run()
