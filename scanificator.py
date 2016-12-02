import xlwt #Module for spreadsheet handling

ipad_dict={}

# Replace the 7's with the number of characters expected
def get_stu():
    input_data1 = str()
    while len(input_data1) < 7 or len(input_data1) > 7:
        input_data1 = str(raw_input('Scan student ID: '))
        if input_data1 == 'save':
            print_xl()
        elif len(input_data1) < 7 or len(input_data1) > 7:
            print('7 digits expected.')
        else:
            return(input_data1)

# Replace the 5's with the number of characters expected
def get_ipad():
    input_data2 = str()
    while len(input_data2) < 5 or len(input_data2) > 5:
        input_data2 = str(raw_input('      Scan iPad: '))
        if input_data2 == 'save':
            print_xl()
        elif len(input_data2) < 5 or len(input_data2) > 5:
            print('5 digits expected.')
        else:
            return(input_data2)

# Print ipad_dict to spreadsheet and exit
def print_xl():
    import xlwt 

    book = xlwt.Workbook(encoding="utf-8")

    sheet1 = book.add_sheet("Sheet 1")

    sheet1.write(0, 1, "ipad")
    sheet1.write(0, 0, "Student")

    i=1 #start writing on line

    for k, v in ipad_dict.items():
        i = i+1
        sheet1.write(i, 0, k)
        sheet1.write(i, 1, v)


    file_name = str(raw_input('filename?: '))
    book.save(file_name + ".xls")
    exit()

print '+-------------------------------+'
print '|          SCANIFICATOR         |'
print '+-------------------------------+'
print '| Instructions:                 |'
print '| 1. Scan things, press enter   |'
print '| 2. Type "save", press enter   |'
print '| 3. Name the file, press enter |'
print '+-------------------------------+'
    
while True:    
    st=get_stu()
    ip=get_ipad()
    ipad_dict[st]=ip
    print '--------------------'
    print ' Student ID:', st
    print 'iPad Number:', ip
    print '--------------------'
