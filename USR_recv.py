import paho.mqtt.client as mqtt # Used to send messages
import json # Used to format/decode messages

# UI window
mainWindow = None

# Quality of Service level
qos_level = 0

# Retain Flag
retain_flag = False

# Function that is used get the main window
def set_mainWindow(var):
    global mainWindow
    mainWindow = var

# Function that is used to send messages to pi
def send_message(msg):
        payload = json.dumps(msg).encode('utf-8')
        client.publish("dgl_usr_data", payload, qos = qos_level, retain= retain_flag)

def background_msg(client, userdata, message):
    try:

        json_package = message.payload.decode()
    
        if(json_package == "blue"):
            mainWindow.setBackgroundColor()

        else:
            print("Error: '" + str(json_package) + "' not recognized.")

    except Exception as e:
        print(e)

# Handles the messages for when the pi updates the image
def image_message(client, userdata, message):

    try:
        
        # Decodes the message
        json_package = message.payload
        imageName = './img/receive_image.jpg'
                       
        f = open(imageName, 'wb')
        f.write(message.payload)
        f.close()
    

        # Handles the sensor type 
        mainWindow.set_image()
    

    # Handles any expections for this function
    except Exception as e:
        print(e)

# Connects to the broker
mqttBroker = "broker.hivemq.com"
client = mqtt.Client("Deliverable_3_sub")
client.connect(mqttBroker)

# listens to the pi data being sent
client.loop_start()
client.subscribe("dgl_image")
client.on_message = image_message


# Connects to a second broker
bg_client = mqtt.Client("background_sub")
bg_client.connect(mqttBroker)

# listens to the pi data being sent
bg_client.loop_start()
bg_client.subscribe("dgl_background")
bg_client.on_message = background_msg

