from datetime import datetime, timedelta
from Models import Product, Customer, Agent, Ticket

class TicketSystem:
    def __init__(self):
        self.products = {}  # Store products in a dictionary {product_id: Product}
        self.customers = {}  # Store customers in a dictionary {customer_id: Customer}
        self.agents = {}  # Store agents in a dictionary {agent_id: Agent}
        self.tickets = {}  # Store tickets in a dictionary {ticket_id: Ticket}
        self.next_ticket_id = 1

    def create_product(self, name, description):
        product_id = len(self.products) + 1
        product = Product(product_id, name, description)
        self.products[product_id] = product
        return product

    def create_customer(self, name, email):
        customer_id = len(self.customers) + 1
        customer = Customer(customer_id, name, email)
        self.customers[customer_id] = customer
        return customer

    def create_agent(self, name, email):
        agent_id = len(self.agents) + 1
        agent = Agent(agent_id, name, email)
        self.agents[agent_id] = agent
        return agent

    def create_ticket(self, title, description, priority, response_time_limit, status, product_id, customer_id):
        ticket_id = self.next_ticket_id
        self.next_ticket_id += 1
        product = self.products.get(product_id)
        customer = self.customers.get(customer_id)
        ticket = Ticket(ticket_id, title, description, priority, response_time_limit, status, product, customer)
        self.tickets[ticket_id] = ticket
        return ticket

    def assign_agent_to_ticket(self, ticket_id, agent_id):
        ticket = self.tickets.get(ticket_id)
        if ticket:
            agent = self.agents.get(agent_id)
            ticket.agent = agent
            ticket.status = "In Progress"
            ticket.response_time_limit = ticket.creation_time + timedelta(hours=ticket.response_time_limit)

    def close_ticket(self, ticket_id):
        ticket = self.tickets.get(ticket_id)
        if ticket:
            ticket.status = "Closed"

    def check_response_time(self, ticket_id):
        ticket = self.tickets.get(ticket_id)
        if ticket and ticket.status == "In Progress":
            if datetime.now() > ticket.response_time_limit:
                print("Response time limit exceeded for ticket:", ticket.ticket_id)
                # You can implement further actions here, like escalating the ticket, notifying stakeholders, etc.

if __name__ == "__main__":
    # Example usage:
    ticket_system = TicketSystem()

    # Create products
    product1 = ticket_system.create_product("Product A", "Description of Product A")

    # Create customers
    customer1 = ticket_system.create_customer("Alice", "alice@example.com")

    # Create agents
    agent1 = ticket_system.create_agent("Agent 1", "agent1@example.com")

    # Create tickets with priority and response time limit
    ticket1 = ticket_system.create_ticket("Bug Fix", "Fix login issue", "High", 24, "Open", product1.product_id, customer1.customer_id)
    print(ticket1)
    # Assign agent to ticket
    ticket_system.assign_agent_to_ticket(ticket1.ticket_id, agent1.agent_id)
    print(ticket1)

    # Check response time for the ticket
    ticket_system.check_response_time(ticket1.ticket_id)
    print(ticket1)

    # Close ticket
    ticket_system.close_ticket(ticket1.ticket_id)
    print(ticket1)
