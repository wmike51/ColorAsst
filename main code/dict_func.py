import pandas as pd

common_colors_g = ["black", "white", "red", "green", "yellow", "blue", "brown", "orange", "pink", "purple", "gray", "grey"]
common_colors = ["black", "white", "red", "green", "yellow", "blue", "brown", "orange", "pink", "purple", "gray"]

def dict_extraction(dict):
    extracted = pd.DataFrame(columns=["ColorName", 'R', 'G', 'B'])
    temp_index_list =[-1] * len(common_colors_g)
    l = -1

    for index, row in dict.iterrows():
        dict_name = str(row[0]).lower()
        temp_index_list = [-1] * len(common_colors_g)

        for c_index, c_name in enumerate(common_colors_g):
            cn = str(c_name)
            temp_index_list[c_index] = dict_name.find(cn)
                
        largest_index = 0
        for t_index, t_item in enumerate(temp_index_list):
            if t_item > temp_index_list[l] :
                largest_index = t_index

        if  temp_index_list[largest_index] != -1 :
            if largest_index == 11:
                largest_index = 10
            d_row = {'ColorName' : common_colors[largest_index], 'R': row[1], 'G' : row[2], 'B' : row[3]}
            extracted = extracted.append(d_row, ignore_index=True)

    extracted = extracted.reset_index(drop=True)
    return(extracted)

def dict_summary(dict):
    count = [0]*11
    for index, row in dict.iterrows() :
        for j, item in enumerate(common_colors):
            if row[0] == item:
                count[j] += 1

    return count

def conf_accuracy(cm):
    total = 0
    correct_pred = 0
    
    for i, col in enumerate(cm):
        for j, value  in enumerate(col):
            total += value
            if i == j:
                correct_pred += value

    return(correct_pred/total)