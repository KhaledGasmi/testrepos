''	
import socket, sys
## use 0.0.0.0  to accept from any address
HOST = '127.0.0.1'
PORT = 5500
counter =0   # Count  active connect

# 1.  Create a  a connection  socket :
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. Bind  the socket to the precise address
try:
    mySocket.bind((HOST, PORT))
except socket.error:
    print(" The binding  socket to address failed !!")
    sys.exit (11)  ## arbitrary error code 
## in terminal check value of $?

while 1:
	# 3.  Waiting for a client connection
	print("Server is ready (Wait for a request ...")
	mySocket.listen(2)

	# 4. Connection is established 
	connect, addr = mySocket.accept()
	counter +=1
	print(f"Client {counter} , on {addr[0]} and Port {addr[1]}")

	# 5. The  Dialog  with the client 
	msgServ ="You are connected to bela Server. Adder Server"
	connect.send(msgServ.encode("Utf8"))
	
	while 1:
		msgClient = connect.recv(1024).decode("Utf8")
		print("Client sent:\t", msgClient)
		
		if msgClient.upper() == "END" or msgClient =="": break
		y= "OK, Continue"
		connect.send(y.encode("Utf8"))
		

	# 6. Close the Connection :
	connect.send("end".encode("Utf8"))
	print("Connection Finishes")
	connect.close()

	ch = input("Give R to redo, or E to End ? \t")
	if ch.upper() =='E':         break


