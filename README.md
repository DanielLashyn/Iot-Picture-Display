# Iot-Picture-Display
The following code was part of an assessment for a class. The main objective was to use MQTT to request an image from a Raspberry Pi and display on the user machine.


## External Packages Used:
### User:
- PyQt5
- paho.mqtt.client
- json
### Pi
- paho.mqtt.client
- json
- cv2

## User Files:
- USR_UI.py
- USR_recv
- USR_main

## Raspberry Pi Files:
- sender.py
- img-> image_1.jpg

## Running the Code:
1) Start the Pi code by typing ```python3 sender.py```
2) Start the user code by type ```python3 USR_main.py```
3) From there you are able to send requests to the Pi using the textbox.
#### Below are user requests the pi recognizes:
- ```d``` to display blue background
- ```o``` to display original image
- ```g``` to display a grayscale version of the original image 
