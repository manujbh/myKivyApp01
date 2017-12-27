import kivy
import sqlite3
import string
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty, StringProperty, ListProperty
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

sqlite_db = "C:/Users/USER-MB/source/GIT_Repo for myKivyApp01/myKivyApp01/myKivyAppDB.db"
conn = sqlite3.connect(sqlite_db)
c = conn.cursor()

class MBApp(App):
    family_names = ListProperty([])
    substep_names = ListProperty([])
    instance1 = ObjectProperty(None)
    instance2 = ObjectProperty(None)
    substep_content = StringProperty()
    substep_content = "##############"

    # this is a native function from Kivy to actually build the app using KV files
    def build(self):
        self.title = 'Guide'

        #create buttons from query result
        c.execute('select distinct control_family from table1')
        #fetch results of query, fetchall() can only be used once
        results1 = c.fetchall()
        #if results is an empty list then exit this function
        if not results1:
            print("exit function")
            return
        myfamilylist = [i[0] for i in results1]
        #print(myfamilylist)
        self.family_names = sorted(myfamilylist)
        self.substep_names = sorted(['Click Family to see substeps'])

    def onClickAction1(self, instance1):
        querytext = instance1.text
        print('The spinner has text: ', querytext)
        c.execute('select control_step from table1 where control_family=?',(querytext,))
        #fetch results of query, fetchall() can only be used once
        results2 = c.fetchall()
        #if results is an empty list then exit this function
        if not results2:
            print("exit function")
            return
        mysubsteps = [i[0] for i in results2]
        print(mysubsteps)
        self.substep_names = sorted(mysubsteps)

    def onClickAction2(self, instance2):
        querytext = instance2.text
        print('The spinner2 has text: ', querytext)
        #use button text to query all related button info from DB; don't use %s its insecure always use ? with a tuple as input
        # The ? SQL parameter interpolation adds quoting for you
        c.execute('select control_step_content, acceptable_evidence from table1 where control_step = ?',(querytext,))
        results2 = c.fetchall()
        #if results is an empty list then exit this function
        if not results2:
            print("exit function because results2 is empty")
            return
        #mysubsteps = [i[0] for i in results2]
        #print(mysubsteps)
        #self.substep_names = sorted(mysubsteps)
        print(results2)
        #self.root.ids.mygrid.text = "Control details and Acceptable evidence details..."
        substep_content = "Control details and Acceptable evidence details..."
        print(substep_content)



if __name__ == '__main__':
    MBApp().run()