# Autonomous Speed Control System

import random

# Simulated data
speed = random.randint(20, 120)
distance = random.randint(5, 100)

print("Current Speed:", speed, "km/h")
print("Obstacle Distance:", distance, "m")

# AI decision logic
if distance < 20:
    speed -= 30
    print("⚠️ Obstacle Detected - Reducing Speed")

elif distance < 40:
    speed -= 10
    print("⚠️ Maintaining Safe Distance")

else:
    print("✅ Road Clear")

print("Updated Speed:", max(speed, 0), "km/h")
