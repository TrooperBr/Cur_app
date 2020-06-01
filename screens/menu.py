from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button


class Menu(Screen):
	name_text = 'OLa'

	def __init__(self,**kwargs):
		super(Menu, self).__init__(**kwargs)


	def create_widgets(self):
		self.add_widget(Button(text='Hellow Word'))



	def on_touch_down(self, touch):
		self.create_widgets()