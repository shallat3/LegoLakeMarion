import numpy as np
import imageio.v2 as imageio
import matplotlib.pyplot as plt
import math

import statistics as st

from fnLakeMarion import mostcommon, shrink, kernelsmooth, colormap, distinctcolors, addborder, colorchange, waterborder

colors = [[142, 181, 236], [170, 197, 240], [196,213,223], [220,234,237], [195,185,126]]

new_colors = [[220,234,237],[196,213,223],[170, 197, 240],[142, 181, 236],[79, 111, 66]]

# shrunksmoothmap = imageio.imread("shrunksmoothmap.jpg")
# shrunksmoothmap = colormap(shrunksmoothmap, colors)
# newborder = addborder(shrunksmoothmap, [195, 185, 126], [142, 181, 236], 2)

                    
# imageio.imwrite("newborder.jpg", newborder.astype(np.uint8))


# newcolors = colorchange(newborder, colors, new_colors)

# imageio.imwrite("finalimage.jpg", newcolors.astype(np.uint8))

baseimage = imageio.imread("newsquarepic.jpg")

baseimage = shrink(baseimage, 500)

baseimage = mostcommon(baseimage, 2)
baseimage = mostcommon(baseimage, 2)

baseimage = colormap(baseimage, colors)

baseimage = shrink(baseimage, 128)
baseimage = kernelsmooth(baseimage, 2)
baseimage = colormap(baseimage, colors)
baseimage = waterborder(baseimage, [195, 185, 126], [142, 181, 236], 2)

baseimage = colorchange(baseimage, colors, new_colors)

baseimage = addborder(baseimage, [79, 111, 66])


imageio.imwrite("finalimage2.jpg", baseimage.astype(np.uint8))














