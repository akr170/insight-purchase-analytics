import sys

pdts = sys.argv[2]
ordr = sys.argv[1]
outf = sys.argv[3]
# The following section of the code reads the file 'products.csv' and stores the 
# product and its department in a dictionary product_info as (key, value) pair
# -------------------------------------------------------
fh = open(pdts, 'r', encoding="utf8")

product_info=dict()
skip1=True

for line in fh:
    if skip1:
        skip1 = False
    else:
        #temp = line
        #temp = temp.strip()
        temp = line.split(',')
        product_info[int(temp[0])] = int(temp[-1])

fh.close()
# -------------------------------------------------------



# The following section of the code reads the file 'order_products.csv' and stores the 
# department_id, number_of_orders, and number_of_reorders
# in a dictionary dept_info as 
# dept_info[dept] = [dept, number_of_orders, number_of_reorders]
# Later in the code number_of_first_orders is calculated as (number_of_orders - number_of_reorders)
# -------------------------------------------------------
dept_info = dict()
skip1 = True

with open(ordr,'r', encoding="utf8") as fh1:
    for line in fh1:
        if skip1:
            skip1 = False
        else:
            #temp = line
            #temp = temp.strip()
            temp = line.split(',')
            try:
                dept = product_info[int(temp[1])]
            except:
                print('Could not locate department_id of product '+temp[1]+'.')
                print('Product '+temp[1]+' from file order_products.csv does not have an entry in products.csv file.')
                print('Program is exiting!')
                quit()
            try:
                dept_info[dept][1] = dept_info[dept][1] + 1
            except:
                dept_info[dept] = [dept, 1, 0]
            dept_info[dept][2] = dept_info[dept][2] + int(temp[-1])
# -------------------------------------------------------


# The keys from the dept_info are then listed and sorted so that a sorted list can be built
sorted_dept_keys = sorted(list(dept_info.keys()))

# The following code builds the formatted output text and then outputs in report.csv
# The first two lines ensures that the old output file, if it exists, gets deleted
fh2 = open(outf,'w')
fh2.close()

fh2 = open(outf,'a')
otpt = 'department_id,number_of_orders,number_of_first_orders,percentage'
fh2.write(otpt)
for i in range(len(sorted_dept_keys)):
    temp = dept_info[sorted_dept_keys[i]]
    otpt = '\n' + str(temp[0]) + ',' + str(temp[1]) + ',' + str(temp[1] - temp[2]) + ',' + '{:.2f}'.format(float(temp[1] - temp[2])/float(temp[1]))
    fh2.write(otpt)


fh2.close()
