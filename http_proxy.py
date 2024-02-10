import random
import socket
import threading
import income_conn


port = 8881
php_port =  80
php_host = '127.0.0.1'
id_len = 5

def main():
    
    global conns
    
    threading.Thread(target=income_conn.listen).start()
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('127.0.0.1', port))
    server.listen(10)

    print('Running on', port)

    while True:
        conn, _ = server.accept()
        data = conn.recv(8192)

        first_line = data.split(b"\n")[0]
        try:
            target = first_line.split()[1]
        except Exception as e:
            print("ERROR", e)
            continue

        host, _ = target.split(b":")

        conn.send(b'HTTP/1.1 200 OK\n\n')

        new_http_bridge(conn, host)
        

# generationg ID for every connection, so target keeps the same
def new_http_bridge(conn:socket, host:bytes):
    
    id = random.randbytes(id_len).hex().encode()
    income_conn.conns[id] = conn
    
    sock = socket.socket()
    sock.connect(('127.0.0.1', php_port))
    sock.send(b"GET / HTTP/1.1\r\n" +
            b"Host2: " + host + b"\r\n" +
            b"Host: " + php_host.encode() + b"\r\n" + 
            b"Id: " + id + b"\r\n\r\n")
    sock.close()
    
    print("Sent remote request", host, id)
    
    return id

if __name__ == "__main__":
    main()
