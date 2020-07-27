import random
from datetime import datetime

from mcstatus import MinecraftServer

from flask import Flask, jsonify, render_template

application = Flask(__name__)
random.seed()  # Initialize the random number generator


@application.route('/')
def index():

    return render_template('index.html')


@application.route('/_test')
def test_data():

    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    value = random.random() * 10

    return jsonify(time=time, value=value)


@application.route('/server-pinger')
def server_data():

    # Example server using HyPixel.
    # An option to add multiple servers via JSON file will be added.
    server_ip = "mc.hypixel.net"

    # IMPORTANT: Edit here your server port.
    # It works with Bungeecord instances and Spigot servers.
    server = MinecraftServer.lookup("{}:25565".format(server_ip))
    players = server.status().players.online

    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    return jsonify(ip=server_ip, time=time, value=players)


if __name__ == '__main__':
    application.run(debug=True, threaded=True)
