import argparse
import time
import urllib.parse
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


def get_max_prime_factor(n):
    prime_factor = 1
    i = 2
    while i <= n / i:
        if n % i == 0:
            prime_factor = i
            n /= i
        else:
            i += 1
    if prime_factor < n:
        prime_factor = n
    return int(prime_factor)


class PrimeNumberRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        q_path = urllib.parse.urlparse(self.path)
        qs = urllib.parse.parse_qs(q_path.query)

        if q_path.path != "/prime":
            self.send_error(HTTPStatus.NOT_FOUND, "wrong path")
            return

        try:
            number = int(qs["number"][0])
        except KeyError:
            self.send_error(HTTPStatus.BAD_REQUEST,
                            "number query parameter is required")
            return
        except ValueError:
            self.send_error(HTTPStatus.BAD_REQUEST,
                            "number must be an integer")
            return

        try:
            add_exec_time = qs["perf"][0] == "1"
        except (KeyError, ValueError):
            add_exec_time = False

        t_start = time.time()
        max_prime = get_max_prime_factor(number)
        t_end = time.time()
        elapsed = (t_end - t_start) * 10e5

        self.send_response(HTTPStatus.OK)
        if add_exec_time:
            self.send_header("x-exec-time", str(elapsed))

        self.end_headers()
        self.wfile.write(f"{max_prime}\n".encode())


def run(bind_addr: str, bind_port: int, add_exec_time: bool = False):
    server_address = bind_addr, bind_port
    PrimeNumberRequestHandler.add_exec_time = add_exec_time
    httpd = ThreadingHTTPServer(server_address, PrimeNumberRequestHandler)
    print(f"Listening on http://{bind_addr}:{bind_port}")
    httpd.serve_forever()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-b", "--bind_addr", default="localhost", help="host to bind server",
        type=str
    )
    parser.add_argument("-p", "--bind_port", default=8080,
                        help="port to bind server", type=int)
    args = parser.parse_args()
    run(args.bind_addr, args.bind_port)
