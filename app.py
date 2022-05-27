from flask import Flask
import json
from product import Product
import os

app = Flask(__name__)


@app.route(f"/{Product.DeviceBoot.value}")
def list_devices():
    devices = []
    os.system("sudo arp-scan --interface=wlx60e327175c37 --localnet > netstat.dat")
    for item in open("netstat.dat", "r").readlines()[2:-3]:
        raw = item.strip("\n").replace("\t", "|")
        devices.append(raw)
    print(devices)
    return json.dumps({"devices": devices})


@app.route("/")
def hello():
    return json.dumps({"name": "Jake"})
