print(
    "lets do ranges! type a starting number, ending before number, and how much you want to increment by!"
)

start = int(input("Sart at: "))
end = int(input("End before: "))
increment = int(input("Increment between values: "))

for i in range(start, end, increment):
    print(i)
