
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class RootContainer(BoxLayout):

    def clickAction1(self, instance):
        # instead of accepting "msg". identify which button was pressed and query from DB the appropriate content. Then start the chain of events for updates.
        # update "lbl1" and "lbl2" with the appropriate content. 
        #self.lbl1.text = msg
        print(instance)
        
    def print_ids(self, *args):
        print("\nids:")
        for widget in self.walk():
            print("{} -> {}".format(widget, widget.id))

    def get_id(self,  instance):
        for id, widget in instance.parent.ids.items():
            if widget.__self__ == instance:
                return id

class MBApp(App):
    # this is a native function from Kivy to actually build the app using KV files
    def build(self):
        return RootContainer()


if __name__ == '__main__':
    MBApp().run()