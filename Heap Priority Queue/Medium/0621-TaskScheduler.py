"""
LeetCode Problem: Task Scheduler
Problem Number: 621
Difficulty: Medium
Topic: Heap Priority Queue
Link: https://leetcode.com/problems/task-scheduler/
"""

class Solution:
    # Frequency + Heap + Queue
    # Calculate the frequencies of each task and add them to max heap
    # Simulate the process, at each step:
    # Check if there are tasks pending in queue that can now be done
    # If there are available tasks, remove the task with highest frequency and do it
    # Increase the number of cycles
    # Time Complexity: O(n)
    # Space Complexity: O(n) -> O(26) -> O(1)
    def leastInterval(self, tasks, n):
        import heapq
        from collections import deque

        freqs = dict()
        for task in tasks:
            freqs[task] = freqs.get(task, 0) + 1
            
        heap = []
        for task, freq in freqs.items():
            heapq.heappush(heap, (-freq, task))
        queue = deque()        

        cycles = 0
        while heap or queue:
            if queue:
                free, (freq, task) = queue[0]
                if free <= cycles:
                    heapq.heappush(heap, queue.popleft()[1])
            if heap:
                freq, task = heapq.heappop(heap)
                if freq < -1:
                    queue.append((cycles + n + 1, (freq + 1, task)))
            cycles += 1

        return cycles

    # Greedy Approach
    # Assume distribution of all the chars with highest frequency sequentially in intervals of n
    # Calculate the empty slots between those elements and see if any idles are needed
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def leastInterval(self, tasks, n):
        freqs = dict()
        max_freq, max_freq_count = 0, 0
        for task in tasks:
            freqs[task] = freqs.get(task, 0) + 1
            if freqs[task] > max_freq:
                max_freq = freqs[task]
                max_freq_count = 1
            elif freqs[task] == max_freq:
                max_freq_count += 1
        
        # The number of empty slots between iterations is given by empty
        empty = (max_freq - 1) * (n - (max_freq_count - 1))

        # The number of slots needed for the remaining tasks
        slots = len(tasks) - max_freq * max_freq_count
        
        # The number of idles that will be used
        idles = min(0, empty - slots)

        return len(tasks) + idles

    # Mathematic Formula
    # Based on the greedy idea, we see that the bottlenecks are caused by tasks with the max frequency
    # There can be be one of two cases:
    # Either we can all tasks fit correctly without needing idle cycles
    # Or tasks with max freq cause idle cycles
    # For a given max freq, we need at least (max_freq - 1) * (n) + 1 cycles
    # For each task with a similar freq, we need one more cycle
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def leastInterval(self, tasks, n):
        freqs = dict()
        max_freq, max_freq_count = 0, 0
        for task in tasks:
            freqs[task] = freqs.get(task, 0) + 1
            if freqs[task] > max_freq:
                max_freq = freqs[task]
                max_freq_count = 1
            elif freqs[task] == max_freq:
                max_freq_count += 1
        
        return max(len(tasks), (max_freq - 1) * (n + 1) + max_freq_count)
