import ee 
from ee_plugin import Map

#*** Start of imports. If edited, may not auto-convert in the playground. ***#
wio =

    # displayProperties: [
      {
        "type": "rectangle"
      }
    ] #
    ee.Geometry.Polygon(
        [[[4.785883945950329, 17.739482729228445],
          [4.785883945950329, -42.34944760379102],
          [79.66869644595033, -42.34944760379102],
          [79.66869644595033, 17.739482729228445]]], None, False)
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

aoi=ee.feature(wio)
# Map the function over one year of data.
collection = ee.ImageCollection('LANDSAT/LC08/C02/T1_L2') \
                     .filterBound('geometry') \
                     .filterDate('2020-01-01', '2021-01-01') \
                     .map(maskL8sr)

composite = collection.median()

# Display the results.
Map.setCenter(wio);  # wio
Map.addLayer(composite, {'bands': ['SR_B4',  'SR_B3',  'SR_B2'], 'min': 0, 'max': 0.3})
Map