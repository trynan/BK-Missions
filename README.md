# BK-Missions
Welcome to BK Missions! This is a program made to make generating a board of goals simple and easy. In this readme I'll talk about how some of it works and some of the details.

1. How does long mission generation works?
Long mission generation takes one goal from the main objective category first (randomly). Then, it chooses the next categories one by one in a random order and chooses goals that fulfill these requirements:
- Goal does not have codes that conflict with the main objective's codes
- Goal does not have codes that conflict with codes that have previously appeared at least twice
- Short mission generation ignores conflicting codes for the second and third goals.

2. Configuration file
Here is an explanation for all of the settings in the configuration file. Tweak these to your liking or change the defaults easily from within the program!
- short = 0 - when 0, long missions will be generated. when 1, short missions will be generated. all other values don't work.
- show_codes = 0 - when 0, codes will not be shown after missions. when 1, codes will be shown. all other values don't work.
- win_size = 360x775+148+156 - controls geometry of the main window. format is "width x height + xoffset + yoffset". xoffset and yoffset are variables that tell the window where on your screen it should show up. width and height control its size.
- show_text = 1 - when 0, the text boxes to the right of the goals will not be shown. when 1, the text boxes will be shown. other values don't work.
- font_size = 10 - controls font size. any positive integer works.

3. Other stuff
- In the settings window the "get current size/position" box will write the current main window's geometry to the text box above the button. You can then use this information to set the value as a default.
- "Apply settings" only applies font size and window size changes, it doesn't really do anything else.
