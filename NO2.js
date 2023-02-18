/**** Start of imports. If edited, may not auto-convert in the playground. ****/
var wiosym_mask = ee.Image("users/PichayaMelody123/wiosymmarin"),
    wiosym_roi = 
    /* color: #d63000 */
    /* shown: false */
    /* displayProperties: [
      {
        "type": "rectangle"
      }
    ] */
    ee.Geometry.Polygon(
        [[[7.481914062500019, 16.19710227789944],
          [7.481914062500019, -40.39396681696679],
          [78.32175781250001, -40.39396681696679],
          [78.32175781250001, 16.19710227789944]]], null, false);
/***** End of imports. If edited, may not auto-convert in the playground. *****/
var roi= ee.FeatureCollection(wiosym_roi).geometry();

var collection = ee.ImageCollection('COPERNICUS/S5P/OFFL/L3_NO2')
  .select('tropospheric_NO2_column_number_density')
  .filterDate('2021-01-01', '2021-12-01')
 

var wiosym = ee.Image ('users/PichayaMelody123/wiosymmarin');


print(collection);

var band_viz = {
  min: 0,
  max: 0.0002,
  palette: ['black', 'blue', 'purple', 'cyan', 'green', 'yellow', 'red']
};
Map.addLayer(wiosym);
Map.addLayer(collection.mean().clip(roi), band_viz, 'S5P N02');

Export.image.toDrive({
  image : collection.mean().clip(roi),
  description: 'NO2_wio',
  maxPixels: 3784216672400,
  region : roi});
