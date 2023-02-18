/**** Start of imports. If edited, may not auto-convert in the playground. ****/
var wio_aoi = 
    /* color: #98ff00 */
    /* displayProperties: [
      {
        "type": "rectangle"
      }
    ] */
    ee.Geometry.Polygon(
        [[[0.8315155157994969, 22.417769841288237],
          [0.8315155157994969, -47.64567491682718],
          [85.9096405157995, -47.64567491682718],
          [85.9096405157995, 22.417769841288237]]], null, false);
/***** End of imports. If edited, may not auto-convert in the playground. *****/

var dataset = ee.Image('WWF/HydroSHEDS/30CONDEM');
var elevation = dataset.select('b1');
var elevationVis = {
  min: -50.0,
  max: 3000.0,
  gamma: 2.0,
};
var aoi = ee.FeatureCollection(wio_aoi).geometry(); 

Map.addLayer(elevation.clip(aoi), elevationVis, 'Elevation');
Export.image.toDrive({
  image : elevation.clip(aoi),
  description: 'DEM_WIO',
  maxPixels: 3784216672400,
  region : aoi});
