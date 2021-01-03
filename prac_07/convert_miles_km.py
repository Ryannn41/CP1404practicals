from kivy.app import App
from kivy.lang import Builder
from kivy.app import StringProperty

miles_to_km = 1.609344

class ConvertApp(App):
    """App for converting miles to km"""
    output_km = StringProperty()

    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "convert m to km"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root









ConvertApp().run()