def friend_list(filename):
    result = {}

    with open(filename, 'r') as f:
        for line in f:
            (v1, v2) = line.split()

            if v1 in result.keys():
                current_friends = result[v1]
                if v2 not in current_friends:
                    current_friends.append(v2)
                result[v1] = sorted(current_friends)
            else:
                result[v1] = [v2]

            if v2 in result.keys():
                current_friends = result[v2]
                if v1 not in current_friends:
                    current_friends.append(v1)
                result[v2] = sorted(current_friends)
            else:
                result[v2] = [v1]
    return result

