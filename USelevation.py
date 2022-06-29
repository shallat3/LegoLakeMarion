import numpy as np
import imageio.v2 as imageio
import matplotlib.pyplot as plt
import math

import statistics as st

from fnLakeMarion import mostcommon, shrink, kernelsmooth, colormap, distinctcolors, addborder, colorchange, waterborder

colors = [[121,196,113], [174,211,97], [237,233,84], [220,205,76], [207,181,68], [195,157,60], [186,138,49], [255,255,255]]

baseimage = imageio.imread("mostcommonUS.jpg")

baseimage = shrink(baseimage, 64, 112)

imageio.imwrite("USfinalshrink.jpg", baseimage.astype(np.uint8))

baseimage = colormap(baseimage, colors)

imageio.imwrite("shrunkcolormapUS.jpg", baseimage.astype(np.uint8))

baseimage = mostcommon(baseimage, 3, [255,255,255])


imageio.imwrite("finalUS.jpg", baseimage.astype(np.uint8))

# shrink to 400x700
# colormap
# mostcommon with 4
