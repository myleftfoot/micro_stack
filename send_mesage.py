#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import sys

# This is the Publisher

client = mqtt.Client()
client.connect("localhost",8883,60)
client.publish("sensors", "weather,location=us-midwest temperature=" + sys.argv[1]);
client.disconnect();