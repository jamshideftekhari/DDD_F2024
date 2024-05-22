from Ticket import TicketCreated, MessageAdded, AttachmentAdded, PrioritySet, ResponseTimeLimitSet
class TicketService:
    def __init__(self, event_store):
        self.event_store = event_store

    def create_ticket(self, ticket_id, product_id, customer_id):
        event = TicketCreated(ticket_id, product_id, customer_id)
        self.event_store.append(event)

    def add_message_to_ticket(self, ticket_id, message):
        event = MessageAdded(ticket_id, message)
        self.event_store.append(event)

    def add_attachment_to_ticket(self, ticket_id, attachment):
        event = AttachmentAdded(ticket_id, attachment)
        self.event_store.append(event)

    def set_priority_for_ticket(self, ticket_id, priority):
        event = PrioritySet(ticket_id, priority)
        self.event_store.append(event)

    def set_response_time_limit_for_ticket(self, ticket_id, response_time_limit):
        event = ResponseTimeLimitSet(ticket_id, response_time_limit)
        self.event_store.append(event)

    def get_ticket_history(self, ticket_id):
        return self.event_store.get_events_for_ticket(ticket_id)
