/**** Start of imports. If edited, may not auto-convert in the playground. ****/
var wio_area = ee.Image("users/PichayaMelody123/wiosymmarin"),
    aoi = 
    /* color: #d63000 */
    /* displayProperties: [
      {
        "type": "rectangle"
      }
    ] */
    ee.Geometry.Polygon(
        [[[7.438755266211179, 16.46769474828897],
          [7.438755266211179, -40.58058466412763],
          [78.98172401621117, -40.58058466412763],
          [78.98172401621117, 16.46769474828897]]], null, false),
    geometry = 
    /* color: #98ff00 */
    /* shown: false */
    ee.Geometry.MultiPoint();
/***** End of imports. If edited, may not auto-convert in the playground. *****/

// SALT MARSH LAYER PREPROCESSING
var dataset = ee.ImageCollection('UQ/murray/Intertidal/v1_1/global_intertidal');

var Int2002_2004 = ee.Image('UQ/murray/Intertidal/v1_1/global_intertidal/2002-2004');

var Int2011_2013 = ee.Image('UQ/murray/Intertidal/v1_1/global_intertidal/2011-2013');


var Int2014_2016 = ee.Image('UQ/murray/Intertidal/v1_1/global_intertidal/2014-2016');

var aoi =ee.FeatureCollection(aoi).geometry();
var visualization = {
  bands: ['classification'],
  min: 0.0,
  max: 1.0,
  palette: ['0000FF']
};

//Open Modis NDVI data
var dataset = ee.ImageCollection('MODIS/006/MYD13A1')
                  .filter(ee.Filter.date('2020-01-01', '2020-12-31'));
var ndvi = dataset.select('NDVI');

var mean_ndvi = ndvi.reduce(ee.Reducer.mean(), (6)).clip(aoi);


var ndviVis = {
  min: 0.0,
  max: 9000.0,
  palette: [
    'FFFFFF', 'CE7E45', 'DF923D', 'F1B555', 'FCD163', '99B718', '74A901',
    '66A000', '529400', '3E8601', '207401', '056201', '004C00', '023B01',
    '012E01', '011D01', '011301'
  ],
};

Map.addLayer(mean_ndvi, ndviVis, 'NDVI');
print(ndvi);



print(dataset);
Map.addLayer(Int2014_2016.clip(aoi), visualization, 'Intertidal areas14-16');
Map.addLayer(Int2011_2013.clip(aoi), visualization, 'Intertidal areas11-13');
Map.addLayer(Int2002_2004.clip(aoi), visualization, 'Intertidal areas02-04');


Export.image.toDrive({
  image : Int2002_2004.clip(aoi),
  description: 'Intertidal_areas2002-04',
  maxPixels: 3784216672400,
  region : aoi});
  
Export.image.toDrive({
  image : Int2011_2013.clip(aoi),
  description: 'Intertidal_areas2011-13',
  maxPixels: 3784216672400,
  region : aoi});  
  
  
Export.image.toDrive({
  image : Int2014_2016.clip(aoi),
  description: 'Intertidal_areas2014-16',
  maxPixels: 3784216672400,
  region : aoi});  
  
  
Export.image.toDrive({
  image : mean_ndvi,
  description: 'ndvi_mean_woi',
  maxPixels: 3784216672400,
  region : aoi});  
  