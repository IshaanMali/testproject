from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview import RecycleView
from kivy.properties import ObjectProperty

class ListWidget(RecycleView):

    def update(self):
        self.data = [{'text':str(i)}for i in self.items]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.items = []

class RootWidget(BoxLayout):
    inputButton = ObjectProperty(None)
    inputContent = ObjectProperty(None)
    outputContent = ObjectProperty(None)

    def add_item(self):
        if self.inputContent.text != "":
            formatted = f'\n -> {self.inputContent.text}'
            self.outputContent.items.append(formatted)
            self.outputContent.update()
            self.inputContent.text = ""

class MyApp(App):
    def build(self):
        return RootWidget()

MyApp().run()