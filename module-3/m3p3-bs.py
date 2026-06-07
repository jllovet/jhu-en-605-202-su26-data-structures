import json
import math
def bs(desired, items, low, high, calls=0):
    calls += 1
    size = (high - low) + 1
    midpoint = (high + low) // 2
    if desired == items[midpoint]:
        return {"location": midpoint, "calls": calls, "len_items": len(items)}
    if size == 1:
        return {"location": -1, "calls": calls, "len_items": len(items)}
    if desired < items[midpoint]:
        return bs(desired, items, low, midpoint, calls)
    if desired > items[midpoint]:
        return bs(desired, items, midpoint+1, high, calls)


experiment_results = []

for x in range(1,11):
    numbers = [_ for _ in range(x)]
    results = [bs(desired=i, items=numbers, low=0, high=len(numbers)) for i in range(len(numbers))]
    experiment_results.append({
        "list_length": x, "max_calls": max([result.get("calls") for result in results]), "log_2_x+1": math.log2(x) + 1 # type: ignore
    })


with open("experiment-results.json", "w") as f:
    json.dump(experiment_results, f, indent=4)

