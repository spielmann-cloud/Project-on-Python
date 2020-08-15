
"""
Name of picture: Grave Houses
@author: Umurzakov Sarvar

"""

""" Importing SimpleGraphics module and random """
from SimpleGraphics import *
import random

"""
     Variables:
            center - center of window
            width - width of parallelepiped
            density - constant variable that shows the amount of 'blocks'. Do not change the density. The programm is
                      configured by density = 80. Otherwise you will damage the picture
            coef - coefficient of equality/incline of our blocks. Our coefficient is constant variable
            n - amount of blocks from left side. n must be equal or greater than 6
"""
center = 399, 299
width = 50
density = 80
coef = 0.54369
n = 6

""" Set color to left side between blocks. Creating left-grass, by using polygon """
setColor(25, 54, 0)
polygon(
    399, 299,
    -400 + center[0], 300 + center[1],
    -400 + width + 5 + center[0], 300 + center[1]
)

""" Set color to left side between blocks. Creating right-grass, by using polygon polygon """
setColor(25, 51, 0)
polygon(
    399, 299,
    400 + center[0], 300 + center[1],
    400 - width - 5 + center[0], 300 + center[1]
)

#setColor(40, 40 ,40)
""" Creating central grass and assign appropriate color """
setColor(25, 51, 0)
polygon(
    399, 299,
    400 - width - 5 + center[0], 300 + center[1],
    -400 + width + 5 + center[0], 300 + center[1]
)

""" Creating moon and set color. We overlay two ellipses, making Turkish moon """
setColor(255, 255, 204)
ellipse(550, 120, 50, 50)
setColor(7, 11, 52)
ellipse(560, 120, 50,50)

""" Create stars, using random positions and ellipse function.
   If you want more/less stars, change 150 to any number you wish """

setColor(255, 255, 204)
for i in range(150):
    x = random.randint(0, 800)
    y = random.randint(0,300)
    ellipse(x,y,1,1)

""" Initialize lists of coordinates. """
xt = [0 for i in range(3*n)]
xb = [0 for i in range(3*n)]
yt = [0 for i in range(3*n)]
yb = [0 for i in range(3*n)]


""" Set first coordinates. We use four equations four our blocks """
xt[0] = -399
yt[0] = -200

xt[1] = xt[0] + width
yt[1] = yt[0]

yt[2] = yt[1] + density
xt[2] = yt[2] * (width - 399) / -200


""" Initialize other coordinates """
for i in range(1,n):
    xt[i * 3] = xt[3*i-1]
    yt[i * 3] = xt[3*i] * (-200)/-399

    yt[3*i+1] = yt[3*i]
    xt[3*i + 1] = yt[3*i + 1] * (width - 399) / (-200)

    yt[3*i + 2] = yt[3*i + 1] + (coef ** (i)) * density
    xt[3*i + 2] = yt[3 * i + 2] * (width - 399) / (-200)

for i in range(3*n):
    xb[i] = xt[i]

yb[0] = 299

yb[1] = yb[0]

yb[2] = xb[2]*299/(width - 399)

for i in range(1,n):
    yb[3*i] = xb[3*i]* 299/-399
    yb[3*i + 1] = xb[3*i + 1]* 299/(width - 399)
    yb[3*i+2] = xb[3*i + 2] * 299/(width - 399)


setColor(60, 60, 65)
xt_cen = [i + center[0] for i in xt]
xb_cen = [i + center[0] for i in xb]
yt_cen = [i + center[1] for i in yt]
yb_cen = [i + center[1] for i in yb]

al = -200 / (width - 399)

""" Creating blocks using polygon and appropriate coordinates """
for i in range(0, n):
    setColor(40, 40, 50)
    polygon(
        xt_cen[3*i], yt_cen[i*3],
        xb_cen[i*3], yb_cen[i*3],
        xb_cen[1+i*3], yb_cen[i*3+1],
        xt_cen[1+i*3], yt_cen[1+i*3]
    )
    setColor(60, 60, 65)
    polygon(
        xt_cen[i*3+1], yt_cen[i*3],
        xb_cen[i*3+1], yb_cen[i*3],
        xb_cen[2+i*3], yb_cen[i*3+2],
        xt_cen[2+i*3], yt_cen[2+i*3]
    )

""" Creating block's lines to highlight them to black color """
setColor(19, 19, 19)
for i in range(3*n-1):
    line(xt[i] + center[0],yt[i] + center[1],xt[i + 1] + center[0], yt[i + 1] + center[1])
    line(xb[i] + center[0],yb[i] + center[1],xb[i + 1] + center[0], yb[i + 1] + center[1])

for i in range(3*n-1):
    line(xt[i] + center[0],yt[i] + center[1],xb[i] + center[0], yb[i] + center[1])


""" Initialize lists of coordinates for blocks that are at right side """
setColor(7, 17, 80)
xt_cen = [-i + center[0] for i in xt]
xb_cen = [-i + center[0] for i in xb]
yt_cen = [i + center[1] for i in yt]
yb_cen = [i + center[1] for i in yb]

""" Creating blocks from right side """
for i in range(0, n):
    setColor(30, 30, 50)
    polygon(
        xt_cen[3*i], yt_cen[i*3],
        xb_cen[i*3], yb_cen[i*3],
        xb_cen[1+i*3], yb_cen[i*3+1],
        xt_cen[1+i*3], yt_cen[1+i*3]
    )
    setColor(40, 40, 45)
    polygon(
        xt_cen[i*3+1], yt_cen[i*3],
        xb_cen[i*3+1], yb_cen[i*3],
        xb_cen[2+i*3], yb_cen[i*3+2],
        xt_cen[2+i*3], yt_cen[2+i*3]
    )

""" Creating block's lines to highlight them to black color """
setColor(19, 19, 19)
for i in range(3*n -1):
    line(xt_cen[i] ,yt[i] + center[1],xt_cen[i + 1], yt[i + 1] + center[1])
    line(xb_cen[i] ,yb[i] + center[1],xb_cen[i + 1], yb[i + 1] + center[1])

for i in range(3*n -1):
    line(xt_cen[i] ,yt[i] + center[1],xb_cen[i], yb[i] + center[1])

""" Set the background color """
background(7, 11, 52)
