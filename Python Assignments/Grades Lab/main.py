tsv_input_file = 'StudentInfo.tsv'

tsv_dict = {}
scores = []
midterm_1_avg = 0
midterm_2_avg = 0
final = 0

# Read the input tsv file and add the content to tsv_dict
with open(tsv_input_file, 'r') as file:
    readfile = file.readlines()
    for row,content in enumerate(readfile):
        tsv_dict[row] = content.split('\t')

# Calculate letter grade averages for each student    
for key,value in tsv_dict.items():
    value[-1] = value[-1][:-1]
    nums_to_avg = value[-3:]
    total = 0
    for num in nums_to_avg:
        total = total + int(num)
    avg = total / 3
    grade_letter = ''
    if avg >= 90:
        grade_letter = 'A'
    elif 90 > avg >= 80:
        grade_letter = 'B'
    elif 80 > avg >= 70:
        grade_letter = 'C'
    elif 70 > avg >= 60:
        grade_letter = 'D'
    elif 60 > avg:
        grade_letter = 'F'
    value.append(f'{grade_letter}\n')

# Add the scores to a list
for element in tsv_dict.values():
    scores.append(element[2:5])

# Calculate midterm 1, midterm 2, and final averages for all students
for student_scores in scores:
    midterm_1_avg = midterm_1_avg + int(student_scores[0])
    midterm_2_avg = midterm_2_avg + int(student_scores[1])
    final = final + int(student_scores[2])

midterm_1_avg = f'{midterm_1_avg / len(scores):.2f}'
midterm_2_avg = f'{midterm_2_avg / len(scores):.2f}'
final = f'{final / len(scores):.2f}'

# Create a new document and write the original information but add the letter grade and test averages
with open('report.txt', 'w') as report:
    for name_scores_grade in tsv_dict.values():
        report.write('\t'.join(name_scores_grade))
    report.write('\n')
    report.write(f'Averages: midterm1 {midterm_1_avg}, midterm2 {midterm_2_avg}, final {final}\n')