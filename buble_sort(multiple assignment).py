buble_list = [5,2,7,3]

for i in range(len(buble_list)):
    for j  in range(i+1,len(buble_list)):
        if buble_list[i] > buble_list[j] :
            buble_list[i], buble_list[j] = buble_list[j], buble_list[i]
print('test git')