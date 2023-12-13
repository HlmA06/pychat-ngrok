import socket
import threading
from pyngrok import ngrok
import atexit

# Asking user for the port number
port = int(input("Başlatmak için port numarası girin: "))

# Starting Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', port))
server.listen()

# Expose the local server using ngrok
public_url = ngrok.connect(port, "tcp")
print("Ngrok URL:", public_url)

# Lists For Clients and Their Nicknames
clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        try:
            client.send(message)
        except Exception as e:
            print("Hata oluştu: ", str(e))
            remove_client(client)

def send_private_message(sender, recipient, message):
    try:
        recipient_index = nicknames.index(recipient)
        recipient_client = clients[recipient_index]
        private_message = f'Private Message ({sender}): {message}'.encode('utf-8')
        recipient_client.send(private_message)
    except ValueError:
        print(f'{recipient} not found.')
    except Exception as e:
        print(f'Error occurred: {str(e)}')

def remove_client(client):
    index = clients.index(client)
    clients.remove(client)
    client.close()
    nickname = nicknames[index]
    broadcast(f'{nickname} left!'.encode('utf-8'))
    nicknames.remove(nickname)

def handle(client):
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if not message:
                break
            if message.startswith('/pm'):
                parts = message.split(' ')
                if len(parts) >= 3:
                    recipient = parts[1]
                    private_message = ' '.join(parts[2:])
                    send_private_message(nicknames[clients.index(client)], recipient, private_message)
                else:
                    client.send('Usage: /pm Recipient Message'.encode('utf-8'))
            else:
                broadcast(f'{nicknames[clients.index(client)]}: {message}'.encode('utf-8'))
        except Exception as e:
            print("Error occurred: ", str(e))
            remove_client(client)

def receive():
    while True:
        client, address = server.accept()
        print(f"Connection established: {str(address)}")
        client.send('NICK'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)
        print(f"Nickname: {nickname}")
        broadcast(f"{nickname} joined!".encode('utf-8'))
        client.send('Connected to the server!'.encode('utf-8'))
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

# Start receiving connections
receive_thread = threading.Thread(target=receive)
receive_thread.start()

# Server kapatıldığında ngrok bağlantısını da kapat
atexit.register(ngrok.disconnect)