import kivy
import sqlite3
import string
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

sqlite_db = "C:/Users/USER-MB/source/GIT_Repos/myKivyApp01/myKivyAppDB.db"
conn = sqlite3.connect(sqlite_db)
c = conn.cursor()

class RootContainer(BoxLayout):
    instance = ObjectProperty(None)

    def clickAction1(self, instance):
        #print(instance)
        #identify the button pressed
        buttonText = (instance.text[0:2],)
        print(buttonText)
        
        #use button text to query all related button info from DB
        #c.execute('select * from moderateBaseline where id=?',buttonText)
        #execute query
        t = (1,)
        c.execute('select * from moderateBaseline where id=?',t)
        #fetch results of query, fetchall() can only be used once
        results = c.fetchall()
        print(results[0][3])
        self.lbl1.text = results[0][4]
        self.lbl2.text = results[0][2]
        


class MBApp(App):
    # this is a native function from Kivy to actually build the app using KV files
    def build(self):
        return RootContainer()


if __name__ == '__main__':
    MBApp().run()