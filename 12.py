def find_group(links, member, linked=set()):
    linked.add(member)
    for link in links[member]:
        if not link in linked:
            linked.add(link)
            linked = linked.union(find_group(links, link, linked))
    return linked


# testLinks = {
#     0: [2],
#     1: [1],
#     2: [0, 3, 4],
#     3: [2, 4],
#     4: [2, 3, 6],
#     5: [6],
#     6: [4, 5]
# }
# print(find_group(testLinks, 4))


with open("12.txt") as f:
    file_links = {}
    for l in f.readlines():
        k, v = l.strip().split(' <-> ')
        file_links[int(k)] = [int(i) for i in v.split(', ')]
    # linked_to_zero = find_group(file_links, 0)
    # print(len(linked_to_zero))

    groups = 0
    grouped_keys = set()
    for k in file_links:
        if not k in grouped_keys:
            group = find_group(file_links, k)
            grouped_keys = grouped_keys.union(group)
            groups += 1
    print(groups)
