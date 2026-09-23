# ==========================================
# EQUIPMENT DIAGNOSTIC SYSTEM
# ==========================================

# ------------------------------------------
# STUDENT-SPECIFIC INPUTS
# ------------------------------------------

LAST_NAME = "SEGUNDO"
SEED_NUM = 2
FAVORITE_ARTIST = "Lany"

# ------------------------------------------
# EXECUTION LOG
# ------------------------------------------

execution_log = []

# ------------------------------------------
# DECORATOR
# Records the diagnostic process
# ------------------------------------------

def diagnostic_log(func):
    def wrapper(*args, **kwargs):
        execution_log.append(f"Started: {func.__name__}")
        
        result = func(*args, **kwargs)
        
        execution_log.append(f"Completed: {func.__name__}")
        return result

    return wrapper


# ------------------------------------------
# FUNCTION 1: GENERATE EQUIPMENT READINGS
# ------------------------------------------

@diagnostic_log
def generate_readings(last_name, seed_num, favorite_artist):

    # Convert text into numerical values
    surname_value = sum(ord(char) for char in last_name)
    artist_value = sum(ord(char) for char in favorite_artist)

    base_value = surname_value + artist_value + seed_num

    # Generate student-specific readings
    temperature = 40 + (base_value % 41)
    voltage = 200 + (base_value % 51)
    current = 5 + (base_value % 11)
    vibration = 1 + (base_value % 10)

    readings = {
        "Temperature": temperature,
        "Voltage": voltage,
        "Current": current,
        "Vibration": vibration
    }

    return readings


# ------------------------------------------
# FUNCTION 2: VALIDATE READINGS
# ------------------------------------------

@diagnostic_log
def validate_readings(readings):

    # Acceptable operating ranges
    limits = {
        "Temperature": (40, 80),
        "Voltage": (200, 250),
        "Current": (5, 15),
        "Vibration": (1, 10)
    }

    validation_results = {}

    for name, value in readings.items():

        minimum, maximum = limits[name]

        if not isinstance(value, (int, float)):
            raise ValueError(f"{name} must be a number.")

        if minimum <= value <= maximum:
            validation_results[name] = "VALID"
        else:
            validation_results[name] = "INVALID"

    return validation_results


# ------------------------------------------
# FUNCTION 3: CALCULATE DIAGNOSTIC SCORE
# ------------------------------------------

@diagnostic_log
def calculate_diagnostic_score(readings):

    # Convert readings into percentages
    temperature_score = (readings["Temperature"] / 80) * 100
    voltage_score = (readings["Voltage"] / 250) * 100
    current_score = (readings["Current"] / 15) * 100
    vibration_score = (readings["Vibration"] / 10) * 100

    average_score = (
        temperature_score
        + voltage_score
        + current_score
        + vibration_score
    ) / 4

    return round(average_score, 2)


# ------------------------------------------
# FUNCTION 4: CLASSIFY EQUIPMENT CONDITION
# ------------------------------------------

@diagnostic_log
def classify_condition(score, validation_results):

    invalid_count = list(validation_results.values()).count("INVALID")

    if invalid_count > 0:
        return "NEEDS ATTENTION"

    elif score < 60:
        return "CRITICAL"

    elif score < 80:
        return "WARNING"

    else:
        return "NORMAL"


# ------------------------------------------
# MAIN DIAGNOSTIC PROGRAM
# ------------------------------------------

def main():

    print("=" * 50)
    print("EQUIPMENT DIAGNOSTIC SYSTEM")
    print("=" * 50)

    print("\nStudent Information:")
    print("Surname:", LAST_NAME)
    print("Seed Number:", SEED_NUM)
    print("Favorite Artist:", FAVORITE_ARTIST)

    try:

        # Check student inputs
        if not LAST_NAME or not LAST_NAME.isalpha():
            raise ValueError("LAST_NAME must contain letters only.")

        if not isinstance(SEED_NUM, int) or not 0 <= SEED_NUM <= 9:
            raise ValueError("SEED_NUM must be a number from 0 to 9.")

        if not FAVORITE_ARTIST:
            raise ValueError("FAVORITE_ARTIST cannot be empty.")

        # Generate readings
        readings = generate_readings(
            LAST_NAME,
            SEED_NUM,
            FAVORITE_ARTIST
        )

        # Validate readings
        validation_results = validate_readings(readings)

        # Calculate diagnostic score
        diagnostic_score = calculate_diagnostic_score(readings)

        # Classify equipment
        condition = classify_condition(
            diagnostic_score,
            validation_results
        )

        # ----------------------------------
        # ASSESSMENT DATA
        # ----------------------------------

        print("\n" + "=" * 50)
        print("ASSESSMENT DATA")
        print("=" * 50)

        print("\nGenerated Equipment Data:")
        for name, value in readings.items():
            print(f"{name}: {value}")

        print("\nValidation Results:")
        for name, result in validation_results.items():
            print(f"{name}: {result}")

        print("\nDiagnostic Results:")
        print(f"Diagnostic Score: {diagnostic_score}")
        print(f"Equipment Condition: {condition}")

        print("\nExecution Log:")
        for log in execution_log:
            print(log)

        print("\n" + "=" * 50)
        print("FINAL OUTPUT")
        print("=" * 50)

        print(f"Equipment Condition: {condition}")
        print(f"Diagnostic Score: {diagnostic_score}")

        print("\nDiagnostic process completed successfully.")

    except ValueError as error:

        # Invalid input is handled without crashing the program
        print("\nERROR:", error)
        print("The invalid input was handled safely.")
        print("The program did not terminate unexpectedly.")


# ------------------------------------------
# RUN PROGRAM
# ------------------------------------------

if __name__ == "_main_":
    main()
# ==========================================
# 2. RECURSIVE FAULT TRACE
# ==========================================

# ------------------------------------------
# FUNCTION 1: GENERATE UNIQUE FAULT CODE
# ------------------------------------------
def generate_fault_code(last_name, seed_num, favorite_artist):
    # Generates a unique numeric starting code from student info
    surname_val = len(last_name) * 5
    artist_val = len(favorite_artist) * 3
    return surname_val + artist_val + seed_num


# ------------------------------------------
# FUNCTION 2: RECURSIVE FAULT TRACER
# ------------------------------------------
def trace_fault(fault_code, level=1):
    # Base Case: Stop when fault code drops to 0 or below
    if fault_code <= 0:
        print(f"Level {level}: Fault Code = 0 -> Termination condition reached. System Cleared.")
        return

    print(f"Level {level}: Fault Code = {fault_code} -> Tracing deeper into system layers...")
    
    # Recursive Call: Decrement the fault code down by 5 each time
    trace_fault(fault_code - 5, level + 1)


# ------------------------------------------
# MAIN RECURSIVE PROGRAM
# ------------------------------------------
def main_recursive():
    print("\n" + "=" * 50)
    print("RECURSIVE FAULT TRACE SYSTEM")
    print("=" * 50)

    # Generate the initial starting fault code
    initial_code = generate_fault_code(LAST_NAME, SEED_NUM, FAVORITE_ARTIST)
    print(f"Initial Student-Specific Fault Code: {initial_code}")
    print("Starting sequence trace...\n")

    # Run the recursive tracer
    trace_fault(initial_code)
    print("\n" + "=" * 50)
    print("RECURSIVE DIAGNOSTIC COMPLETE")
    print("=" * 50)


# ------------------------------------------
# RUN BOTH PROGRAMS TOGETHER
# ------------------------------------------
if __name__=="__main__":
    main()
    main_recursive()