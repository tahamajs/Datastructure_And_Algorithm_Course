def find_max_valid_sequence(nodes):
    stack = []
    start_indices = {}
    end_indices = {}
    filtered_nodes = []

    for i, node in enumerate(nodes):
        if filtered_nodes and node == filtered_nodes[-1]:
            continue

        filtered_nodes.append(node)
        end_indices[node] = len(filtered_nodes) - 1

        if node not in start_indices:
            start_indices[node] = len(filtered_nodes) - 1

    max_depth = 0
    current_depth = 0
    bad_sequence = False

    for i, node in enumerate(filtered_nodes):
        if i == start_indices[node] and i == end_indices[node]:
            current_depth += 1
            max_depth = max(max_depth, current_depth)
            current_depth -= 1
            continue

        if i == start_indices[node]:
            stack.append(node)
            current_depth += 1

        if i == end_indices[node]:
            if stack and stack[-1] == node:
                stack.pop()
                current_depth -= 1
            else:
                bad_sequence = True
                break

        max_depth = max(max_depth, current_depth)

    if stack:
        bad_sequence = True

    return max_depth if not bad_sequence else -1


def main():
    n = int(input())
    nodes = []
    max_sequence_length = 0
    invalid_sequence = False

    for _ in range(n):
        tmp = int(input())
        if tmp == 0:
            result = find_max_valid_sequence(nodes)
            if result == -1:
                invalid_sequence = True
                break
            max_sequence_length = max(max_sequence_length, result)
            nodes = []
        else:
            nodes.append(tmp)

    if not invalid_sequence:
        result = find_max_valid_sequence(nodes)
        if result == -1:
            invalid_sequence = True
        max_sequence_length = max(max_sequence_length, result)

    print(-1 if invalid_sequence else max_sequence_length)


if __name__ == "__main__":
    main()
