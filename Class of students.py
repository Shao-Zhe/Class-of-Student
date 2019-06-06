class CalUtils:

    def __init__(self):
        self.name = []
        self.height = []
        self.total_student_count = 0
        self.total_student_height = 0.0


    def calAvgHeight(self):

      file = open('listOfStudentHeight.txt', 'r')

      for line in file.readlines():
        data = line.split('\t')
        self.name.append(data[0])
        self.height.append(float(data[1]))

      self.total_student_count = len(self.name)

      self.total_student_height = sum(self.height)

      avg_height = self.total_student_height / self.total_student_count


      file.close()

      print(round(avg_height, 2))


    def main(self):
      input_new_user = input("Do you want to input new student name? Y/N: ")

      if input_new_user == 'Y' :
        file = open('listOfStudentHeight.txt', 'a')
        name = input('Enter a name: ')
        height = input('Enter height: ')
        file.write(name + '\t' + height)
          
      else:

        exit()

      file.close()


      file = open('listOfStudentHeight.txt', 'r')

      for line in file.readlines():
        data = line.split('\t')
        self.name.append(data[0])
        self.height.append(float(data[1]))

      self.total_student_count = len(self.name)

      self.total_student_height = sum(self.height)

      new_avg_height = self.total_student_height / self.total_student_count


      file.close()

      print(round(new_avg_height, 2))

student = CalUtils()
student.calAvgHeight()
student.main()

