




import string
import re
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
from sklearn.metrics import plot_confusion_matrix

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


#function to determine the age of a user in years

def account_length(df , yr_col = "year"):
    grp_data = df.groupby(['user_id','year']).count()
    
    user = 0
    mini = 200000
    maxi = 0
    
    user_record = []
    year_record = []

    for x in grp_data.index:
        #
        if user == x[0]:
            if int(x[1]) <= int(mini):
                mini = int(x[1])
            elif int(x[1]) > int(maxi):
                maxi = int(x[1])

            
        if user != x[0]:
            
            if user != 0:
                year_record.append((int(maxi)-int(mini)))
                user_record.append(int(user))
                user = int(x[0])
                mini = int(x[1])
                maxi = int(x[1])

            else:
                user = int(x[0])
                mini = int(x[1])
                maxi = int(x[1])
           
    return user_record, year_record



punct = set(string.punctuation)

def tokenize_text(text):
    # remove numbers
    text_nonum = re.sub(r'\d+', '', text)
    # remove punctuations and convert characters to lower case
    text_nopunct = "".join([char.lower() for char in text_nonum if char not in punct]) 
    # substitute multiple whitespace with single whitespace
    # Also, removes leading and trailing whitespaces
    text_no_doublespace = re.sub('\s+', ' ', text_nopunct).strip()
    return nltk.word_tokenize(text_no_doublespace)



def remove_short_revs(df,col = 'review'):
    indexNames = []
    sub_5_reviews = []
#enumerate through the cloned_df reviews and find any reviews with less than 15 words
#this is important as there were reviews with simply characters and one words.
    for i,rev in enumerate(df[col]):
        if len(rev)<15:
            indexNames.append(i)
            sub_5_reviews.append(rev)
        
    return df.drop(indexNames)



def score(model, X = None, y = None, text = 'Train'):
    model.fit(X,y)
    print(f'{text} score',model.score(X,y))
    plot_confusion_matrix(model,X,y)