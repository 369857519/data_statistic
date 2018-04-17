import unicodecsv


def read_csv(filename):
    with open(filename, 'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)

localpath='/Users/qilianshan/Documents/studySpace/python/dataAnalysis'
enrollments = read_csv('./enrollments.csv')
daily_engagement = read_csv('./daily-engagement.csv')
project_submissions = read_csv('./project-submissions.csv')


### For each of these three tables, find the number of rows in the table and
### the number of unique students in the table. To find the number of unique
### students, you might want to create a set of the account keys in each table.
def getLen(list, keyname):
    res = list;
    unique_students = set();
    for stu in res:
        unique_students.add(stu[keyname])
    return len(res), len(unique_students)


enrollLen = getLen(enrollments, 'account_key')
enrollment_num_rows = enrollLen[0]  # Replace this with your code
enrollment_num_unique_students = enrollLen[1]  # Replace this with your code

engagellLen = getLen(daily_engagement, 'acct')
engagement_num_rows = engagellLen[0]  # Replace this with your code
engagement_num_unique_students = engagellLen[1]  # Replace this with your code

for engage_record in daily_engagement:
    engage_record['account_key']=engage_record['acct']
    del[engage_record['acct']]
# print(enrollments[0]['acct'])
print daily_engagement[0]['account_key'];

subMissionLen = getLen(project_submissions, 'account_key')
submission_num_rows = subMissionLen[0]  # Replace this with your code
submission_num_unique_students = subMissionLen[1]  # Replace this with your code