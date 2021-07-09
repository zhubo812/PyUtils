
def printList(datalist = []):
    for i in range(len(datalist)):
        print(datalist[i] )

def mergeList(list1, list2 = []):
    if len(list1) == 0:
        return list2
    if len(list2) == 0:
        return list1
    list3 = []
    for list1_i in range(len(list1)):
        for list2_i in range(len(list2)):
            list3_item = str(list1[list1_i]) + '-' + str(list2[list2_i])
            list3.append(list3_item)
    return list3

def row2columnList(datalist = []):
    list_cr = [[]]
    for col in range(len(datalist[0])):
        list_tmp = []
        for row in range(len(datalist)):
            list_tmp.append(datalist[row][col])
        list_cr.append(list_tmp)
    return list_cr

def traversalPath(datalist = []):
    list_tmp = []
    for row in range(len(datalist)):
        list_tmp = mergeList(list_tmp, datalist[row])
    return list_tmp

if __name__ == '__main__':
    M = [['a1', 'b1', 'c1', 'd1', 'e1', 'e1', 'e1'] ,
         ['a2', 'b2', 'c2', 'd2', 'e2', 'e1', 'e1'] ,
         ['a2', 'b2', 'c2', 'd2', 'e2', 'e1', 'e1'],
         ['a3', 'b3', 'c3', 'd3', 'e3', 'e1', 'e1']]
    M_tmp = row2columnList(M)
    tp_list = traversalPath(M_tmp)
    printList(tp_list)
    print(len(tp_list) )
