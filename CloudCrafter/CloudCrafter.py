from wordcloud import WordCloud
import matplotlib.pyplot as plt
import fitz
from docx import Document
from extract_keywords import *
from error_message import *

print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
print("* * * * * * * * * * * * * * * * 欢迎来到词云工匠~~ * * * * * * * * * * * * * * * *")
print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
print("* * * * * * 本产品致力于为您提供优质的词云生成功能， 满足您从文本到词云的一切需求 * * * * * *")
print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
print("* * * * * * * * * * * 本产品支持输入的文本类型有 pdf，docx，txt * * * * * * * * * * *")
print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
print("*温馨提示：图片型pdf暂时不支持生成词云哦~")
while True:
    filepath=input("请输入要生成词云的文件路径(退出程序请输入0)：").strip('"')  # 读取要生成词云的文件路径
    filepath=filepath.replace('\\','\\\\')  # 确保路径的有效性
    filetype=filepath.split('.')[-1]  # 获取文件类型
    if filetype=='0':  # 如果输入0，则退出程序
        exit()
    with open('D:\\Desktop\\CloudCrafter\\stopword_all.txt',mode='r',encoding='utf-8') as f:
        stop_words=f.readlines()  # 读取停用词库
        for i in range(len(stop_words)):
            stop_words[i]=stop_words[i].strip('\n')  # 按换行符分割出每一个停用词
    stop_words_set=set(stop_words)  # 将停用词存储到集合中
    if filetype=='txt':  # 处理txt类型的文本
        try:
            with open(filepath,mode='r',encoding='utf-8',errors='ignore') as f:
                filecontents=f.read()  # 读取文本内容
                filecontents=filecontents.replace('\n',' ')  # 初步处理文本内容
        except:
            show_error()  # 如果读取文件失败，则进行异常处理
            continue
        keywords_dic=extract_keywords(filecontents)  # 提取关键词，并将其存储在字典中
        # 创建一个词云实例化对象，并设置属性
        wordcloud=WordCloud(font_path='D:\\Desktop\\CloudCrafter\\simhei.ttf',width=400,height=500,max_words=500,
                            background_color='white',stopwords=stop_words_set).fit_words(keywords_dic)
        plt.figure(figsize=(8,7),facecolor=None)  # 创建一个绘图窗口，设置窗口大小和背景色
        plt.imshow(wordcloud)  # 设置为在窗口上显示词云图像
        plt.axis("off")  # 设置为不显示坐标轴
        plt.tight_layout(pad=0)  # 自动调整子图参数
        plt.show()  # 显示绘制的词云图像
    elif filetype=='pdf':  # 处理pdf类型的文本
        pdf_text=''
        try:
            pdf_file = fitz.open(filepath)  # 打开pdf文件
            num_pages = pdf_file.page_count  # 获取pdf文件的页数
            for i in range(num_pages):  # 遍历pdf文件的每一页
                page = pdf_file.load_page(i)  # 加载文件的当前页
                text = page.get_text()  # 提取当前页的文本内容
                text = text.replace('\n', ' ')
                pdf_text += text  # 对提取到的文本进行初步处理
        except:
            show_error()  # 如果读取文件失败，则进行异常处理
            continue
        keywords_dic = extract_keywords(pdf_text)  # 提取关键词，并将其存储在字典中
        # 创建一个词云实例化对象，并设置属性
        wordcloud = WordCloud(font_path='D:\\Desktop\\CloudCrafter\\simhei.ttf', width=400, height=500, max_words=500,
                              background_color='white',stopwords=stop_words_set).fit_words(keywords_dic)
        plt.figure(figsize=(8, 7), facecolor=None)  # 创建一个绘图窗口，设置窗口大小和背景色
        plt.imshow(wordcloud)  # 设置为在窗口上显示词云图像
        plt.axis("off")  # 设置为不显示坐标轴
        plt.tight_layout(pad=0)  # 自动调整子图参数
        plt.show()  # 显示绘制的词云图像
    elif filetype=='docx':  # 处理docx类型的文本
        doc_contents=''
        try:
            doc_file = Document(filepath)  # 打开现有的Word文档
            for paragraph in doc_file.paragraphs:  # 遍历并处理文档中的段落
                doc_contents=doc_contents+paragraph.text
        except:
            show_error()  # 如果读取文件失败，则进行异常处理
            continue
        keywords_dic = extract_keywords(doc_contents)  # 提取关键词，并将其存储在字典中
        # 创建一个词云实例化对象，并设置属性
        wordcloud = WordCloud(font_path='D:\\Desktop\\CloudCrafter\\simhei.ttf', width=400, height=500, max_words=500,
                              background_color='white',stopwords=stop_words_set).fit_words(keywords_dic)
        plt.figure(figsize=(8, 7), facecolor=None)  # 创建一个绘图窗口，设置窗口大小和背景色
        plt.imshow(wordcloud)  # 设置为在窗口上显示词云图像
        plt.axis("off")  # 设置为不显示坐标轴
        plt.tight_layout(pad=0)  # 自动调整子图参数
        plt.show()  # 显示绘制的词云图像
    else:
        print("对不起，您输入的文件格式暂不支持，请您重新输入！")  # 处理输入文件格式不支持的情况
        continue
