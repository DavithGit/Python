"""
Objective:
Create a Python script to track heart rate readings and calculate the average heart rate.
Requirements:
Define time_slots as a list with times of day (e.g., "Morning", "Midday", "Afternoon", "Evening").
Use a loop to prompt the user for heart rate (in BPM) at each time slot.
Create a multi-level list heart_rates to store the time slots and their corresponding heart rates.
Calculate the average heart rate and display it.
Sample Output:
Enter your heart rate (in BPM) in the Morning: 70
Enter your heart rate (in BPM) at Midday: 75
Enter your heart rate (in BPM) in the Afternoon: 72
Enter your heart rate (in BPM) in the Evening: 68
Average heart rate today: 71.25 BPM
"""
time_slots=["Morning", "Midday", "Afternoon", "Evening"]
heart_rate=[]
total=0
heart_rate_with_times = []

for time in time_slots:
    heart_rate = int(input(f"Please enter the {time} heart rate level: "))
    while heart_rate > 200 or heart_rate < 60:
        correct_number = input(
            f"The bpm {heart_rate} is outside of normal ranges. Are you sure? (Y or N)")
        if correct_number == "Y" or correct_number == "y":
            break
        else:
            heart_rate = int(input(f"Please enter the {time} heart rate level: "))
    heart_rate_with_times.append([time, heart_rate])

# print results to screen
    for item in range(len(heart_rate_with_times)):
        print(f"For {heart_rate_with_times[item][0]} the heart rate was {heart_rate_with_times[item][1]}")
    total += heart_rate_with_times[item][1]

    average = total / len(heart_rate_with_times)
    print(f"Your average heart rate today was: {average:.1f}")