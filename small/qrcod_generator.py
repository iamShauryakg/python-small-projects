# first install qrcode using pip 

import qrcode as qr

image1 = qr.make("https://www.youtube.com/watch?v=th4OBktqK1I")
image1.save('youtube.png')