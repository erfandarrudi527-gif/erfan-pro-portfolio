import os, sys
sys.path.append('C:/Users/erfan/Desktop/WebDev_Master_Learning_Hub/builders')
from react_dynamic_widgets import generate_react_widget

missing = []
for i in range(1, 66):
    w = generate_react_widget(i, f"Topic {i}")
    if "ویژگی «Topic" in w or "Active Component" in w:
        missing.append(i)

print(f"Total missing custom widgets in React: {len(missing)} out of 65")
print("Missing IDs:", missing)
