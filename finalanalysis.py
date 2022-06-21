import numpy as np
import imageio.v2 as imageio
import matplotlib.pyplot as plt
import math

import statistics as st

from fnLakeMarion import mostcommon, shrink, kernelsmooth, colormap, distinctcolors, addborder, colorchange, waterborder, maketiles, countcolors

new_colors = [[142, 181, 236],[170, 197, 240],[196,213,223],[220,234,237],[79, 111, 66]]

img = imageio.imread("finalimage2.jpg")



img = colormap(img, new_colors)
img = waterborder(img, [79, 111, 66], [220, 234, 237], 2)


maketiles(img, new_colors)

imageio.imwrite("finalimage3.jpg", img.astype(np.uint8))



colors = {"lightblue": [220,234,237] , "medlightblue":[196,213,223], "meddarkblue":[170, 197, 240], "darkblue":[142, 181, 236], "green": [79, 111, 66] }

print(countcolors(img, colors))




