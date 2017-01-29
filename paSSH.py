#! /usr/bin/env python

import sys, socket, argparse, paramiko, logging
logging.basicConfig() #turn off Paramiko logging

class SSH_Server(paramiko.ServerInterface):
    def check_auth_password(self, user, passwd):
        print "[*] Connection Attempt: user= " + str(user) + " | passwd= " + str(passwd)
        return paramiko.AUTH_FAILED

def Reveal(keyfile, port):
    print "\n===================== paSSH [SSH Password Revealer] ====================="
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('', port))
        s.listen(5)
        while 1:
            client, addr = s.accept()
            sess = paramiko.Transport(client)
            sess.add_server_key(paramiko.RSAKey(filename=keyfile))
            sess.start_server(server=SSH_Server())
    except Exception, e:
        print "[-] Exception: " + str(e)

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument('-k', '--keyfile')
    p.add_argument('-p', '--port', type=int)
    args = p.parse_args()

    if (not args.keyfile) or (not args.port):
        print "[*] Arguments are missing.  Usage: python " + sys.argv[0] + " -k [RSA private key file] -p [port]\n"
        sys.exit(0)

    else:
        Reveal(args.keyfile, args.port)
