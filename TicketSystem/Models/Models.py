from datetime import datetime, timedelta

class Product:
    def __init__(self, product_id, name, description):
        self.product_id = product_id
        self.name = name
        self.description = description

    def __str__(self):
        return self.name + " - " + self.description    

class Customer:
    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.email = email

    def __str__(self):
        return self.name + " - " + self.email    

class Agent:
    def __init__(self, agent_id, name, email):
        self.agent_id = agent_id
        self.name = name
        self.email = email

    def __str__(self):
        return self.name + " - " + self.email    

class Message:
    def __init__(self, message_id, content, author, attachments=None):
        self.message_id = message_id
        self.content = content
        self.author = author
        self.attachments = attachments if attachments else []

    def add_attachment(self, attachment):
        self.attachments.append(attachment)

    def __str__(self):
        return self.content + " - " + self.author    

class Ticket:
    def __init__(self, ticket_id, title, description, priority, response_time_limit, status, product, customer, agent=None):
        self.ticket_id = ticket_id
        self.title = title
        self.description = description
        self.priority = priority
        self.response_time_limit = response_time_limit
        self.status = status
        self.product = product
        self.customer = customer
        self.agent = agent
        self.messages = []
        self.creation_time = datetime.now()

    def add_message(self, content, author, attachments=None):
        message_id = len(self.messages) + 1
        message = Message(message_id, content, author, attachments)
        self.messages.append(message)
        return message
    
    def __str__(self):
        return self.title + " - " + self.status + " - " + self.product.name + " - " + self.customer.name + " - " + (self.agent.name if self.agent else "Unassigned") + " - " + str(self.creation_time) 
