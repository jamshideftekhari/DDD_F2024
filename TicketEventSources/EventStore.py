class EventStore:
    def __init__(self):
        self.events = []

    def append(self, event):
        self.events.append(event)

    def get_events_for_ticket(self, ticket_id):
        return [event for event in self.events if getattr(event, 'ticket_id', None) == ticket_id]
