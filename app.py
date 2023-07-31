from flask import Flask,request
import backend_config

app=Flask(__name__)

@app.route("/",methods=["POST"])
def get_ip_address():
    ip_address=request.args["ip_address"]
    reference_host=request.args["host"]
    result=backend_config.take_traceroute(ip_address,reference_host)