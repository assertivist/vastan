MAX_SEQ = 255
TIMEOUT = 10

# packets are like
# [
#       int id,
#       int last_id_i_got_from_u,
#       bitfield ack,
#       [
#           [byte type, varying data],
#           ...
#       ]
# ]
# and then get dumped into
import rencode

from enum import Enum
class PackType(Enum):
    
    # composable packet types

    hello = 0x01
    name = 0x02
    goodbye = 0x03
    chat = 0x04
    heartbeat = 0x05
    
    # maybe something like this for
    # game packets: sending only what
    # is necessary

    # player_head_only = 0x06
    # player_rot_only = 0x07
    # player_xz_only = 0x08
    # player_xz_rot = 0x09
    # player_xz_head_rot = 0x0A
    # player_xyz_only = 0x0B
    # player_xyz_head = 0x0C
    # player_xyz_head_rot = 0x0D
    # player_fire = 0x0E
    # laser_xy = 0x0F
    # laser_xyz = 0x10
    # grenade_xyz = 0x11
    # missile_xyz = 0x12

import asyncio

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
        else:
            self.clients[addr].handle_packet(data)    

    def error_received(self, exc):
        print('Error:', exc)

    def connection_lost(self, exc):
        print('connection closed', exc)

class ConnectedClient:

    name = "UnamedPlayer"
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
                # number, encode, send
                # update ack
                pass          

    def handle_packet(self, data):


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
        # decode
        #d = rencode.loads(data)

        print('received "{}"').format(d)

        pid = int(d[0])

        if pid > last_received:
            # by how much?
            diff = 0
            # if difference greater than MAX_SEQ - 1, 
                # we wrapped around
            # otherwise:
                # if the difference is negative:
                    # old packet
                    # insert into history
                    # update ack
                # difference is positive:
                    # new packet
                    # update last received
                    # update ack


    def connection_lost(self, exc):
        print('closing transport', exc)

    def make_ack(self):
        # look at history
        # 1 for received, 0 for no packet
        pass

