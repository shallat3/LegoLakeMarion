import numpy as np
import imageio.v2 as imageio
import matplotlib.pyplot as plt
import math

import statistics as st

pic = imageio.imread("realsquarelake.JPG")
# plt.figure(figsize=(5,5))
# plt.imshow(pic)

print(pic.shape)

newpic = np.ndarray((96, 96, 3))
print(newpic.shape)

for x in range(newpic.shape[0]):
    for y in range(newpic.shape[1]):
        realx = 7*x + 3
        realy = 7*y + 3

        # current_group = {}
        # rgb = ""
        # for x2 in range(-3, 3):
        #     for y2 in range(-3, 3):
        #         cur_pixel = f"{pic[realx+x2][realy+y2][0]}-{pic[realx+x2][realy+y2][1]}-{pic[realx+x2][realy+y2][2]}"
        #         if cur_pixel in current_group.keys():
        #             current_group[cur_pixel] = current_group[cur_pixel] + 1
        #         else:
        #             current_group[cur_pixel] = 1

        #         max_val = list(current_group.values())
        #         max_key = list(current_group.keys())
        #         rgb = max_key[max_val.index(max(max_val))].split('-')
                


        # newpic[x][y][0] = int(rgb[0])
        # newpic[x][y][1] = int(rgb[1])
        # newpic[x][y][2] = int(rgb[2])

        newpic[x][y] = pic[realx][realy]

middlepixel = newpic

imageio.imwrite("output.jpg", middlepixel.astype(np.uint8))

for x in range(newpic.shape[0]):
    for y in range(newpic.shape[1]):

        if x < 2 or x > 93 or y < 2 or y > 93:
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

        if x < 3 or x > 94 or y < 3 or y > 94:
            newpic[x][y] = [0,0, 0]
            continue

        curgroup = {}
        for x2 in range (-3, 2):
            for y2 in range(-3, 2):
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
        else:
            piececount["tan"] += 1
print(piececount)