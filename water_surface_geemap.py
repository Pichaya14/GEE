import ee 
from ee_plugin import Map

#*** Start of imports. If edited, may not auto-convert in the playground. ***#
wio = ee.Image("users/PichayaMelody123/wiosymmarin"),
    roi =

    # displayProperties: [
      {
        "type": "rectangle"
      }
    ] #
    ee.Geometry.Polygon(
        [[[7.600390625000015, 16.357749805052997],
          [7.600390625000015, -44.672032402835995],
          [79.49492187500002, -44.672032402835995],
          [79.49492187500002, 16.357749805052997]]], None, False)
#**** End of imports. If edited, may not auto-convert in the playground. ****#

wiosym = ee.Image('users/PichayaMelody123/wiosymmarin')
Map.addLayer(wiosym)


dataset = ee.Image('WORLDCLIM/V1/BIO')
annualMeanTemperature = dataset.select('bio12').clip(roi)
visParams = {
  'min': -230.0,
  'max': 300.0,
  'palette': ['blue', 'purple', 'cyan', 'green', 'yellow', 'red'],
}
Map.setCenter(71.72, 52.48, 3.0)
Map.addLayer(annualMeanTemperature, visParams, 'Annual rain perception')
Map