# python3


def compute_optimal_summands(n):
    assert 1 <= n <= 10 ** 9
    summands = []

    i = 1
    while n >= 2 * i + 1:
        summands.append(i)
        n -= i
        i += 1
    if n > 0:
        summands.append(n)

    return summands


if __name__ == '__main__':
    input_n = int(input())
    output_summands = compute_optimal_summands(input_n)
    print(len(output_summands))
    print(*output_summands)
