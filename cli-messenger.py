import socket

role = int(input("enter your role:\n1: host\n2: join\n(1 or 2)\n==>> "))

if role == 1:

    HOST = input("enter your ip: ")
    PORT = int(input("enter a free port(example:12345): "))

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(1)
    print(f"server is listening on {HOST}:{PORT}")

    client, addr = server.accept()
    print(f"connected by {addr}")

    while True:
        data = client.recv(1024).decode()
        if not data or data.lower() == "exit":
            print("connection closed from client")
            break
        print(f"data from client: {data}")
        replay = input("write your messege: ")
        client.send(replay.encode())
    
    client.close()
    server.close()

elif role == 2:
    HOST = input("enter host ip: ")
    PORT = int(input("enter host port: "))

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    while True:
        replay = input("write: ")
        client.send(replay.encode())
        if replay.lower == "exit":
            break
    
        data = client.recv(1024).decode()
        print(f"data from server: {data}")
        
    client.close()
