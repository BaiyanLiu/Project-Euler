from utils import factorial_series


def main():
    factorials = factorial_series(9)
    factorials = {str(i): factorials[i] for i in range(len(factorials))}
    sums, chains = {}, {}
    print(sum(1 for i in range(1000000) if find_chain([i], factorials, sums, chains) == 60))


def find_chain(nums: list[int], factorials: dict[str, int], sums: dict[int, int], chains: dict[int, int]) -> int:
    curr = nums[-1]
    if curr in chains:
        chain = len(nums) + chains[curr] - 1
        cache_chains(nums, len(nums) - 1, chain, chains)
        return chain
    if curr not in sums:
        sums[curr] = sum(factorials[c] for c in str(curr))
    if (next_num := sums[curr]) in nums:
        chain = len(nums)
        loop_index = nums.index(next_num)
        for i in nums[loop_index:]:
            chains[i] = chain - loop_index
        cache_chains(nums, loop_index, chain, chains)
        return chain
    else:
        return find_chain(nums + [next_num], factorials, sums, chains)


def cache_chains(nums: list[int], end: int, chain: int, chains: dict[int, int]) -> None:
    for i in range(end):
        chains[nums[i]] = chain - i


if __name__ == '__main__':
    main()
