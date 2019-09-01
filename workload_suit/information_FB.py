import random
import linecache

file =["/FB-2009_samples_24_times_1hr_0.tsv","/FB-2009_samples_24_times_1hr_1.tsv","/FB-2010_samples_24_times_1hr_0.tsv","/FB-2010_samples_24_times_1hr_withInputPaths_0.tsv"]

def getinf(n, file_str):
    num_list = [[0] * 2 for i in range(n)]
    num_len1 = [0] * 101
    file_str += file[random.randint(0,3)]
    print(file_str)
    f = open(file_str, "r")
    length = len(f.readlines())
    temp_item = 0

    while (temp_item < n):
        # print(temp_item)
        line_num = random.randint(1, length - 1)
        # random read line
        # lineinfo = linecache.getline(file_str, line_num)

        # first n lines of this tsv
        lineinfo = linecache.getline(file_str, temp_item + 1)

        item = lineinfo.split("\t")
        # print(lineinfo)
        # max interval =99
        num_list[temp_item][0] = 99 if int(item[2]) > 100 else int(item[2])
        num_list[temp_item][1] = int(len(item[3])/2)
        if int(item[2])>99:
            num_len1[100] +=1
        else:
            num_len1[int(item[2])] += 1
        temp_item +=1


    return num_list


# getinf(30, "/Users/liuzifeng/Desktop/project/workload_spark/FB-2010_samples_24_times_1hr_withInputPaths_0.tsv")

# getinf(5894, "/Users/liuzifeng/Desktop/project/workload_spark/FB-2009_samples_24_times_1hr_0.tsv")
# getinf(50, "/Users/liuzifeng/Desktop/project/workload_spark/FB-2009_samples_24_times_1hr_0_first50jobs.tsv")
# getinf(6638, "/Users/liuzifeng/Desktop/project/workload_spark/FB-2009_samples_24_times_1hr_1.tsv")
# getinf(24442, "/Users/liuzifeng/Desktop/project/workload_spark/FB-2010_samples_24_times_1hr_0.tsv")
# getinf(25428, "/Users/liuzifeng/Desktop/project/workload_spark/FB-2010_samples_24_times_1hr_withInputPaths_0.tsv")

# data size statistic
# [0, 86, 752, 717, 1072, 1730, 208, 222, 343, 239, 249, 234, 41, 1, 0, 0, 0, 0, 0, 0]
# [0, 2, 1, 6, 2, 10, 18, 6, 2, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 183, 799, 829, 864, 1934, 251, 245, 332, 432, 343, 362, 62, 2, 0, 0, 0, 0, 0, 0]
# [0, 1126, 35, 2360, 1687, 2427, 2250, 2304, 3359, 2222, 3570, 1677, 1145, 278, 2, 0, 0, 0, 0, 0]
# [0, 1746, 20, 2729, 1792, 2242, 2471, 2244, 2794, 2165, 3931, 1713, 1337, 239, 5, 0, 0, 0, 0, 0]

# interval statistic
# [0, 3550, 2285, 58, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 9, 31, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 4108, 2470, 60, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 22423, 2016, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 23365, 2062, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
