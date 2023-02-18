import ee 
from ee_plugin import Map

#*** Start of imports. If edited, may not auto-convert in the playground. ***#
aoi =

    # displayProperties: [
      {
        "type": "rectangle"
      }
    ] #
    ee.Geometry.Polygon(
        [[[-6.78915625000001, 23.328454152970004],
          [-6.78915625000001, -47.92641519630721],
          [79.34365624999998, -47.92641519630721],
          [79.34365624999998, 23.328454152970004]]], None, False)
#**** End of imports. If edited, may not auto-convert in the playground. ****#

# A function to mask out pixels that did not have observations.
def maskEmptyPixels(image):
  # Find pixels that had observations.
  withObs = image.select('num_observations_1km').gt(0)
  return image.updateMask(withObs)


# A function to mask out cloudy pixels.
def maskClouds(image):
  # Select the QA band.
  QA = image.select('state_1km')
  # Make a mask to get bit 10, the internal_cloud_algorithm_flag bit.
  bitMask = 1 << 10
  # Return an image masking out cloudy areas.
  return image.updateMask(QA.bitwiseAnd(bitMask).eq(0))


# Start with an image collection for a 1 month period.
# and mask out areas that were not observed.
collection = ee.ImageCollection('MODIS/006/MOD09GA') \
        .filterDate('2020-01-01', '2021-12-31') \
        .map(maskEmptyPixels)

# Get the total number of potential observations for the time interval.
totalObsCount = collection \
        .select('num_observations_1km') \
        .count()

# Map the cloud masking function over the collection.
collectionCloudMasked = collection.map(maskClouds)
print (collectionCloudMasked)
# Get the total number of observations for non-cloudy pixels for the time
# interval.  The result is unmasked to set to unity so that all locations
# have counts, and the ratios later computed have values everywhere.
clearObsCount = collectionCloudMasked \
        .select('num_observations_1km') \
        .count() \
        .unmask(0)
roi = ee.FeatureCollection(aoi).geometry()
modis_b1 = collectionCloudMasked.select('sur_refl_b01')
Band1 = modis_b1.reduce(ee.Reducer.median(), (14)).clip(roi)
print(modis_b1)
print(Band1)
#Applied turbidity measurement equation from http:#drr.ikcest.Org/static/upload/c2/c233934a-bbdb-11e8-b94f-00163e0618d6.pdf
SPM = Band1.expression( '-1.91*(1140.25*(b1))/10000',
   {'b1': Band1.select('sur_refl_b01_median'),})

print(SPM)
#Map.addLayer(
   # collectionCloudMasked.median(),
   # {bands: ['sur_refl_b01'],
   #  gain: 0.07,
    # gamma: 3
    #},
  #  'median of masked collection'
 # )

Map.addLayer(SPM,
    {'bands': ['constant'],
     'gain': 1,
     'gamma': 3
    },
    'Total suspended Matter (mg/l)'
  )



Map