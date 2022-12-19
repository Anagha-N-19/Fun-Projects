import time


def counter(t):
    while t >= 0:
        mins = t // 60
        sec = t % 60
        if mins < 10 and sec < 10:
            timer = f"0{mins}:0{sec}"
        elif mins < 10:
            timer = f"0{mins}:{sec}"
        elif sec < 10:
            timer = f"{mins}:0{sec}"
        print(f"\r{timer}", end="")
        time.sleep(1)
        t -= 1
    print("\nOver")


t = int(input("Enter countdown time in seconds: "))
counter(t)
