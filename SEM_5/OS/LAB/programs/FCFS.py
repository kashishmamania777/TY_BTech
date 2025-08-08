import matplotlib.pyplot as plt

# Function to calculate the waiting time for each process
def calculate_waiting_time(processes, n, burst_time, waiting_time, arrival_time):
    # Initialize service time
    service_time = [0] * n
    service_time[0] = arrival_time[0]
    waiting_time[0] = 0  # Waiting time for the first process is 0

    # Calculating waiting time for each process
    for i in range(1, n):
        # Add burst time of previous processes to the service time
        service_time[i] = service_time[i - 1] + burst_time[i - 1]
        
        # Find waiting time as difference between service time and arrival time
        waiting_time[i] = service_time[i] - arrival_time[i]

        # If waiting time for a process is negative, set it to 0
        if waiting_time[i] < 0:
            waiting_time[i] = 0

# Function to calculate the turnaround time for each process
def calculate_turnaround_time(processes, n, burst_time, waiting_time, turnaround_time):
    # Calculating turnaround time by adding burst_time and waiting_time
    for i in range(n):
        turnaround_time[i] = burst_time[i] + waiting_time[i]

# Function to calculate the response time for each process
def calculate_response_time(waiting_time, response_time):
    for i in range(len(waiting_time)):
        response_time[i] = waiting_time[i]

# Function to calculate average waiting, turnaround, and response time
def calculate_average_time(processes, n, burst_time, arrival_time):
    waiting_time = [0] * n
    turnaround_time = [0] * n
    response_time = [0] * n
    total_waiting_time = 0
    total_turnaround_time = 0
    total_response_time = 0

    # Function to find waiting time of all processes
    calculate_waiting_time(processes, n, burst_time, waiting_time, arrival_time)

    # Function to find turnaround time for all processes
    calculate_turnaround_time(processes, n, burst_time, waiting_time, turnaround_time)

    # Function to find response time for all processes
    calculate_response_time(waiting_time, response_time)

    # Display processes with their burst time, waiting time, turnaround time, and response time
    print("\nProcess\tBurst Time\tArrival Time\tWaiting Time\tTurnaround Time\tResponse Time")

    # Calculating total waiting time, turnaround time, and response time
    for i in range(n):
        total_waiting_time += waiting_time[i]
        total_turnaround_time += turnaround_time[i]
        total_response_time += response_time[i]
        print(f"P{i+1}\t\t{burst_time[i]}\t\t{arrival_time[i]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}\t\t{response_time[i]}")

    print(f"\nAverage waiting time: {total_waiting_time / n:.2f}")
    print(f"Average turnaround time: {total_turnaround_time / n:.2f}")
    print(f"Average response time: {total_response_time / n:.2f}")

    return waiting_time, turnaround_time, response_time

# Function to draw Gantt chart
def draw_gantt_chart(processes, n, burst_time, waiting_time):
    start_time = waiting_time
    end_time = [start_time[i] + burst_time[i] for i in range(n)]

    plt.figure(figsize=(10, 5))

    for i in range(n):
        plt.barh(y='Process ' + str(processes[i]), width=burst_time[i], left=start_time[i], color='blue', edgecolor='black')
        plt.text(start_time[i] + burst_time[i]/2, processes[i], f'P{processes[i]}', ha='center', va='center', color='white')

    plt.xlabel('Time')
    plt.ylabel('Processes')
    plt.title('Gantt Chart for FCFS Scheduling')
    plt.show()

# Main function to execute FCFS algorithm
def fcfs_scheduling():
    # Taking number of processes as input from user
    n = int(input("Enter the number of processes: "))

    processes = list(range(1, n + 1))
    burst_time = []
    arrival_time = []

    # Taking arrival time and burst time of all processes as input from user
    for i in range(n):
        at = int(input(f"Enter arrival time for process P{i+1}: "))
        arrival_time.append(at)
    for i in range(n):
        bt = int(input(f"Enter burst time for process P{i+1}: "))
        burst_time.append(bt)

    # Calculate and display average waiting, turnaround, and response time
    waiting_time, turnaround_time, response_time = calculate_average_time(processes, n, burst_time, arrival_time)

    # Draw Gantt chart
    draw_gantt_chart(processes, n, burst_time, waiting_time)

# Running the FCFS scheduling algorithm
fcfs_scheduling()
