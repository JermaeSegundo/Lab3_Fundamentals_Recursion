 # telemetry_module.py

# Req 1 & 3: Generator that yields streaming data points sequentially
def data_stream(last_name, seed_num, favorite_artist):
    # Base calculation using your student input values
    base = len(last_name) + seed_num + len(favorite_artist)
    
    # Simulates a continuous stream of telemetry readings 
    # (Includes one negative value to test exception handling!)
    simulated_readings = [base * 4, base * 6, -50, base * 12, base * 18]
    
    for reading in simulated_readings:
        yield reading

# Req 4: Lambda function used to transform/calibrate raw sensor data
calibrate_data = lambda x: round(x * 1.05, 2)