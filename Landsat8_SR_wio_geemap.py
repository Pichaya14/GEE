import ee 
from ee_plugin import Map

#*** Start of imports. If edited, may not auto-convert in the playground. ***#
wio =

    # shown: False #
    # displayProperties: [
      {
        "type": "rectangle"
      }
    ] #
    ee.Geometry.Polygon(
        [[[-1.1801562499999951, 22.240800146484577],
          [-1.1801562499999951, -40.201954377811155],
          [81.08546875, -40.201954377811155],
          [81.08546875, 22.240800146484577]]], None, False)
#**** End of imports. If edited, may not auto-convert in the playground. ****#
# This example demonstrates the use of the Landsat 8 Collection 2, Level 2
# QA_PIXEL band (CFMask) to mask unwanted pixels.

def maskL8sr(image):
  # Bit 0 - Fill
  # Bit 1 - Dilated Cloud
  # Bit 2 - Cirrus
  # Bit 3 - Cloud
  # Bit 4 - Cloud Shadow
  qaMask = image.select('QA_PIXEL').bitwiseAnd(parseInt('11111', 2)).eq(0)
  saturationMask = image.select('QA_RADSAT').eq(0)

  # Apply the scaling factors to the appropriate bands.
  opticalBands = image.select('SR_B.').multiply(0.0000275).add(-0.2)
  thermalBands = image.select('ST_B.*').multiply(0.00341802).add(149.0)

  # Replace the original bands with the scaled ones and apply the masks.
  return image.addBands(opticalBands, None, True) \
      .addBands(thermalBands, None, True) \
      .updateMask(qaMask) \
      .updateMask(saturationMask)


# Map the function over one year of data.
collection = ee.ImageCollection('LANDSAT/LC08/C02/T1_L2') \
                     .filterDate('2015-01-01', '2022-12-31') \
                     .map(maskL8sr)

composite = collection.median().clip(wio)

# Display the results.
Map.setCenter(-4.52, 40.29, 7);  # Iberian Peninsula
Map.addLayer(composite, {'bands': ['SR_B4',  'SR_B3',  'SR_B2'], 'min': 0, 'max': 0.3})


Export.image.toDrive({
  'image' : composite,
  'description': 'L8_SR_wio_2015_2022',
  'maxPixels': 3784216672400,
  'region' : wio})
Map