from DifferentialDriveSimulatedRobot import *
from DR_3DOFDifferentialDrive import *

if __name__ == "__main__":

    # feature map. Position of 2 point features in the world frame.
    M2D = [np.array([[-40, 5]]).T,
           np.array([[-5, 40]]).T,
           np.array([[-5, 25]]).T,
           np.array([[-3, 50]]).T,
           np.array([[-20, 3]]).T,
           np.array([[40, -40]]).T]
    xs0 = np.zeros((6, 1))   # initial simulated robot pose

    # instantiate the simulated robot object
    robot = DifferentialDriveSimulatedRobot(xs0, M2D)

    # ------------------ circular path ------------
   #  usk = np.array([[0.5], [0.025]])
   #  xsk_1 = robot.xsk_1

   #  for i in range(3*2500):
   #      xsk = robot.fs(xsk_1, usk)
   #      xsk_1 = xsk
   # ------------------ circular path ------------


# ------------------ 8-shape path ------------
    xsk_1 = robot.xsk_1
    usk1 = np.array([[0.5], [0.025]])
    usk2 = np.array([[0.5], [-0.025]])

    for t in range(3):
        for i in range(2500):
            xsk = robot.fs(xsk_1, usk1)
            xsk_1 = xsk

        for i in range(2500):
            xsk = robot.fs(xsk_1, usk2)
            xsk_1 = xsk

   # ------------------ 8 shape path ------------


#     kSteps = 5000  # number of simulation steps
#     xsk_1 = xs0 = np.zeros((6, 1))  # initial simulated robot pose
#     index = [IndexStruct("x", 0, None), IndexStruct("y", 1, None), IndexStruct("yaw", 2, 1)]  # index of the state vector used for plotting

#     x0 = Pose3D(np.zeros((3, 1)))
#     dr_robot = DR_3DOFDifferentialDrive(index, kSteps, robot, x0)
#     dr_robot.LocalizationLoop(x0, np.array([[0.5, 0.03]]).T)

#     exit(0)
