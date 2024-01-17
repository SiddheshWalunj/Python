import docx2txt


file_path = r'C:\Users\Siddhesh\Desktop\Data_Science\read_data.docx'


def read_word(file):
    a = docx2txt.process(file)
    print(a)


read_word(file_path)
