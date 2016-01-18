import asyncio
import rencode
from enum import Enum

MAX_SEQ = 255
TIMEOUT = 10

# packets are like
# [
#       int id,
#       int last_id_i_got_from_u,
#       bitfield ack,
#       byte type,
#       varying data
# ]

class PackType(Enum):
    hello = 0x01
    name = 0x02
    goodbye = 0x03
    chat = 0x04
    heartbeat = 0x05


class Network:
    def __init__(self):
        pass

def bitlist_from_int(num):
    return list(1 if digit == "1" else 0 for digit in bin(num)[2:])

class ServerProtocol:

    clients = list()
    next_packet_id = 0
    
    def connection_made(self, transport):
        print('connection', transport)
        self.transport = transport

    def datagram_received(self, data, addr):
        print('Data received: ', data, addr)
        if addr not in self.clients:
            self.clients[addr] = ConnectedClient(addr, self.transport)    

    def error_received(self, exc):
        print('Error:', exc)

    def connection_lost(self, exc):
        print('connection closed', exc)

class ConnectedClient:

    pending_updates = []
    sent_packets = []
    next_packet_id = 0
    last_received = 0
    ack = 255

    def __init__(self, addr, transport):
        self.addr = addr
        self.transport = transport

    def send(self, data):
        self.transport.sendto(data)

    def update(self):
        if len(pending_updates) > 1:
            for update in pending_updates:
                

    def next_id():
        new_id = next_packet_id
        next_packet_id += 1
        if next_packet_id > MAX_SEQ:
            next_packet_id = 0


class ClientProtocol:

    local_packet_id = 0
    remote_packet_id = 0
    last_received = 0
    packets = []
    
    def connection_made(self, transport):
        self.transport = transport

    def datagram_received(self, data, addr):
        last_received = 0
        d = rencode.loads(data)

        print('received "{}"'.format(d)

        pid = int(d[0])

        if pid > last_received:
            # by how much?
            diff = 


    def connection_lost(self, exc):
        print('closing transport', exc)

    def make_ack(self):


