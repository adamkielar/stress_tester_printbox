# Testing client
Client tests prime_number_httpd.py server

## How to use:
To start server:
- `python prime_number_httpd.py -b localhost -p 8080`

To start client:
- `python stress_tester.py -n [number] -r [request_number] -t [thread_number]`