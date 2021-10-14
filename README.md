# Mock_Data_Simulator
Health data simulator


Mock_data simulates mock data for certain period of time as mentioned in yaml file
Process_data process the data into df evrey new second and calucates avg,max for the things for given time to segregate

currently i have simulated for 1 hour and and have breakdown 15 min data frames. you can change the parameters for hourly basis

By changing following in config we can get hourly basis

For example we need to run simulation for 2 hours and we need hourly basis in which we recive two rows

timeTorRunSimulationInSeconds: 7200( to run simulation for 2 hours)
timeToSegregate: 3600(1 hour in seconds)
