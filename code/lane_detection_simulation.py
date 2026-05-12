# Lane Detection Simulation

import random

# Simulated lane position
lane_offset = random.randint(-50, 50)

print("Lane Offset:", lane_offset)

if lane_offset < -20:
    print("⬅️ Adjust Vehicle Right")
elif lane_offset > 20:
    print("➡️ Adjust Vehicle Left")
else:
    print("✅ Vehicle Centered in Lane")
