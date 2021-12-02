def ingest_data(filename):
    f = open(filename, "r")
    return [int(i.replace("\n", "")) for i in f.readlines()]

data = ingest_data("./Day 1/data.txt")
def part_1():
    depth_increase = 0
    cur_num = -1
    for x in data:
        if cur_num < 0:
            cur_num = x
        else:
            if cur_num < x:
                depth_increase += 1
            cur_num = x
    print(depth_increase)
def part_2():
    depth_increase = 0
    window_index = 0
    window = []
    for x in data:
        print(window)
        print("--------")
        window_len = len(window)
        if window_len < 4:
            window.append(x)
        else:
            win1_value = sum(window[0:3])
            print(window[0:3])
            win2_value = sum(window[1:4])
            print(window[1:4])
            print("---------")
            if win2_value > win1_value:
                depth_increase += 1
            window = window[1:4]
            window.append(x)
    win1_value = sum(window[0:3])
    print(window[0:3])
    win2_value = sum(window[1:4])
    print(window[1:4])
    print("---------")
    if win2_value > win1_value:
        depth_increase += 1
    print(depth_increase)
part_2()
