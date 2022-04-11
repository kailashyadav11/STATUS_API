import socket

HOSTNAME = socket.gethostname()
# HOST = socket.gethostbyname(HOSTNAME)
HOST = "0.0.0.0"
PORT = 80
CLUSTER_DB = "/opt/seagate/cortx/status/db/cluster_status.json"
