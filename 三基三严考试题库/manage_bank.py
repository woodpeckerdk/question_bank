from common import QuestionBank

bank = QuestionBank("question_base.csv")

def manage_menu():
    while True:
        print("\n--- 题库管理菜单 ---")
        print("1. 添加题目")
        print("2. 删除题目")
        print("3. 修改题目")
        print("4. 退出")
        choice = input("请选择操作（1-4）: ").strip()

        if choice == '1':
            bank.add_question()
        elif choice == '2':
            bank.delete_question()
        elif choice == '3':
            old_stem = input("原题干：")
            new_stem = input("新题干：")
            new_content = input("新内容（统一字符串，可换行）：\n")
            bank.modify_question(old_stem, new_stem, new_content)
        elif choice == '4':
            print("退出题库管理。")
            break
        else:
            print("无效选择，请重新输入。")

if __name__ == "__main__":
    manage_menu()
