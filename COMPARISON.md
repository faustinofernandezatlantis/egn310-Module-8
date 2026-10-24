In this assignment, both implementations manage ticket priorities correctly, but they handle new ticket arrivals differently.

When a new ticket arrives in ticket_queue.py, the heapq.heappush function adds the tuple to the underlying list and performs a sift-up (or percolate-up) operation. This only compares and swaps elements along a single path in the binary heap from the leaf to the root. It places the new ticket in its correct position without touching or reordering the rest of the queue.

In contrast, sorted_version.py appends the new ticket to the list and then calls Python's .sort() method. This triggers Timsort over the entire list, re-evaluating and re-sorting every single element from scratch, even those that were already in order.

Therefore, the sorted list version does noticeably more work on every arrival because it performs a full list re-sort instead of a targeted heap tree adjustment.