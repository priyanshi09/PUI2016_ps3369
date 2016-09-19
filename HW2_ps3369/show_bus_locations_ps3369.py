from __future__ import print_function
import json
import urllib as ulr 
import os
import sys

url ="http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + sys.argv[1] + "&VehicleMonitoringDetailLevel=calls&LineRef=" + sys.argv[2]

response = ulr.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

loc = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

print("Bus Line: " +  sys.argv[2] )

B_acv = len(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])
print("number of active buses: " + str (B_acv))

for i in range(B_acv):
    print("Bus " + str(i) + " is at latitude " + str(loc[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude'])+ "and longitude " + str(loc[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']))
