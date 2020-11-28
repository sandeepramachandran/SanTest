import kivy
from kivy.app import App
from kivy.uix.label import Label

class myApp(App):
    def build(self):
        #return Label(text="Tech with San")
        return Label(text="Hello")

if __name__== "__main__":
    myApp().run()
else:
    print ("Someghing s wonr")