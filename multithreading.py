import time
import threading

def calc_square(numbers):
    print("Square of Numbers")
    for number in numbers:
        time.sleep(0.2)
        print(f"square: {number*number}")


def calc_cube(numbers):
    print("Cube of numbers")
    for num in numbers:
        time.sleep(0.2)
        print(f"cube: {num*num*num}")



arr = [2, 3, 8, 9]
t = time.time()

t1 = threading.Thread(target=calc_square, args=(arr,))
t2 = threading.Thread(target=calc_cube, args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()

print(f"done in : {time.time() - t}")
