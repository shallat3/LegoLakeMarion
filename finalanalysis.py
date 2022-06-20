import numpy as np
import imageio.v2 as imageio
import matplotlib.pyplot as plt
import math

import statistics as st

from fnLakeMarion import mostcommon, shrink, kernelsmooth, colormap, distinctcolors, addborder, colorchange, waterborder, maketiles


img = imageio.imread("finalimage2.jpg")

maketiles(img)

