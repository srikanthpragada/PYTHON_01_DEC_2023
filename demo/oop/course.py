class Course:
    # class attribute or static attribute
    taxrate = 12

    @staticmethod
    def settaxrate(newrate):
        Course.taxrate = newrate

    # Constructor
    def __init__(self, title, duration=36, fee=5000):
        # Object attributes
        self.title = title
        self.duration = duration
        self.fee = fee

    # Methods
    def getnetfee(self):
        return self.fee + self.fee * Course.taxrate // 100

    def setduration(self, duration):
        self.duration = duration

    def show(self):
        print('Title    : ', self.title)
        print('Duration : ', self.duration)
        print('Fee      : ', self.fee)


Course.settaxrate(15)  # invoke static method using classname
# create objects
c1 = Course("Java SE")  # invoke  __init__()
c1.show()  # invoke method


print(c1.getnetfee())
c1.setduration(40)

c2 = Course("Python", 36, 6000)

l = [10, 20]
l.append(30)
