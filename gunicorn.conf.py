bind = '0.0.0.0:8000'  # Replace with the desired host and port

# Number of worker processes to spawn
workers = 4

# Number of threads per worker
threads = 2

# Maximum requests to process per worker before restarting it
max_requests = 1000

# Maximum number of simultaneous clients that a worker can handle
worker_connections = 1000

# Timeout for graceful worker shutdown
timeout = 30

# Set the access log file path
accesslog = '-'  # Log to stdout

# Set the error log file path
errorlog = '-'  # Log to stdout

# Log level
loglevel = 'info'
