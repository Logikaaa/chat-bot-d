from socket import*
import threading

client_socket = socket(AF_INET, SOCK_STREAM)
name = input("Введіть ім'я:")
client_socket.connect(('localhost', 8080))
client_socket.send(name.encode())

def send_message():
    while True:
        client_massage = input()
        if client_massage.lower() == "exit":
            client_socket.close()
            break
        client_socket.send(client_massage.encode())

while True:
    try:
        message = client_socket.recv(1024).decode().strip()
        if message:
            print(message)
    except:
        break


