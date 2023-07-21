import socket

def send_file(file_path, host, post):

    BUFFER_SIZE = 4096
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try: 
        with open(file_path, 'rb') as file:
            while True:
                data = file.read(BUFFER_SIZE)
                if not data:
                    break
                client_socket.sendall(data)
            
        print('Done!!!')
        
    except Exception as e:
        print('Error: ', e)
        
    finally:
        client_socket.close()
        
        
if __name__ == "__main__":
    file_to_send = ""  # Data path
    target_host = "" # Target IP address
    target_port = 12345 # Target port
    send_file(file_to_send, target_host, target_port)