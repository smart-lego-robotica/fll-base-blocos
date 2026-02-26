from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub(broadcast_channel=1)
sensorToque = ForceSensor(port=Port.F)
motorDirecao = Motor(port=Port.E, reset_angle=True)
marcha = 0
marchaDisplay = "N"

motorDirecao.reset_angle(0)

hub.light.on(color=Color.RED)
wait(1000)
hub.speaker.beep()
hub.light.on(color=Color.GREEN)
hub.display.char(marchaDisplay)

while True:
    velocidade = sensorToque.force()
    direcao = motorDirecao.angle()

    print(motorDirecao.speed())
    
    if (Button.LEFT in hub.buttons.pressed() and marcha > -1):
        marcha -= 1
        wait(50)

    if (Button.RIGHT in hub.buttons.pressed() and marcha < 2):
        marcha += 1
        wait(50)


    if (marcha == -1):
        marchaDisplay = "R"
    elif (marcha == 0):
        marchaDisplay = "N"
    elif (marcha == 1):
        marchaDisplay = "1"
    elif (marcha == 2):
        marchaDisplay = "2"

    # Velocidade, direcao, marcha(-1, 0, 1, 2)
    hub.ble.broadcast(data=[velocidade, direcao, marcha])

    if (abs(motorDirecao.speed()) < 5):
        motorDirecao.run_target(700, 0, then=Stop.COAST)
    
    hub.display.char(marchaDisplay)

    wait(100)