import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import subprocess
import summarize as sm

RST = 0

disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)
disp.begin()
disp.clear()
disp.display()

width = disp.width
height = disp.height
image1 = Image.new('1', (width, height))
draw = ImageDraw.Draw(image1)
draw.rectangle((0,0,width,height), outline=0, fill=0)

padding = -2
top = padding
bottom = height-padding
x = 0
font = ImageFont.load_default()

while True:
    [keys,ent] = sm.get_text()
    phrases = keys[1]
    print('key phrases: ', phrases)
    draw.rectangle((0,0,width,height), outline=0, fill=255)

    # Write two lines of text.
    disp.clear()
    disp.display()
    draw.text((x, top+16),       phrases ,   font=font, fill=0)
    '''draw.text((x, top+8),     "Circuit Digest", font=font, fill=255)
    draw.text((x, top+16),    "For more Videos",  font=font, fill=255)
    draw.text((x, top+25),    "Visit at",  font=font, fill=255)
    draw.text((x, top+34),    "www.circuitdigest.com",  font=font, fill=255)'''

    # Display image.
    disp.image(image1)
    disp.display()
    time.sleep(2)