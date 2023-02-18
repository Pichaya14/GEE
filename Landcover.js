/**** Start of imports. If edited, may not auto-convert in the playground. ****/
var wio_aoi = 
    /* color: #d63000 */
    /* displayProperties: [
      {
        "type": "rectangle"
      }
    ] */
    ee.Geometry.Polygon(
        [[[-1.6739118878374493, 23.01617109796296],
          [-1.6739118878374493, -45.01365005604784],
          [86.91983811216255, -45.01365005604784],
          [86.91983811216255, 23.01617109796296]]], null, false);
/***** End of imports. If edited, may not auto-convert in the playground. *****/
var dataset = ee.Image('COPERNICUS/CORINE/V20/100m/2012');
var landCover = dataset.select('landcover');

var aoi =ee.FeatureCollection(wio_aoi).geometry();


Map.addLayer(landCover.clip(aoi), {}, 'Land Cover');



Export.image.toDrive({
  image : landCover.clip(aoi),
  description: 'Landcover',
  maxPixels: 3784216672400,
  region : aoi});
