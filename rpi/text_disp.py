
import gaugette.ssd1306
import time
import sys
 
RESET_PIN = 15
DC_PIN    = 16
 
led = gaugette.ssd1306.SSD1306(reset_pin=RESET_PIN, dc_pin=DC_PIN)
led.begin()
led.clear_display()
text = 'Hello!'
led.draw_text2(0,0,text,2)
text2 = 'Hello!'
led.draw_text2(0,16,text2,1)
text3 = 'Hello!'
led.draw_text2(32,25,text3,1)
led.display()