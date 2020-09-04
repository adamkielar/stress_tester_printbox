import argparse
import socket
import urllib.parse
from http.client import HTTPConnection


def test_server(number: int, request_number: int, ):
    params = urllib.parse.urlencode({'number': number, 'perf': request_number})
    path = f'/prime?{params}'
    conn = HTTPConnection('localhost', 8080)
    conn.request('GET', path)
    response = conn.getresponse()
    print(response.status, response.reason, response.msg)
    print(response.read())
    conn.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Started testing server.')
    parser.add_argument('-n', '--number', default=1000000000001,
                        help='prime number', type=int)
    parser.add_argument('-r', '--request_number', default=1,
                        help='number of request', type=int)
    parser.add_argument('-t', '--thread_number', default=1,
                        help='number of connections', type=int)
    args = parser.parse_args()
    test_server(args.number, args.request_number)
