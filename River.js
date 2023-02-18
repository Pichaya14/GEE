/**** Start of imports. If edited, may not auto-convert in the playground. ****/
var wio_aoi = 
    /* color: #d63000 */
    /* shown: false */
    /* displayProperties: [
      {
        "type": "rectangle"
      }
    ] */
    ee.Geometry.Polygon(
        [[[-1.6739118878374493, 23.01617109796296],
          [-1.6739118878374493, -45.01365005604784],
          [86.91983811216255, -45.01365005604784],
          [86.91983811216255, 23.01617109796296]]], null, false);
/***** End of imports. If edited, may not auto-convert in the playground. *****/
var dataset = ee.FeatureCollection("WWF/HydroSHEDS/v1/FreeFlowingRivers");

dataset = dataset.style({
  color: "B2B2B3",
  width: 1.0,
});

var aoi = ee.FeatureCollection(wio_aoi).geometry();

Map.addLayer(dataset.clip(aoi), {}, "Free Flowing Rivers");