from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
right_attachment = Motor(Port.D, Direction.CLOCKWISE)
left_attachment_ = Motor(Port.A, Direction.COUNTERCLOCKWISE)
color_sensor = ColorSensor(Port.C)
left_wheel = Motor(Port.E, Direction.COUNTERCLOCKWISE)
right_wheel = Motor(Port.F, Direction.CLOCKWISE)
drive_base = DriveBase(left_wheel, right_wheel, 88.9, 112)
