import math
import socket
import sys
import time
import errno
from multiprocessing import Process

def process_start(s_sock):
    s_sock.send(str.encode('Online Calculator.... Mathematical Functions: [1-Logarithmic | 2-Square Root | 3-Exponential] >> Enter your choice of operation: '))
    while True:
        data = s_sock.recv(2048)
        data = data.decode('utf-8')
        print(data)
        
        if not data:
            break
        elif data == '1':
            s_sock.send(str.encode('Enter numbers: '))
            calc = s_sock.recv(2048)
            calc = int(calc)
            calc = str(math.log(calc))
            print(calc)
            s_sock.send(str.encode('The answer is '+calc+ ' <<Press any key to continue>>'))
        elif data == '2':
             s_sock.send(str.encode('Enter numbers:'))
             calc = s_sock.recv(2048)
             calc = int(calc)
             calc = str(math.sqrt(calc))
             print(calc)
             s_sock.send(str.encode('The answer is '+calc+ ' <<Press any key to continue>>'))
        elif data == '3':
             s_sock.send(str.encode('Enter a number to calculate:'))
             calc = s_sock.recv(2048)
             calc = int(calc)
             calc = str(math.exp(calc))
             print(calc)
             s_sock.send(str.encode('The answer is '+calc+ ' <<Press any key to continue>>'))
        else:
            s_sock.send(str.encode('Error!! Function not available!'))
        break

    s_sock.close()

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("",8888))
    print("\nListening...")
    s.listen(3)
    try:
        while True:
            try:
                s_sock, s_addr = s.accept()
                p = Process(target=process_start, args=(s_sock,))
                p.start()

            except socket.error:

                print('Got a socket error')

    except Exception as e:
        print('An exception occurred!')
       	print(e)
        sys.exit(1)

    finally:
        s.close()

