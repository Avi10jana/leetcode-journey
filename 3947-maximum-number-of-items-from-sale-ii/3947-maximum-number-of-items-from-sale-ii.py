from collections import defaultdict

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)

        # Step 1: Find cheapest and max_factor
        cheapest = min(cost for _, cost in items)
        max_factor = max(factor for factor, _ in items)

        # Step 2: Calculate count of multiples for each factor
        freq = [0] * (max_factor + 1)

        for factor, _ in items:
            freq[factor] += 1

        for i in range(1, max_factor + 1):
            if freq[i] > 0:
                multiple = 2 * i
                while multiple <= max_factor:
                    freq[i] += freq[multiple]
                    multiple += i

        # Step 3: Collect profitable pair opportunities
        cost_count = defaultdict(int)

        for factor, cost in items:
            count = freq[factor] - 1

            if count > 0 and cost <= 2 * cheapest:
                cost_count[cost] += count

        # Step 4: Buy optimally
        total = 0

        for cost in sorted(cost_count):
            count = cost_count[cost]

            include = min(count, budget // cost)

            total += 2 * include
            budget -= include * cost

        total += budget // cheapest

        return total