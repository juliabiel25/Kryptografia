import imageio.v2 as iio
import cv2
import random

import numpy as np


def to_binary(im):
    for i in range(len(im)):
        for j in range(len(im[i])):
            if sum(im[i][j]) / 3 > 255 / 2:
                for k in range(3):
                    im[i][j][k] = 255
            else:
                for k in range(3):
                    im[i][j][k] = 0
    return im


def clear(im):
    for i in range(len(im)):
        for j in range(len(im[i])):
            for k in range(3):
                im[i][j][k] = 255

    return im

def pixel_black(px1, px2):
    if px1[0] == 0 and px1[1] == 0 and px1[2] == 0:
        return True
    if px2[0] == 0 and px2[1] == 0 and px2[2] == 0:
        return True
    else:
        return False


random.seed()
im = iio.imread('binary2.png')
im = to_binary(im)  # get rid of non-white and non-black pixels


# copy and resize the origianl img array representation
shape = im.shape
im_cp = im
part1 = cv2.resize(im_cp, (shape[1]*2, shape[0]))

im_cp = im
part2 = cv2.resize(im_cp, (shape[1]*2, shape[0]))
print(im.shape)

for i in range(len(im)):
    for j in range(len(im[i])):

        j1 = j * 2
        j2 = j * 2 + 1

        # white pixel - generate 2 identical parts
        if im[i][j][0] == 255 and im[i][j][1] == 255 and im[i][j][2] == 255:
            if random.randint(0, 1) == 0:
                # PART 1
                # first pixel
                part1[i][j1][0] = 0
                part1[i][j1][1] = 0
                part1[i][j1][2] = 0

                # second pixel
                part1[i][j2][0] = 255
                part1[i][j2][1] = 255
                part1[i][j2][2] = 255

                # PART 2
                # first pixel
                part2[i][j1][0] = 0
                part2[i][j1][1] = 0
                part2[i][j1][2] = 0

                # second pixel
                part2[i][j2][0] = 255
                part2[i][j2][1] = 255
                part2[i][j2][2] = 255
            else:
                # PART 1
                # first pixel
                part1[i][j1][0] = 255
                part1[i][j1][1] = 255
                part1[i][j1][2] = 255

                # second pixel
                part1[i][j2][0] = 0
                part1[i][j2][1] = 0
                part1[i][j2][2] = 0

                # PART 2
                # first pixel
                part2[i][j1][0] = 255
                part2[i][j1][1] = 255
                part2[i][j1][2] = 255

                # second pixel
                part2[i][j2][0] = 0
                part2[i][j2][1] = 0
                part2[i][j2][2] = 0


        # black pixel - generate 2 different parts
        if im[i][j][0] == 0 and im[i][j][1] == 0 and im[i][j][2] == 0:
            if random.randint(0, 1) == 0:
                # PART 1
                # first pixel
                part1[i][j1][0] = 0
                part1[i][j1][1] = 0
                part1[i][j1][2] = 0

                # second pixel
                part1[i][j2][0] = 255
                part1[i][j2][1] = 255
                part1[i][j2][2] = 255

                # PART 2
                # first pixel
                part2[i][j1][0] = 255
                part2[i][j1][1] = 255
                part2[i][j1][2] = 255

                # second pixel
                part2[i][j2][0] = 0
                part2[i][j2][1] = 0
                part2[i][j2][2] = 0
            else:
                # PART 1
                # first pixel
                part1[i][j1][0] = 255
                part1[i][j1][1] = 255
                part1[i][j1][2] = 255

                # second pixel
                part1[i][j2][0] = 0
                part1[i][j2][1] = 0
                part1[i][j2][2] = 0

                # PART 2
                # first pixel
                part2[i][j1][0] = 0
                part2[i][j1][1] = 0
                part2[i][j1][2] = 0

                # second pixel
                part2[i][j2][0] = 255
                part2[i][j2][1] = 255
                part2[i][j2][2] = 255

# write parts as PNG
iio.imwrite('part1.jpg', part1[:, :, 0])
iio.imwrite('part2.jpg', part2[:, :, 0])

# merge parts back
final = part1
for i in range(len(final)):
    for j in range(len(final[i])):
        if pixel_black(part1[i][j], part2[i][j]):
            final[i][j][0] = 0
            final[i][j][1] = 0
            final[i][j][2] = 0
        else:
            final[i][j][0] = 255
            final[i][j][1] = 255
            final[i][j][2] = 255


iio.imwrite('final.jpg', final[:, :, 0])