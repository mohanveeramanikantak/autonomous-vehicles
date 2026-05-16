# Parking Assistant System

import random
import time

# Simulated obstacle distance (in cm)
distance = random.randint(1, 100)

print("Obstacle Distance:", distance, "cm")

time.sleep(1)

# Parking guidance
if distance > 50:
    print("✅ Safe to Park")

elif distance > 20:
    print("⚠️ Warning: Vehicle Getting Close")

else:
    print("🛑 Stop Immediately")
