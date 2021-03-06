#!/usr/bin/env python

import rospy
import subprocess
from std_srvs.srv import Trigger, TriggerResponse
import os


kill_command = "pkill luakit"
start_command = "luakit --display=:0 -U {url}".format(
    url=rospy.get_param('qt_robot/face/url')
)


def callback_srv(_):
    os.system(kill_command)
    process = subprocess.Popen(start_command, shell=True)

    resp = TriggerResponse()
    resp.success = True
    resp.message = "Browser started with PID: %d" % process.pid
    return resp


if __name__ == "__main__":

    rospy.init_node("pi_browser_starter_server")

    service_name = rospy.get_param("qt_robot/face/start_browser_on_pi_service")
    srv = rospy.Service(service_name, Trigger, callback_srv)
    rospy.loginfo("Ready to start the face web browser")
    rospy.spin()
