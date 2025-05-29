def greet(name: str) -> str:
    """
    A simple greeting function.
    
    Args:
        name (str): The name to greet
        
    Returns:
        str: A greeting message
    """
    return f"Hello, {name}!"

def main():
    """Main function to demonstrate the greeting."""
    name = input("What's your name? ")
    message = greet(name)
    print(message)

if __name__ == "__main__":
    main() 