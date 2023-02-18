import ee 
from ee_plugin import Map

#*** Start of imports. If edited, may not auto-convert in the playground. ***#
image = ee.Image("users/PichayaMelody123/wiosymmarin"),
    wiosym_roi =

    # displayProperties: [
      {
        "type": "rectangle"
      }
    ] #
    ee.Geometry.Polygon(
        [[[7.3828125, 16.636191878397664],
          [7.3828125, -40.979898069620134],
          [79.1015625, -40.979898069620134],
          [79.1015625, 16.636191878397664]]], None, False)
#**** End of imports. If edited, may not auto-convert in the playground. ****#

roi = ee.FeatureCollection(wiosym_roi).geometry


collection = ee.ImageCollection('COPERNICUS/S5P/OFFL/L3_HCHO') \
  .select('tropospheric_HCHO_column_number_density') \
  .filterDate('2019-06-01', '2019-06-06')



band_viz = {
  'min': 0.0,
  'max': 0.0003,
  'palette': ['black', 'blue', 'purple', 'cyan', 'green', 'yellow', 'red']
}

Map.addLayer(collection.mean(), band_viz, 'S5P HCHO')
Map.setCenter(0.0, 0.0, 2)


Export.image.toDrive({
  'image' : collection.mean().clip(roi),
  'description': 'HCHO',
  'maxPixels': 3784216672400,
  'region' : roi})
Map