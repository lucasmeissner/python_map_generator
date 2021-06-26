import numpy as np
from perlin_noise import PerlinNoise


def genMap(mapSize, octave, seed):
    shape = (mapSize, mapSize)
    noise = PerlinNoise(octaves=octave, seed=seed)
    noise2 = PerlinNoise(octaves=octave*4, seed=seed)
    noise3 = PerlinNoise(octaves=octave*6, seed=seed)
    noiseMap = np.zeros(shape)

    for i in range(shape[0]):
        for j in range(shape[1]):
            noiseVal = noise([i/mapSize, j/mapSize])
            noiseVal += 0.3 * noise([i/mapSize, j/mapSize])
            noiseVal += 0.1 * noise([i/mapSize, j/mapSize])
            noiseMap[i][j] = noiseVal
    
    return noiseMap
