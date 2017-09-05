import time
import pyautogui as pag

#a small decorator that adds a 3 second countdown so that i can position my mouse 
def withcountdown(func):
	def innerfunc(*args, **kwargs):
		for i in range(3)[::-1]:
			print(i+1)
			time.sleep(1)
		func(*args, **kwargs)
	return innerfunc

myfunc = withcountdown(pag.typewrite) # added a small time out to the pyautogui funciton 

myfunc("def hw(times):\n\tprint('hello world'*times)")
