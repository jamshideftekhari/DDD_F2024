from datetime import datetime

class Ticket:
    def __init__(self, ticket_id, product_id, customer_id):
        self.ticket_id = ticket_id
        self.product_id = product_id
        self.customer_id = customer_id
        self.status = "Open"
        self.messages = []
        self.attachments = []
        self.priority = None
        self.response_time_limit = None
        self.creation_time = datetime.now()

    def add_message(self, message):
        self.messages.append(message)

    def add_attachment(self, attachment):
        self.attachments.append(attachment)

    def set_priority(self, priority):
        self.priority = priority

    def set_response_time_limit(self, response_time_limit):
        self.response_time_limit = response_time_limit

class TicketEvent:
    pass

class TicketCreated(TicketEvent):
    def __init__(self, ticket_id, product_id, customer_id):
        self.ticket_id = ticket_id
        self.product_id = product_id
        self.customer_id = customer_id

class MessageAdded(TicketEvent):
    def __init__(self, ticket_id, message):
        self.ticket_id = ticket_id
        self.message = message

class AttachmentAdded(TicketEvent):
    def __init__(self, ticket_id, attachment):
        self.ticket_id = ticket_id
        self.attachment = attachment

class PrioritySet(TicketEvent):
    def __init__(self, ticket_id, priority):
        self.ticket_id = ticket_id
        self.priority = priority

class ResponseTimeLimitSet(TicketEvent):
    def __init__(self, ticket_id, response_time_limit):
        self.ticket_id = ticket_id
        self.response_time_limit = response_time_limit
