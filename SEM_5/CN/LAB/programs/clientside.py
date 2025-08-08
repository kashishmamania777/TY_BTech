import socket
from time import sleep

s = socket.socket()
host = socket.gethostname()
port = 8080

try:
    s.connect((host, port))
    print("Connected to", str(host) + ": " + str(port))

    # Get the list of messages to be sent
    msg = input("Enter list of messages to be sent separated by ',': ").split(',')
    
    # Calculate the window size as 2^(number of frames - 1)
    number_of_frames = len(msg)
    n = 2 ** (number_of_frames - 1)
    
    print(f"Message list: {msg}, Calculated Window size: {n}\n")

    # Send the window size and number of messages to the server
    s.send(bytes(str(n), "utf-8"))
    s.send(bytes(str(number_of_frames), "utf-8"))

    # Sliding window buffer
    windowBuffer = msg[:n]  # Initially fill the window with the first `n` messages
    seq_num = 0  # Sequence number
    unacked = {}  # Dictionary to track unacknowledged frames

    s.settimeout(5)  # Set a 5-second timeout to avoid hanging

    while True:
        # Send messages in the window
        if seq_num < len(msg):
            print(f"\tSending Seq {seq_num}: {msg[seq_num]}...")
            s.send(bytes(f"{seq_num},{msg[seq_num]}", "utf-8"))
            unacked[seq_num] = msg[seq_num]  # Mark frame as unacknowledged
            seq_num += 1
            sleep(1)

        try:
            # Try to receive the ACK
            ack = s.recv(1024).decode("utf-8")
            ack_num = int(ack.split(":")[1].strip())  # Extract sequence number from ACK
            print(f"{ack}", end="\t")

            # Remove the acknowledged frame from the buffer
            if ack_num in unacked:
                del unacked[ack_num]

            # Update sliding window if all ACKs for current window are received
            if seq_num - len(unacked) == n:
                # Move window
                windowBuffer = msg[seq_num:seq_num + n]
                print(f"Sliding Window: {windowBuffer}")

        except socket.timeout:
            # Timeout occurred, resend unacknowledged frames
            print("\nTimeout occurred, resending unacknowledged frames...\n")
            for seq in unacked:
                print(f"\tResending Seq {seq}: {unacked[seq]}")
                s.send(bytes(f"{seq},{unacked[seq]}", "utf-8"))
                sleep(1)

        # Break when all messages are acknowledged
        if seq_num == len(msg) and len(unacked) == 0:
            print("\nMessage Sent Successfully!")
            break

except Exception as e:
    print(f"Error: {e}")

finally:
    s.close()
