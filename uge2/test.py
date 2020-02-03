import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='A program that downloads a URL and stores it locally')
    parser.add_argument('url', help='The URL to process')
    parser.add_argument('-d', '--destination',
                        help='The name of the file to store the url in')

    args = parser.parse_args()
    print('URL:', args.url)
    print('Destination:', args.destination)


# parser = argparse.ArgumentParser(description='Process some integers.')
# parser.add_argument('integers', metavar='N', type=int, nargs='+',
#                     help='an integer for the accumulator')
# parser.add_argument('--sum', dest='accumulate', action='store_const',
#                     const=sum, default=max,
#                     help='sum the integers (default: find the max)')

# args = parser.parse_args()
# print(args.accumulate(args.integers))
