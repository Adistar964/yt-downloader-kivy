from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatIconButton,MDFlatButton,MDRectangleFlatButton,Button,MDFloatingActionButton
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.textfield import MDTextField
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from kivymd.uix.progressbar import MDProgressBar
from kivymd.uix.gridlayout import GridLayout
from kivy.core.clipboard import Clipboard as cb
from kivymd.toast import toast
from kivy.properties import ObjectProperty
from threading import Thread
import pytube as pt

class helpnav(MDScreen):
	pass

class about(MDScreen):
	pass

class tutorial(MDScreen):
	pass

class main(MDScreen):

	url = ObjectProperty(None)

	def show(self,typed):
		msg = GridLayout()
		msg.cols = 1
		msg.add_widget(MDLabel(text='Downloading...'))
		self.prog = MDProgressBar()
		msg.add_widget(self.prog)
		cancel = MDFlatButton(text='Cancel', on_release=self.stpvid)
		self.dialog = MDDialog(type='custom',content_cls=msg,
								buttons=[cancel],size_hint=(0.5,0.5),
								pos_hint={'top':0.7,'right':0.7})
		self.dialog.auto_dismiss = False
		Thread(target=lambda:self.download(typed)).start()

	def paste(self,*args):
		self.url.focus = True
		self.url.text = cb.paste()

	def stpvid(self,*args):
		self.dialog.dismiss()

	def progfunc(self, stream,chunk,bytes_remaining):
		self.dialog.open()
		size = stream.filesize
		remaining = size - bytes_remaining
		self.percent = remaining / size * 100 
		self.prog.value = self.percent

	def completefunc(self,*args):
		self.dialog.dismiss()
		dialog = MDDialog(text='Completed!',size_hint=(.5,.5),
							pos_hint={'top':0.7,'right':0.7},
							buttons=[MDFlatButton(text='close',
							on_release=lambda x:dialog.dismiss())])
		dialog.open()
		toast('Completed Successfully!')

	def download(self,typed):
		if len(self.url.text.strip()) != 0:
			try:
				self.vid = pt.YouTube(self.url.text)
				self.vid.register_on_progress_callback(self.progfunc)
				self.vid.register_on_complete_callback(self.completefunc)
				self.dialog.open()

			except:
				toast('invalid URL')
				dialog1 = MDDialog(text='Invalid URL!',size_hint=(0.5,0.5),
									pos_hint={'top':0.7,'right':0.7},
										buttons=[MDFlatButton(text='close',
												on_release=lambda x:dialog1.dismiss())])
				dialog1.open()
			else:
				toast("Download Started")
				if typed:
					self.vid.streams.first().download()
				else:
					self.vid.streams.filter(only_audio=True).first().download()

		else:
			toast("Provide URL!")
			dialog2 = MDDialog(text='Provide an URL!',size_hint=(0.5,0.5),
								pos_hint={'top':0.7,'right':0.7},
									buttons=[MDFlatButton(text='close',
											on_release=lambda *args:dialog2.dismiss())])
			dialog2.open()

class ytd(MDApp):
	def build(self):
		self.smanager = ScreenManager()
		self.smanager.add_widget(main(name='main'))
		self.smanager.add_widget(helpnav(name='helpnav'))
		self.smanager.add_widget(about(name='about'))
		self.smanager.add_widget(tutorial(name='tutorial'))
		return self.smanager

app = ytd()
app.run()