n = int(input())
budget_list = list(map(int, input().split()))
budget_total = int(input())
max_budget = 0

if sum(budget_list) <= budget_total:
    max_budget = max(budget_list)
else:
    budget_list.sort()
    max_budget = budget_total // n

    for i in range(n):
        budget_total -= budget_list[i]
        if budget_total > 0:
            max_budget = max(max_budget, budget_total // (n - i - 1))

print(max_budget)