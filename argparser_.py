import argparse
parser = argparse.ArgumentParser(description="Testing the argument parser")
# parser.add_argument("echo", help="echo the string you use here")
parser.add_argument("square", help="returns the square of the value passed in", type=int)
parser.add_argument("-v", "--verbosity", help="increase the verbosity", action="store_true")
args = parser.parse_args()

if args.verbosity:
    print("verbosity turned on")
# print (args.echo)
print (args.square**2)