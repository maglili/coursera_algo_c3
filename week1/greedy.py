def completion_time(ans):
    """
    Computing weighted completion time.
    """
    sum_ = 0
    pass_time = 0
    for w, l in ans:
        pass_time += l
        sum_ += w * (pass_time)
    return sum_


path = "./data/jobs.txt"
jobs = []
with open(path, "r") as fh:
    for idx, row in enumerate(fh):
        if idx == 0:
            continue

        row = row.split()
        row = [int(x) for x in row]
        jobs.append((row[0], row[1]))

print("raw weighted sum:", completion_time(jobs))

# Q1
ans = sorted(jobs, key=lambda x: [x[0] - x[1], x[0]], reverse=True)
print("Greedy algo_1:", completion_time(ans))

# Q2
ans = sorted(jobs, key=lambda x: [x[0] / x[1], x[0]], reverse=True)
print("Greedy algo_2:", completion_time(ans))
