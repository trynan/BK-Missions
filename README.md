# BK-Missions
Welcome to BK Missions! This is a program made to make generating a board of goals simple and easy. In this readme I'll talk about how some of it works and some of the details. BK Missions was an idea by CrozB. He came up with the logic for generating a set of goals, and also the goals themselves.

## 1. How does long mission generation work?
Long mission generation takes one goal from the main objective category first (randomly). Then, it chooses the next categories one by one in a random order and chooses goals that fulfill these requirements:
- Goal does not have codes that conflict with codes that have previously appeared at least twice.
- Short mission generation ignores conflicting codes for the second and third goals.

## 2. Configuration file
Here is an explanation for all of the settings in the configuration file. Tweak these to your liking or change the defaults easily from within the program!
- short = False - when False, long missions will be generated. when True, short missions will be generated. all other values don't work.
- show_codes = False - when False, codes will not be shown after missions. when True, codes will be shown. all other values don't work.
- win_size = 360x775+148+156 - controls geometry of the main window. format is "width x height + xoffset + yoffset". xoffset and yoffset are variables that tell the window where on your screen it should show up. width and height control its size.
- show_text = True - when False, the text boxes to the right of the goals will not be shown. when True, the text boxes will be shown. other values don't work.
- font_size = 10 - controls font size. any positive integer works.

## 3. Other stuff
- In the settings window the "get current size/position" box will write the current main window's geometry to the text box above the button. You can then use this information to set the value as a default.
- "Apply settings" only applies font size and window size changes, it doesn't really do anything else.
- If a custom seed is not being used, the current seed is chosen using the random library from python (random.randrange(100000, 1000000)). This ends up being a pseudo-randomly chosen six-digit number.
- If a custom seed is used, you can choose any string of digits (or even letters) and it should work (assuming I understand the random library well enough). There's probably a limit to how long the string can be but I don't know what it is.
- Your computer may think the .exe from the release is a virus; this is an issue with using pyinstaller to create an executable from a python file. The source code is in the python file. If you don't trust the .exe but you have python installed (>3.0 should work I think?) , you can just run the python file instead.
