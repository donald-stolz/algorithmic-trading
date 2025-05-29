from src.main import greet

def test_greet():
    """Test the greet function with various inputs."""
    assert greet("World") == "Hello, World!"
    assert greet("Python") == "Hello, Python!"
    assert greet("") == "Hello, !" 