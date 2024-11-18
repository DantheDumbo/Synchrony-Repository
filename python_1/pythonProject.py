# Function to display the menu of options
def display_menu():
    print("Skiing Performance Tracker")
    print("1. Add Skiing Time for a Run")
    print("2. View All Skiing Times")
    print("3. Calculate Average Skiing Time")
    print("4. Exit")
    user_choice = input("Enter the number of your choice: ")
    return user_choice

# Function to add skiing time for a run
def add_skiing_time(runs_times_list):
    skier_name = input("Enter the skier's name: ")
    skiing_time = float(input(f"Enter the skiing time for {skier_name}'s run (in minutes): "))
    # Adding skier's name and time to the list as a tuple
    runs_times_list.append((skier_name, skiing_time))
    print(f"{skier_name}'s skiing time has been added!")

# Function to view all skiing times for different runs
def view_all_skiing_times(runs_times_list):
    if len(runs_times_list) == 0:
        print("No skiing times available. Please add some times first.")
    else:
        print("\nList of All Skiing Runs and Times:")
        for skier, skiing_time in runs_times_list:
            print(f"{skier}: {skiing_time} minutes")

# Function to calculate the average skiing time of all runs
def calculate_average_skiing_time(runs_times_list):
    if len(runs_times_list) == 0:
        print("No skiing times available to calculate average.")
    else:
        total_time = 0
        for skier, skiing_time in runs_times_list:
            total_time += skiing_time
        average_time = total_time / len(runs_times_list)
        print(f"The average skiing time of all runs is: {average_time:.2f} minutes")

# Main function to run the Skiing Performance Tracker
def run_skiing_tracker():
    # List to store skier names and their skiing times
    skier_runs = []

    while True:
        # Display the menu and get user choice
        user_choice = display_menu()
        
        if user_choice == '1':
            # Add skiing time for a run
            add_skiing_time(skier_runs)
        elif user_choice == '2':
            # View all skiing times
            view_all_skiing_times(skier_runs)
        elif user_choice == '3':
            # Calculate and display average skiing time
            calculate_average_skiing_time(skier_runs)
        elif user_choice == '4':
            # Exit the program
            print("Exiting the system. Have a great day!")
            break
        else:
            print("Invalid choice, please try again.")

# Run the Skiing Performance Tracker
run_skiing_tracker()