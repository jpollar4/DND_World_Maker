# Requires Python Image Library!

import sys
import Image
import random

if __name__ == '__main__':

	XSIZE = 2000
	YSIZE = 2000
	landtypes = {
		0: "desert",
		1: "grass",
		2: "forest",
		3: "mountain",
		4: "ocean",
		5: "dirt",
		6: "jungle",
		7: "snow",
	}

	worldmaparray = []
	for x in range(XSIZE):
		worldmapy = []
		for y in range(YSIZE):			
			tile = {'type': 4}
			worldmapy.append(tile)
		worldmaparray.append(worldmapy);


	for i in range (0,50):
		#make islands
		terraintype = random.randint(0,7);

		pointerx = random.randint(0,XSIZE-1)
		pointery = random.randint(0,YSIZE-1)
		worldmaparray[pointerx][pointery]['type'] = 1;
		while True:
			if(pointerx < 10 or pointerx > XSIZE-10 or pointery < 10 or pointery > YSIZE-10):
				break
			pointerx += (1 - random.randint(0,2))*5
			pointery += (1 - random.randint(0,2))*5
			for x in range(0,5):
				for y in range(0,5):
					if(pointery > (YSIZE-100) or pointery < 100):
						worldmaparray[pointerx + (2-x)][pointery+ (2-y)]['type'] = 7;
					else:
						worldmaparray[pointerx + (2-x)][pointery+ (2-y)]['type'] = terraintype;

			if random.randint(0,XSIZE*4) == 50:
				break




	img = Image.new( 'RGB', (XSIZE,YSIZE), "black") # create a new black image
	pixels = img.load() # create the pixel map
	

	for i in range(0, XSIZE):    # for every pixel:
	    for j in range(0, YSIZE):
	    	if(worldmaparray[i][j]['type'] == 0):
	    		pixels[i,j] = (254, 178, 102)
	    	elif(worldmaparray[i][j]['type'] == 1):
	    		pixels[i,j] = (0, 204, 0)
	    	elif(worldmaparray[i][j]['type'] == 2):
	    		pixels[i,j] = (51, 102, 0)
	    	elif(worldmaparray[i][j]['type'] == 3):
	    		pixels[i,j] = (64, 64, 64)
	    	elif(worldmaparray[i][j]['type'] == 4):
	    		pixels[i,j] = (51, 153, 255)
	    	elif(worldmaparray[i][j]['type'] == 5):
	    		pixels[i,j] = (102, 51, 0)
	    	elif(worldmaparray[i][j]['type'] == 6):
	    		pixels[i,j] = (25, 51, 0)	    		
	    	elif(worldmaparray[i][j]['type'] == 7):
	    		pixels[i,j] = (255, 255, 255)
	    	else:
	    		pixels[i,j] = (0, 0, 0)


	        
	 

	img.save('out.bmp')