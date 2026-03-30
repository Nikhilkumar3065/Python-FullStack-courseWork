from dsa.recursion import Recursion
from dsa.sorting import Sorting
from dsa.searching import Searching
from dsa.stack import Stack
from dsa.queue import Queue
from utils.logger import setup_logger
import logging

setup_logger()

def main():
    recursion = Recursion()
    sorting = Sorting()
    searching = Searching()

    while True:
        print("\nDSA TOOLKIT")
        print("1. Factorial")
        print("2. Bubble Sort")
        print("3. Linear Search")
        print("4. Exit")

        choice = input("Enter choice: ")

        try:
            if choice == "1":
                n = int(input("Enter number: "))
                result = recursion.factorial(n)
                print("Result:", result)
                logging.info(f"Factorial({n}) = {result}")

            elif choice == "2":
                arr = list(map(int, input("Enter numbers separated by space: ").split()))
                print("Sorted:", sorting.bubble_sort(arr))

            elif choice == "3":
                arr = list(map(int, input("Enter numbers separated by space: ").split()))
                target = int(input("Enter target: "))
                print("Index:", searching.linear_search(arr, target))

            elif choice == "4":
                print("Exiting application.")
                break

            else:
                print("Invalid choice")

        except Exception as e:
            print("Error:", e)
            logging.error(str(e))


if __name__ == "__main__":
    main()