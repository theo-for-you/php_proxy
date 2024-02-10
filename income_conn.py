
import socket
import http_proxy
import threading

port = 8882
conns = {}


# Listening for php server to call
def listen():
    global conns, port
    
    listen_sock = socket.socket()
    listen_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_sock.bind(('127.0.0.1', port))
    listen_sock.listen(10)
    
    print("Listening on", port)
    
    while True:
        conn_remote, _ = listen_sock.accept()
        id = conn_remote.recv(http_proxy.id_len*2)
        
        if id in conns:
            conn_local = conns[id]
            print("Bridge connected", id)
            threading.Thread(target=bridge, args=(conn_local, conn_remote, )).start()
            
            
            
def bridge(local_conn: socket.socket, remote_server: socket.socket):
    
        
        def send(from_s: socket.socket, to_s: socket.socket):
            while True:
                to_s.send(from_s.recv(2000))   
                 
        threading.Thread(target=send, args=(local_conn, remote_server, )).start()
        threading.Thread(target=send, args=(remote_server, local_conn, )).start()
        