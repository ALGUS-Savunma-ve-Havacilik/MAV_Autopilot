"""
mavsim
    - Chapter 2 assignment for Beard & McLain, PUP, 2012
    - Update history:
        1/10/2019 - RWB
"""
import sys
sys.path.append('..')

# import viewers and video writer
from mav_viewer import MAV_Viewer
# from video_writer import video_writer

#import the dynamics
from chp3.mav_dynamics import mav_dynamics as Dynamics

# import parameters
import parameters.sim_params as SIM

# import message types
from messages.state_msg import StateMsg

import numpy as np

# initialize messages
state = StateMsg()  # instantiate state message

# initialize dynamics object
dyn = Dynamics(SIM.ts_sim)

# initialize viewers and video
VIDEO = False  # True==write video, False==don't write video
mav_view = MAV_Viewer()

if VIDEO == True:
    video = video_writer(video_name="chap3_video.avi",
                         bounding_box=(0, 0, 1000, 1000),
                         output_rate=SIM.ts_video)

# initialize the simulation time
sim_time = SIM.t0

# main simulation loop
while sim_time < SIM.t_end:
    # Will need to set the initial state to check stuff
    #-------vary forces to check viewer-------------
    fx = 0
    fy = 0
    fz = 0
    if sim_time < 5:
        l = 0.1
    else:
        l = 0
    m = 0.0
    n = 0.0
    U = np.array([fx, fy, fz, l, m, n])

    dyn.update_state(U)
    state = dyn.msg_true_state
    #-------update viewer and video---------------
    #the issue is on the following line when VIDEO == True
    mav_view.update(state)
    if VIDEO == True: video.update(sim_time)

    #-------increment time-------------
    sim_time += SIM.ts_sim

print("Press Ctrl-Q to exit...")
if VIDEO == True: video.close()
