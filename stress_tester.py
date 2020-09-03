import argparse
import time



def test_server(request_number: int, connection_number: int, number: int):
    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Started testing server.')
    parser.add_argument('-r', '--request_number', default=1,
                        help='number of server requests', type=int)
    parser.add_argument('-c', '--connection_number', default=1,
                        help='number of simultaneous connections', type=int)
    parser.add_argument('-n', '--number', default=1000000000001,
                        help='prime number', type=int)
