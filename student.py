def show_student():
    name = input("请输入学生姓名：")
    print(f"学生姓名：{name}")
    gender = input("请输入学生性别：")
    print(f"学生性别：{gender}")
    score = float(input("请输入学生成绩："))
    print(f"学生成绩：{score}")
    clazz = input("请输入学生班级：")
    print(f"学生班级：{clazz}")

if __name__ == "__main__":
    show_student()
