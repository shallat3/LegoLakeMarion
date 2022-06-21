
import numpy as np
import imageio.v2 as imageio
import matplotlib.pyplot as plt
import math

import statistics as st





def mostcommon(image, neighborhood):
    xsize = image.shape[0]
    ysize = image.shape[1]

    toreturn = np.ndarray((xsize, ysize, 3))

    for x in range(xsize):
        for y in range(ysize):
            
            if x < neighborhood or x > xsize - neighborhood - 1 or y < neighborhood or y > ysize - neighborhood - 1:
                toreturn[x][y] = image[x][y]
                continue

            curgroup = {}
            for x2 in range (-1*neighborhood, neighborhood + 1):
                for y2 in range(-1*neighborhood, neighborhood + 1):
                    curpixel = f"{image[x+x2][y+y2][0]}-{image[x+x2][y+y2][1]}-{image[x+x2][y+y2][2]}"
                    if curpixel in curgroup.keys():
                        curgroup[curpixel] += 1
                    else:
                        curgroup[curpixel] = 1


            max_val = list(curgroup.values())
            max_key = list(curgroup.keys())
            rgb = max_key[max_val.index(max(max_val))].split('-')

                
            toreturn[x][y][0] = float(rgb[0])
            toreturn[x][y][1] = float(rgb[1])
            toreturn[x][y][2] = float(rgb[2])
    return toreturn


def shrink(image, newsize):
    toreturn = np.ndarray((newsize, newsize, 3))

    ratio = image.shape[0] / newsize

    for x in range(newsize):
        for y in range(newsize):
            toreturn[x][y] = image[round(ratio * x) + round(ratio / 2)][round(ratio * y) + round(ratio / 2)]

    return toreturn

def kernelsmooth(image, neighborhood):
    xsize = image.shape[0]
    ysize = image.shape[1]

    toreturn = np.ndarray((xsize, ysize, 3))

    for x in range(xsize):
        for y in range(ysize):

            if x < neighborhood or x > xsize - neighborhood - 1 or y < neighborhood or y > ysize - neighborhood - 1:
                toreturn[x][y] = image[x][y]
                continue

            r = []
            g = []
            b = []
            for x2 in range (-1 * neighborhood, neighborhood + 1):
                for y2 in range(-1 * neighborhood, neighborhood + 1):
                    r.append(image[x + x2][y + y2][0])
                    g.append(image[x + x2][y + y2][1])
                    b.append(image[x + x2][y + y2][2])

            toreturn[x][y][0] = st.mean(r)
            toreturn[x][y][1] = st.mean(g)
            toreturn[x][y][2] = st.mean(b)
    return toreturn



def colormap(image, colorlist):
    toreturn = np.ndarray((image.shape[0], image.shape[1], 3))

    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            curpixel = image[x][y]

            curbestind = -1
            curbestdist = 99999
            for i in range(len(colorlist)):
                curcolor = colorlist[i]
                
                curdist = math.sqrt((curcolor[0] - curpixel[0])**2 + (curcolor[1] - curpixel[1])**2 + (curcolor[2] - curpixel[2])**2)

                if curdist < curbestdist:
                    curbestdist = curdist
                    curbestind = i
            toreturn[x][y] = colorlist[curbestind]

    return toreturn




def distinctcolors(image, colorlist):
    colordict = {}

    distinctcolors = [[0, 0, 0], [255, 0, 0], [0, 255, 0], [0, 0, 255], [255, 255, 255]]

    toreturn = np.ndarray((image.shape[0], image.shape[1], 3))

    for i in range(len(colorlist)):
        key = f"{colorlist[i][0]}-{colorlist[i][1]}-{colorlist[i][2]}"

        colordict[key] = distinctcolors[i]


    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            curkey = f"{int(image[x][y][0])}-{int(image[x][y][1])}-{int(image[x][y][2])}"
            toreturn[x][y] = colordict[curkey]

    return toreturn

            
def waterborder(image, outside, tothis, pixelrange):
    xsize = image.shape[0]
    ysize = image.shape[1]

    toreturn = image.copy()

    for x in range(xsize):
        for y in range(ysize):
            if int(image[x][y][0]) != outside[0] and int(image[x][y][1]) != outside[1] and int(image[x][y][0]) != outside[2]:

                if x < pixelrange or x > xsize - pixelrange - 1 or y < pixelrange or y > ysize - pixelrange - 1:
                    continue

                for x2 in range(-1 * pixelrange, pixelrange + 1):
                    for y2 in range(-1 * pixelrange, pixelrange + 1):
                        if (image[x+x2][y+y2] == outside).all():
                            toreturn[x][y] = tothis

    return toreturn
    

def colorchange(image, old, new):
    xsize = image.shape[0]
    ysize = image.shape[1]

    toreturn = image.copy()

    colordict = {}

    for i in range(len(old)):
        curpixel = f"{old[i][0]}-{old[i][1]}-{old[i][2]}"
        colordict[curpixel] = new[i]

    
    for x in range(xsize):
        for y in range(ysize):
            curpixel = f"{int(image[x][y][0])}-{int(image[x][y][1])}-{int(image[x][y][2])}"
            
            toreturn[x][y] = colordict[curpixel]

    return toreturn


def addborder(image, bordercolor):
    toreturn = image.copy()
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            if x < 3 or y < 3 or x > image.shape[0] - 4 or y > image.shape[1] - 4:
                toreturn[x][y] = bordercolor

    return toreturn


def maketiles(image, colors):

    colormap = {}

    for i in range(len(colors)):
        curcolor = f"{colors[i][0]}-{colors[i][1]}-{colors[i][2]}"
        colormap[curcolor] = i


    tilewidx = int(image.shape[0] / 16)
    tilewidy = int(image.shape[1] / 16)

    for x in range(tilewidx):
        for y in range(tilewidy):

            curtile = np.ndarray((16, 16, 3))
            curinst = np.ndarray((16,16))

            for x2 in range(16):
                for y2 in range(16):
                    curpixel = image[16*x + x2][16*y + y2]
                    curtile[x2][y2] = curpixel
                    curcolor = f"{int(curpixel[0])}-{int(curpixel[1])}-{int(curpixel[2])}"

                    for color, number in colormap.items():
                        if color == curcolor:
                            curinst[x2][y2] = number

            file = open(f"tileinstructions/{x+1}-{y+1}.txt", "w")

            arr = " ".join(str(curinst).split("."))
            file.write(arr)
            file.close()
            
            imageio.imwrite(f"tiles/{x+1}-{y+1}.jpg", curtile.astype(np.uint8))


def countcolors(image, colors):

    colorcount = {}
    
    for color in colors.keys():
        colorcount[color] = 0

    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            for color, rgb in colors.items():

                if int(image[x][y][0]) == rgb[0] and int(image[x][y][1]) == rgb[1] and int(image[x][y][1]) == rgb[1]:
                    colorcount[color] += 1

    return colorcount