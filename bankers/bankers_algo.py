

def banker_algorithm(allocation, max_matrix, available):

    n = int(input("Enter the number of Processes: "))
    m = int(input("Enter the number of Resources: "))

    need = []

    for i in range(n):
        temp = []
        for j in range(m):
            temp.append(0)
        need.append(temp)

    for i in range(n):
        for j in range(m):
            need[i][j] = max_matrix[i][j] - allocation[i][j]

    def check(i):
        for j in range(m):
            if need[i][j] > available[j]:
                return False
        return True

    # implementing Banker's Algorithm
    sequence = ['0']*n
    visited = [0]*n
    count = 0

    while count < n:
        safe = False
        for i in range(n):
            if visited[i] == 0 and check(i):
                sequence[count] = "P" + str(i)
                count += 1
                visited[i] = 1
                safe = True
                for j in range(m):
                    available[j] += allocation[i][j]

        if not safe:
            break

    if (count < n):
        print("The System is Unsafe!")

    else:
        print("The System is Safe!")
        print("Safe Sequence is", sequence)
        print("Available resource is", available)


# Allocation Matrix
alloc = [[0, 1, 0], [2, 0, 0],
         [3, 0, 2], [2, 1, 1], [0, 0, 2]]

# MAX Matrix
maX = [[7, 5, 3], [3, 2, 2],
       [9, 0, 2], [2, 2, 2], [4, 3, 3]]

avail = [3, 3, 2]  # Available Resources

banker_algorithm(alloc, maX, avail)
