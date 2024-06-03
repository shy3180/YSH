def base_count(seq):
    data = dict()
    for base in seq:
        if base not in data:
            base[base] = 0

            data[base] += 1

    return data
