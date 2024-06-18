import sys
import socket
import logging

class Client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.sock = None

    def run(self):
        logging.basicConfig(filename="client.log", level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s")

        if len(sys.argv) != 3:
            print("Try Again")
            return

        self.ip = sys.argv[1]
        self.port = int(sys.argv[2])


        if not self.ip or not self.port:
            print("Please provide IP and Port")
            return

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        if not self.sock:
            logging.error("Failed to create socket")
            return

        try:
            self.sock.connect((self.ip, self.port))
        except socket.error as e:
            print("Failed to connect")
            return

        while True:
            message = input("Enter message: ")
            self.sock.sendall(message.encode())
            data = self.sock.recv(1024)

            if message.lower() == "network":
                print("Easter Egg: ".format(data.decode()))
                logging.info("Recieved Easter Egg message: ".format(data.decode()))
            else:
                print(data.decode())
                logging.info("Recieved message: ".format(data.decode()))

        self.sock.close()

if __name__ == "__main__":
    client = Client("",0)
    client.run()
