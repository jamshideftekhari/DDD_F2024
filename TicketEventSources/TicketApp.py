from EventStore import EventStore
from TicketService import TicketService
from Ticket import TicketCreated, MessageAdded, AttachmentAdded, PrioritySet, ResponseTimeLimitSet

event_store = EventStore()
ticket_service = TicketService(event_store)

# Create a ticket
ticket_service.create_ticket(ticket_id=1, product_id=101, customer_id=201)

# Add messages and attachments to the ticket
ticket_service.add_message_to_ticket(ticket_id=1, message="Issue reported: Login not working")
ticket_service.add_attachment_to_ticket(ticket_id=1, attachment="screenshot.png")

# Set priority and response time limit for the ticket
ticket_service.set_priority_for_ticket(ticket_id=1, priority="High")
ticket_service.set_response_time_limit_for_ticket(ticket_id=1, response_time_limit=24)

# Get the history of events for the ticket
ticket_history = ticket_service.get_ticket_history(ticket_id=1)

# Print the events
for event in ticket_history:
    if isinstance(event, TicketCreated):
        print(f"Ticket #{event.ticket_id} created for product #{event.product_id} by customer #{event.customer_id}")
    elif isinstance(event, MessageAdded):
        print(f"Message added to Ticket #{event.ticket_id}: {event.message}")
    elif isinstance(event, AttachmentAdded):
        print(f"Attachment added to Ticket #{event.ticket_id}: {event.attachment}")
    elif isinstance(event, PrioritySet):
        print(f"Priority set for Ticket #{event.ticket_id}: {event.priority}")
    elif isinstance(event, ResponseTimeLimitSet):
        print(f"Response time limit set for Ticket #{event.ticket_id}: {event.response_time_limit} hours")
