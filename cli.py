import argparse

from bot.orders import place_market_order, place_limit_order
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)


def main():
    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        validate_side(args.side)
        validate_order_type(args.type)
        validate_quantity(args.quantity)

        if args.type.upper() == "LIMIT":
            if args.price is None:
                raise ValueError("Price is required for LIMIT orders")

            validate_price(args.price)

        print("\nOrder Request Summary")
        print(f"Symbol: {args.symbol}")
        print(f"Side: {args.side}")
        print(f"Type: {args.type}")
        print(f"Quantity: {args.quantity}")

        if args.price:
            print(f"Price: {args.price}")

        if args.type.upper() == "MARKET":
            response = place_market_order(
                args.symbol,
                args.side,
                args.quantity
            )

        else:
            response = place_limit_order(
                args.symbol,
                args.side,
                args.quantity,
                args.price
            )

        print("\nOrder Placed Successfully")
        print(f"Order ID: {response.get('orderId')}")
        print(f"Status: {response.get('status')}")
        print(f"Executed Qty: {response.get('executedQty')}")

    except Exception as e:
        print(f"\nError: {e}")


if __name__ == "__main__":
    main()