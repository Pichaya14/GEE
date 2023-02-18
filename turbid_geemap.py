import ee 
from ee_plugin import Map

#*** Start of imports. If edited, may not auto-convert in the playground. ***#
AOI =

    # shown: False #
    # displayProperties: [
      {
        "type": "rectangle"
      }
    ] #
    ee.Geometry.Polygon(
        [[[-10.80595281780066, 25.762158839740746],
          [-10.80595281780066, -58.46965295691649],
          [100.99092218219934, -58.46965295691649],
          [100.99092218219934, 25.762158839740746]]], None, False)
#**** End of imports. If edited, may not auto-convert in the playground. ****#
dataset = ee.ImageCollection('COPERNICUS/S3/OLCI') \
                  .filterDate('2019-06-01', '2019-06-04')

roi = ee.FeatureCollection(AOI). geometry()
# Select bands for visualization and apply band-specific scale factors.
rgb = dataset.select(['Oa05_radiance']) \
              .median().clip(roi) \
              .multiply(ee.Image([0.0100953]))

visParams = {
  'min': 0,
  'max': 6,
  'gamma': 1.5,
}

Map.setCenter(46.043, 1.45, 5)
Map.addLayer(rgb, visParams, 'RGB')
Map