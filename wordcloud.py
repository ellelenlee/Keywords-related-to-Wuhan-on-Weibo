import json
import collections
import jieba.analyse
import matplotlib as mpl
from imageio import imread
from wordcloud import WordCloud

# mpl.use('TkAgg')
import matplotlib.pyplot as plt
from PIL import Image

Image.new("RGB" ,(512,512),(0,0,255)).save("wuhan.png","PNG")

stopword=['微博', '我们', '全文', '...',  '视频', '真的']

def gen_img(texts, img_file):
    data = ' '.join(text for text in texts)
    image_coloring = imread(img_file)
    wc = WordCloud(
        background_color='white',
        mask=image_coloring,
        collocations=False,
        max_words=200,
        stopwords=stopword,
        font_path='/Library/Fonts/STHeiti Light.ttc'
    )
    wc.generate(data)

#     plt.figure()
#     plt.imshow(wc, interpolation="bilinear")
#     plt.axis("off")
#     plt.show()

    wc.to_file(img_file.split('.')[0] + '_wc.png')

if __name__ == '__main__':
    keyword = '武汉'
    mblogs = json.loads(open('result_{}.json'.format(keyword), 'r', encoding='utf-8').read())
    print('微博总数：', len(mblogs))

    words = []
    for blog in mblogs:
        words.extend(jieba.analyse.extract_tags(blog['text']))
    print("总词数：", len(words))

word_counts = collections.Counter(words) 
word_counts_top10 = word_counts.most_common(10) 
print (word_counts_top10)
    
gen_img(words, 'wuhan.png')
