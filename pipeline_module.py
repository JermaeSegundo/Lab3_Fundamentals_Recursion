# pipeline_module.py
import functools
# Req 2: Organize program into separate modules by importing our custom module
import telemetry_module 

# ------------------------------------------
# STUDENT-SPECIFIC INPUTS 
# ------------------------------------------
LAST_NAME = "SEGUNDO"            
SEED_NUM = 2                   
FAVORITE_ARTIST = "LANY"  


# Req 5: Decorator function to monitor a major processing function
def pipeline_monitor(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("[MONITOR] Initializing Intelligent Telemetry Pipeline...")
        result = func(*args, **kwargs)
        print("[MONITOR] Pipeline execution finished successfully.")
        return result
    return wrapper


# Req 7: Recursive function to analyze or trace a detected abnormal condition
def trace_abnormal_condition(severity_level, count=1):
    # Base condition reached
    if severity_level <= 0:
        print("   -> Recursive Isolation Complete: Condition stabilized.")
        return count - 1
    
    print(f"   -> Trace Level {count}: Analyzing abnormal spike (Severity remaining: {severity_level})...")
    # Recursive call
    return trace_abnormal_condition(severity_level - 1, count + 1)


# Req 8 & 9: Main processing logic, exception handling, and report display
@pipeline_monitor
def run_diagnostic_pipeline():
    processed_count = 0
    valid_count = 0
    invalid_count = 0
    abnormal_count = 0
    total_recursive_calls = 0
    
    print("=" * 50)
    print("INTELLIGENT EQUIPMENT MONITORING PIPELINE")
    print("=" * 50)
    
    # Req 3: Initializing the generator stream without storing the whole stream at once
    stream = telemetry_module.data_stream(LAST_NAME, SEED_NUM, FAVORITE_ARTIST)
    
    for raw_value in stream:
        processed_count += 1
        print(f"\nProcessing Reading #{processed_count}: Raw Value = {raw_value}")
        
        # Req 6: Exception handling to manage invalid telemetry values without terminating
        try:
            if raw_value < 0:
                raise ValueError(f"Invalid Telemetry Signal: Negative value ({raw_value}) detected!")
            
            # Req 4: Apply lambda transformation
            calibrated_value = telemetry_module.calibrate_data(raw_value)
            valid_count += 1
            print(f"   Calibrated Value: {calibrated_value}")
            
            # Threshold to trigger abnormal condition check
            if calibrated_value > 100:
                abnormal_count += 1
                print("   [ALERT] Abnormal condition detected! Initiating recursive trace:")
                # Req 7: Trace abnormal condition via recursion
                calls = trace_abnormal_condition(3)
                total_recursive_calls += calls
                
        except ValueError as error_message:
            invalid_count += 1
            print(f"   [EXCEPTION HANDLED] {error_message}")

    # Determine overall status rule based on processed findings
    if invalid_count > 1 or abnormal_count > 2:
        overall_status = "CRITICAL ALERT"
    elif abnormal_count > 0:
        overall_status = "MAINTENANCE REQUIRED"
    else:
        overall_status = "OPERATIONAL"

    # Req 8 & 9: Output Final Structured Diagnostic Report
    print("\n" + "=" * 50)
    print("FINAL PIPELINE DIAGNOSTIC REPORT")
    print("=" * 50)
    print(f"Total Processed Readings   : {processed_count}")
    print(f"Valid Telemetry Readings   : {valid_count}")
    print(f"Invalid Telemetry Readings : {invalid_count}")
    print(f"Detected Abnormal Spikes   : {abnormal_count}")
    print(f"Total Recursive Trace Calls: {total_recursive_calls}")
    print(f"Overall Equipment Status   : {overall_status}")
    print("=" * 50)


if __name__ == "_main_":
    run_diagnostic_pipeline()
