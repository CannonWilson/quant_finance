import matplotlib.pyplot as plt
import random
import operator

class RandomWalk():

    def __init__(self, mode, p_up, inc_factor, 
                 dec_factor, num_steps, start_val):
        self.mode = mode
        self.p_up = p_up
        self.inc_factor = inc_factor
        self.dec_factor = dec_factor
        self.num_steps = num_steps
        self.start_val = start_val
    
    def visualize(self, values):
        plt.plot(values)
        plt.title(self.mode.capitalize() + ' Random Walk')
        plt.xlabel('Time Step')
        plt.ylabel('Value')
        print('showing')
        plt.show()

    def calc_values(self):
        val = self.start_val
        vals = [val]
        op = operator.mul if self.mode == 'geometric' else operator.add 
        for _ in range(self.num_steps):
            rand_num = random.uniform(0,1)
            if val == 0:
                next_val = 0
            elif rand_num <= self.p_up: # increase val
                next_val = op(val, self.inc_factor)
            else: # decrease val
                next_val = op(val, self.dec_factor)
            vals.append(next_val)
            val = next_val
        return vals