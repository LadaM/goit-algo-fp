def choose_foods_greedy(foods, budget):
    # sorting by calories per cost
    sorted_items = sorted(
        foods.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True
    )
    selected_foods = []
    total_cost = 0
    total_calories = 0

    for food, properties in sorted_items:
        if total_cost + properties["cost"] <= budget:
            selected_foods.append(food)
            total_cost += properties["cost"]
            total_calories += properties["calories"]

    return {
        "selected_items": selected_foods,
        "total_cost": total_cost,
        "total_calories": total_calories,
    }


def choose_foods_dp(foods, budget):
    num_items = len(foods)
    # initialize dp table with 0 values since expected values are positive
    dp_table = [[0] * (budget + 1) for _ in range(num_items + 1)]

    for i in range(1, num_items + 1):
        for b in range(budget + 1):
            cost_i = foods[list(foods.keys())[i - 1]]["cost"]
            calories_i = foods[list(foods.keys())[i - 1]]["calories"]

            if cost_i <= b:
                dp_table[i][b] = max(
                    dp_table[i - 1][b], dp_table[i -
                                                 1][b - cost_i] + calories_i
                )
            else:
                dp_table[i][b] = dp_table[i - 1][b]

    # if no solution is found
    if dp_table[num_items][budget] == 0:
        return {
            "selected_items": [],
            "total_cost": 0,
            "total_calories": 0,
            "message": "No valid solution within the given budget."
        }

    selected_foods = []
    total_calories = dp_table[num_items][budget]

    b = budget
    for i in range(num_items, 0, -1):
        if dp_table[i][b] != dp_table[i - 1][b]:
            selected_foods.append(list(foods.keys())[i - 1])
            b -= foods[selected_foods[-1]]["cost"]

    selected_foods.reverse()

    return {
        "selected_items": selected_foods,
        "total_cost": budget - b,
        "total_calories": total_calories,
    }


def main():
    budget = 100
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350},
    }
    print("\nGreedy solution:")
    print(choose_foods_greedy(items, budget))
    print("\nDynamic programming solution:")
    print(choose_foods_dp(items, budget))


if __name__ == "__main__":
    main()
