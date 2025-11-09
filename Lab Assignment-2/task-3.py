import math

def calculate_area():
    print("Choose a shape to calculate the area:")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Triangle")
    print("4. Square")
    print("5. Trapezoid")
    print("6. Ellipse")
    
    choice = input("Enter the number of your choice: ")
    
    if choice == '1':
        radius = float(input("Enter the radius of the circle: "))
        area = math.pi * radius ** 2
        print(f"The area of the circle is: {area}")
        
    elif choice == '2':
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = length * width
        print(f"The area of the rectangle is: {area}")
        
    elif choice == '3':
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        area = 0.5 * base * height
        print(f"The area of the triangle is: {area}")
        
    elif choice == '4':
        side = float(input("Enter the side of the square: "))
        area = side ** 2
        print(f"The area of the square is: {area}")
        
    elif choice == '5':
        base1 = float(input("Enter the first base of the trapezoid: "))
        base2 = float(input("Enter the second base of the trapezoid: "))
        height = float(input("Enter the height of the trapezoid: "))
        area = 0.5 * (base1 + base2) * height
        print(f"The area of the trapezoid is: {area}")
        
    elif choice == '6':
        a = float(input("Enter the semi-major axis (a) of the ellipse: "))
        b = float(input("Enter the semi-minor axis (b) of the ellipse: "))
        area = math.pi * a * b
        print(f"The area of the ellipse is: {area}")
        
    else:
        print("Invalid choice. Please choose a number between 1 and 6.")

# Call the function
calculate_area()
