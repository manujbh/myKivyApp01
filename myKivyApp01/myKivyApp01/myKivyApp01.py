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

sqlite_db = "C:/Users/USER-MB/source/GIT_Repos/myKivyApp01/myKivyAppDB.db"
conn = sqlite3.connect(sqlite_db)
c = conn.cursor()

class ScrollableLabel(ScrollView):
    pass

class RootContainer(BoxLayout):
    instance = ObjectProperty(None)
    layout_content = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(RootContainer, self).__init__(**kwargs)

    def clickAction1(self, instance):
        #print(instance)
        #identify the button pressed
        t = (1,)
        buttonText = (instance.text[0:2],)
        print(buttonText)
        
        #use button text to query all related button info from DB
        #c.execute('select * from moderateBaseline where id=?',t)
        c.execute('select * from moderateBaseline where family=?',buttonText)

        #fetch results of query, fetchall() can only be used once
        results = c.fetchall()
        print(results)
        print(results[0][3])
        self.lbl1.text = results[1][4]
        #self.lbl2.text = '\n'.join([x[2] for x in results])
        myresult = '\n'.join([x[3] for x in results])
        self.lbl5.text = myresult
        #self.lbl5.text = '\n'.join([x[3] for x in results])

        #get to parent ScrollView and bind
        scrollable = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
        #following doesn't work. Error says "cannot add object, it already has a parent
        #scrollable.add_widget(self.lbl5)
        

        # dynamically add buttons 
        #for x in L:
            #x = self.add_widget(Button(text = os.listdir('saves')[x]))

class MBApp(App):
    # this is a native function from Kivy to actually build the app using KV files
    def build(self):
        return RootContainer()


if __name__ == '__main__':
    MBApp().run()