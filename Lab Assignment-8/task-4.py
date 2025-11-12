class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, name, price):
        if not isinstance(name, str) or not isinstance(price, (int, float)) or price < 0:
            return "Invalid Input"
        self.items[name] = price
        return f"Added {name}"

    def remove_item(self, name):
        if name in self.items:
            del self.items[name]
            return f"Removed {name}"
        return "Item Not Found"

    def total_cost(self):
        return sum(self.items.values())


# 🤖 AI-Generated Test Cases
def test_shopping_cart():
    print("=== ShoppingCart Tests ===")
    cart = ShoppingCart()
    results = [
        (cart.add_item("Apple", 1.5), "Added Apple"),
        (cart.add_item("Banana", 0.8), "Added Banana"),
        (cart.add_item("Milk", 2.0), "Added Milk"),
        (cart.add_item("Invalid", -1), "Invalid Input"),
        (cart.remove_item("Banana"), "Removed Banana"),
        (cart.remove_item("Bread"), "Item Not Found"),
    ]
    cart.add_item("Eggs", 3.0)
    expected_total = 1.5 + 2.0 + 3.0
    results.append((cart.total_cost(), expected_total))

    passed, failed = 0, 0
    for i, (result, expected) in enumerate(results, 1):
        print(f"{'✅ PASS' if result == expected else '❌ FAIL'}: Test {i}")
        if result == expected: passed += 1
        else: failed += 1
    print(f"\nSummary: {passed} Passed, {failed} Failed")
    print("Final Cart:", cart.items)

if __name__ == "__main__":
    test_shopping_cart()
