import socket, random
from time import sleep

s = socket.socket()
host = socket.gethostname()
port = 8080
s.bind((host, port))
s.listen(5)
print("Server Running...")

# Accept the connection
c, addr = s.accept()
print(f"Connected to {addr}")

# Initialize
receivedMsg = {}
n = int(c.recv(1024).decode("utf-8"))
msgLength = int(c.recv(1024).decode("utf-8"))
print(f"The size of the message is {msgLength} and sliding window size is {n}\n")
expected_seq = 0  # Expected sequence number

try:
    while True:
        if len(receivedMsg) < msgLength:
            msg = c.recv(1024).decode("utf-8").split(',')
            seq_num = int(msg[0])
            data = msg[1]
            
            if seq_num == expected_seq:
                print(f"Received Message: Seq {seq_num} -> {data}")
                receivedMsg[seq_num] = data
                expected_seq += 1
            else:
                print(f"Out of order message received. Expected {expected_seq}, got {seq_num}")

            # Randomly simulate ACK loss (reduced chances to 1 in 5)
            randomAckLoss = random.randint(0, 4)
            if randomAckLoss == 0:
                print(f"\nSimulating loss of ACK for Seq {seq_num}\n")
                continue  # Skip sending ACK to simulate loss
            else:
                print(f"\tSending ACK for Seq {seq_num}...")
                c.send(bytes(f"Ack: {seq_num}", "utf-8"))

        # Check if all messages are received
        if len(receivedMsg) == msgLength:
            print(f"\n>>Final Received Message: {receivedMsg}")
            print("Connection Closed!")
            break
except Exception as e:
    print(f"Error: {e}")
finally:
    c.close()
