from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Axis
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub(observe_channels=[1])
motorEsquerdo = Motor(port=Port.A)

motorDireito = Motor(port=Port.E, positive_direction=Direction.COUNTERCLOCKWISE)

chassi = DriveBase(motorEsquerdo, motorDireito, wheel_diameter=62, axle_track=80)
hub.light.on(Color.RED)



while (hub.ble.observe(1) is None):
    print("Esperando Conexão...")
    wait(500)

hub.light.on(Color.GREEN)

while True:
    # Velocidade, direcao, marcha(-1, 0, 1, 2)
    velocidade = hub.ble.observe(1)[0] * -30
    direcao = hub.ble.observe(1)[1]
    marcha = hub.ble.observe(1)[2] * 20

    print(f"Velocidade {velocidade}")
    print(f"Direcao {direcao}")

    if (abs(velocidade) > 10):
        motorEsquerdo.run((velocidade-direcao) * marcha)
        motorDireito.run((velocidade+direcao) * marcha)
    else:
        motorEsquerdo.run(0)
        motorDireito.run(0)

    wait(50)



# hub.ble.observe()