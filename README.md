# BK-Missions
Welcome to BK Missions! This is a program made to make generating a board of goals simple and easy. In this readme I'll talk about how some of it works and some of the details. BK Missions was an idea by CrozB. He came up with the logic for generating a set of goals, and also the goals themselves.

There are currently two versions of the app. The first one was the tk version, named so because it was written using the tk library for the graphic interface. The second one is the Qt version, since it was written using the Qt library for the graphic interface. The internal logic behind each is the same and they both contain the same core functionality, but the Qt version is more recently worked on. Ultimately, I used this project as a way to learn how to use both of these libraries.

## 1. How does mission generation work?
Mission generation takes one goal from the main objective category first (randomly). Then, it chooses the next categories one by one in a random order and chooses goals that fulfill these requirements:
- Goal does not have codes that conflict with codes that have previously appeared at least twice.
- Short mission generation ignores conflicting codes for the second and third goals.

## 2. Other stuff
- If a custom seed is not being used, the current seed is chosen using the random library from python (random.randrange(100000, 1000000)). This ends up being a pseudo-randomly chosen six-digit number.
- If a custom seed is used, you can choose any string of digits (or even letters) and it should work (assuming I understand the random library well enough). There's probably a limit to how long the string can be but I don't know what it is.
- Your computer may think the .exe from the release is a virus; this is an issue with using pyinstaller to create an executable from a python file. The source code is in the python file. If you don't trust the .exe but you have python installed (>3.0 should work), you can just run the python file instead. The only non-standard libraries which you may need to install are tk (for the tk version) and PySide6 (for the Qt version).
