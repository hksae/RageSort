import itertools


def bit_radix_sort(data, radix_bits=8):
    def _core_sort(subset, bit_count, step=8):
        if len(subset) < 2 or bit_count <= 0:
            return subset

        high_bit = 1 << (bit_count - 1)
        working_data = [num ^ high_bit for num in subset]

        num_passes = (max(0, bit_count - 1) + step - 1) // step
        mask = (1 << step) - 1

        for p in range(num_passes):
            shift = p * step
            buckets = [[] for _ in range(1 << step)]

            for num in working_data:
                idx = (num >> shift) & mask
                buckets[idx].append(num)

            working_data = list(itertools.chain.from_iterable(buckets))

        return [num ^ high_bit for num in working_data]

    if len(data) < 2:
        return data[:]

    zeros = [x for x in data if x == 0]
    non_zeros = [x for x in data if x != 0]

    if not non_zeros:
        return zeros

    max_bits = 0
    for x in non_zeros:
        length = abs(x).bit_length()
        if length > max_bits:
            max_bits = length

    pos_groups = [[] for _ in range(max_bits + 1)]
    neg_groups = [[] for _ in range(max_bits + 1)]

    for x in non_zeros:
        if x < 0:
            neg_groups[abs(x).bit_length()].append(x)
        else:
            pos_groups[x.bit_length()].append(x)

    sorted_result = []

    for i in range(max_bits, 0, -1):
        if neg_groups[i]:
            abs_group = [abs(x) for x in neg_groups[i]]
            sorted_abs = _core_sort(abs_group, i, step=radix_bits)
            sorted_result.extend([-val for val in sorted_abs[::-1]])

    sorted_result.extend(zeros)

    for i in range(max_bits + 1):
        if pos_groups[i]:
            sorted_result.extend(_core_sort(pos_groups[i], i, step=radix_bits))

    return sorted_result