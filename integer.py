

def IntegerOptimization(cost, value, budget):
    total_cost = 0
    best_value = 0
    best_choice = None
    for x in range(2 ** len(cost)):
        list_bits = [int(bit) for bit in format(x, f'0{len(cost)}b')]
        cost_sum = 0
        value_sum = 0
        for y, is_valid in enumerate(list_bits):
            if is_valid:
                cost_sum += cost[y]
                value_sum += value[y]
        if cost_sum <= budget and value_sum > best_value:
            best_value = value_sum
            best_choice = list_bits
    cost_sum = 0
    for x in range(len(best_choice)):    
        if best_choice[x] == 1:
            cost_sum += cost[x]
    print("Total Cost: ", cost_sum)
    print("Total Value:", best_value)

import json

if __name__ == "__main__":
    with open("config.json", "r") as configuration:
        Configuration = json.load(configuration)
    IntegerOptimization(Configuration.get("cost"), Configuration.get("value"), Configuration.get("budget"))