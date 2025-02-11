from time import sleep
import paho.mqtt.client as mqtt
import json
import cv2


# Image names:

ORGIMAGE  = "./img/image_1.jpg"
GRAYSCALE = "./img/image_2.jpg"

#TOPIC = "image_send"

# Function that is used to send messages to pi
def send_message(msg):
        payload = json.dumps(msg).encode('utf-8')
        client.publish("dgl_usr_data", payload, qos = qos_level, retain= retain_flag)


# Handles the Messages from the user
def on_message(client, userdata, message):

    try:
        global update_parking

        # Decodes the message
        json_package = message.payload.decode("utf-8")
        json_package = json.loads(json_package)

 
        if(json_package == "d"):
            msg = "blue"
            msg = msg.encode()
            client.publish("dgl_background", msg)
            print("Display the frame")

        # Sends the original image
        elif(json_package == "o"):
            global byteArr
            client.publish("dgl_image", byteArr) 
            print("Publish the original image")

        # Sends the gray scale image
        elif(json_package =="g"):
            global gray_img
            client.publish("dgl_image", gray_img)
            print("Publish grayscale image")

    # Handles any expections for this function
    except Exception as e:
        print(e)


# Opens original file and saves it as a gray scale image
gray_img = cv2.imread(ORGIMAGE, 0)
cv2.imwrite(GRAYSCALE, gray_img, [int(cv2.IMWRITE_JPEG_QUALITY), 100])

# Opens the original image
with open(ORGIMAGE, 'rb') as file:
    filecontent = file.read()
    byteArr = bytearray(filecontent)

# Opens the Gray scale version of the image
with open(GRAYSCALE, 'rb') as file:
    filecontent = file.read()
    gray_img = bytearray(filecontent)



#Connects to the broker
mqttBroker = "broker.hivemq.com"
client = mqtt.Client("Large_file_send")
client.connect(mqttBroker)

# Listen for the data being sent
client.loop_start()
client.subscribe("dgl_usr_data")
client.on_message = on_message


# Keeps the program alive
while True:
    sleep(0.2)


