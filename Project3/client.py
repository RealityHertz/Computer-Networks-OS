import argparse
import socket
import struct

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--server', type=str, required=True, help='Server IP address')
    parser.add_argument('-p', '--port', type=int, required=True, help='Server port')
    parser.add_argument('-l', '--log-file', type=str, required=True, help='Path to log file')
    return parser.parse_args()

def log(msg, log_file):
    with open(log_file, 'a') as f:
        f.write

