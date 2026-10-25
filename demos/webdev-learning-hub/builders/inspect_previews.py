import os

with open('C:/Users/erfan/Desktop/WebDev_Master_Learning_Hub/builders/generate_sandbox_previews.py', 'r', encoding='utf-8') as f:
    text = f.read()

react_idx = text.find('def get_react_preview')
react_code = text[react_idx:]
import re
handled = re.findall(r'if topic_id == (\d+)|elif topic_id == (\d+)', react_code)
handled_ids = [int(a or b) for a, b in handled]
print("Currently handled React topic IDs:", handled_ids)
