weekday_hours = float(input("Enter weekday study hours: "))
weekend_hours = float(input("Enter weekend study hours: "))

week_hours = weekday_hours * 5 + weekend_hours * 2
month_hours = week_hours * 4

print(f"Weekly hours: {week_hours}")

if week_hours < 7:
    print("Pace: slow pace")
elif week_hours < 12:
    print("Pace: normal pace")
else:
    print("Pace: strong pace")

print(f"Monthly hours: {month_hours}")