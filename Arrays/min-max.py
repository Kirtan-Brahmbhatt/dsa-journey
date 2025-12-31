class MinMaxArray:
    def __init__(self, arr):
        self.arr = arr

    def find_min_max(self):
        min_val = self.arr[0]
        max_val = self.arr[0]

        for i in range(1, len(self.arr)):
            if self.arr[i] < min_val:
                min_val = self.arr[i]
            if self.arr[i] > max_val:
                max_val = self.arr[i]

        print("Minimum:", min_val)
        print("Maximum:", max_val)


# Taking input from user
n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    val = int(input("Enter element: "))
    arr.append(val)

obj = MinMaxArray(arr)
obj.find_min_max()
