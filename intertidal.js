/**** Start of imports. If edited, may not auto-convert in the playground. ****/
var aoi = 
    /* color: #d63000 */
    /* displayProperties: [
      {
        "type": "rectangle"
      }
    ] */
    ee.Geometry.Polygon(
        [[[-23.196328877875377, 25.426571732673924],
          [-23.196328877875377, -45.380577059318085],
          [81.92085862212463, -45.380577059318085],
          [81.92085862212463, 25.426571732673924]]], null, false);
/***** End of imports. If edited, may not auto-convert in the playground. *****/
var dataset = ee.ImageCollection('UQ/murray/Intertidal/v1_1/global_intertidal');

var visualization = {
  bands: ['classification'],
  min: 0.0,
  max: 1.0,
  palette: ['0000FF']
};

var Int2002_2004 = ee.Image('UQ/murray/Intertidal/v1_1/global_intertidal/2002-2004');

var Int2011_2013 = ee.Image('UQ/murray/Intertidal/v1_1/global_intertidal/2011-2013');


var Int2014_2016 = ee.Image('UQ/murray/Intertidal/v1_1/global_intertidal/2014-2016');



Map.addLayer(dataset, visualization, 'Intertidal areas');

Export.image.toDrive({
  image : Int2002_2004.clip(aoi),
  description: 'Intertidal_areas2002-04',
  maxPixels: 3784216672400,
  region : aoi});
  
Export.image.toDrive({
  image : Int2011_2013.clip(aoi),
  description: 'Int2011_2013',
  maxPixels: 3784216672400,
  region : aoi});
  
Export.image.toDrive({
  image : Int2014_2016.clip(aoi),
  description: 'Intertidal_areas2014-2016',
  maxPixels: 3784216672400,
  region : aoi});
  