from jieba.analyse import *

def extract_keywords(filecontents):
    '''
    此函数用于提取适当数量的中英文关键词
    :param filecontents: 读取到的文本内容（字符串）
    :return: 字典类型，键：中英文关键词 值：出现频次
    '''
    cn_keywords = extract_tags(filecontents, topK=50, withWeight=True)  # 提取中英文关键字
    new_cn_keywords={}  # 创建存储关键词和对应频次的字典
    for i in range(len(cn_keywords)):  # 遍历每一个提取到的关键字
        new_cn_keywords[cn_keywords[i][0]]=cn_keywords[i][1]  # 把关键字调整为键值对格式
    return new_cn_keywords