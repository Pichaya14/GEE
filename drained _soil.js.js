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

var dataset = ee.ImageCollection("JAXA/GCOM-C/L3/OCEAN/CHLA/V1")
                .filterDate('2020-01-01', '2020-12-31')
                // filter to daytime data only
                .filter(ee.Filter.eq("SATELLITE_DIRECTION", "D"));

// Multiply with slope coefficient
var image = dataset.mean().multiply(0.0016);
print(image);
var vis = {
  bands: ['CHLA_AVE'],
  min: -2,
  max: 2,
  palette: [
    '3500a8','0800ba','003fd6',
    '00aca9','77f800','ff8800',
    'b30000','920000','880000'
  ]
};

Map.addLayer(image.clip(roi), vis, "Chlorophyll-a concentration");

Export.image.toDrive({
  image : image.clip(roi),
  description: 'Chl_a',
  maxPixels: 3784216672400,
  region : roi});