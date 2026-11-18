# Architecture

The package has three core concepts:

1. `Event`: immutable structured event data.
2. `EventLogger`: creates events and dispatches them to handlers.
3. `EventHandler`: protocol implemented by output destinations.

The initial implementation includes `JsonlHandler`. Future handlers can
implement the same `handle(event)` method for CSV, console, databases,
message queues or remote services.
