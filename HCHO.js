/**** Start of imports. If edited, may not auto-convert in the playground. ****/
var image = ee.Image("users/PichayaMelody123/wiosymmarin"),
    wiosym_roi = 
    /* color: #0b4a8b */
    /* displayProperties: [
      {
        "type": "rectangle"
      }
    ] */
    ee.Geometry.Polygon(
        [[[7.3828125, 16.636191878397664],
          [7.3828125, -40.979898069620134],
          [79.1015625, -40.979898069620134],
          [79.1015625, 16.636191878397664]]], null, false);
/***** End of imports. If edited, may not auto-convert in the playground. *****/

var roi = ee.FeatureCollection(wiosym_roi).geometry;


var collection = ee.ImageCollection('COPERNICUS/S5P/OFFL/L3_HCHO')
  
  .select('tropospheric_HCHO_column_number_density')
  .filterDate('2019-06-01', '2019-06-06');



var band_viz = {
  min: 0.0,
  max: 0.0003,
  palette: ['black', 'blue', 'purple', 'cyan', 'green', 'yellow', 'red']
};

Map.addLayer(collection.mean(), band_viz, 'S5P HCHO');
Map.setCenter(0.0, 0.0, 2);


Export.image.toDrive({
  image : collection.mean().clip(roi),
  description: 'HCHO',
  maxPixels: 3784216672400,
  region : roi});
