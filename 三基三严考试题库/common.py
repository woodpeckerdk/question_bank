import pandas as pd
from pypinyin import lazy_pinyin, Style


class Question:
    def __init__(self, stem, content):
        self.index1 = stem
        self.index2 = self.get_initials(stem).upper()
        self.full_text = f"{stem}\n{content}"

    def get_initials(self, text):
        return ''.join(lazy_pinyin(text, style=Style.FIRST_LETTER))

    def matches(self, keyword):
        return keyword in self.index1 or keyword in self.index2


class QuestionBank:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.df = pd.read_csv(csv_file).fillna("")
        self.questions = self.load_questions()

    def load_questions(self):
        return [Question(row['题干'], row['内容']) for _, row in self.df.iterrows()]

    def save(self):
        self.df.to_csv(self.csv_file, index=False,encoding='utf-8-sig')

    def search(self, keyword):
        return [q for q in self.questions if q.matches(keyword)]

    def add_question(self):
        stem = input("请输入题干：")
        if stem in self.df['题干'].values:
            print("⚠️ 题干重复，未添加。")
            return False
        content = input("请输入选项及答案（统一字符串，可换行）：\n")
        new_row = {'题干': stem, '内容': content}
        self.df = pd.concat([self.df, pd.DataFrame([new_row])], ignore_index=True)
        self.questions.append(Question(stem, content))
        self.save()
        print("✅ 添加成功。")
        return True

    def delete_question(self):
        stem = input("请输入要删除的题干：")
        if stem not in self.df['题干'].values:
            print("⚠️ 未找到该题目。")
            return False
        self.df = self.df[self.df['题干'] != stem]
        self.save()
        print("✅ 已删除。")
        return True

    def modify_question(self, old_stem, new_stem, new_content):
        if old_stem not in self.df['题干'].values:
            print("⚠️ 原题干未找到。")
            return False
        self.df.loc[self.df['题干'] == old_stem, ['题干', '内容']] = [new_stem, new_content]
        self.save()
        print("✅ 已修改。")
        return True

