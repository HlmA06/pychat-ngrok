import socket
import threading

# Choosing Nickname
nickname = input("Adınızı girin: ")

# Connecting To Server
host = input("Ngrok URL'sini girin: ")  # Bu URL'yi server.py çalıştırıldıktan sonra alın
port = int(input("Sunucu port numarasını girin: "))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'NICK':
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            print("Bir hata oluştu!")
            client.close()
            break

def send_private_message(recipient, message):
    private_message = f'/pm {recipient} {message}'
    client.send(private_message.encode('utf-8'))

def write():
    while True:
        message = input('')
        if message.startswith('/pm'):
            parts = message.split(' ')
            if len(parts) >= 3:
                recipient = parts[1]
                private_message = ' '.join(parts[2:])
                send_private_message(recipient, private_message)
            else:
                print('Kullanım: /pm KullaniciAdi Mesajiniz')
        else:
            client.send(f'{nickname}: {message}'.encode('utf-8'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()