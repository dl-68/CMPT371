# Import socket module
from socket import *
import sys # In order to terminate the program
import _thread

FLAG = False  # this is a flag variable for checking quit

# function for receiving message from client
def recv_from_client(conn):
	global FLAG
	try:
		# Receives the request message from the client
		message = conn.recv(1024).decode()
		# if 'q' is received from the client the server quits
		if message == 'q':
			conn.send('q'.encode())
			print('Closing connection')
			conn.close()
			FLAG = True
		print('Message Received: ' + message)
		return message
	except:
		conn.close()


# function for receiving message from client
def send_to_client(conn, message):
	global FLAG
	try:
		send_msg = eval(message)
		#print(send_msg)	
		conn.send(str(send_msg).encode())

	except:
		conn.close()


# this is main function
def main():
	global FLAG
	HOST = 'localhost'
	serverPort = 12345
	serverSocket = socket(AF_INET, SOCK_STREAM)
	serverSocket.bind((HOST, serverPort))
	serverSocket.listen(5)
	print('The chat server is ready to connect to a Calc client')

	def client_thread(conn):
		while True:
			message = recv_from_client(conn)
			send_to_client(conn, message)

	while True:
		connectionSocket, addr = serverSocket.accept()
		print('Server is connected with a Calc client\n')
		_thread.start_new_thread(client_thread, (connectionSocket,))

	# closing serverScoket before exiting
	serverSocket.close()
	#Terminate the program after sending the corresponding data
	sys.exit()


# This is where the program starts
if __name__ == '__main__':
	main()
