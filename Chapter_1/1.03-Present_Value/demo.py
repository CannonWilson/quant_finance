import argparse
import math

def check_args(args):
    assert args.delta_t > 0


def main(args):
    """
    Calculate the present value 
    of funds received in the 
    future
    """
    check_args(args)

    pv = args.future_val * math.e**(-args.rate*args.delta_t)
    print('Present Value: ', pv)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description = ("Implements simple or compounding (either "
                                                    "discrete or continuous) interest payments"))
    parser.add_argument('--future_val', type=float, required=True,
                        help=("The dollar value of the funds received "
                              "(positive) or required (negative) in the future"))
    parser.add_argument('--rate', type=float, required=True,
                        help=("The annual rate of return achievable between "
                              "the present and the future "))
    parser.add_argument('--delta_t', type=float, required=True,
                        help=("The number of years elapsed between "
                              "the present and when the funds "
                              "are received"))
    
    
    args = parser.parse_args()
    main(args)