class DiskScheduler:
    def __init__(self, requests, start_position):
        self.requests = sorted(requests)  # Sort requests for LOOK
        self.start_position = start_position
        self.head_movement = 0

    def fcfs(self):
        current_position = self.start_position
        total_head_movement = 0

        print("FCFS Scheduling:")
        for request in self.requests:
            total_head_movement += abs(request - current_position)
            print(f"Moving from {current_position} to {request}")
            current_position = request

        print(f"Total head movement: {total_head_movement}")

    def look(self):
        current_position = self.start_position
        total_head_movement = 0
        left_requests = []
        right_requests = []

        # Divide requests into two categories
        for request in self.requests:
            if request < current_position:
                left_requests.append(request)
            else:
                right_requests.append(request)

        # Process right requests
        for request in right_requests:
            total_head_movement += abs(request - current_position)
            print(f"Moving from {current_position} to {request}")
            current_position = request

        # Process left requests
        if left_requests:
            total_head_movement += abs(current_position - left_requests[-1])
            current_position = left_requests[-1]
            print(f"Moving from {current_position + (1 if right_requests else 0)} to {current_position}")

            for request in reversed(left_requests):
                total_head_movement += abs(request - current_position)
                print(f"Moving from {current_position} to {request}")
                current_position = request

        print(f"Total head movement: {total_head_movement}")

# Example Usage
if __name__ == "__main__":
    requests = [98, 183, 37, 122, 14, 124, 65, 67]
    start_position = 53

    disk_scheduler = DiskScheduler(requests, start_position)
    disk_scheduler.fcfs()
    print("\n")
    disk_scheduler.look()
