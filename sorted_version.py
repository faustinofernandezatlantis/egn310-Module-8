import csv

def add_ticket_sorted(queue, priority, number, description):
    if priority not in (1, 2, 3):
        raise ValueError(f"Priority must be 1, 2, or 3, got: {priority}")
    queue.append((priority, number, description))
    queue.sort()

def next_ticket_sorted(queue):
    if not queue:
        return None
    return queue.pop(0)

def pending_count_sorted(queue):
    return len(queue)

def main():
    queue = []
    
    with open('tickets.csv', mode='r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            add_ticket_sorted(queue, int(row['priority']), int(row['number']), row['description'])

    while pending_count_sorted(queue) > 0:
        p, num, desc = next_ticket_sorted(queue)
        print(f"{p} {num} {desc}")

if __name__ == '__main__':
    main()