# import kivy module
import kivy

# this restrict the kivy version i.e
# below this kivy version you cannot
# use the app or software
kivy.require("1.9.1")

# base Class of your App inherits from the App class.
# app:always refers to the instance of your application
from kivy.app import App

# BoxLayout arranges children
# in a vertical or horizontal box.
from kivy.uix.boxlayout import BoxLayout

# class in which we are defining action on click
class RootWidget(BoxLayout):

	def btn_clk(self):
		self.lbl.text = "You have been pressed"


# creating action class and calling
# Rootwidget by returning it
class ActionApp(App):

	def build(self):
		return RootWidget()

# creating the myApp root for ActionApp() class
myApp = ActionApp()

# run function runs the whole program
# i.e run() method which calls the
# target function passed to the constructor.
myApp.run()
