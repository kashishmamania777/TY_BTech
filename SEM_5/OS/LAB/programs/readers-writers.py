import threading
import time
import random

read_count = 0
shared_data = 0
read_count_mutex = threading.Lock()
resource_access = threading.Semaphore(1)
reader_priority = threading.Lock()

def reader(reader_id, iterations=5):
    global read_count

    for _ in range(iterations):
        time.sleep(random.randint(1, 3))
        with reader_priority:
            with read_count_mutex:
                read_count += 1
                if read_count == 1:
                    resource_access.acquire()
        print(f"Reader {reader_id} is reading the resource. Readers count: {read_count}")
        time.sleep(random.randint(1, 2))
        with read_count_mutex:
            read_count -= 1
            print(f"Reader {reader_id} has finished reading. Readers count: {read_count}")
            if read_count == 0:
                resource_access.release()
def writer(writer_id, iterations=5):
    global shared_data

    for _ in range(iterations):
        time.sleep(random.randint(1, 3))
        resource_access.acquire()
        shared_data += 1
        print(f"Writer {writer_id} is writing to the resource. Updated data: {shared_data}")
        time.sleep(random.randint(1, 2))

        print(f"Writer {writer_id} has finished writing.")
        resource_access.release()
def simulate_readers_writers(num_readers, num_writers, iterations=5):
    reader_threads = []
    writer_threads = []
    for i in range(num_readers):
        t = threading.Thread(target=reader, args=(i, iterations))
        reader_threads.append(t)
        t.start()
    for i in range(num_writers):
        t = threading.Thread(target=writer, args=(i, iterations))
        writer_threads.append(t)
        t.start()

    for t in reader_threads + writer_threads:
        t.join()


if __name__ == "__main__":

    num_readers = 3
    num_writers = 2
    iterations = 5
    simulate_readers_writers(num_readers, num_writers, iterations)