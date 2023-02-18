import ee 
from ee_plugin import Map

#*** Start of imports. If edited, may not auto-convert in the playground. ***#
AOI =

    # shown: False #
    # displayProperties: [
      {
        "type": "rectangle"
      },
      {
        "type": "rectangle"
      }
    ] #
    ee.Geometry.MultiPolygon(
        [[[[3.106980421385961, 23.022987400889438],
           [3.106980421385961, -51.76520991741075],
           [81.15385542138596, -51.76520991741075],
           [81.15385542138596, 23.022987400889438]]],
         [[[18.57573042138596, 36.97133334830778],
           [18.57573042138596, 36.97133334830778],
           [18.57573042138596, 36.97133334830778],
           [18.57573042138596, 36.97133334830778]]]], None, False)
#**** End of imports. If edited, may not auto-convert in the playground. ****#
imgVV = ee.ImageCollection('COPERNICUS/S1_GRD') \
        .filter(ee.Filter.listContains('transmitterReceiverPolarisation', 'VV')) \
        .filter(ee.Filter.eq('instrumentMode', 'IW')) \
        .select('VV')

def func_lrc(image):
          edge = image.lt(-30.0)
          maskedImage = image.mask().And(edge.Not())
          return image.updateMask(maskedImage) \
        .map(func_lrc)






desc = imgVV.filter(ee.Filter.eq('orbitProperties_pass', 'DESCENDING'))
asc = imgVV.filter(ee.Filter.eq('orbitProperties_pass', 'ASCENDING'))

spring = ee.Filter.date('2015-03-01', '2020-04-20')
lateSpring = ee.Filter.date('2015-04-21', '2020-06-10')
summer = ee.Filter.date('2015-06-11', '2020-08-31')

descChange = ee.Image.cat(
        desc.filter(spring).mean(),
        desc.filter(lateSpring).mean(),
        desc.filter(summer).mean())

ascChange = ee.Image.cat(
        asc.filter(spring).mean(),
        asc.filter(lateSpring).mean(),
        asc.filter(summer).mean())


Map.addLayer(ascChange, {'min': -25, 'max': 5}, 'Multi-T Mean ASC', True)
Map.addLayer(descChange, {'min': -25, 'max': 5}, 'Multi-T Mean DESC', True)
Map