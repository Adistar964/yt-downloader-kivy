import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.actionbar import (ActionBar, ActionButton,
							 ActionGroup, ActionItem,
							 ActionLabel, ActionOverflow,
							 ActionPrevious, ActionDropDown,
							 ActionView)
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock
from kivy.core.window import Window

from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.config import Config
from kivy.core.clipboard import Clipboard as cb

import kivysome 
from pytube import YouTube
import pytube
from threading import Thread

Window.size = (360,600)


kivysome.enable("https://kit.fontawesome.com/46f5059413.js", group=kivysome.FontGroup.SOLID)

Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

class helptut(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)	

	def on_back(self, *args):
		ytd964.smanager.current = 'main'
		ytd964.smanager.transition.direction = 'right'


class about(FloatLayout):
	pass

class helpp(FloatLayout):
	pass

class ht(ScrollView):
	pass

class yterror(FloatLayout):
	pass

class ytsuccess(FloatLayout):
	pass

class lenerror(FloatLayout):
	pass

class main(Screen):
	submit = ObjectProperty(None)
	inp = ObjectProperty(None)
	def __init__(self, **_):
		super().__init__(**_)

		self.submit.bind(on_release=self.on_press)

	def download(self):
		ytvid = self.yt.streams.first()
		ytvid.download()

	def putText(self):
		text = cb.paste()
		self.inp.text = self.inp.text + text 

	def lengtherror(self):
		Popup(title='No URL!', content=lenerror(), size_hint=(None,None), size=(320,320)).open()

	def on_press(self, *args):
		if len(self.inp.text.strip()) == 0:
			self.lengtherror()
		else:
			try:
				self.yt = YouTube(str(self.inp.text).strip())
				d = Thread(target=self.download())
				d.start()
				self.success()
			except pytube.exceptions.RegexMatchError:
				self.showerror()

	def success(self):
		Popup(title='Success!', content=ytsuccess(), size_hint=(None,None), size=(300,300)).open()

	def showerror(self):
		Popup(title='Url error!', content=yterror(), size_hint=(None,None), width=300, height=300).open()

	def showAbout(self, *args):
		msg = Popup(title='Info', content=about(),
					size_hint=(None,None),
					width=300, height=200)
		msg.open()

	def showHelp(self, *args):
		msg = Popup(title='Help', content=helpp(),
					size_hint=(None,None),
					width=330, height=230)
		msg.open()

	def showTut(self, *args):
		ytd964.smanager.current = 'helptut'
		ytd964.smanager.transition.direction = 'left'

# kv = Builder.load_file('my.kv') 

class MyApp(App):
	def build(self):
		self.icon = 'icon.png'
		self.title = '964-YTD'

		self.smanager = ScreenManager()

		self.main2 = Screen(name='main')
		self.main = main()
		self.main2.add_widget(self.main)
		self.smanager.add_widget(self.main2)

		self.main = Screen(name='helptut')
		self.helptut = helptut()
		self.main.add_widget(self.helptut)
		self.smanager.add_widget(self.main)

		return self.smanager

if __name__ == '__main__':
	ytd964 = MyApp()
	ytd964.run()
