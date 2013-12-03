#!/usr/bin/env python
#Tiago de Freitas Pereira <tiagofrepereira@gmail.com>
#Fri Jul 13 14:30:00 CEST 2012

"""
Example packge
"""
import numpy
import argparse

def main():

  ##########
  # General configuration
  ##########

  parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
  parser.add_argument('-s', '--string', type=str, dest='string', default='STRING', help='Example of string (defaults to "%(default)s")')

  parser.add_argument('-n', '--number', dest="number", default=64, type=int, help="Example of number (defaults to '%(default)s')")

  parser.add_argument('-c', '--choice', type=str, choices=('A', 'B', 'C'), default='C', dest='choice', help='Example of choice (defaults to "%(default)s")')

  args = parser.parse_args()
  
  print(args)

  return 0

if __name__ == "__main__":
  main()
