import ee 
from ee_plugin import Map

#*** Start of imports. If edited, may not auto-convert in the playground. ***#
roi =

    # shown: False #
    # displayProperties: [
      {
        "type": "rectangle"
      }
    ] #
    ee.Geometry.Polygon(
        [[[-4.918656349182129, 25.23839327459631],
          [-4.918656349182129, -49.78576313476571],
          [78.75321865081787, -49.78576313476571],
          [78.75321865081787, 25.23839327459631]]], None, False),
    imageVisParam = {"opacity":1,"bands":["jan"],"min":0,"max":380,"palette":["ecffbd","ffff00","3af6ff","467aff","313eff","0008ff"]}
#**** End of imports. If edited, may not auto-convert in the playground. ****#
jan = ee.Image("OpenLandMap/CLM/CLM_PRECIPITATION_SM2RAIN_M/v01")
print(jan)

feb = ee.Image("OpenLandMap/CLM/CLM_PRECIPITATION_SM2RAIN_M/v01")

march = ee.Image("OpenLandMap/CLM/CLM_PRECIPITATION_SM2RAIN_M/v01")

apr = ee.Image("OpenLandMap/CLM/CLM_PRECIPITATION_SM2RAIN_M/v01")

may = ee.Image("OpenLandMap/CLM/CLM_PRECIPITATION_SM2RAIN_M/v01")

jun = ee.Image("OpenLandMap/CLM/CLM_PRECIPITATION_SM2RAIN_M/v01")

jul= ee.Image("OpenLandMap/CLM/CLM_PRECIPITATION_SM2RAIN_M/v01")

aug = ee.Image("OpenLandMap/CLM/CLM_PRECIPITATION_SM2RAIN_M/v01")

sep = ee.Image("OpenLandMap/CLM/CLM_PRECIPITATION_SM2RAIN_M/v01")

oct = ee.Image("OpenLandMap/CLM/CLM_PRECIPITATION_SM2RAIN_M/v01")

nov = ee.Image("OpenLandMap/CLM/CLM_PRECIPITATION_SM2RAIN_M/v01")

dec = ee.Image("OpenLandMap/CLM/CLM_PRECIPITATION_SM2RAIN_M/v01")

visualization = {
  'bands': ['jan'],
  'min': 0.0,
  'max': 380.0,
  'palette': ['ecffbd', 'ffff00', '3af6ff', '467aff', '313eff', '0008ff']
}

visualization = {
  'bands': ['feb'],
  'min': 0.0,
  'max': 380.0,
  'palette': ['ecffbd', 'ffff00', '3af6ff', '467aff', '313eff', '0008ff']
}

visualization = {
  'bands': ['mar'],
  'min': 0.0,
  'max': 380.0,
  'palette': ['ecffbd', 'ffff00', '3af6ff', '467aff', '313eff', '0008ff']
}

visualization = {
  'bands': ['apr'],
  'min': 0.0,
  'max': 380.0,
  'palette': ['ecffbd', 'ffff00', '3af6ff', '467aff', '313eff', '0008ff']
}

visualization = {
  'bands': ['maj'],
  'min': 0.0,
  'max': 380.0,
  'palette': ['ecffbd', 'ffff00', '3af6ff', '467aff', '313eff', '0008ff']
}

visualization = {
  'bands': ['jun'],
  'min': 0.0,
  'max': 380.0,
  'palette': ['ecffbd', 'ffff00', '3af6ff', '467aff', '313eff', '0008ff']
}

visualization = {
  'bands': ['jul'],
  'min': 0.0,
  'max': 380.0,
  'palette': ['ecffbd', 'ffff00', '3af6ff', '467aff', '313eff', '0008ff']
}

visualization = {
  'bands': ['aug'],
  'min': 0.0,
  'max': 380.0,
  'palette': ['ecffbd', 'ffff00', '3af6ff', '467aff', '313eff', '0008ff']
}


visualization = {
  'bands': ['sep'],
  'min': 0.0,
  'max': 380.0,
  'palette': ['ecffbd', 'ffff00', '3af6ff', '467aff', '313eff', '0008ff']
}

visualization = {
  'bands': ['oct'],
  'min': 0.0,
  'max': 380.0,
  'palette': ['ecffbd', 'ffff00', '3af6ff', '467aff', '313eff', '0008ff']
}

visualization = {
  'bands': ['nov'],
  'min': 0.0,
  'max': 380.0,
  'palette': ['ecffbd', 'ffff00', '3af6ff', '467aff', '313eff', '0008ff']
}

visualization = {
  'bands': ['dec'],
  'min': 0.0,
  'max': 380.0,
  'palette': ['ecffbd', 'ffff00', '3af6ff', '467aff', '313eff', '0008ff']
}


Map.centerObject(roi)

Map.addLayer(jan.clip(roi), visualization, "Precipitation jan in mm")
Map.addLayer(feb.clip(roi), visualization, "Precipitation feb in mm")
Map.addLayer(march.clip(roi), visualization, "Precipitation march in mm")
Map.addLayer(apr.clip(roi), visualization, "Precipitation apr in mm")
Map.addLayer(may.clip(roi), visualization, "Precipitation may in mm")
Map.addLayer(jun.clip(roi), visualization, "Precipitation jun in mm")
Map.addLayer(jul.clip(roi), visualization, "Precipitation jul in mm")
Map.addLayer(aug.clip(roi), visualization, "Precipitation aug in mm")
Map.addLayer(sep.clip(roi), visualization, "Precipitation sep in mm")
Map.addLayer(oct.clip(roi), visualization, "Precipitation oct in mm")
Map.addLayer(nov.clip(roi), visualization, "Precipitation nov in mm")
Map.addLayer(dec.clip(roi), visualization, "Precipitation dec in mm")
Map