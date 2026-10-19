"""CodeAlpha Python Internship - Task 2: Stock Portfolio Tracker"""

STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 135,
}


def get_portfolio():
    portfolio = {}
    print("Available stocks:")
    for name, price in STOCK_PRICES.items():
        print(f"  {name}: ${price}")
    print("\nEnter stock name and quantity. Type 'done' when finished.\n")

    while True:
        name = input("Stock name: ").strip().upper()
        if name == "DONE":
            break
        if name not in STOCK_PRICES:
            print("Stock not found. Choose from the list above.")
            continue
        try:
            qty = int(input(f"Quantity of {name}: "))
            if qty <= 0:
                raise ValueError
        except ValueError:
            print("Please enter a positive whole number.")
            continue
        portfolio[name] = portfolio.get(name, 0) + qty
    return portfolio


def summarize(portfolio):
    lines, total = [], 0
    for name, qty in portfolio.items():
        value = STOCK_PRICES[name] * qty
        total += value
        lines.append(f"{name}: {qty} x ${STOCK_PRICES[name]} = ${value}")
    lines.append(f"Total investment: ${total}")
    return lines


def save_to_file(lines, filename="portfolio.txt"):
    with open(filename, "w") as f:
        f.write("\n".join(lines) + "\n")
    print(f"Saved to {filename}")


def main():
    portfolio = get_portfolio()
    if not portfolio:
        print("No stocks entered.")
        return

    lines = summarize(portfolio)
    print("\n--- Portfolio Summary ---")
    print("\n".join(lines))

    if input("\nSave result to file? (y/n): ").strip().lower() == "y":
        save_to_file(lines)


if __name__ == "__main__":
    main()
