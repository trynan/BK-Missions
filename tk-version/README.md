# BK-Missions (tk version)
Welcome to the tk version of BK Missions! This is the original graphical version created in python using the tk library. Here I will explain everything which is specific to this version.

## 1. Configuration file
The Qt version does not use a config file. Here is an explanation of the things you can tweak in there to change default settings.
- short = False - when False, long missions will be generated. When True, short missions will be generated. All other values don't work.
- show_codes = False - when False, codes will not be shown after missions. when True, codes will be shown. all other values don't work.
- win_size = 360x775+148+156 - controls geometry of the main window. Format is "width x height + xoffset + yoffset". xoffset and yoffset are variables that tell the window where on your screen it should show up. width and height control its size.
- show_text = True - when False, the text boxes to the right of the goals will not be shown. When True, the text boxes will be shown. other values don't work.
- font_size = 10 - controls font size. Any positive integer works.

## 2. Other stuff
- In the settings window the "get current size/position" box will write the current main window's geometry to the text box above the button. You can then use this information to set the value as a default.
- "Apply settings" only applies font size and window size changes, it doesn't really do anything else.