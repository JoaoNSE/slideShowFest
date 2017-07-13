from pykeyboard import PyKeyboard
import time
k = PyKeyboard()

# To Create an Alt+Tab combo
#k.press_key(k.alt_key)
def cliqueAuto():
	while True:
		k.tap_key(k.tab_key)
		time.sleep(3)

#k.release_key(k.alt_key)
