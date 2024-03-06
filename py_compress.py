import os
from ipynbcompress import compress
filename = './my_paypal.ipynb'
out = './compressed_my_paypal.ipynb'
os.stat(filename).st_size
compress(filename, output_filename=out, img_width=800, img_format='jpeg')