/**** Start of imports. If edited, may not auto-convert in the playground. ****/
var roi = 
    /* color: #d63000 */
    /* shown: false */
    /* displayProperties: [
      {
        "type": "rectangle"
      }
    ] */
    ee.Geometry.Polygon(
        [[[-4.58131015083768, 22.697903106722446],
          [-4.58131015083768, -45.99486601538318],
          [80.14525234916232, -45.99486601538318],
          [80.14525234916232, 22.697903106722446]]], null, false),
    vis = {"bands":["CHLA_AVE"],"min":-2,"max":2,"palette":["3500a8","0800ba","003fd6","00aca9","77f800","ff8800","b30000","920000","880000"]};
/***** End of imports. If edited, may not auto-convert in the playground. *****/
var wiosym = ee.Image('users/PichayaMelody123/wiosymmarin');
Map.addLayer(wiosym);

var April = ee.ImageCollection('JAXA/GCOM-C/L3/OCEAN/CHLA/V1')
                .filterDate('202-12-01', '2021-12_30')
                // filter to daytime data only
                .filter(ee.Filter.eq('SATELLITE_DIRECTION', 'D'));
print(April);

// Multiply with slope coefficient
var april = April.mean().multiply(0.0016).log10();
print(april);


Map.addLayer(april.clip(roi), vis, 'Chlorophyll-a concentration');

Export.image.toDrive({
  image : april.clip(roi),
  description: 'Chl_a',
  maxPixels: 3784216672400});
