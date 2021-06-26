import noiseGen
from PIL import Image
import numpy as np

testMap = noiseGen.genMap(200, 10, np.random.randint(1000))

blue = [65,105,225]
green = [34,139,34]
beach = [238, 214, 175]
snow = [255, 250, 250]
mountain = [139, 137, 137]

color_map = np.zeros((testMap.shape[1], testMap.shape[0], 3), dtype=np.uint8)
for i in range(testMap.shape[0]):
    for j in range(testMap.shape[1]):
        if testMap[i][j] < -0.05:
            color_map[i][j] = blue
        elif testMap[i][j] < 0:
            color_map[i][j] = beach
        elif testMap[i][j] < 0.6:
            color_map[i][j] = green
        elif testMap[i][j] < 0.7:
            color_map[i][j] = mountain
        elif testMap[i][j] < 9:
            color_map[i][j] = snow

img = Image.fromarray(color_map, 'RGB')
img.show()