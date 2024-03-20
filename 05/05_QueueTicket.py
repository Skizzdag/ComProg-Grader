def QueueTicket():
    Queue = []
    first = []
    wait = []
    timewait = []
    step = 0
    for i in range(int(input())):
        inp = input().split()
        if inp[0] == "reset":
            first.append(inp[1])
        elif inp[0] == "new":
            if len(Queue) == 0:
                first.append(inp[1])
                Queue.append(first)
            else:
                Queue.append([int(Queue[-1][0])+1,inp[1]])
            print("ticket",Queue[-1][0])
        elif inp[0] == "next":
            print("call",Queue[step][0])
            wait.append(Queue[step])
            step += 1
        elif inp[0] == "order":
            print("qtime",wait[-1][0],int(inp[1])-int(wait[-1][1]))
            timewait.append(int(inp[1])-int(wait[-1][1]))
        elif inp[0] == "avg_qtime":
            avg = float(sum(timewait)/len(timewait))
            print("avg_qtime",round(avg,4))

QueueTicket()