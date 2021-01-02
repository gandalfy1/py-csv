def remove_file_line(file_pathname, file_line_number):
    
    #read all of the lines and save it in a list
    with open(file_pathname, "r") as csv_file:
        file_lines = csv_file.readlines()

     # if line number is in valid return
    if file_line_number < 1 or file_line_number > len(file_lines):
        return
    
    # build new file content
    del file_lines[file_line_number-1]

    result = ""        
    for line in file_lines:
        result += line
    
    # replace file content with new 
    with open(file_pathname,"w") as csv_file:
        csv_file.write(result)
        

remove_file_line("./mock.csv",2)