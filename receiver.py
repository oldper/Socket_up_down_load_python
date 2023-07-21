import socket

def receive_file(save_path, host, port):
    BUFFER_SIZE = 4096
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        server_socket.bind((host,port))
        server_socket.listen()
        
        print(f"Wait connction from {host}:{port}.")
        
        client_socket, client_address = server_socket.accept()
        
        print(f"connect with {client_address}!")
        
        with open(save_path, 'wb') as file:
            while True:
                data = client_socket.recv(BUFFER_SIZE)
                if not data:
                    break
                file.write(data)
                
                
        print('Done!')
        
    except Exception as e:
        print("Error: ", e)
        
    finally:
        client_socket.close()
        server_socket.close()
        
        
if __name__ == "__main__":
    save_received_file = "" #Path for saving data
    host_ip = "0.0.0.0" # listen all usable IP address
    listen_port = 12345  # listen port
    receive_file(save_received_file, host_ip, listen_port)