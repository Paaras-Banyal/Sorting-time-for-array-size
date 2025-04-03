import time
import random
import tkinter as tk
from tkinter import messagebox

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        
        merge_sort(left_half)
        merge_sort(right_half)
        
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def measure_time(sorting_function, arr):
    start_time = time.time()
    sorting_function(arr)
    end_time = time.time()
    return end_time - start_time

def run_sorting():
    try:
        size = int(entry.get())
        if size <= 0:
            raise ValueError("Size must be greater than 0")
        arr = [random.randint(1, 10000) for _ in range(size)]
        
        arr_bubble = arr.copy()
        arr_merge = arr.copy()
        arr_quick = arr.copy()
        
        time_bubble = measure_time(bubble_sort, arr_bubble)
        time_merge = measure_time(merge_sort, arr_merge)
        time_quick = measure_time(lambda x: quick_sort(x), arr_quick)
        
        result_label.config(text=f"Bubble Sort: {time_bubble:.6f} sec\n"
                               f"Merge Sort: {time_merge:.6f} sec\n"
                               f"Quick Sort: {time_quick:.6f} sec")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid positive integer.")

# Tkinter GUI setup
root = tk.Tk()
root.title("Sorting Algorithm Comparison")
root.geometry("400x300")

tk.Label(root, text="Enter array size:").pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)

tk.Button(root, text="Run Sorting", command=run_sorting).pack(pady=10)
result_label = tk.Label(root, text="", justify=tk.LEFT)
result_label.pack(pady=10)

root.mainloop()