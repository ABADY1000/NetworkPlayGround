import socket as s

name = s.gethostname()
host = 'localhost'
port = 10_000
print(name)


c = s.socket(s.AF_INET, s.SOCK_STREAM, 0)

c.bind((host, port))
c.listen(5)
while True:
    d, addr = c.accept()
    print("Received data form ({}) with data:\n{}\n\n".format(addr,d))
    c.send("Your data is received")
    c.close()


