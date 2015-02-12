import sys


if __name__ == '__main__':
	worldmapx = []
	for x in range(10):
		worldmapy = []
		for y in range(10):
			tile = {'type': 'Grass', 'height': (y*x)}
			worldmapy.append(tile)
		worldmapx.append(worldmapy);
	for i in worldmapx:
		print i

	print "hey!"
	print worldmapx[4][5]['type']
	print worldmapx[4][5]['height']
