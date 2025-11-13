import calc_area

print("1 - Rectangle  2 - Triangle  3 - Circle")
choice = input("Enter number: ").strip()

if choice == "1":
    a = float(input("Enter length side a: "))
    b = float(input("Enter length side b: "))
    s = calc_area.area_rectangle(a, b)
elif choice == "2":
    base = float(input("Enter Base: "))
    height = float(input("Enter Height: "))
    s = calc_area.area_triangle(base, height)
elif choice == "3":
    r = float(input("Enter Radius: "))
    s = calc_area.area_circle(r)
else:
    print("Wrong choice")
    raise SystemExit

print(f"Area = {s:.2f} m\u00B2")