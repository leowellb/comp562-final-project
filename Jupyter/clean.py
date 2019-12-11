import csv


def clean_drugs():

    whole_final = []
    sub_final = []
    info_legal_index = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 17, 18, 19, 25, 29]
    age = {"-0.95197": "18-24", "-0.07854": "25-34", "0.49788": "35-44", "1.09449": "45-54",
           "1.82213": "55-64", "2.59171": "65+"}
    gender = {"0.48246": "Female", "-0.48246": "Male"}
    education = {"-2.43591": "Left before 16", "-1.73790": "Left at 16", "-1.43719": "Left at 17",
                 "-1.22751": "Left at 18", "-0.61113": "Some College", "-0.05921": "Professional Diploma",
                 "0.45468": "University Degree", "1.16365": "Masters Degree", "1.98437": "Doctorate Degree"}
    country = {"-0.09765": "Australia", "0.24923": "Canada", "-0.46841": "New Zealand", "-0.28519": "Other",
               "0.21128": "Republic of Ireland", "0.96082": "UK", "-0.57009": "USA"}
    ethnicity = {"-0.50212": "Asian", "-1.10702": "Black", "1.90725": "Black/Asian", "0.12600": "White/Asian",
                 "-0.22166": "White/Black", "0.11440": "Other", "-0.31685": "White"}

    with open("drug_consumption.txt") as drugs:

        lines = [line.rstrip('\n') for line in drugs]

    for line in lines:
        temp = []
        temp2 = []
        line = line.split(',')
        illicit = False
        for index in range(len(line)):
            temp2.append(line[index])
            if index in info_legal_index:
                if index == 1:
                    temp.append(age[str(line[index])])
                elif index == 2:
                    temp.append(gender[str(line[index])])
                elif index == 3:
                    temp.append(education[str(line[index])])
                elif index == 4:
                    temp.append(country[str(line[index])])
                elif index == 5:
                    temp.append(ethnicity[str(line[index])])
                else:
                    temp.append(line[index])
            else:
                if line[index] != 'CL0':
                    illicit = True
        if illicit:
            temp.append(1)
        else:
            temp.append(0)
        whole_final.append(temp2)
        sub_final.append(temp)

    with open('cleaned_drug.csv', 'w', newline='') as f:

        attribute = ['ID', 'Age', 'Gender', 'Education', 'Country', 'Ethnicity', 'Nscore', 'Escore', 'Oscore', 'Ascore',
                     'Cscore', 'Impulsive', 'SS', 'Alcohol', 'Caffeine', 'Cannabis', 'Chocolate', 'Legal High',
                     'Nicotine', 'Illicit Drugs']
        writer = csv.writer(f)
        writer.writerow(attribute)

        for lines in sub_final:
            writer.writerow(lines)


clean_drugs()




