import kivy
import sqlite3
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
        # instead of accepting "msg". identify which button was pressed and query from DB the appropriate content. Then start the chain of events for updates.
        # update "lbl1" and "lbl2" with the appropriate content. 
        #self.lbl1.text = msg
        print(instance)
        print(instance.text[0:5])
        #execute query
        c.execute('''select enhancement from moderateBaseline where id=1''')
        #fetch results of query
        print(c.fetchall())

class MBApp(App):
    # this is a native function from Kivy to actually build the app using KV files
    def build(self):
        return RootContainer()


if __name__ == '__main__':
    MBApp().run()