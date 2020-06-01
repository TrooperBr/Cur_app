from kivy.app import App
from screens.manager import Gerenciador_Telas

class AppAula(App):
	"""docstring for AppAula"""
	def __init__(self, **kwargs):
		super(AppAula, self).__init__(**kwargs)

	def build(self):
		return Gerenciador_Telas()




if __name__ == '__main__':
	AppAula().run()