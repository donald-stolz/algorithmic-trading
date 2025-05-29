import os
from pathlib import Path
from dotenv import load_dotenv

# Get the project root directory
ROOT_DIR = Path(__file__).parent.parent

# Load environment variables from .env file
load_dotenv(ROOT_DIR / '.env')

# API Configuration
ALPACA_API_KEY = os.getenv('ALPACA_API_KEY')
ALPACA_SECRET_KEY = os.getenv('ALPACA_SECRET_KEY')

# Database Configuration
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = int(os.getenv('DB_PORT', 5432))
DB_NAME = os.getenv('DB_NAME', 'algo_trading')
DB_USER = os.getenv('DB_USER', 'postgres')
DB_PASSWORD = os.getenv('DB_PASSWORD')

# Trading Configuration
MAX_POSITION_SIZE = float(os.getenv('MAX_POSITION_SIZE', 100000))
RISK_PER_TRADE = float(os.getenv('RISK_PER_TRADE', 0.02))
MAX_OPEN_TRADES = int(os.getenv('MAX_OPEN_TRADES', 5))

# Logging Configuration
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
LOG_FILE_PATH = os.getenv('LOG_FILE_PATH', 'logs/trading.log')

# Validate required environment variables
def validate_config():
    required_vars = [
        'ALPACA_API_KEY',
        'ALPACA_SECRET_KEY',
        'DB_PASSWORD'
    ]
    
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    
    if missing_vars:
        raise ValueError(
            f"Missing required environment variables: {', '.join(missing_vars)}. "
            "Please check your .env file."
        )

# Create a .env.example file with the same structure but without sensitive values
def create_env_example():
    example_content = """# API Keys
ALPACA_API_KEY=your_api_key_here
ALPACA_SECRET_KEY=your_secret_key_here

# Database Configuration
DB_HOST=localhost
DB_PORT=5432
DB_NAME=algo_trading
DB_USER=postgres
DB_PASSWORD=your_db_password_here

# Trading Configuration
MAX_POSITION_SIZE=100000
RISK_PER_TRADE=0.02
MAX_OPEN_TRADES=5

# Logging Configuration
LOG_LEVEL=INFO
LOG_FILE_PATH=logs/trading.log
"""
    
    with open(ROOT_DIR / '.env.example', 'w') as f:
        f.write(example_content)

if __name__ == '__main__':
    create_env_example() 