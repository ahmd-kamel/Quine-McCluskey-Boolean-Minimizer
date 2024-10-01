import sys
from expression_parser import get_minterms, extract_vars

def count_ones_in_minterm(minterm):
    return minterm.count(1)

def group_minterms(minterms):
    grouped_minterms = {}
    for minterm in minterms:
        num_ones = count_ones_in_minterm(minterm)
        if num_ones not in grouped_minterms:
            grouped_minterms[num_ones] = []
        grouped_minterms[num_ones].append(minterm)
    return grouped_minterms

def can_combine(term1, term2):
    diff_count = 0
    for bit1, bit2 in zip(term1, term2):
        if bit1 != bit2:
            diff_count += 1
        if diff_count > 1:
            return False
    return diff_count == 1

def combine_terms(term1, term2):
    combined_term = []
    for bit1, bit2 in zip(term1, term2):
        if bit1 == bit2:
            combined_term.append(bit1)
        else:
            combined_term.append('x')
    return tuple(combined_term)

def find_prime_implicants(minterms):
    grouped_minterms = group_minterms(minterms)
    prime_implicants = []

    while True:
        new_groups = {}
        combined = set()

        group_keys = sorted(grouped_minterms.keys())

        for i in range(len(group_keys) - 1):
            group_1 = grouped_minterms[group_keys[i]]
            group_2 = grouped_minterms[group_keys[i + 1]]

            for term1 in group_1:
                for term2 in group_2:
                    if can_combine(term1, term2):
                        combined_term = combine_terms(term1, term2)
                        combined.add(term1)
                        combined.add(term2)

                        num_ones = combined_term.count(1)
                        if num_ones not in new_groups:
                            new_groups[num_ones] = []
                        if combined_term not in new_groups[num_ones]:
                            new_groups[num_ones].append(combined_term)

        for group in grouped_minterms.values():
            for term in group:
                if term not in combined:
                    prime_implicants.append(term)

        if not new_groups:
            break

        grouped_minterms = new_groups

    return prime_implicants

def prime_implicants_to_sop(prime_implicants, variables):
    sop_terms = []
    for implicant in prime_implicants:
        term = []
        for i, bit in enumerate(implicant):
            if bit == 0:
                term.append(f'!{variables[i]}')
            elif bit == 1:
                term.append(variables[i])

        sop_terms.append(''.join(term))
    return ' + '.join(sop_terms)


if __name__ == "__main__":
    # expression = '(A|!B|!C)&(A|!B|C)&(A|B|!C)'
    # expression = '(A&B&C) | (!A) | (A&!B&C)'
    # expression = 'A|B'
    expression = sys.argv[1]
    vars = extract_vars(expression)
    minterms = get_minterms(expression)
    prime_implicants = find_prime_implicants(minterms)
    sop = prime_implicants_to_sop(prime_implicants, vars)
    print("The minimized (SOP) expression:", sop)
