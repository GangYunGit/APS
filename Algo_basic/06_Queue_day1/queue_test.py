# Queue

# # 선형 큐
# N = 3
# q = [0] * N
# front = -1
# rear = -1
#
# rear += 1       # enqueue(10)
# q[rear] = 10
#
# rear += 1       # enqueue(20)
# q[rear] = 20
#
# rear += 1       # enqueue(30)
# q[rear] = 30
#
# front += 1      # dequeue()
# print(q[front])
#
# front += 1      # dequeue()
# print(q[front])
#
# front += 1      # dequeue()
# print(q[front])

# 원형 큐
N = 3
q = [0] * N
front = 0
rear = 0

rear = (rear + 1) % N      # enqueue(10)
q[rear] = 10

rear = (rear + 1) % N       # enqueue(20)
q[rear] = 20

rear = (rear + 1) % N      # enqueue(30)
q[rear] = 30

# 크기를 초과 가능
rear = (rear + 1) % N      # enqueue(40)
q[rear] = 40

front = (front + 1) % N      # dequeue()
print(q[front])

front = (front + 1) % N      # dequeue()
print(q[front])

front = (front + 1) % N      # dequeue()
print(q[front])