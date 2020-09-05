# Testing client
Client tests prime_number_httpd.py server

## How to use:
To start server:
- `python prime_number_httpd.py -b localhost -p 8080`

To start client:
- `python stress_tester.py -n [number] -r [request_number] -t [thread_number]`

Parameters:
- number will be used in get_max_prime_factor() function
- request_number: number of requests per connection
- thread_number: number of threads

Client returns following data:
- Min. value
- Max. value
- Mean value of data
- Median value of data
- Standard deviation of data