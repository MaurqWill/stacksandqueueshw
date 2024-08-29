class OrderNode:
    def __init__(self, order_id, details):
        self.order_id = order_id
        self.details = details
        self.next = None

class KitchenOrderStack:
    def __init__(self):
        self.top = None

    def push(self, order_id, details):
        new_order = OrderNode(order_id, details)
        new_order.next = self.top
        self.top = new_order

    def pop(self):
        if not self.top:
            return "No orders to process"
        removed_order = self.top
        self.top = self.top.next
        return removed_order

    def check_top_order(self):
        if not self.top:
            return "No orders in the kitchen queue"
        return self.top

    def display(self):
        current = self.top
        while current:
            print(f"Order ID: {current.order_id}, Details: {current.details}")
            current = current.next

class CustomerOrderNode:
    def __init__(self, order_id, details, priority):
        self.order_id = order_id
        self.details = details
        self.priority = priority
        self.next = None

class CustomerOrderQueue:
    def __init__(self):
        self.front = None

    def enqueue(self, order_id, details, priority):
        new_order = CustomerOrderNode(order_id, details, priority)

        # Insert in priority order (lower number = higher priority)
        if self.front is None or self.front.priority > priority:
            new_order.next = self.front
            self.front = new_order
        else:
            current = self.front
            while current.next is not None and current.next.priority <= priority:
                current = current.next
            new_order.next = current.next
            current.next = new_order

    def dequeue(self):
        if self.front is None:
            return "No orders to process"
        removed_order = self.front
        self.front = self.front.next
        return removed_order

    def peek(self):
        if not self.front:
            return "No orders in the customer queue"
        return self.front

    def display(self):
        current = self.front
        while current:
            print(f"Order ID: {current.order_id}, Details: {current.details}, Priority: {current.priority}")
            current = current.next


# Kitchen stack operations
kitchen_stack = KitchenOrderStack()
kitchen_stack.push(1, "Burger and Fries")
kitchen_stack.push(2, "Pasta")
kitchen_stack.push(3, "Salad")

print("Kitchen Orders:")
kitchen_stack.display()

# Removing completed orders
completed_order = kitchen_stack.pop()
print(f"Completed Order: {completed_order.order_id} - {completed_order.details}")

print("Orders to Complete:")
kitchen_stack.display()

# Customer queue operations
customer_queue = CustomerOrderQueue()
customer_queue.enqueue(1, "Burger and Fries", 1)
customer_queue.enqueue(2, "Pasta", 2)
customer_queue.enqueue(3, "Salad", 3)

print("Customer Orders:")
customer_queue.display()

# Processing orders
processed_order = customer_queue.dequeue()
print(f"Processed Order: {processed_order.order_id} - {processed_order.details}")

print("Customer Orders After Processing:")
customer_queue.display()
