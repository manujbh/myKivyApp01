import kivy
import sqlite3
import string
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

# if there is a need to load another kv file
#from kivy.lang import Builder
#Builder.load_file('MB2.kv')

MY_BUTTON_TEXT = "ACCZ"

sqlite_db = "C:/Users/USER-MB/source/GIT_Repo for myKivyApp01/myKivyApp01/myKivyAppDB.db"
conn = sqlite3.connect(sqlite_db)
c = conn.cursor()

class SubControlButtons(Button):
    theRoot = ObjectProperty(None)

class FamilyButtons(Button):
    theRoot = ObjectProperty(None)


class RootContainer(BoxLayout):
    instance1 = ObjectProperty(None)
    instance2 = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(RootContainer, self).__init__(**kwargs)
        #create buttons from query result
        #self.lbl5.add_widget(Button(text=MY_BUTTON_TEXT, text_size = self.size, on_press=lambda x:self.clickAction1(MY_BUTTON_TEXT)))
        self.lbl5.add_widget(Button(text=MY_BUTTON_TEXT, text_size = self.size, on_press=lambda x:self.stringAction1(MY_BUTTON_TEXT)))
        #self.lbl5 = Button(text="ACC", text_size = self.size)
        #self.lbl5.bind(on_press=lambda x:self.clickAction1(self))
        #self.add_widget(self.lbl5)


    def clickAction2(self, instance2):
        self.lbl2.text = instance2.text
        #pass


    def stringAction1(self, string1):
        print(string1)


    def clickAction1(self, instance1):
        print("instance = " + str(instance1))
        #identify the button pressed
        buttonText = (instance1.text[0:2],)
        print(buttonText)
        
        #use button text to query all related button info from DB
        c.execute('select * from moderateBaseline where family=?',buttonText)

        #fetch results of query, fetchall() can only be used once
        results = c.fetchall()
        #print(results)
        #print(results[0][3])
        self.lbl2.text = results[1][4]
        #bind root so we can identify on_press in the buttons below
        #self.bind(self)
        # set height of grid before populating with buttons
        self.lbl3.bind(minimum_height=self.lbl3.setter('height'))
        print("lbl3.bind complete")
        # clear all old children
        self.lbl3.clear_widgets()
        print("lbl3 cleared")
        # dynamically add buttons
        for x in results:
            #self.lbl3.add_widget(Button(text=str(x[3])))
            self.lbl3.add_widget(SubControlButtons(text=str(x[3]), theRoot = self))

    

class MBApp(App):
    # this is a native function from Kivy to actually build the app using KV files
    def build(self):
        #call RootContainer
        return RootContainer()
        # remove the RootContainer call above. Make all the KV file formatting under App 
        # (i.e. remove formatting from under RootContainer to one indent left)
        # see ShowcaseApp and how it treats screen organization
        #root.lbl5.add_widget(FamilyButtons(text="AC - Control", theRoot = self, text_size = self.size, on_press = self.clickAction1(self)))


if __name__ == '__main__':
    MBApp().run()