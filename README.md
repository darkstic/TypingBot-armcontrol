The goal of this project is to build and program a robotic arm to be able to effectively complete typing tests on typing.com, without requiring any user input beyond running the code.

We are fully aware that using a robotic arm is easily one of the least accurate, efficient or simple ways to go about this. We don't really care because our way is more fun.

The project in question is split into three main components:
1. The python code, which installs the libraries and dependancies needed for the program to function. It also includes a program that analyzes a section of the screen and converts it to text, passing it one character at a time as string values to the second component.
2. The second component is code written in .ino to run on either an Arduino Mega r3 or an Uno r3. This code interprets the string values sent by the first component and executes functions based on the inputs to move the arm and press the keys corresponding with the characters received.
3. The third part of the project consists of a small collection of .stl files to be 3d-printed in order to construct the arm.

Instructions for running the code are as follows:

Run the installer first.
Change the COM port variable in the backbone code to be the correct COM port that the Arduino is connected to.
Upload the arduino code to the arduino.
Make sure the serial monitor is closed in arduino, leaving it open will overload the USB.
Edit the bbox variable to fit the correct dimensions that the typing.com prompt box fills.

To use the program:

Open and sign into typing.com.
run the backbone code and minimize the page. You have 5 seconds before it starts after running it.
Make sure typing.com is opened correctly for the program to run.
The code will process the image within the bbox parameters and will send what it says one character at a time through the serial port as string values.


Please note that this project is still in development and does not yet function. More commits will come as the program progresses!
