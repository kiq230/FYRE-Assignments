import time
from machine import ADC, Pin

# ==============================================================================
# HARDWARE & ADC CONFIGURATION
# ==============================================================================
# On the Arduino Nano ESP32, physical header pin A0 connects to native GPIO 1.
adc_pin = Pin(1)
adc = ADC(adc_pin)

# Configure the attenuation:
# By default, ESP32 ADCs measure up to ~1.0V. Setting attenuation to ATTN_11DB 
# extends the input voltage measurement range up to the full 3.3V power rail.
adc.atten(ADC.ATTN_11DB)

# Constants for voltage calculation
MAX_ADC_VALUE = 65535  # MicroPython's 16-bit ADC scale (2^16 - 1)
MAX_VOLTAGE = 3.3      # Full-scale voltage reference in Volts

# ==============================================================================
# DATA LOGGING SETUP (CSV)
# ==============================================================================
CSV_FILENAME = "sensor_data5.csv"

# Open the file in append mode ("a").
# If the file does not exist, MicroPython will create it in the local flash.
# If it already exists, new entries will be added at the bottom.
file = open(CSV_FILENAME, "a")

# If the file is newly created or empty, write the header row.
# We check the file size using tell() or simply write a header if starting a new run.
if file.tell() == 0:
    file.write("Elapsed_Time_Seconds,Raw_ADC,Voltage_Volts\n")
    file.flush()  # Ensure header is immediately written to flash storage

print(f"Logging started. Saving data to {CSV_FILENAME}...")
print("Press Ctrl+C in your REPL terminal to stop logging safely.\n")

# ==============================================================================
# MAIN LOGGING LOOP
# ==============================================================================
start_time_ms = time.ticks_ms()

try:
    while True:
        # 1. Read Raw 16-bit ADC Value (0 to 65535)
        raw_value = adc.read_u16()

        # 2. Convert Raw Value to Actual Volts
        # Formula: Voltage = (Raw ADC / 65535) * 3.3V
        voltage = (raw_value / MAX_ADC_VALUE) * MAX_VOLTAGE

        # 3. Calculate Elapsed Time in Seconds
        elapsed_time_sec = time.ticks_diff(time.ticks_ms(), start_time_ms) / 1000.0

        # 4. Format Data as CSV Row
        # Format: Elapsed_Time, Raw_ADC, Voltage (rounded to 3 decimal places)
        log_entry = f"{elapsed_time_sec:.2f},{raw_value},{voltage:.3f}\n"

        # 5. Write to File
        file.write(log_entry)
        
        # Calling flush() forces MicroPython to immediately write the buffer from 
        # RAM into the board's flash memory, preventing data loss if power drops.
        file.flush()

        # Print to console for real-time monitoring
        print(f"Time: {elapsed_time_sec:.2f}s | Raw: {raw_value} | Voltage: {voltage:.3f}V")

        # 6. Sampling Interval Delay (0.5 Seconds = 500 ms)
        time.sleep(0.5)

except KeyboardInterrupt:
    print("\nLogging stopped by user.")

finally:
    # Always close the file safely when exiting the program!
    file.close()
    print("File safely closed.")