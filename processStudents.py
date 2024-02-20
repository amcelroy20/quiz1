''' 
*   Professor B would like to know which of his student have a GPA below 3.0.
    To accomplish this, read the file - students.csv into the program. The program
    should evaluate the GPA to see if it is higher or lower than 3.0. If it is,
    then it should be written out to the file - processedStudents.csv. (This file
    already contains headers and the headers should NOT be overwritten.)

*   Create a VE and name it quiz_ve. Install the 3rd party libraries- wordcloud and imageio.
    Make sure your VE is NOT part of your repository. Make sure your .gitignore
    IS part of your repo. The code will produce a heart-shaped wordcloud of the most
    frequently appearing words in the text of Romeo and Juliet.

*   Create a dictionary of each student where the student FULL NAME (proper casing) is the key
    and the GPA is the value. 

*   print out the dictionary

*   print out the corresponding GPA for student - Luke Brazzi

*   push your repo to GitHub. Only your VE should not be in your repo. Everything else should be
    pushed. Submit your Github repo URL in the response field of the quiz.

I have outlined comments for each step of the program. You are
not required to use them but it is provided to help you work
through the logic of the problem.


'''


import csv


# create a file object to open the file in read mode

infile = open('students.csv', 'r')

# create a csv object from the file object

csv_infile = csv.reader(infile)

#skip the header row

next(csv_infile)

#create an outfile object for the pocessed record

outfile = open('processedstudents.csv', 'a')

#create a new dictionary named 'student_dict'

student_dict = {}

#use a loop to iterate through each row of the file

for i in csv_infile:

    #check if the GPA is below 3.0. If so, write the record to the outfile
    
    if float(i[8]) < 3.00:
        outfile.write(f'{i}\n')

    # append the record to the dictionary with the student Full name in proper case 
    # as the Key and the value as the GPA
    
        fullname = i[2].capitalize() + ' ' + i[3].capitalize()

        student_dict[fullname]=i[8]

#print the entire dictionary

print(student_dict)

#Print the corresponding GPA for student 'Luke Brazzi'

print(f"Luke Brazzi's GPA: {student_dict['Luke Brazzi']}")

#close the outfile

outfile.close()



#display the wordcloud
from pathlib import Path
from wordcloud import WordCloud
import imageio.v2 as imageio
import matplotlib.pyplot as plt


text = Path("RomeoAndJuliet.txt").read_text()
mask_image = imageio.imread("mask_heart.png")
wordcloud = WordCloud(colormap="prism", mask=mask_image, background_color="white")
wordcloud = wordcloud.generate(text)
wordcloud = wordcloud.to_file("RomeoAndJulietHeart.png")
plt.imshow(wordcloud)
plt.show()







