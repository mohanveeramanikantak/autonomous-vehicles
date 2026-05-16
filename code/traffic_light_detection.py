# Traffic Light Detection Simulation

import random
import time

# Possible traffic lights
traffic_lights = ["RED", "YELLOW", "GREEN"]

# Random signal
signal = random.choice(traffic_lights)

print("Traffic Light Detected:", signal)

time.sleep(1)

# Vehicle action
if signal == "RED":
    print("🛑 Stop Vehicle")

elif signal == "YELLOW":
    print("⚠️ Slow Down")

else:
    print("✅ Move Forward")
