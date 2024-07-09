import heapq

def find_k_largest(arr, k):
    heap = arr[:k]
    heapq.heapify(heap)
    
    for num in arr[k:]:
        if num > heap[0]:
            heapq.heapreplace(heap, num)

    
    return heap

arr = [5, 2, 1, 3, 7, 15, 25, 45, 18, 9, 12, 50, 3, 102, 30, 55, 88, 228]
k = 3
result = find_k_largest(arr, k)
print(f"The {k} largest elements in the array are: {result}")
