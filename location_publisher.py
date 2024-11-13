#!/usr/bin/env python
import rospy
from nav_msgs.msg import Odometry
from flask import Flask, jsonify

app = Flask(__name__)
robot_location = {"x": 0.0, "y": 0.0, "z": 0.0}

def odom_callback(msg):
    global robot_location
    robot_location["x"] = msg.pose.pose.position.x
    robot_location["y"] = msg.pose.pose.position.y
    robot_location["z"] = msg.pose.pose.position.z

@app.route('/location', methods=['GET'])
def get_location():
    return jsonify(robot_location)

def ros_subscriber():
    rospy.init_node('location_listener', anonymous=True)
    rospy.Subscriber("/odom", Odometry, odom_callback)
    app.run(host='0.0.0.0', port=5000)

if __name__ == '__main__':
    ros_subscriber()
