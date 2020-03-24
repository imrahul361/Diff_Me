import filecmp

fold1 = raw_input("Enter 1st folder path: ")
fold2 = raw_input("Enter 2nd folder path: ")
comparison = filecmp.dircmp(fold1,fold2)
common_files = ', '.join(comparison.common) 
fold1_left_files = ', '.join(comparison.left_only)
fold2_left_files = ', '.join(comparison.right_only)

report_path = raw_input("Where you want to save the report? ")
with open(report_path + 'fold_diff.txt','w') as folder_report:
    folder_report.write("Common Files:"+ common_files+'\n')
    folder_report.write('\n'+"Only in 1st Folder: "+ fold1_left_files)
    folder_report.write('\n'+"Only in 2nd Folder: "+ fold2_left_files)

print("Successfully Done\n")