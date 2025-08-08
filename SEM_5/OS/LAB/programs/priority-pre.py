def priority_scheduling():
    n = int(input("Enter number of processes: "))
    processes = []
    for i in range(n):
        arrival_time = int(input(f"Enter Arrival Time for Process P{i+1}: "))
        burst_time = int(input(f"Enter Burst Time for Process P{i+1}: "))
        priority = int(input(f"Enter Priority for Process P{i+1} (lower number indicates higher priority): "))
        processes.append([f'P{i+1}', arrival_time, burst_time, priority])

    processes.sort(key=lambda x: x[1])

    completed = 0
    current_time = 0
    waiting_time = [0] * n
    turnaround_time = [0] * n
    response_time = [-1] * n
    remaining_time = [process[2] for process in processes]
    gantt_chart = []

    while completed != n:
        highest_priority = None
        for i in range(n):
            if processes[i][1] <= current_time and remaining_time[i] > 0:
                if highest_priority is None or processes[i][3] < processes[highest_priority][3]:
                    highest_priority = i

        if highest_priority is None:
            current_time += 1
            continue

        if response_time[highest_priority] == -1:
            response_time[highest_priority] = current_time - processes[highest_priority][1]

        gantt_chart.append(processes[highest_priority][0])
        remaining_time[highest_priority] -= 1
        current_time += 1

        if remaining_time[highest_priority] == 0:
            completed += 1
            finish_time = current_time
            turnaround_time[highest_priority] = finish_time - processes[highest_priority][1]
            waiting_time[highest_priority] = turnaround_time[highest_priority] - processes[highest_priority][2]

    avg_waiting_time = sum(waiting_time) / n
    avg_turnaround_time = sum(turnaround_time) / n
    avg_response_time = sum(response_time) / n

    print("\nProcess\tArrival Time\tBurst Time\tPriority\tWaiting Time\tTurnaround Time\tResponse Time")
    for i in range(n):
        print(f"{processes[i][0]}\t\t{processes[i][1]}\t\t{processes[i][2]}\t\t{processes[i][3]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}\t\t{response_time[i]}")
    
    print(f"\nAverage Waiting Time: {avg_waiting_time:.2f}")
    print(f"Average Turnaround Time: {avg_turnaround_time:.2f}")
    print(f"Average Response Time: {avg_response_time:.2f}")
    print("\nGantt Chart:")
    print(" -> ".join(gantt_chart))

priority_scheduling()
