import os
from ipynbcompress import compress

filename = './my_paypal.ipynb'
out = './compressed_my_paypal.ipynb'

compress(filename, output_filename=out, img_width=500, img_format='png')