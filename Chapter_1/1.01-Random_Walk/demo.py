import matplotlib.pyplot as plt
import argparse
from random_walk import RandomWalk

def check_args(args):
    """
    Check that command-line arguments 
    have been declared correctly
    """
    assert args.mode in ['geometric', 'arithmetic']
    if args.mode == 'geometric': 
        assert args.inc_factor >= 1
        assert 0 <= args.dec_factor <= 1
    if args.mode == 'arithmetic':
        assert args.inc_factor >= 0
        assert args.dec_factor <= 0
    assert args.num_steps > 0
    assert args.start_val > 0


def main(args):

    check_args(args)
    model = RandomWalk(args.mode, args.p_up, args.inc_factor, 
                 args.dec_factor, args.num_steps, args.start_val)
    vals = model.calc_values()
    model.visualize(vals)



if __name__ == "__main__":

    parser = argparse.ArgumentParser(description = 'Implements geometric or arithmetic random walk')
    parser.add_argument('-m', '--mode', type=str, required=True,
                        help=("The mode for the random walk, either "
                              "'geometric' or 'arithmetic'"))
    parser.add_argument('-pu', '--p_up', type=float, required=False, default=0.5,
                        help=("The probability that the value at the "
                              "next time step increases"))
    parser.add_argument('-if', '--inc_factor', type=float, required=True,
                        help=("The number the current value is multiplied "
                              "by (geometric) or what gets added to the "
                              "current value (arithmetic) at each time step"))
    parser.add_argument('-df', '--dec_factor', type=float, required=True,
                        help=("The number the current value is multiplied "
                              "by (geometric) or what gets subtracted from the "
                              "current value (arithmetic) at each time step"))
    parser.add_argument('-n', '--num_steps', type=int, required=False, default=20,
                        help=("The number of steps to run the experiment"))
    parser.add_argument('-s', '--start_val', type=float, required=False, default=100,
                        help=("The starting value for the experiment"))
    
    args = parser.parse_args()
    main(args)