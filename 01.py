class PyStudent():
    name = None
    age = 18
    course = 'python'
    def doHomework(self):
        print('我在做作业')
        return None


yueyue = PyStudent()
print(yueyue.name)
print(yueyue.age)
yueyue.doHomework()