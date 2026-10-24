import heapq
import csv

def add_ticket(queue, priority, number, description):
    if priority not in (1, 2, 3):
        raise ValueError(f"Priority must be 1, 2, or 3, got: {priority}")
    heapq.heappush(queue, (priority, number, description))

def next_ticket(queue):
    if not queue:
        return None
    return heapq.heappop(queue)

def pending_count(queue):
    return len(queue)

def main():
    queue = []
    
    # Load tickets from CSV
    with open('tickets.csv', mode='r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            add_ticket(queue, int(row['priority']), int(row['number']), row['description'])

    # Write output to output.txt and print to terminal
    with open('output.txt', mode='w', encoding='utf-8') as out_file:
        while pending_count(queue) > 0:
            p, num, desc = next_ticket(queue)
            line = f"{p} {num} {desc}"
            print(line)
            out_file.write(line + "\n")

if __name__ == '__main__':
    main()