from flask import Flask
import json
from product import Product
import os
from utils import get_interface
from flask_cors import CORS, cross_origin

app = Flask(__name__)

# Global vars
interface = ""

@app.route(f"/{Product.DeviceBoot.value}")
@cross_origin()
def list_devices():
    devices = []
    os.system(f"sudo arp-scan --interface={get_interface()} --localnet > netstat.dat")
    for item in open("netstat.dat", "r").readlines()[2:-3]:
        raw = item.strip("\n").replace("\t", "|")
        devices.append(raw)
    print(devices)
    return json.dumps({"devices": devices})


@app.route("/")
def hello():
    return json.dumps({"name": "Jake"})
