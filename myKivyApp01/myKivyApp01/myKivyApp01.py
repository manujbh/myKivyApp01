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
        c.execute('select distinct control_family from table1')
        #fetch results of query, fetchall() can only be used once
        results1 = c.fetchall()
        #if results is an empty list then exit this function
        if not results1:
            print("exit function")
            return
        # dynamically add buttons
        # set height of grid before populating with buttons
        self.lbl5.bind(minimum_height=self.lbl5.setter('height'))
        for x in results1:
            #self.lbl3.add_widget(SubControlButtons(text=str(x[0]), theRoot=self))
            #self.lbl5.add_widget(Button(text=str(x[0]), text_size=self.size, on_press=lambda x:self.clickAction1(MY_BUTTON_TEXT)))
            self.lbl5.add_widget(Button(text=str(x[0]), text_size=self.size, on_press=lambda x:self.clickAction1(str(x[0]))))


    def clickAction2(self, instance2):
        self.lbl2.text = instance2.text
        buttonString = instance2.text[0:]
        print(buttonString)
        #use button text to query all related button info from DB
        c.execute('select control_step_content, acceptable_evidence from table1 where control_step = ?',(buttonString,))
        #fetch results of query, fetchall() can only be used once
        results = c.fetchall()
        #if results is an empty list then exit this function
        if not results:
            print("exit function")
            return
        #print Acceptable_Evidence in lbl1 
        self.lbl1.text = "[b]Acceptable Evidence for " + buttonString + " :[/b] \n" + results[0][1] + "\n"
        #print Control_Step_Content in lbl2 
        self.lbl2.text = "[b]Control Step (" + buttonString + ") Description:[/b] \n" + results[0][0] + "\n"


    def callClickAction1(self, instance1):
        #identify the button pressed
        buttonText = instance1.text[0:2]
        print(buttonText)
        self.clickAction1(buttonText)


    def stringAction1(self, string1):
        print(string1)


    def clickAction1(self, buttonString):
        #use button text to query all related button info from DB; don't use %s its insecure always use ? with a tuple as input
        # The ? SQL parameter interpolation adds quoting for you
        c.execute('select control_step from table1 where control_family=?',(buttonString,))
        #c.execute('select Control_Step from table1 where control_step like ?',('{}%'.format(buttonString),))
        #fetch results of query, fetchall() can only be used once
        results = c.fetchall()
        print(results)
        #if results is an empty list then exit this function
        if not results:
            print("exit function")
            return
        
        c.execute('select control_family_desc from table2 where control_family=?',(buttonString,))
        results2 = c.fetchall()
        #if results is an empty list then exit this function
        if not results2:
            print("exit function because results2 is empty")
            return
        
        self.lbl1.text = "Acceptable evidence details for control step will be displayed here"
        self.lbl2.text = "[b] Click Control Steps below to see details [/b]\n" + results2[0][0]
        # set height of grid before populating with buttons
        self.lbl3.bind(minimum_height=self.lbl3.setter('height'))
        # clear all old children
        self.lbl3.clear_widgets()
        # dynamically add buttons
        for x in results:
            self.lbl3.add_widget(SubControlButtons(text=str(x[0]), theRoot=self))


    

class MBApp(App):
    # this is a native function from Kivy to actually build the app using KV files
    def build(self):
        #call RootContainer
        return RootContainer()


if __name__ == '__main__':
    MBApp().run()