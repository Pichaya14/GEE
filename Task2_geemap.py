import ee 
from ee_plugin import Map

#*** Start of imports. If edited, may not auto-convert in the playground. ***#
ROI =

    # displayProperties: [
      {
        "type": "rectangle"
      }
    ] #
    ee.Geometry.Polygon(
        [[[-3.084855508204458, 22.891885047810465],
          [-3.084855508204458, -47.29840236248417],
          [88.67295699179554, -47.29840236248417],
          [88.67295699179554, 22.891885047810465]]], None, False)
#**** End of imports. If edited, may not auto-convert in the playground. ****#
dataset = ee.ImageCollection("JAXA/GCOM-C/L3/OCEAN/CHLA/V3").clip(ROI) \
                .filterDate('2021-12-01', '2022-01-01') \
                .filter(ee.Filter.eq("SATELLITE_DIRECTION", "D"))

# Multiply with slope coefficient
image = dataset.mean().multiply(0.0016).log10()

vis = {
  'bands': ['CHLA_AVE'],
  'min': -2,
  'max': 2,
  'palette': [
    '3500a8','0800ba','003fd6',
    '00aca9','77f800','ff8800',
    'b30000','920000','880000'
  ]
}

Map.addLayer(image, vis, "Chlorophyll-a concentration")
Map