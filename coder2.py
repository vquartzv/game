from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.core.clipboard import Clipboard
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.label import Label
Window.clearcolor = (.7, .7, .7, 1)

class integer(App):
	x=0
	text=''
	a=TextInput(text="/", size_hint=(1, .2), pos_hint={'y':.7}, font_size = "30sp", background_active=' ', background_normal=' ', background_color=(.9, .9, .9, 1))

class CodeApp(App):	
	def build_skrean(self):
		b=BoxLayout(size_hint=(1, .1), pos_hint={'y':.6})
		b.add_widget(Button(text="cope", on_press=self.cope))
		b.add_widget(Button(text="clear", on_press=self.clear))
		b.add_widget(Button(text='ok', on_press=self.ok))
		znach=['@p', '@e', '@a', '~', '1', '2', '3', '+', '4', '5', '6', '-', '7', '8', '9', '_', '[', '0', ']', ' ']
		c=GridLayout(cols=4, size_hint=(1, .5))
		[c.add_widget(Button(text=i, on_press=self.click_n)) for i in znach]
		
		d=BoxLayout(size_hint=(1, .08), pos_hint={'y':0.91})
		d.add_widget(Button(text="back", on_press=self.back, background_normal=' ', background_color=(.7, .7, .7, 1)))
		d.add_widget(Button(text="done", on_press=self.done, background_normal=' ', background_color=(.7, .7, .7, 1)))
		
		self.alfa.append(integer.a)
		self.alfa.append(b)
		self.alfa.append(c)
		self.alfa.append(d)
		
	
	def cope(self, instance):
		Clipboard.copy(integer.a.text)
	def clear(self, instance):
		integer.a.text="/"
	def ok(self, instance):
		integer.text+=integer.a.text
	def click(self, instance):
		integer.a.text+=instance.text+' '
	def click_n(self, instance):
		integer.a.text+=instance.text
		
	
	def build_menu(self):
		file='code'+str(integer.x)+'.txt'
		d=BoxLayout(size_hint=(1, .08), pos_hint={'y':0.91})
		d.add_widget(Button(text="back", on_press=self.back, background_normal=' ', background_color=(.7, .7, .7, 1)))
		d.add_widget(Button(text="done", on_press=self.done, background_normal=' ', background_color=(.7, .7, .7, 1)))
		
		self.array=[]
		with open(file, "r") as f:
		          	for ticker in f.readlines():
		          		self.array.append(ticker.strip())
		v=StackLayout(size_hint=(1, .9))
		[v.add_widget(Button(text=i, on_press=self.click, size_hint=(.25, None), size=(300, 150))) for i in self.array]
		self.alfa.append(d)
		self.alfa.append(v)
		
		 
	
	
	def done(self, instance):
		if integer.x<3:
			integer.x+=1
			self.fl.clear_widgets()
			CodeApp().run()
			
			
	def back(self, instance):
		if integer.x>0:
			integer.x-=1
			self.fl.clear_widgets()
			CodeApp().run()
		
	def tester(self):
		self.fl=FloatLayout()
		print('hello')
		if integer.x==0:
			self.alfa=[]
			self.build_skrean()
		if integer.x>0:
			self.alfa=[]
			self.build_menu()
		[self.fl.add_widget(b) for b in self.alfa]
		print("q")
		return self.fl
	
	def build(self):
		return self.tester()
		
	
	

if __name__=="__main__":
	CodeApp().run()