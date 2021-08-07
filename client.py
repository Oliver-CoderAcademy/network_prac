import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# instance = Class(argument1, argument2)

client_socket.connect(("10.0.0.24", 65432))

message_to_send = input("What would you like to send to the server? \n")

client_socket.sendall(bytes(message_to_send, "utf-8"))

received_message = client_socket.recv(1024)

print("You received from the server this message:")
print(repr(received_message))
# print a string representation of the bytes received

client_socket.close()