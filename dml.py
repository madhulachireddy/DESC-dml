f = open("C:\\Users\Meghana\Desktop\DML_CREATION.txt")
dic_list = []
final_data = {}
count = 1
for i in f:
    #print(i)

    c = i.split('|')
    c = map(lambda s: s.strip(), c)
    list1 = ['obj_prpt_nm','obj_prpt_dat_type','obj_prpt_len','is_nlbl_flg','default_value']
    final_data = dict(zip(list1, c))
    final_data['delimiter'] = ','
    final_data['obj_prpt_ord_nbr'] = count
    final_data['is_prmy_key_flg'] = 'N'
    count = count+1
    dic_list.append(final_data)
print(dic_list)
