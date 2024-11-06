"""
An example of using the argparse module to parse command line arguments.

Try running this script with the following commands:
python argparse_demo.py --help
python argparse_demo.py --greeting "Howdy" --caps "World"
python argparse_demo.py "World" --caps
"""
import argparse

parser = argparse.ArgumentParser(description='A demo of argparse')
parser.add_argument('name', type=str, help='The name to print')
parser.add_argument('--greeting', type=str, default='Hello', help='The greeting to use')
parser.add_argument('--caps', action='store_true', help='Print the name in all caps')
args = parser.parse_args()

if args.caps:
    print(f'{args.greeting}, {args.name}!'.upper())
else:
    print(f'{args.greeting}, {args.name}!')