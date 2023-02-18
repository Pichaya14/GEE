import ee 
from ee_plugin import Map

#*** Start of imports. If edited, may not auto-convert in the playground. ***#
AOI2 =

    # shown: False #
    # displayProperties: [
      {
        "type": "rectangle"
      }
    ] #
    ee.Geometry.Polygon(
        [[[-0.6700541379996361, 20.256302660281214],
          [-0.6700541379996361, -42.46052317558683],
          [85.28697711200036, -42.46052317558683],
          [85.28697711200036, 20.256302660281214]]], None, False)
#**** End of imports. If edited, may not auto-convert in the playground. ****#

#COPERNICUS/S2_CLOUD_PROBABILITY dataset, the
# ee.Algorithms.Sentinel2.CDI() method for computing a
# cloud displacement index and directionalDistanceTransform()
# for computing cloud shadows.
# Sentinel-2 Level 1C data.  Bands B7, B8, B8A and B10 from this
# dataset are needed as input to CDI and the cloud mask function.
s2 = ee.ImageCollection('COPERNICUS/S2')
# Cloud probability dataset.  The probability band is used in
# the cloud mask function.
s2c = ee.ImageCollection('COPERNICUS/S2_CLOUD_PROBABILITY')
# Sentinel-2 surface reflectance data for the composite.
s2Sr = ee.ImageCollection('COPERNICUS/S2_SR')


# Dates over which to create a median composite.
start = ee.Date('2020-01-01')
end = ee.Date('2020-12-31')

studyArea = ee.FeatureCollection(AOI2). geometry()

def func_gxe(feature):
 # return feature.simplify({maxError: 100})
#studyArea = Area.map(func_gxe)


#studyArea = ee.FeatureCollection(NMD).geometry()
# Simplify the feature
#studyAreaSimple = ee.Feature(studyArea).simplify({maxError: 100000})

Map.centerObject(studyArea, 14)


# S2 L1C for Cloud Displacement Index (CDI) bands.

def func_hyn(image)return image.clip(studyArea)}:
s2 = s2.filterBounds(studyArea).filterDate(start, end).map(function(image){return image.clip(studyArea)}
s2 = s2.filterBounds(studyArea).filterDate(start, end).map(func_hyn) \
    .select(['B7', 'B8', 'B8A', 'B10', 'B11'])

# S2Cloudless for the cloud probability band.
s2c = s2c.filterDate(start, end) \
         .filterBounds(studyArea)

def func_dkk(image)return image.clip(studyArea)};: \
         .map(function(image){return image.clip(studyArea)} \
         .map(func_dkk)

# S2 L2A for surface reflectance bands.
s2Sr = s2Sr.filterDate(start, end) \
         .filterBounds(studyArea)

def func_fal(image)return image.clip(studyArea)}: \
         .map(function(image){return image.clip(studyArea)} \
         .map(func_fal) \
         .select(['B2', 'B3', 'B4', 'B5','B11','B12'])


# Join two collections on their 'system:index' property.
# The propertyName parameter is the name of the property
# that references the joined image.

def indexJoin(collectionA, collectionB, propertyName):
  joined = ee.ImageCollection(ee.Join.saveFirst(propertyName).apply({
    'primary': collectionA,
    'secondary': collectionB,
    'condition': ee.Filter.equals({
      'leftField': 'system:index',
      'rightField': 'system:index'})
  }))
  # Merge the bands of the joined image.

def func_crq(image):
    return image.addBands(ee.Image(image.get(propertyName)).clip(studyArea))

  return joined.map(func_crq)





# Aggressively mask clouds and shadows.
def maskImage(image):
  # Compute the cloud displacement index from the L1C bands.
  cdi = ee.Algorithms.Sentinel2.CDI(image)
  s2c = image.select('probability').clip(studyArea)
  cirrus = image.select('B10').multiply(0.0001).clip(studyArea)

  # Assume low-to-mid atmospheric clouds to be pixels where probability
  # is greater than 65%, and CDI is less than -0.5. For higher atmosphere
  # cirrus clouds, assume the cirrus band is greater than 0.01.
  # The final cloud mask is one or both of these conditions.
  isCloud = s2c.gt(65).And(cdi.lt(-0.5)).Or(cirrus.gt(0.01))

  # Reproject is required to perform spatial operations at 10m scale.

  isCloud = isCloud.focal_min(3).focal_max(16)
  isCloud = isCloud.reproject({'crs': cdi.projection(), 'scale': 10})

  # Project shadows from clouds we found in the last step(UTM)
  shadowAzimuth = ee.Number(90) \
      .subtract(ee.Number(image.get('MEAN_SOLAR_AZIMUTH_ANGLE')))

  # With the following reproject, the shadows are projected 5km.
  isCloud = isCloud.directionalDistanceTransform(shadowAzimuth, 50)
  isCloud = isCloud.reproject({'crs': cdi.projection(), 'scale': 100})

  isCloud = isCloud.select('distance').mask()
  return image.select('B2', 'B3' ,'B4','B5','B12').updateMask(isCloud.Not().clip(studyArea))


# Join the cloud probability dataset to surface reflectance.
withCloudProbability = indexJoin(s2Sr, s2c, 'cloud_probability')
# Join the L1C data to get the bands needed for CDI.
withS2L1C = indexJoin(withCloudProbability, s2, 'l1c')

# Map the cloud masking function over the joined collection.
masked = ee.ImageCollection(withS2L1C.map(maskImage))

# Take the median, specifying a tileScale to avoid memory errors.
median = masked.reduce(ee.Reducer.median(), (20)).clip(studyArea)
print (median)


# Covert pixel value to TOA reflectance divide by 10,000
#Green_ref = median.expression (
  # 'GREEN/10000', {
  # 'GREEN': median.select('B3_median'),})

#Red_ref = median.expression (
  # 'RED/10000', {
   #'RED': median.select('B4_median'),})

#Blue_ref = median.expression (
  #  'BLUE/10000', {
   #   'BLUE': median.select('B2_median'),})

# Display the results.
viz = {'bands': ['B4_median', 'B3_median', 'B2_median'], 'min': 0, 'max': 3000}
#print (Green_ref)
#print (Red_ref)
#print(Blue_ref)


Map.addLayer(median.clip(studyArea),viz, 'median_cloundfree')
Map.addLayer(studyArea)

#Applied turbidity measurement equation red-0.0014/0.0013
TU = median.expression(
    '((RED/10000) - 0.014) / (0.013)', {
    'RED': median.select('B4_median'),

})
#applied (B3*B5)/(B4+B12)
#v1 = median.expression('((B3)*(B5))/(B4+B12))', {
   #'B3': median.select('B3_median'), 'B5': median.select('B5_median'), 'B4': median.select('B4_median'), 'B12_median': median.select('B12_median')})


#applied (B3+B5)/(B2/B3)
#v2 = median.expression('(((B3_median)+(B5_median))/((B2_median)/(B3_median))', {
   #'B3_median': median.select('B3_median'), 'B5_median': median.select('B5_median'), 'B4_median': median.select('B4_median'), 'B2_median': median.select('B2_median')})

##v2Viz = {min:-1, max: 2, palette: ['00FFFF', '0000FF']}


#applied NDTI Red-green/red+green
#TU = median.expression('(((RED/10000)+(Blue/10000))-(Green/10000))/(((RED/10000)+(Blue/10000))+(Green/10000))', {
  #  'RED': median.select('B4_median'), 'Green': median.select('B3_median'), 'Blue': median.select('B2_median')})

TUViz = {'min':-1, 'max': 2, 'palette': ['00FFFF', '0000FF']}
#NDTIViz = {min:-1, max: 2, palette: ['00FFFF', '0000FF']}
#Red_refViz =  {min:0, max:0.1, palette: ['6c3082', '78184a']}

#Map.addLayer(v1,v1Viz, 'v1', False)
#Map.addLayer(v2,v2Viz, 'v2', False)

#Map.addLayer(NDTI,NDTIViz, 'NDTI', False)
Map.addLayer(TU,TUViz, 'TURBIDITY_O', False)
#Map.addLayer(Red_ref, Red_refViz, 'red_median_ref')
print(TU)




#Export the image, specifying scale and region.


Export.image.toDrive({
  'image': TU,
  'description': 'TU',
  'scale': 1000,
  'region' : TU
})




  #scale: 10,
  #region : AOI2
#})



Map