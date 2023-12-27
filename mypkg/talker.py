import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class Talker():
    def __int__(self):
        self.pub = node.create_publisher(Int16,"countup",
        self.n = 0)

rclpy.init()
node = Node("talker")
talker = Talker()

def cb():
    msg = Int16()
    msg.data = talaker.n
    talker.pub.publish(msg)
    talker.n += 1

node.create_timer(0.5, cd)
rclpy.spin(node)
