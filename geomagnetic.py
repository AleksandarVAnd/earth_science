import time
import requests as req
try:
    from PIL import Image
except ImportError:
    exit("The script requires the PIL module. To install : # pip install Pillow")
res = req.get('http://data.niggg.bas.bg/kp_for/kp_temp.png', stream = True) #the stream is necessary for PIL to process it
img = res.raw
kp = Image.open(img) #<PIL.PngImagePlugin.PngImageFile image mode=P size=550x367 at 0x22B56EA76A0>
kp = kp.convert('RGBA') #originally a palette so converting it makes it easier to process
analyze = kp.crop((51, 114, 545, 160)) #between kp=4.75 and kp=6.25
width, height = analyze.size
timing = time.asctime()
timing = timing.replace(':', '-') #can't save a file with the ':' sign in the name
for x in range(width):
    for y in range(height):
        colors = analyze.getpixel((x,y))
        if colors==(255, 255, 0, 255): #yellow
            print('Active geomagnetic conditions')
            kp.show()
            break
        elif colors==(255, 0, 0, 255): #red
            kp.save(f'storm on {timing}.png', 'PNG')
            kp.show()
            break
        elif colors==(0, 204, 255, 255): #forecast
            print('Danger forecasted!')
            kp.show()
            break
    else: #black
        continue
    break
