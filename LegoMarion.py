from tkinter import S
import numpy as np
import imageio.v2 as imageio
import matplotlib.pyplot as plt
import math

import statistics as st



panelwid = 8
studwid = panelwid * 16


mediummostcommon = imageio.imread("mediumsmoothed.JPG")




# mediumimage = np.ndarray((500, 500, 3))
# medratio = pic.shape[0] / mediumimage.shape[0]
# print(medratio)

# for x in range(mediumimage.shape[0]):
#     for y in range(mediumimage.shape[1]):
#         realx = round(medratio * x) + round(medratio / 2)
#         realy = round(medratio * y) + round(medratio / 2)

#         mediumimage[x][y] = pic[realx][realy]

# imageio.imwrite("mediumimage.jpg", mediumimage.astype(np.uint8))




# mediummostcommon = np.ndarray((500, 500, 3))

# for x in range(mediumimage.shape[0]):
#     for y in range(mediumimage.shape[1]):

#         if x < 3 or x > mediumimage.shape[0] - 4 or y < 3 or y > mediumimage.shape[1] - 4:
#             mediummostcommon[x][y] = mediumimage[x][y]
#             continue

#         curgroup = {}
#         for x2 in range (-3, 4):
#             for y2 in range(-3, 4):
#                 curpixel = f"{mediumimage[x+x2][y+y2][0]}-{mediumimage[x+x2][y+y2][1]}-{mediumimage[x+x2][y+y2][2]}"
#                 if curpixel in curgroup.keys():
#                     curgroup[curpixel] += 1
#                 else:
#                     curgroup[curpixel] = 1


#         max_val = list(curgroup.values())
#         max_key = list(curgroup.keys())
#         rgb = max_key[max_val.index(max(max_val))].split('-')

        
#         mediummostcommon[x][y][0] = float(rgb[0])
#         mediummostcommon[x][y][1] = float(rgb[1])
#         mediummostcommon[x][y][2] = float(rgb[2])

# imageio.imwrite("mediumsmoothed.jpg", mediummostcommon.astype(np.uint8))







# for x in range(pic.shape[0]):
#     for y in range(pic.shape[1]):

#         if x < 2 or x > pic.shape[0] - 3 or y < 2 or y > pic.shape[1] - 3:
#             continue

#         r = []
#         g = []
#         b = []
#         for x2 in range (-2, 3):
#             for y2 in range(-2, 3):
#                 r.append(pic[x + x2][y + y2][0])
#                 g.append(pic[x + x2][y + y2][1])
#                 b.append(pic[x + x2][y + y2][2])

#         smoothedbigimage[x][y][0] = st.mean(r)
#         smoothedbigimage[x][y][1] = st.mean(g)
#         smoothedbigimage[x][y][2] = st.mean(b)
# # plt.figure(figsize=(5,5))
# # plt.imshow(pic)
# imageio.imwrite("smoothedbig.jpg", smoothedbigimage.astype(np.uint8))



ratio = mediummostcommon.shape[0] / studwid
print(ratio)

newpic = np.ndarray((studwid, studwid, 3))
print(newpic.shape)

for x in range(newpic.shape[0]):
    for y in range(newpic.shape[1]):
        realx = round(ratio*x) + 2
        realy = round(ratio*y) + 2

        newpic[x][y] = mediummostcommon[realx][realy]

middlepixel = newpic

imageio.imwrite("output.jpg", middlepixel.astype(np.uint8))

print(middlepixel.shape[1])

for x in range(newpic.shape[0]):
    for y in range(newpic.shape[1]):

        if x < 2 or x > studwid - 3 or y < 2 or y > studwid - 3:
            continue

        r = []
        g = []
        b = []
        for x2 in range (-2, 3):
            for y2 in range(-2, 3):
                r.append(newpic[x + x2][y + y2][0])
                g.append(newpic[x + x2][y + y2][1])
                b.append(newpic[x + x2][y + y2][2])

        newpic[x][y][0] = st.mean(r)
        newpic[x][y][1] = st.mean(g)
        newpic[x][y][2] = st.mean(b)
smoothpixel = newpic
imageio.imwrite("output2.jpg", smoothpixel.astype(np.uint8))


light = [186, 212, 225]
middle = [153, 197, 242]
dark = [115, 181, 239]
tan = [201, 185, 123]
darkgreen = [79, 111, 66]

red = [255, 0, 0]
green = [0, 255, 0]
blue = [0,0,255]

newpic = middlepixel

for x in range(newpic.shape[0]):
    for y in range(newpic.shape[1]):

        r = newpic[x][y][0]
        g = newpic[x][y][1]
        b = newpic[x][y][2]
        


        lightdist = math.sqrt((light[0]-r)**2 + (light[1] - g)**2 + (light[2] - b)**2)
        middledist = math.sqrt((middle[0]-r)**2 + (middle[1] - g)**2 + (middle[2] - b)**2)
        darkdist = math.sqrt((dark[0]-r)**2 + (dark[1] - g)**2 + (dark[2] - b)**2)
        tandist = math.sqrt((tan[0]-r)**2 + (tan[1] - g)**2 + (tan[2] - b)**2)
        
        dists = []


        dists = [lightdist, middledist, darkdist, tandist]
        mindist = round(min(dists), 3)

        if mindist == round(lightdist, 3):
            newpic[x][y] = red
        elif mindist == round(middledist,3):
            newpic[x][y] = green
        elif mindist == round(darkdist,3):
            newpic[x][y] = blue
        elif mindist == round(tandist,3):
            newpic[x][y] = [0,0,0]



closestpixel = newpic
imageio.imwrite("output3.jpg", closestpixel.astype(np.uint8))






toloop = newpic.copy()
for x in range(toloop.shape[0]):
    for y in range(toloop.shape[1]):

        if x < 3 or x > studwid - 4 or y < 3 or y > studwid - 4:
            newpic[x][y] = [0,0, 0]
            continue

        curgroup = {}
        for x2 in range (-3, 4):
            for y2 in range(-3, 4):
                curpixel = f"{toloop[x+x2][y+y2][0]}-{toloop[x+x2][y+y2][1]}-{toloop[x+x2][y+y2][2]}"
                if curpixel in curgroup.keys():
                    curgroup[curpixel] += 1
                else:
                    curgroup[curpixel] = 1


        max_val = list(curgroup.values())
        max_key = list(curgroup.keys())
        rgb = max_key[max_val.index(max(max_val))].split('-')

        
        newpic[x][y][0] = float(rgb[0])
        newpic[x][y][1] = float(rgb[1])
        newpic[x][y][2] = float(rgb[2])
        
averagepixel = newpic
imageio.imwrite("output4.jpg", averagepixel.astype(np.uint8))

piececount = {"dark": 0, "middle": 0, "light": 0, "tan": 0}
for x in range(newpic.shape[0]):
    for y in range(newpic.shape[1]):
        if (newpic[x][y] == red).all():
            piececount["dark"] += 1
        elif (newpic[x][y] == green).all():
            piececount["middle"] += 1
        elif (newpic[x][y] == blue).all():
            piececount["light"] += 1
        elif (newpic[x][y] == [0,0,0]).all():
            piececount["tan"] += 1
print(piececount)



for x in range(newpic.shape[0]):
    for y in range(newpic.shape[1]):
        if (newpic[x][y] == red).all():
            newpic[x][y] = dark
        elif (newpic[x][y] == green).all():
            newpic[x][y] = middle
        elif (newpic[x][y] == blue).all():
            newpic[x][y] = light
        else:
            newpic[x][y] = darkgreen

realset = newpic
imageio.imwrite("output5.jpg", realset.astype(np.uint8))






legos = np.ndarray((studwid, studwid))
for x in range(newpic.shape[0]):
    for y in range(newpic.shape[1]):
        if (newpic[x][y] == dark).all():
            legos[x][y] = 0
        elif (newpic[x][y] == middle).all():
            legos[x][y] = 1
        elif (newpic[x][y] == light).all():
            legos[x][y] = 2
        else:
            legos[x][y] = 3



for x in range(panelwid):
    for y in range(panelwid):

        cur_tile = np.ndarray((16,16,3))
        cur_instructions = np.ndarray((16,16))

        for x2 in range(16):
            for y2 in range(16):
                cur_tile[x2][y2] = newpic[x*16 + x2][y*16 + y2]

                
                cur_instructions[x2][y2] = legos[x*16 + x2][y*16 + y2]

        file = open(f"tileinstructions/{x+1}-{y+1}.txt", "w")

        arr = " ".join(str(cur_instructions).split("."))
        file.write(arr)
        file.close()
        imageio.imwrite(f"tiles/{x+1}-{y+1}.jpg", cur_tile.astype(np.uint8))




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