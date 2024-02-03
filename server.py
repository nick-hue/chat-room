import socket
import select

def host_connection(IP_ADDRESS, PORT, MAX_CONNECTIONS):
    IP_ADDRESS = '127.0.0.1'  # LocalHost
    PORT = 12345  # Arbitrary non-privileged port
    MAX_CONNECTIONS = 2

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((IP_ADDRESS, PORT))
    server_socket.listen(MAX_CONNECTIONS)

    sockets_list = [server_socket]
    clients = {}

    print(f'Listening for connections on {IP_ADDRESS}:{PORT}...')

    def receive_message(client_socket):
        try:
            message_header = client_socket.recv(10)
            if not len(message_header):
                return False
            message_length = int(message_header.decode('utf-8').strip())
            return {"header": message_header, "data": client_socket.recv(message_length)}
        except:
            return False

    while True:
        read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)
        
        for notified_socket in read_sockets:
            if notified_socket == server_socket:
                client_socket, client_address = server_socket.accept()
                
                if len(sockets_list) - 1 < MAX_CONNECTIONS:  # -1 for the server socket itself
                    user = receive_message(client_socket)
                    if user is False:
                        continue
                    
                    sockets_list.append(client_socket)
                    clients[client_socket] = user
                    print('Accepted new connection from {}:{}, username: {}'.format(*client_address, user['data'].decode('utf-8')))
                else:
                    print('Max connections reached. Connection refused.')
                    client_socket.close()
                    
            else:
                message = receive_message(notified_socket)
                
                if message is False:
                    print('Closed connection from: {}'.format(clients[notified_socket]['data'].decode('utf-8')))
                    sockets_list.remove(notified_socket)
                    del clients[notified_socket]
                    continue
                
                user = clients[notified_socket]
                print(f'Received message from {user["data"].decode("utf-8")}: {message["data"].decode("utf-8")}')
                
                for client_socket in clients:
                    if client_socket != notified_socket:
                        client_socket.send(user['header'] + user['data'] + message['header'] + message['data'])
        
        for notified_socket in exception_sockets:
            sockets_list.remove(notified_socket)
            del clients[notified_socket]
