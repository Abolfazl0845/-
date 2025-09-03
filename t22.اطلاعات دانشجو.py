class Human:
    def init(self, name="", age=0, height=0.0, weight=0.0):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def input_human_data(self):
        self.name = input("نام را وارد کنید: ")
        self.age = int(input("سن را وارد کنید: "))
        self.height = float(input("قد را وارد کنید (به سانتی‌متر): "))
        self.weight = float(input("وزن را وارد کنید (به کیلوگرم): "))

    def display_human_info(self):
        print("\n-----------------------------")
        print("اطلاعات شخصی:")
        print(f"نام: {self.name}")
        print(f"سن: {self.age}")
        print(f"قد: {self.height} سانتی‌متر")
        print(f"وزن: {self.weight} کیلوگرم")


class Student(Human):
    def init(self, name="", age=0, height=0.0, weight=0.0, student_id="", major=""):
        super().init(name, age, height, weight)
        self.student_id = student_id
        self.major = major

    def input_student_data(self):
        self.input_human_data()
        self.student_id = input("شماره دانشجویی را وارد کنید: ")
        self.major = input("رشته تحصیلی را وارد کنید: ")

    def display_student_info(self):
        self.display_human_info()
        print("\nاطلاعات دانشجویی:")
        print(f"شماره دانشجویی: {self.student_id}")
        print(f"رشته تحصیلی: {self.major}")
        print("-----------------------------")


student = Student()
student.input_student_data()
print("\nدر حال نمایش اطلاعات کامل دانشجو...")
student.display_student_info()