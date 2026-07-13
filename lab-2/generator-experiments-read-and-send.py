# Example from Gemini
def controlled_generator():
    try:
        while True:
            try:
                val = (yield "Ready")
                print(f"Received: {val}")
            except ValueError:
                print("Handled a ValueError internally! Keeping the loop alive.")
    finally:
        print("Cleaning up resources...")

g = controlled_generator()
print(next(g)) # Prime it

g.send("Hello")
g.throw(ValueError) # Inject an exception externally
g.close() # Safely shut down

# Ready
# Received: Hello
# Handled a ValueError internally! Keeping the loop alive.
# Cleaning up resources...