import matplotlib.pyplot as plt
import time
import numpy as np


def visualize_bubble_sort(arr, sort_type="ascending", delay=1.0):
    """
    Visualize bubble sort algorithm step by step using static plots with delay

    Parameters:
    arr (list): The array to be sorted
    sort_type (str): "ascending" or "descending"
    delay (float): Delay in seconds between steps (default: 1.0)
    """
    arr = arr.copy()  # Create a copy to avoid modifying the original array
    n = len(arr)

    # Setup figure
    plt.figure(figsize=(10, 6))

    # Display initial array
    plt.subplot(1, 1, 1)
    plt.bar(range(len(arr)), arr, color='#3498db')
    plt.title("Initial Array")
    for i, v in enumerate(arr):
        plt.text(i, v + 0.1, str(v), ha='center')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.ylim(0, max(arr) * 1.15)
    plt.tight_layout()
    plt.show()
    print("Initial array:", arr)

    # Add delay after initial display
    time.sleep(delay)

    # Step counter
    step = 1

    # Run the algorithm and show visualizations
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            # Create colors for comparison visualization
            colors = ['#3498db'] * n
            colors[j] = '#e74c3c'  # Red for compared elements
            colors[j + 1] = '#e74c3c'

            # Display comparison
            plt.figure(figsize=(10, 6))
            plt.bar(range(len(arr)), arr, color=colors)
            plt.title(f"Step {step}: Comparing {arr[j]} and {arr[j + 1]}")
            for i, v in enumerate(arr):
                plt.text(i, v + 0.1, str(v), ha='center')
            plt.xlabel('Index')
            plt.ylabel('Value')
            plt.ylim(0, max(arr) * 1.15)
            plt.tight_layout()
            plt.show()
            print(f"Step {step}: Comparing {arr[j]} and {arr[j + 1]}")
            step += 1

            # Add delay after comparison
            time.sleep(delay)

            # Check if swap is needed
            condition = arr[j] > arr[j + 1] if sort_type == "ascending" else arr[j] < arr[j + 1]
            if condition:
                # Swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

                # Display after swap
                plt.figure(figsize=(10, 6))
                plt.bar(range(len(arr)), arr, color=colors)
                plt.title(f"Step {step}: Swapped {arr[j]} and {arr[j + 1]}")
                for i, v in enumerate(arr):
                    plt.text(i, v + 0.1, str(v), ha='center')
                plt.xlabel('Index')
                plt.ylabel('Value')
                plt.ylim(0, max(arr) * 1.15)
                plt.tight_layout()
                plt.show()
                print(f"Step {step}: Swapped {arr[j]} and {arr[j + 1]}")
                step += 1

                # Add delay after swap
                time.sleep(delay)

        if not swapped:
            break

    # Show final sorted array
    plt.figure(figsize=(10, 6))
    plt.bar(range(len(arr)), arr, color='#2ecc71')  # Green for sorted array
    plt.title("Sorting Complete!")
    for i, v in enumerate(arr):
        plt.text(i, v + 0.1, str(v), ha='center')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.ylim(0, max(arr) * 1.15)
    plt.tight_layout()
    plt.show()
    print("Sorting complete:", arr)


def manual_visualization(arr, sort_type="ascending"):
    """
    Step-by-step visualization with manual control
    """
    arr = arr.copy()
    n = len(arr)

    # List to store all frames
    all_states = []
    compare_indices = []
    descriptions = []

    # Initial state
    all_states.append(arr.copy())
    compare_indices.append((-1, -1))
    descriptions.append("Initial Array")

    # Run the algorithm and record states
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            # Comparison step
            compare_indices.append((j, j + 1))
            all_states.append(arr.copy())
            descriptions.append(f"Comparing {arr[j]} and {arr[j + 1]}")

            condition = arr[j] > arr[j + 1] if sort_type == "ascending" else arr[j] < arr[j + 1]
            if condition:
                # Swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

                # Record state after swap
                compare_indices.append((j, j + 1))
                all_states.append(arr.copy())
                descriptions.append(f"Swapped {arr[j]} and {arr[j + 1]}")

        if not swapped:
            break

    # Final state with no comparison
    compare_indices.append((-1, -1))
    all_states.append(arr.copy())
    descriptions.append("Sorting Complete!")

    # Display state by state
    step = 0
    while step < len(all_states):
        plt.figure(figsize=(12, 6))

        current_state = all_states[step]
        comp_indices = compare_indices[step]

        # Create bar colors
        colors = ['#3498db' for _ in range(len(current_state))]  # Default blue

        if comp_indices[0] != -1:  # If there's a comparison
            colors[comp_indices[0]] = '#e74c3c'  # Red for compared elements
            colors[comp_indices[1]] = '#e74c3c'
        elif step > 0:  # Final state
            colors = ['#2ecc71' for _ in range(len(current_state))]  # All green when complete

        # Create bars
        plt.bar(range(len(current_state)), current_state, color=colors)

        # Add values on top of bars
        for i, v in enumerate(current_state):
            plt.text(i, v + 0.1, str(v), ha='center')

        plt.title(f"Step {step}: {descriptions[step]}", fontsize=14)
        plt.xlabel('Index', fontsize=12)
        plt.ylabel('Value', fontsize=12)
        plt.ylim(0, max(max(arr) * 1.15, 1))  # Add space for text

        plt.tight_layout()
        plt.show()

        # Get user input for next action
        print(f"\nStep {step} of {len(all_states) - 1}: {descriptions[step]}")

        if step < len(all_states) - 1:
            action = input("\nPress Enter for next step, 'b' for previous step, 'q' to quit: ")
            if action.lower() == 'q':
                break
            elif action.lower() == 'b' and step > 0:
                step -= 1
            else:
                step += 1
        else:
            print("End of visualization. Press Enter to exit.")
            input()
            break


# Text-based visualization for environments where matplotlib doesn't work
def text_visualize_bubble_sort(arr, sort_type="ascending"):
    """A text-based visualization of bubble sort for environments where matplotlib doesn't work"""
    arr = arr.copy()  # Create a copy to avoid modifying the original array
    n = len(arr)

    print("\n" + "=" * 50)
    print(f"BUBBLE SORT VISUALIZATION ({sort_type.upper()})")
    print("=" * 50)

    # Display initial array
    print("\nINITIAL ARRAY:")
    visualize_array_text(arr)

    # Step counter
    step = 1

    # Run the algorithm and show visualizations
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            # Display comparison
            print(f"\nSTEP {step}: Comparing elements at index {j} and {j + 1}")
            comparison_arr = arr.copy()
            visualize_array_text(comparison_arr, [j, j + 1])
            step += 1

            # Check if swap is needed
            condition = arr[j] > arr[j + 1] if sort_type == "ascending" else arr[j] < arr[j + 1]
            if condition:
                # Swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

                # Display after swap
                print(f"\nSTEP {step}: Swapped {arr[j]} and {arr[j + 1]}")
                swap_arr = arr.copy()
                visualize_array_text(swap_arr, [j, j + 1])
                step += 1
            else:
                print(f"No swap needed ({arr[j]} {'≤' if sort_type == 'ascending' else '≥'} {arr[j + 1]})")

        if not swapped:
            print("\nEarly termination: No swaps in this pass, array is sorted!")
            break

    # Show final sorted array
    print("\nSORTING COMPLETE!")
    visualize_array_text(arr, highlight_all=True)
    print("=" * 50)


def visualize_array_text(arr, highlight_indices=None, highlight_all=False):
    """Display array as text with highlighting"""
    # Value representation
    values = []
    for i, val in enumerate(arr):
        if highlight_all:
            values.append(f"\033[92m{val:3d}\033[0m")  # Green for all elements
        elif highlight_indices and i in highlight_indices:
            values.append(f"\033[91m{val:3d}\033[0m")  # Red for highlighted elements
        else:
            values.append(f"{val:3d}")

    # Print values
    print("Values: [" + ", ".join(values) + "]")

    # Print indices
    indices = [f"{i:3d}" for i in range(len(arr))]
    print("Indices: [" + ", ".join(indices) + "]")

    # Visual bar representation
    max_val = max(arr)
    for i, val in enumerate(arr):
        bar_length = int((val / max_val) * 20)
        if highlight_all:
            bar = "\033[92m" + "█" * bar_length + "\033[0m"  # Green bars
        elif highlight_indices and i in highlight_indices:
            bar = "\033[91m" + "█" * bar_length + "\033[0m"  # Red bars
        else:
            bar = "█" * bar_length
        print(f"{i:2d} | {bar} {val}")

def generate_random_ints(sort_type="ascending"):
    size = input("Enter the amount of random integers to be sorted:")
    arr = np.random.randint(1,100, size=int(size))

    size = len(arr)

    # Track number of comparisons and swaps for demonstration
    comparisons = 0
    swaps = 0

    start_time = time.time()
    # Traverse through all array elements
    for i in range(size - 1):
        # Flag to optimize if no swaps occur in a pass
        swapped = False

        # Last i elements are already in place
        for j in range(size - i - 1):
            comparisons += 1

            # Compare adjacent elements
            condition = arr[j] > arr[j + 1] if sort_type == "ascending" else arr[j] < arr[j + 1]

            # Swap if condition is met
            if condition:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                swaps += 1

        # If no swaps occurred in this pass, array is sorted
        if not swapped:
            break

    execution_time = time.time() - start_time

    print(f"Total comparisons: {comparisons}")
    print(f"Total swaps: {swaps}")
    print(f"Total execution time: {execution_time}")


# Example usage:
if __name__ == "__main__":
    # Sample array
    sample_array = [12, 15, 28, 32, 10, 10, 10]

    print("Bubble Sort Visualization")
    print("------------------------")
    print("1. Ascending Order")
    print("2. Descending Order")
    choice = input("Select sorting type (1/2): ")

    sort_type = "ascending" if choice == "1" else "descending"

    print("\nVisualization type:")
    print("1. Simple matplotlib visualization (static plots)")
    print("2. Interactive manual visualization")
    print("3. Text-based visualization (for environments where matplotlib doesn't work)")
    print("4. Array size testing")
    vis_choice = input("Select visualization type (1/2/3): ")

    # Add delay input for option 1
    delay = 1.0  # Default value
    if vis_choice == "1":
        delay_input = input("Enter delay between steps in seconds (default: 1.0): ")
        if delay_input.strip():
            try:
                delay = float(delay_input)
            except ValueError:
                print("Invalid input. Using default delay of 1.0 seconds.")

    try:
        if vis_choice == "1":
            visualize_bubble_sort(sample_array, sort_type, delay)
        elif vis_choice == "2":
            manual_visualization(sample_array, sort_type)
        elif vis_choice == "3":
            text_visualize_bubble_sort(sample_array, sort_type)
        elif vis_choice == "4":
            generate_random_ints(sort_type)

    except Exception as e:
        print(f"Visualization failed with error: {e}")
        print("Falling back to text-based visualization...")
        text_visualize_bubble_sort(sample_array, sort_type)