import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# instance = MyClass(argument1, argument2...)

port_number = 65432
server_socket.bind(("0.0.0.0", port_number))
server_socket.listen()
print(f"Listening for incoming connection on port {port_number}...")

connection, address = server_socket.accept()
print(f"Connected by {address}.")

while True:
    # for as long as you receive data...
    # grab it in chunks of 1024 bytes
    data = connection.recv(1024)
    # (if you didn't get any data, stop listening)
    if not data:
        break
    # and return it back to the sender in upper case
    connection.sendall(data.upper())

server_socket.close()