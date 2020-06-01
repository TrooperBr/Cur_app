from kivy.uix.screenmanager import ScreenManager
from screens.menu import Menu




class Gerenciador_Telas(ScreenManager):
	telas = [Menu]



	def __init__(self, **kwargs):
		super(Gerenciador_Telas, self).__init__(**kwargs)
		for i in self.telas:
			self.add_widget(i(name=i.name_text))