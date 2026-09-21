def show_student():
    name = input("请输入学生姓名：")
    print(f"学生姓名：{name}")
    gender = input("请输入学生性别：")
    print(f"学生性别：{gender}")
    score = float(input("请输入学生成绩："))
    print(f"学生成绩：{score}")
    #组员D：成绩等级判断
    if score >= 90:
        level = "优秀"
    elif score >= 80:
        level = "良好"
    elif score >= 60:
        level = "及格"
    else:
        level = "不及格"
    print(f"成绩等级：{level}")
    clazz = input("请输入学生班级：")
    print(f"学生班级：{clazz}")

if __name__ == "__main__":
    show_student()

