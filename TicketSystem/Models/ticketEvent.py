class TicketCreatedEvent:
    def __init__(self, ticket_id, title, description, priority, response_time_limit, status, product_id, customer_id):
        self.ticket_id = ticket_id
        self.title = title
        self.description = description
        self.priority = priority
        self.response_time_limit = response_time_limit
        self.status = status
        self.product_id = product_id
        self.customer_id = customer_id

class TicketStatusUpdatedEvent:
    def __init__(self, ticket_id, new_status):
        self.ticket_id = ticket_id
        self.new_status = new_status

class TicketEventHandler:
    def handle_ticket_created(self, event):
        print(f"Ticket created: {event.title} (ID: {event.ticket_id})")

    def handle_ticket_status_updated(self, event):
        print(f"Ticket status updated: Ticket ID {event.ticket_id} - New Status: {event.new_status}")

class TicketService:
    def __init__(self):
        self.event_handler = TicketEventHandler()

    def create_ticket(self, title, description, priority, response_time_limit, status, product_id, customer_id):
        # Create ticket logic
        ticket_id = self.generate_ticket_id()  # Assume you have a method to generate unique ticket IDs
        # Emit domain event
        event = TicketCreatedEvent(ticket_id, title, description, priority, response_time_limit, status, product_id, customer_id)
        self.event_handler.handle_ticket_created(event)
        return ticket_id

    def update_ticket_status(self, ticket_id, new_status):
        # Update ticket status logic
        # Emit domain event
        event = TicketStatusUpdatedEvent(ticket_id, new_status)
        self.event_handler.handle_ticket_status_updated(event)

    def generate_ticket_id(self):
        # Logic to generate unique ticket ID
        pass

# Example usage:
ticket_service = TicketService()

# Create a new ticket
ticket_id = ticket_service.create_ticket("Bug Fix", "Fix login issue", "High", 24, "Open", 1, 1)

# Update ticket status
ticket_service.update_ticket_status(ticket_id, "In Progress")
