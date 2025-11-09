def cm_to_inches(cm: float) -> float:
    """
    Convert centimetres to inches.
    Formula: 1 inch = 2.54 centimetres
    """
    return cm / 2.54


def main():
    print("Centimetres to Inches Converter\n")
    try:
        cm_value = float(input("Enter length in centimetres: "))
    except ValueError:
        print("Invalid input! Please enter a numeric value.")
        return

    inches = cm_to_inches(cm_value)
    print(f"{cm_value} cm = {inches:.2f} inches")


if __name__ == "__main__":
    main()
