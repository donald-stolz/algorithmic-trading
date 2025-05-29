import alpaca_trade_api as tradeapi
from config import ALPACA_API_KEY, ALPACA_SECRET_KEY, ALPACA_ENDPOINT

# Instantiate Alpaca REST API Connection
api = tradeapi.REST(key_id=ALPACA_API_KEY, secret_key=ALPACA_SECRET_KEY, 
                    base_url=ALPACA_ENDPOINT, api_version='v2')

def main():
    """Main function to demonstrate the greeting."""
    stock = input("Buy a share of which stock? ")
    quantity = input("How many shares? ")
    print(f"Buying {quantity} shares of {stock}")
    api.submit_order(
        symbol=stock,
        qty=quantity,
        side='buy',
        type='market',
    )
    print(f"Submitted order to buy {quantity} shares of {stock}")
    # Display positions
    positions = api.list_positions()
    for position in positions:
        print(f"Symbol: {position.symbol}, Quantity: {position.qty}, Market Value: ${position.market_value}")
    # Get orders
    orders = api.list_orders()
    for order in orders:
        print(f"Symbol: {order.symbol}, Quantity: {order.qty}, Status: {order.status}")

if __name__ == "__main__":
    main() 