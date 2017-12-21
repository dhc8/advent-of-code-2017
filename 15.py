def generator_factory(factor, starting_value):
    def generator(iterations=0):
        """0 iterations means infinite"""
        val = starting_value
        i = 0
        while True:
            if i == iterations and iterations != 0:
                break
            product = val * factor
            val = product % 2147483647
            yield val
            i += 1
    return generator


def generator_a_factory(starting_value):
    return generator_factory(16807, starting_value)


def generator_b_factory(starting_value):
    return generator_factory(48271, starting_value)


def compare_bits(gen_a, gen_b, bits=16):
    divisor = 2 ** bits
    matches = 0
    for a, b in zip(gen_a, gen_b):
        match = a % divisor == b % divisor
        if match:
            matches += 1
    return matches


def do_comparison(a_starting_val, b_starting_val, iterations=40000000):
    gen_a = generator_a_factory(a_starting_val)
    gen_b = generator_b_factory(b_starting_val)
    return compare_bits(gen_a(iterations), gen_b(iterations))


def picky_generator_a_factory(starting_value):
    gen_a = generator_a_factory(starting_value)

    def picky_generator(iterations):
        i = 0
        for a in gen_a():
            if i == iterations:
                break
            if a % 4 == 0:
                yield a
                i += 1

    return picky_generator


def picky_generator_b_factory(starting_value):
    gen_b = generator_b_factory(starting_value)

    def picky_generator(iterations):
        i = 0
        for a in gen_b():
            if i == iterations:
                break
            if a % 8 == 0:
                yield a
                i += 1

    return picky_generator


def do_picky_comparison(a_starting_val, b_starting_val, iterations=5000000):
    gen_a = picky_generator_a_factory(a_starting_val)
    gen_b = picky_generator_b_factory(b_starting_val)
    return compare_bits(gen_a(iterations), gen_b(iterations))


# Test
# generator_a = generator_a_factory(65)
# generator_b = generator_b_factory(8921)
# print([i for i in generator_a(5)])
# print([i for i in generator_b(5)])
# print(do_comparison(65, 8921, 5))
# print(do_comparison(65, 8921))

# Part 1
# print(do_comparison(512, 191))

# Part 2
# print(do_picky_comparison(65, 8921, 1056))
# print(do_picky_comparison(65, 8921))
print(do_picky_comparison(512, 191))
