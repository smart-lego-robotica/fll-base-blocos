from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, hub_menu, run_task
import MissaoA
import MissaoB
import MissaoC


mission_selected = hub_menu("A", "B")

while True:

    if (mission_selected == "A"):
        wait(100)
        run_task(MissaoA.Principal())
        mission_selected = hub_menu("B", "A")

    elif (mission_selected == "B"):
        wait(100)
        run_task(MissaoB.Principal())
        mission_selected = hub_menu("C", "B")

    elif (mission_selected == "C"):
        run_task(MissaoC.Principal())
        mission_selected = hub_menu("C", "B")
