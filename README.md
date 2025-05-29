# Bubble Sort Analysis 

## Project Overview
I chose to study the bubble sort algorithm in an unconventional way—by asking my computer science roommate for a recommendation, and he suggested bubble sort! This project implements and analyzes bubble sort, including performance metrics and visualizations.

## Implementation Details
I built a simple bubble sort implementation in Python, testing it with various input sizes and enabling user input to adjust the list size. The program tracks:
- Execution time
- Number of comparisons
- Number of swaps

To enhance the project, I created visualizations using Claude and Matplotlib to display a graph of the algorithm's progress. The graph updates automatically with each swap, refreshing and plotting the state before and after. To make the visualization viewable, I used `time.sleep` to slow down the rendering. Additionally, I developed:
- A manually controlled version for step-by-step viewing
- A text-based version that does not rely on Matplotlib

## Bubble Sort Overview
Bubble sort is a straightforward sorting algorithm that repeatedly iterates through a list, compares adjacent elements, and swaps them if they are in the wrong order. The process continues until no swaps are needed, indicating the list is sorted. The algorithm gets its name because smaller elements "bubble" to the top (beginning) of the list with each iteration.

### Time Complexity
- **Worst Case**: O(n²)  
  The outer loop runs n-1 times, and the inner loop performs one fewer comparison each pass. The total number of comparisons is calculated as:  
  \[(n-1) + (n-2) + (n-3) + \dots + 2 + 1 = \sum_{i=1}^{n-1} i = \frac{(n-1)n}{2}\]  
  This simplifies to \((n^2 - n)/2\), confirming the worst-case time complexity of O(n²).
- **Best Case**: O(n)  
  When the list is already sorted and a swap-check is implemented, the algorithm can terminate early, resulting in a linear time complexity.

### Characteristics
While bubble sort is simple to understand and implement, its O(n²) time complexity makes it inefficient for large datasets compared to advanced algorithms like quicksort or mergesort. However, its simplicity makes it valuable for educational purposes and small datasets.

## Conclusion
Bubble sort is an excellent learning tool due to its straightforward logic, but its inefficiency for large lists—except in the best-case scenario—limits its practical use compared to more efficient sorting algorithms.
