import numpy as np 


# Load facedata.npy as ndarray
face_data = np.load('facedata.npy')
print face_data.item().keys()

# Load albedo matrix 
albedo = face_data.item().get('albedo')
print albedo

# Load uniform albedo matrix
uniform_albedo = face_data.item().get('uniform_albedo')
print uniform_albedo

# Load heightmap 
heightmap = face_data.item().get('heightmap')
print heightmap

# Load light source
light_source = face_data.item().get('lightsource')
print light_source