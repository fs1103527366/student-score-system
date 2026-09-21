def show_student():
    name = input("请输入学生姓名：")
    print(f"学生姓名：{name}")
    score = float(input("请输入学生成绩："))
    print(f"学生成绩：{score}")
    # 组员B新增代码
    clazz = input("请输入学生班级：")
    print(f"学生班级：{clazz}")

if __name__ == "__main__":
    show_student()
