import ee 
from ee_plugin import Map

#*** Start of imports. If edited, may not auto-convert in the playground. ***#
wio_aoi =

    # shown: False #
    # displayProperties: [
      {
        "type": "rectangle"
      }
    ] #
    ee.Geometry.Polygon(
        [[[-1.6739118878374493, 23.01617109796296],
          [-1.6739118878374493, -45.01365005604784],
          [86.91983811216255, -45.01365005604784],
          [86.91983811216255, 23.01617109796296]]], None, False)
#**** End of imports. If edited, may not auto-convert in the playground. ****#
dataset = ee.FeatureCollection("WWF/HydroSHEDS/v1/FreeFlowingRivers")

dataset = dataset.style(**{
  'color': "B2B2B3",
  'width': 1.0,
})

aoi = ee.FeatureCollection(wio_aoi).geometry()

Map.addLayer(dataset.clip(aoi), {}, "Free Flowing Rivers")
Map