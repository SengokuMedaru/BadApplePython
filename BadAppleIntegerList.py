# Linux files are ordered by sequence,
# so if they're not put in a list in integer order,
# the frames will be read in the order of 0.jpg, 1000.jpg, 1001.jpg 
# instead of 0.jpg, 1.jpg, 2.jpg.

# Thus, I've written a script to help order the frames properly

for frameCounter in range(0, 32855, 5):
    output = open(".\\BadAppleIntegerList.txt", "a+")
    output.write("file '" + str(frameCounter) + ".jpg'\n")

