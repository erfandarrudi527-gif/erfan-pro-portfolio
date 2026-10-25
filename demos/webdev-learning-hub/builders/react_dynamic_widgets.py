# -*- coding: utf-8 -*-
"""
Full, custom-tailored, interactive live simulations for all 65 React Topics.
Delegates to react_widgets_part1 and react_widgets_part2.
"""
import os, sys
BASE_DIR = os.path.dirname(__file__)
sys.path.append(BASE_DIR)

from react_widgets_part1 import get_widget_part1
from react_widgets_part2 import get_widget_part2

def generate_react_widget(tid, title):
    w1 = get_widget_part1(tid, title)
    if w1:
        return w1
    w2 = get_widget_part2(tid, title)
    if w2:
        return w2
    return f"""
    <div class="react-live-demo">
      <div style="font-size:13px; font-weight:700; color:#38bdf8;">کامپوننت فعال: {title}</div>
    </div>
    """

print("React Dynamic Preview Engine ready for all 65 topics.")
