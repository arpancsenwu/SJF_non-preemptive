# Function to calculate waiting time for all processes
def calculate_waiting_time(processes, n, bt, at, wt):
    # Initialize variables
    remaining_bt = bt[:]
    complete = 0
    current_time = 0
    minimum_bt = float('inf')
    shortest = 0
    check = False

    while complete != n:
        # Find the process with the shortest burst time among the processes that have arrived
        for j in range(n):
            if at[j] <= current_time and remaining_bt[j] < minimum_bt and remaining_bt[j] > 0:
                minimum_bt = remaining_bt[j]
                shortest = j
                check = True

        if not check:  # If no process is ready, increment the current time
            current_time += 1
            continue

        # Reduce the remaining burst time of the shortest process
        remaining_bt[shortest] = 0
        minimum_bt = float('inf')

        # Increment the completion count
        complete += 1
        finish_time = current_time + bt[shortest]

        # Calculate waiting time
        wt[shortest] = finish_time - bt[shortest] - at[shortest]

        # If waiting time for a process is negative, set it to 0
        if wt[shortest] < 0:
            wt[shortest] = 0

        # Update current time
        current_time = finish_time


# Function to calculate turn around time for all processes
def calculate_turn_around_time(processes, n, bt, wt, tat):
    # Calculating turn around time by adding burst time and waiting time
    for i in range(n):
        tat[i] = bt[i] + wt[i]


# Function to calculate and display the average times and details
def calculate_average_time(processes, n, bt, at):
    wt = [0] * n  # Waiting time
    tat = [0] * n  # Turn-around time

    # Function to find waiting time for all processes
    calculate_waiting_time(processes, n, bt, at, wt)

    # Function to find turn around time for all processes
    calculate_turn_around_time(processes, n, bt, wt, tat)

    # Store the data to display it later in the correct order
    results = []
    total_wt = 0
    total_tat = 0
    for i in range(n):
        results.append((processes[i], at[i], bt[i], wt[i], tat[i]))
        total_wt += wt[i]
        total_tat += tat[i]

    # Sort the results by process ID to display them in ascending order
    results.sort(key=lambda x: x[0])

    # Display processes along with their burst time, arrival time, waiting time, and turn around time
    print("\nProcesses    Arrival Time    Burst Time    Waiting Time    Turn-Around Time")
    for result in results:
        print(f"   {result[0]} \t\t {result[1]} \t\t {result[2]} \t\t {result[3]} \t\t {result[4]}")

    print(f"\nAverage waiting time = {total_wt / n:.2f}")
    print(f"Average turn-around time = {total_tat / n:.2f}")


# Function to perform SJF scheduling
def sjf_scheduling():
    n = int(input("Enter number of processes: "))

    processes = []
    burst_time = []
    arrival_time = []

    for i in range(n):
        processes.append(i + 1)  # Process IDs
        bt = int(input(f"Enter burst time for process {i + 1}: "))
        at = int(input(f"Enter arrival time for process {i + 1}: "))
        burst_time.append(bt)
        arrival_time.append(at)

    # Sorting by arrival time (processes with same arrival will be ordered later by burst time)
    sorted_processes = sorted(zip(arrival_time, burst_time, processes))

    # Unzipping the sorted list into respective lists
    arrival_time, burst_time, processes = zip(*sorted_processes)

    # Perform calculations for the sorted processes
    calculate_average_time(processes, n, list(burst_time), list(arrival_time))


# Driver code to test the function
if __name__ == "__main__":
    sjf_scheduling()
