from controller import *

robot = Robot()
timestep = 5
robot.step(timestep)

motor_left = robot.getDevice('motor.left')
motor_right=robot.getDevice('motor.right')
motor_left.setPosition(float('inf'))
motor_right.setPosition(float('inf'))

def avancer(vitesse):
    motor_left.setVelocity(vitesse)
    motor_right.setVelocity(vitesse)
    return True
def reculer(vitesse):
    motor_left.setVelocity(-vitesse)
    motor_right.setVelocity(-vitesse)
    return True
def tourner_g(vitesse):
    motor_left.setVelocity(-vitesse)
    motor_right.setVelocity(vitesse)
    return True
def tourner_d(vitesse):
    motor_left.setVelocity(vitesse)
    motor_right.setVelocity(-vitesse)
    return True
def arreter():
    motor_left.setVelocity(0)
    motor_right.setVelocity(0)
    return True
#boucle principale
initialisation=0
while robot.step(timestep)!=-1:
    distanceSensors = []
    for i in range(7):
        ds = robot.getDevice('prox.horizontal.'+str(i))
        ds.enable(timestep)
        distanceSensors.append(ds)
    vals =[distanceSensors[i].getValue() for i in range(7)]
    
    if vals[2]<1:
        avancer(5)
    else :
        reculer(5)  
        
            
        
    
    
        
        
        