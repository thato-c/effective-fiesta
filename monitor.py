import psutil
import datetime
import time

def monitor_performance(interval):
    # Specify the limit for the repeat
    loop_no = 10
    cpu_count = 0
    memory_count = 0
    disk_count = 0
    current_time = datetime.datetime.now()

    #print("Printing Time of day")

    with open("C:/Users/tchit/OneDrive/effective-fiesta/ComputerPerformanceLog.txt", "r+") as file:
        file.truncate(0)
        if current_time.hour < 12:
            file.write("Good Morning! Here's your morning data\n\n")
        elif current_time.hour > 12 and current_time.hour < 18:
            file.write("Good Afternoon! Here's your afternoon data\n\n")

    while loop_no > 0:
        # Get CPU usage
        cpu_percent = psutil.cpu_percent(interval=interval)
        cpu_count += cpu_percent

        # Get memory usage
        memory = psutil.virtual_memory()
        memory_percent = memory.percent
        memory_count += memory_percent

        # Get disk usage
        disk = psutil.disk_usage('/')
        disk_percent = disk.percent
        disk_count += disk_percent

        #print("Printing results")

        try:
        # Print performance stats to a file
            with open("C:/Users/tchit/OneDrive/effective-fiesta/ComputerPerformanceLog.txt", "a") as file:
                file.write(f"Date and Time: {datetime.datetime.now()}\n")
                file.write(f"CPU usage: {cpu_percent}%\n")
                file.write(f"Memory Usage: {memory_percent}%\n")
                file.write(f"Disk Usage: {disk_percent}%\n")
                file.write("--------------------------------\n")
        except FileNotFoundError:
            print("File not found")
        except IOError:
            print("Error reading the file")
        except Exception as e:
            print("An error occurred: ", str(e))
        else:
            print("File read successfully")
        finally:
            print("End of file handling process")

        # Wait for the specified interval
        time.sleep(interval)
        loop_no -= 1

    # Return the average
    loop_count = 10 - loop_no
    cpu_average = "{:.2f}".format(cpu_count / loop_count)
    memory_average = "{:.2f}".format(memory_count / loop_count)
    disk_average = "{:.2f}".format(disk_count / loop_count)

    # Print performance metrics
    #print("Printing averages")
    with open("ComputerPerformanceLog.txt", "a") as file:
        file.write(f"CPU Average: {cpu_average}%\n")
        file.write(f"Memory Average: {memory_average}%\n")
        file.write(f"Disk Average: {disk_average}%\n")
        file.write("--------------------------------\n")

# Specify the monitoring interval in seconds
monitor_interval = 5

# Start monitoring
monitor_performance(monitor_interval)
