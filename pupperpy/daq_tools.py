from threading import Timer
from pupperpy.imu_tools import IMU
from pupperpy.object_detection import ObjectSensors
from UDPComms import Subscriber
import numpy as np

CV_PORT = 9120
CMD_PORT = 8810
# From StandfordQuadrupped.pupper.Config
max_x_velocity = 0.4
max_y_velocity = 0.3
max_yaw_rate = 2.0

class RepeatTimer(Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.functions(*self.args, **self.kwargs)

class DataLogger(object):
    def __init__(self, rate=0.1):
        self.obj_sensors = ObjectSensors()
        self.imu = IMU()
        self.cv_sub = Subscriber(CV_PORT)
        self.cmd_sub = Subscriber(CMD_PORT)
        self.data = None
        self.data_columns  = ['timestamp', 'x_acc', 'y_acc', 'z_acc', 'roll',
                             'pitch', 'yaw', 'left_obj', 'right_obj',
                             'center_obj', 'bbox_x', 'bbox_y', 'bbox_h',
                             'bbox_w', 'robo_x_vel', 'robo_y_vel',
                             'robo_yaw_rate']
        self.timer = RepeatTimer(rate, self.log)

    def log(self):
        imu = self.imu_read()
        obj = self.obj_sensors.read()


        try:
            cv = self.cv_sub.get()
        except:
            cv = dict.fromkeys(['bbox_x', 'bbox_y', 'bbox_h', 'bbox_w'], np.nan)

        try:
            cmd = self.cmd_sub.get()
        except:
            cmd = {'ly': 0, 'lx': 0, 'rx': 0}

        x_vel = cmd['ly'] * max_x_velocity
        y_vel = cmd['lx'] * -max_y_velocity
        yaw_rate = cmd['rx'] * -max_yaw_rate
        time = dt.now().timestamp

        row = np.array([time, imu['x_acc'], imu['y_acc'], imu['z_acc'],
                        imu['roll'], imu['pitch'], imu['yaw'],
                        obj['left'], obj['right'], obj['center'],
                        cv['bbox_x'], cv['bbox_y'], cv['bbox_h'],
                        cv['bbox_w'], x_vel, y_vel, yaw_rate])
        self.add_data(row)

    def add_data(self, row):
        if self.data is None:
            self.start_time = row[0]
            row[0] -= self.start_time
            self.data = row
        else:
            row[0] -= self.start_time
            self.data = np.vstack([data, row])

    def save_data(self, fn):
        np.save(fn, self.data)

    def run(self):
        print('Running logger...')
        self.timer.start()

    def stop(self):
        self.timer.cancel()
        print('Logger stopped')

