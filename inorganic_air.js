/**** Start of imports. If edited, may not auto-convert in the playground. ****/
var aoi = 
    /* color: #98ff00 */
    /* displayProperties: [
      {
        "type": "rectangle"
      }
    ] */
    ee.Geometry.Polygon(
        [[[-1.5770312500000072, 29.38247470965441],
          [-1.5770312500000072, -47.03994780338958],
          [81.39171875, -47.03994780338958],
          [81.39171875, 29.38247470965441]]], null, false);
/***** End of imports. If edited, may not auto-convert in the playground. *****/
var pm25 = ee.ImageCollection('NASA/GSFC/MERRA/aer/2').select('SSSMASS25')
                  .filter(ee.Filter.date('2021-01-01', '2022-01-01'));
                  
print(pm25);          

var pm25_clip = pm25.clip(aoi);

