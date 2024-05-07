create database ticketDB;
use ticketDB;

CREATE TABLE Product (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT
);

CREATE TABLE Customer (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL
);

CREATE TABLE Agent (
    agent_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL
);

CREATE TABLE Message (
    message_id INT AUTO_INCREMENT PRIMARY KEY,
    content TEXT NOT NULL,
    author_id INT,
    customer_id INT,
    ticket_id INT NOT NULL,
    attachments TEXT,
    FOREIGN KEY (author_id) REFERENCES Agent(agent_id) ON DELETE CASCADE,
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id) ON DELETE CASCADE,
    FOREIGN KEY (ticket_id) REFERENCES Ticket(ticket_id) ON DELETE CASCADE
);


CREATE TABLE Ticket (
    ticket_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    priority VARCHAR(50) NOT NULL,
    response_time_limit INT,
    status VARCHAR(50) NOT NULL,
    product_id INT NOT NULL,
    customer_id INT NOT NULL,
    agent_id INT,
    creation_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES Product(product_id) ON DELETE CASCADE,
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id) ON DELETE CASCADE,
    FOREIGN KEY (agent_id) REFERENCES Agent(agent_id) ON DELETE SET NULL
);

-- Insert test data for Product table
INSERT INTO Product (name, description) VALUES
('Product A', 'Description of Product A'),
('Product B', 'Description of Product B');

-- Insert test data for Customer table
INSERT INTO Customer (name, email) VALUES
('Alice', 'alice@example.com'),
('Bob', 'bob@example.com');

-- Insert test data for Agent table
INSERT INTO Agent (name, email) VALUES
('Agent 1', 'agent1@example.com'),
('Agent 2', 'agent2@example.com');

-- Insert test data for Ticket table
INSERT INTO Ticket (title, description, priority, response_time_limit, status, product_id, customer_id, agent_id)
VALUES
('Bug Fix', 'Fix login issue', 'High', 24, 'Open', 1, 1, 1),
('Feature Request', 'Add new feature', 'Medium', 48, 'Open', 2, 2, NULL);

-- Insert test data for Message table
INSERT INTO Message (content, author_id, customer_id, ticket_id, attachments)
VALUES
('Issue still persists.', NULL, 1, 1, NULL),
('We will look into it.', 1, NULL, 1, NULL),
('Please see the attached screenshot.', NULL, 2, 2, 'screenshot1.png');

