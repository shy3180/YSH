def make_gugu(num):
    with open(f"gugu_{num}_result.txt", "w") as handle:
        for i in range(1, 10):
            handle.write(f"{num} X {i} = {num*i}\n")


make_gugu(3)

for i in range(1, 101):
    make_gugu(i)
