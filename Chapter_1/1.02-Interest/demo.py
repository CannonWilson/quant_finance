import argparse
import numpy as np
import matplotlib.pyplot as plt
import math

def check_args(args):
    assert args.type in ['simple', 'discrete', 'continuous']
    assert args.time > 0
    assert args.initial > 0
    assert args.num_payments > 0
    assert args.num_payments


def visualize(x_time, y_dollars, type):
    plt.plot(x_time, y_dollars)
    plt.title(("Investment Value Under " +
                 type.capitalize() + " Interest"))
    plt.xlabel("Time (years)")
    plt.ylabel("Investment Value ($)")
    plt.show()

def main(args):
    """
    Run the main algorithm showing 
    how an investment's value changes 
    over time under different types 
    of interest. 

    Note: in the simple and discrete 
    cases, floor division is used 
    in order to reflect the 
    discontinuous nature of payments 
    being made in the real world.
    """
    check_args(args)

    x_time = np.linspace(0, args.time, args.num_intervals)
    inv_vals = []
    val = 0
    for time in x_time:
        if args.type == 'simple':
            val = args.initial * (1 + (args.rate/args.num_payments)*(time//(1/args.num_payments)))
        elif args.type == 'discrete':
            val = args.initial * (1 + (args.rate/args.num_payments))**(time//(1/args.num_payments))
        else:
            val = args.initial * math.e**(args.rate * time)
        inv_vals.append(val)
    
    visualize(x_time, inv_vals, type=args.type)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description = ("Implements simple or compounding (either "
                                                    "discrete or continuous) interest payments"))
    parser.add_argument('--type', type=str, required=True,
                        help=("Choose 'simple' 'discrete' or 'continuous'"))
    parser.add_argument('--time', type=float, required=True,
                        help=("Number of years investment is held"))
    parser.add_argument('--rate', type=float, required=True, default=0.05,
                        help=("The interest rate"))
    parser.add_argument('--initial', type=float, required=True,
                        help=("The amount (in dollars) of the initial investment"))
    parser.add_argument('--num_payments', type=float, required=False, default=2,
                        help=("The number of interest payments per annum"))
    parser.add_argument('--num_intervals', type=int, required=False, default=1000,
                        help=("The number of intervals to plot on the graph"))
    
    args = parser.parse_args()
    main(args)