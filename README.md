# EV_charging_station_simulator_using(zmq,ocpp,threading)

## Approach
1.import dependencies \n
  threading (To perform tasks concurrently)
  zmq(messaging library)
  ocpp (used for communication between EV charging stations and central management systems)
  tkinter (for simple UI to show output)
  
2.Creating Central Management System (server) - (central_management_system.ipynb)
  ChargePoint- defines method to handle communication with a charging point in an EV charging station
  worker- continuously listens for messages on a ZeroMQ socket and responds accordingly

3.Creating an function simulates and connects to the CMS to show charging station status accordingly- charging_station,py

## Steps to implement code
In terminal run charging_station.py using code(python charging_station.py)

### Results
give input (start_charging)
output:
![image](https://github.com/antonynishioj/EV_charging_station_simulator_using-zmq-ocpp-threading-/assets/157102286/d16c7dcd-f627-430c-9471-dbeb7d9f2da7)


give input (start_charging)
output:
![image](https://github.com/antonynishioj/EV_charging_station_simulator_using-zmq-ocpp-threading-/assets/157102286/ba239d27-1524-4516-a21d-168235bcbb20)
