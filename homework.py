def minimize_job(jobs):

    order = sorted(range(len(jobs)), key=lambda i: jobs[i][1])
    
    t = 0 
    total = 0
    for i in order:
        t += jobs[1][0]
        total += max(0,t-jobs[i][1])
    
    return order,total

jobs = [(4,7),(2,5),(3,9),(6,8)]
order, tardiness = minimize_job(jobs)

print("Time work is given :" ,order)
print("total tardiness : ", tardiness) 