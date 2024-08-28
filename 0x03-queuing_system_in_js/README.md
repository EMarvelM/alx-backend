# Queuing System in JavaScript

This project involves creating a queuing system using Redis, Node.js, Express, and Kue. The goal is to understand how to interact with Redis, manage queues, and handle asynchronous operations in a JavaScript environment.

## Learning Objectives

- Set up and run a Redis server locally.
- Perform basic operations using the Redis client.
- Use Redis with Node.js for storing and retrieving data.
- Manage queues using Kue and integrate them with an Express app.
- Handle asynchronous operations and manage queue jobs.

## Project Requirements

- Environment: Ubuntu 18.04, Node.js 12.x, Redis 5.0.7
- Code: Written in JavaScript using ES6 syntax.
- Package manager: npm
- All code files should end with a new line.

## Installation and Setup

1. **Install Redis:**

   Download and compile the latest stable version of Redis:

   ```bash
   $ wget http://download.redis.io/releases/redis-6.0.10.tar.gz
   $ tar xzf redis-6.0.10.tar.gz
   $ cd redis-6.0.10
   $ make

   ```

    Start Redis in the background:
    
    ```bash
    $ src/redis-server &
    ```

