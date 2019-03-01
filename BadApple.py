# Code to convert every frame into a graphical plot

from PIL import Image

# Iterate through every frame extracted from the video (Only every 5th frame was extracted)
for frameCounter in range(0, 32855, 5):
    im = Image.open(".\\Bad Apple Frames\\frame" + str(frameCounter) + ".jpg", "r")
    output = open(".\\Bad_Apple_matplotlib_code\\" + str(frameCounter) + ".txt", "a+")
    whiteX = []
    whiteY = []

    plotPoints1 = "plt.plot(["

    x = 0
    y = 0

    # There is a total of 691200 pixels in this list (so 691200 pixels per frame)
    pix_val = list(im.getdata())

    # Loop through every single pixel in the frame
    for pixel in range(len(pix_val)):

        # If the column of the frame is finished, go on to the next column
        if (y == 960):
            y = 0
            x += 1

        # If the pixel is white (rgb = 0,0,0), add the coordinates of the white pixel into the arrays
        if(pix_val[pixel][0] == 0):
            whiteX.append(x)
            whiteY.append(y)

        y += 1

    #Begin inserting x-coordinates
    for index in range(len(whiteX)):
        plotPoints1 += str(whiteX[index]) + ","

    # Remove trailing comma
    plotPoints1 = plotPoints1[:-1]

    # Begin inserting y-coordinates
    plotPoints1 += "], ["

    for index in range(len(whiteY)):
        plotPoints1 += str(whiteY[index]) + ","

    # Remove trailing comma
    plotPoints1 = plotPoints1[:-1]

    # Complete the statement
    plotPoints1 += "], 'k.')"

    # If the screen is white, change the broken line of code into a working one
    if plotPoints1=="plt.plot(], ], 'k.')":
        plotPoints1 = "plt.plot([], [], 'k.')"

    # Write code for matplotlib into txt files
    output.write("import matplotlib.pyplot as plt\n\n\n")
    output.write(plotPoints1+"\n")
    output.write("plt.subplots_adjust(top=1.00, bottom=0.00, left=0.30, right=0.90, hspace=0.20, wspace=0.20)\n")
    output.write("plt.xlim(0, 720)\n")
    output.write("plt.ylim(0, 960)\n")
    output.write("plt.axis([0, 720, 0, 960])\n")
    output.write("plt.savefig('." + "\\\\" + "Bad_Apple_matplotlib_plots" + "\\\\")
    output.write(str(frameCounter) + ".jpg')")

    output.close
