/**** Start of imports. If edited, may not auto-convert in the playground. ****/
var image = ee.Image("users/PichayaMelody123/wiosymmarin"),
    wiosym_roi = 
    /* color: #98ff00 */
    /* shown: false */
    /* displayProperties: [
      {
        "type": "rectangle"
      }
    ] */
    ee.Geometry.Polygon(
        [[[6.417613239267119, 17.06696465048263],
          [6.417613239267119, -40.639223540239065],
          [78.83948823926711, -40.639223540239065],
          [78.83948823926711, 17.06696465048263]]], null, false);
/***** End of imports. If edited, may not auto-convert in the playground. *****/
var roi= ee.FeatureCollection(wiosym_roi).geometry();

var collection = ee.ImageCollection('COPERNICUS/S5P/OFFL/L3_CO')
  .select('CO_column_number_density')
  .filterDate('2021-01-01', '2021-12-01');
 

var wiosym = ee.Image ('users/PichayaMelody123/wiosymmarin');


print(collection);

var band_viz = {
  min: 0,
  max: 0.05,
  palette: ['black', 'blue', 'purple', 'cyan', 'green', 'yellow', 'red']
};
Map.addLayer(wiosym);
Map.addLayer(collection.mean().clip(roi), band_viz, 'S5P_CO');

Export.image.toDrive({
  image : collection.mean().clip(roi),
  description: 'CO_wio21_1km',
  maxPixels: 3784216672400,
  region : roi});
