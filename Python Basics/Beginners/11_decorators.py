import time
from datetime import datetime, timedelta


def time_taken(base_func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = base_func(*args, **kwargs)
        #Here python unpacks the arguments tuples into individual arguments and passes them to the base_func.
        #here *args is used to unpack the positional arguments and **kwargs is used to unpack the keyword arguments.
        #This allows the wrapper function to accept any number of positional and keyword arguments and pass them to the base_func without needing to know the specific arguments in advance.
        #Here python unpacks keyword arguments dictionary into individual keyword arguments and passes them to the base_func.
        end = time.time()
        print(f"Time taken: {(end - start):.4f} seconds")
        return result
    return wrapper

@time_taken
def some_function(name, age):
    print(f"Executing some function for {name} of age {age}...")
    time.sleep(2) 
    print("Function execution completed.")
    print(datetime.now() + timedelta(minutes=30))


# if __name__ == "__main__":
#     some_function()    

# func = time_taken(some_function)
# func()
some_function("Alice", 30)
print("\n")


print("=============================================================================================================")
print("Starting space mission operations...\n")

def mission_timer(func):
    def wrapper(*args, **kwargs):
        print("Mission started...")
        print(f"Current time: {datetime.now()}")
        for i in range(3):
            print(f"Mission in progress... {i+1}/3")
            time.sleep(1) 
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Mission completed in {(end - start):.4f} seconds.")
        return result
    return wrapper

@mission_timer
def launch_probe(probe_name, target_planet):
    print(f"Launching probe: {probe_name} to planet {target_planet}...")
    time.sleep(2) 
    print(f"Probe {probe_name} launched successfully!")
    print(f"Target Planet: {target_planet}")
    print(f"Estimated arrival time: {datetime.now() + timedelta(days=365)}")
    print(f"Probe {probe_name} is now en route to {target_planet}.")
    print(f"Probe has reached the planet {target_planet} and is now conducting scientific experiments.")

@mission_timer
def deploy_satellite(satellite_name, orbit, altitude):
    print(f"Deploying satellite: {satellite_name}...")
    time.sleep(3) 
    print(f"Satellite {satellite_name} deployed successfully!")
    print(f"Orbit: {orbit}, Altitude: {altitude} km")

if __name__ == "__main__":
    launch_probe("Voyager 1", "Jupiter")
    print("\n")
    deploy_satellite("Hubble Space Telescope", "Low Earth Orbit", 547)
    print("Mission operations completed. All systems are nominal.")
