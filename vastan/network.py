import asyncio
import rencode

MAX_SEQ = 255
TIMEOUT = 10

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
			self.clients[addr] = dict()

	def next_id():
		new_id = next_packet_id
		next_packet_id += 1
		if next_packet_id > MAX_SEQ:
			next_packet_id = 0

	def error_received(self, exc):
		print('Error:', exc)

	def connection_lost(self, exc):
		print('connection closed', exc)

class ClientProtocol:
	remote_packet_id = 0
	last_received = 0
	
	def connection_made(self, transport):
		self.transport = transport

	def datagram_received(self, data, addr):
		last_received = 0
		print('received "{}"'.format(data.decode()))

