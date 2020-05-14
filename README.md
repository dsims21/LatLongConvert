# LatLongConvert

This script takes a file in the form of [ID, Lat, Long] and will append locations to an output file. 

The current implementation, requires ~1 second per lat/long combination. The time complexity is O(N) so the longer the list, the longer the time taken. 

In large files there will be failures along the way, which is why the entire process is repeated 3 times. The first pass will get the majority of lat/long combinations. The second pass should get the ones that caused timeout errors, but are still viable. The third pass is just for good measure.  
