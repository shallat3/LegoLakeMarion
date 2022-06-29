import numpy as np
import imageio.v2 as imageio
import matplotlib.pyplot as plt
import math

import statistics as st

from fnLakeMarion import mostcommon, shrink, kernelsmooth, colormap, distinctcolors, addborder, colorchange, waterborder

colors = [[142, 181, 236], [170, 197, 240], [196,213,223], [220,234,237], [195,185,126]]

new_colors = [[220,234,237],[196,213,223],[170, 197, 240],[142, 181, 236],[79, 111, 66]]



baseimage = imageio.imread("newsquarepic.jpg")

baseimage = shrink(baseimage, 500)

imageio.imwrite("step1.jpg", baseimage.astype(np.uint8))

baseimage = mostcommon(baseimage, 2)
imageio.imwrite("step2.jpg", baseimage.astype(np.uint8))

baseimage = mostcommon(baseimage, 2)
imageio.imwrite("step3.jpg", baseimage.astype(np.uint8))

baseimage = colormap(baseimage, colors)
imageio.imwrite("step4.jpg", baseimage.astype(np.uint8))

baseimage = shrink(baseimage, 128)
imageio.imwrite("step5.jpg", baseimage.astype(np.uint8))

baseimage = kernelsmooth(baseimage, 2)
imageio.imwrite("step6.jpg", baseimage.astype(np.uint8))

baseimage = colormap(baseimage, colors)
imageio.imwrite("step7.jpg", baseimage.astype(np.uint8))

baseimage = waterborder(baseimage, [195, 185, 126], [142, 181, 236], 2)
imageio.imwrite("step8.jpg", baseimage.astype(np.uint8))

baseimage = colorchange(baseimage, colors, new_colors)
imageio.imwrite("step9.jpg", baseimage.astype(np.uint8))

baseimage = addborder(baseimage, [79, 111, 66])


imageio.imwrite("finalimage2.jpg", baseimage.astype(np.uint8))














