import docx2txt


def read_word():
    a = docx2txt.process(r'C:\Users\Siddhesh\Desktop\Data_Science\read_data.docx')
    print(a)


read_word()
