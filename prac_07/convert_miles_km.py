from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

miles_to_km = 1.609344
2

class ConvertApp(App):
    """App for converting miles to km"""
    output_km = StringProperty()

    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "convert m to km"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self):
        """calculate function"""
        miles = self.convert()
        result = miles * miles_to_km
        self.root.ids.output_label.text = str(result)

    def handle_updown(self, change):
        """handle up and down button, show text change"""
        miles = self.convert() + change
        self.root.ids.input_miles.text = str(miles)
        self.handle_calculate()


    def convert(self):
        """set 0.0 if invalid input and avoid error"""
        try:
            return float(self.root.ids.input_miles.text)
        except ValueError:
            return 0.0


ConvertApp().run()
