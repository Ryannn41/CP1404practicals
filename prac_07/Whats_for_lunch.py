from kivy.app import App
from kivy.lang import Builder
from kivy.app import StringProperty
import random


class FirstKivy(App):
    message = StringProperty()

    def build(self):
        self.title = "What's for lunch?"
        self.root = Builder.load_file("first_layout.kv")
        return self.root

    def press_button(self):
        if random.randint(1, 100) <= 10:
            self.message = "Japanese food"
        elif 10 <= random.randint(1, 100) <= 20:
            self.message = "sushi"
        elif 20 <= random.randint(1, 100) <= 30:
            self.message = "Chinese food"
        elif 30<= random.randint(1, 100) <= 40:
            self.message = "steak"
        elif 40<= random.randint(1, 100) <= 50:
            self.message = "Mcdonald's"
        elif 50<= random.randint(1, 100) <= 60:
            self.message = "KFC"
        elif 60<= random.randint(1, 100) <= 70:
            self.message = "hotpot"
        elif 70<= random.randint(1, 100) <= 80:
            self.message = "dumplings"
        elif 80<= random.randint(1, 100) <= 90:
            self.message = "chicken rice"
        else:
            self.message = "noodles"


if __name__ == '__main__':
    first_kivy_app = FirstKivy()
    first_kivy_app.run()
