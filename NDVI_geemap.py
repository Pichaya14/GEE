import ee 
from ee_plugin import Map

# Import the Landsat 8 TOA image collection.
l8 = ee.ImageCollection('LANDSAT/LC08/C01/T1_TOA')

# Get the least cloudy image in 2015.
image = ee.Image(
  l8.filterBounds() \
    .filterDate('2015-01-01', '2015-12-31') \
    .sort('CLOUD_COVER') \
    .first()
)

# Compute the Normalized Difference Vegetation Index (NDVI).
nir = image.select('B5')
red = image.select('B4')
ndvi = nir.subtract(red).divide(nir.add(red)).rename('NDVI')

# Display the result.
Map.centerObject(image, 9)
ndviParams = {'min': -1, 'max': 1, 'palette': ['blue', 'white', 'green']}
Map.addLayer(ndvi, ndviParams, 'NDVI image')

def addNDVI(image):
  ndvi = image.normalizedDifference(['B5', 'B4']).rename('NDVI')
  return image.addBands(ndvi)


# Test the addNDVI function on a single image.
ndvi = addNDVI(image).select('NDVI')

Map