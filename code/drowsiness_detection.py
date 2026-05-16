# Driver Drowsiness Detection System

import random
import time

# Simulated eye closure percentage
eye_closure = random.randint(10, 100)

print("Eye Closure Level:", eye_closure, "%")

time.sleep(1)

# Drowsiness detection
if eye_closure > 70:
    print("🚨 Drowsiness Detected!")
    print("⚠️ Please Take a Break")

elif eye_closure > 40:
    print("😴 Driver Appears Tired")

else:
    print("✅ Driver is Alert")
