/**** Start of imports. If edited, may not auto-convert in the playground. ****/
var wio = ee.Image("users/PichayaMelody123/wiosymmarin"),
    roi = 
    /* color: #98ff00 */
    /* shown: false */
    /* displayProperties: [
      {
        "type": "rectangle"
      }
    ] */
    ee.Geometry.Polygon(
        [[[7.600390625000015, 16.357749805052997],
          [7.600390625000015, -44.672032402835995],
          [79.49492187500002, -44.672032402835995],
          [79.49492187500002, 16.357749805052997]]], null, false);
/***** End of imports. If edited, may not auto-convert in the playground. *****/

var wiosym = ee.Image('users/PichayaMelody123/wiosymmarin');
Map.addLayer(wiosym);


var dataset = ee.ImageCollection('JRC/GSW1_3/MonthlyRecurrence');

var visualization = {
  bands: ['monthly_recurrence'],
  min: 0.0,
  max: 100.0,
  palette: ['ffffff', 'ffbbbb', '0000ff']
};



Map.addLayer(dataset, visualization, 'Monthly Recurrence');


Export.image.toDrive({
  image : dataset.mean().clip(roi),
  description: 'water_Recurrence',
  maxPixels: 3784216672400,
  region : roi});
