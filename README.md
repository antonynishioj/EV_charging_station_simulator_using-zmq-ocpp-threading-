# EV_charging_station_simulator_using(zmq,ocpp,threading)

## Approach
1.import dependencies <br />
  threading (To perform tasks concurrently) <br />
  zmq(messaging library) <br />
  ocpp (used for communication between EV charging stations and central management systems) <br />
  tkinter (for simple UI to show output) <br />
  <br />
2.Creating Central Management System (server) - (central_management_system.ipynb) <br />
  ChargePoint- defines method to handle communication with a charging point in an EV charging station <br />
  worker- continuously listens for messages on a ZeroMQ socket and responds accordingly <br />
<br />
3.Creating an function simulates and connects to the CMS to show charging station status accordingly- charging_station.py <br />
<br />
## Steps to implement code
In terminal run charging_station.py using code(python charging_station.py) <br />

### Results
give input (start_charging) <br />
output: <br />
![image](https://github.com/antonynishioj/EV_charging_station_simulator_using-zmq-ocpp-threading-/assets/157102286/d16c7dcd-f627-430c-9471-dbeb7d9f2da7)
<br />
<br />
give input (start_charging) <br />
output: <br />
![image](https://github.com/antonynishioj/EV_charging_station_simulator_using-zmq-ocpp-threading-/assets/157102286/ba239d27-1524-4516-a21d-168235bcbb20)
