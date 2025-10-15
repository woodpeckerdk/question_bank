from common import QuestionBank

bank = QuestionBank("question_base.csv")

def query_loop():
    while True:
        keyword = input("请输入题干关键字或拼音首字母（exit退出）：").strip().upper()
        if keyword.lower() == 'exit':
            break
        results = bank.search(keyword)
        if results:
            print(f"\n共找到 {len(results)} 条匹配：\n")
            for q in results:
                print(q.full_text)
                print("-" * 40)
        else:
            print("未找到匹配题目。\n")
            bank.add_question()

if __name__ == "__main__":
    query_loop()
