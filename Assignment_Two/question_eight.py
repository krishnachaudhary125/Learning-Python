# 8. AI Experiment Tracker with Variable Scope
# Create a program that tracks the number of AI experiments performed.
# Requirements:
# ● Declare a global variable experiment_count.
# ● Create functions:
# ○ run_experiment()
# ○ show_count()
# ● Each call to run_experiment() should increase the global count.
# ● Demonstrate the difference between local and global scope.

experiment_count = 0

def run_experiment():
    global experiment_count  
    experiment_count += 1

    experiment_name = "AI Model Training"

    print(f"Running Experiment #{experiment_count}")
    print("Local Variable:", experiment_name)

def show_count():
    print("Total Experiments Performed:", experiment_count)

run_experiment()
run_experiment()
run_experiment()

show_count()

print("\nGlobal Variable:", experiment_count)