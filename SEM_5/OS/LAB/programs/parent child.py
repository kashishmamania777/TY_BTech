import os

def child_process():
    # Display child process information
    print(f"Child Process ID: {os.getpid()}")
    print(f"Parent Process ID (from Child): {os.getppid()}")
    
    # Open and read a file using file system calls
    try:
        with open("example.txt", "r") as file:
            content = file.read()
            print("\nFile content read by child process:\n")
            print(content)
    except FileNotFoundError:
        print("File 'example.txt' not found. Please ensure the file exists.")

def parent_process():
    # Display parent process information
    print(f"Parent Process ID: {os.getpid()}")
    
# Main function
def main():
    # Fork to create a new process
    pid = os.fork()
    
    if pid > 0:
        # Parent process
        parent_process()
    elif pid == 0:
        # Child process
        child_process()
    else:
        print("Fork failed.")

if __name__ == "__main__":
    main()
