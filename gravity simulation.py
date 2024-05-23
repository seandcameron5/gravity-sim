import numpy as np
import matplotlib.pyplot as plt
import math

G = 100

class Body:
    def __init__(self, x, y, v_x, v_y, m):
        self.x = x
        self.y = y
        self.v_x = v_x
        self.v_y = v_y
        self.m = m
        
    def __repr__(self):
        return str(self.x) + " " + str(self.y) + " " + str(self.v_x) + " " + str(self.v_y) + " " + str(self.m) 


class Body_List:
    def __init__(self, body_list):
        self.body_list = body_list
    def update(self, dt):
        for updating_body in self.body_list:
            dv_x_total = 0
            dv_y_total = 0
            for other_body in self.body_list:
                r_x = other_body.x - updating_body.x
                r_y = other_body.y - updating_body.y
                r = np.sqrt(r_x**2 + r_y**2)
                if r != 0:
                    da = G * other_body.m / r**2 * dt
                    dv_x = da * dt * r_x / r
                    dv_y = da * dt * r_y / r
                    dv_x_total += dv_x
                    dv_y_total += dv_y
            updating_body.x += updating_body.v_x * dt
            updating_body.y += updating_body.v_y * dt
            updating_body.v_x += dv_x_total
            updating_body.v_y += dv_y_total
            #print(updating_body)
            
    def evolve(self, time_span, dt):
        for i in range(math.ceil(time_span / dt)):
            for body in self.body_list:
                plt.plot(body.x, body.y, 'bo')
            plt.pause(0.01)
            self.update(dt)
        plt.show()

#m_1 = 1500
a = 2.3

#Planet around sun
#body_list = Body_List([Body(0, 0, 0, 0, m_1), Body(0.25, 0.25, -a, a, 1)])

# Triangle
body_list = Body_List([Body(0, 0, a*np.cos(2 * np.pi / 3), a*np.sin(2 * np.pi / 3), 100), Body(0.5, np.sqrt(3) / 2, a*1, 0, 100), Body(1, 0, a*np.cos(4 * np.pi / 3), a*np.sin(4 * np.pi / 3), 100)])

body_list.evolve(0.5, 0.001)