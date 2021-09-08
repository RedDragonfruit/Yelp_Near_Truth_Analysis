




import string
import re
import matplotlib.pyplot as plt
import seaborn as sns

def text_cleaning(text):
    '''
    lowercase, remove text in square brackets,remove links,remove special characters
    and remove words containing numbers.
    '''
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub("\\W"," ",text) # remove special chars
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    
    return text


#Plot function
def sns_barplot(x,y=None,df=None,start = 1,grid = True, title = None, x_label = None, y_label = None,color_set ='Set1'):
    len(x)
    fig, ax = plt.subplots(figsize = (10,10))
    sns.set(style='darkgrid')
    
    color = sns.color_palette(color_set)
    
    ax.grid (grid)
    
    
    if df == None and type(x) is list:
        ax = sns.barplot(x = x, y = y, palette = color)
    #elif y == None:
    #    pass
    plt.title(title,size = 20)
    plt.xlabel(x_label, size = 15)
    plt.ylabel(y_label, size = 15)
    i = 0
    labels = []
    count = []
    
    while i < len(x):
        labels.append(i+start)
        count.append(0+i)
        i+=1
    
    plt.xticks(count,labels, size = 15);
