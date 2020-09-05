import argparse
import statistics
import threading
import urllib.parse
from http.client import HTTPConnection

elapsed_list = []


def test_server(number: int, request_number: int):
    params = urllib.parse.urlencode({'number': number, 'perf': 1})
    path = f'/prime?{params}'

    conn = HTTPConnection('localhost', 8080)

    for i in range(0, request_number):
        print('Request number ', i)
        conn.request('GET', path)
        response = conn.getresponse()
        elapsed_number = float(response.getheader('x-exec-time'))
        elapsed_list.append(elapsed_number)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Started testing client.')
    parser.add_argument('-n', '--number', default=1000000000001,
                        help='number', type=int)
    parser.add_argument('-r', '--request_number', default=1,
                        help='number of request', type=int)
    parser.add_argument('-t', '--thread_number', default=1,
                        help='number of connections', type=int)
    args = parser.parse_args()

    for j in range(0, args.thread_number):
        print('Thread number ', j)
        client = threading.Thread(
            target=test_server(args.number, args.request_number),
            args=(j,))
        client.start()

    print('Elapsed list ', elapsed_list)
    print('Min of data: ', min(elapsed_list))
    print('Max of data: ', max(elapsed_list))
    print('Mean of data: ', statistics.mean(elapsed_list))
    print('Median of data: ', statistics.median(elapsed_list))
    if len(elapsed_list) > 1:
        print('Standard deviation: ', statistics.stdev(elapsed_list))
