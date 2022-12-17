import socket as s

name = s.gethostname()
host = 'localhost'
port = 10_000
print(name)


c = s.socket(s.AF_INET, s.SOCK_STREAM, 0)

c.connect((host, port))
data = c.recv(1024)
print("Data: ".format(data))
c.close()

