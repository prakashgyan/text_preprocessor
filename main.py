import pandas as pd
from text_prepcocessing import celan_sentences

if __name__ == "__main__":
    
    df1 = pd.read_json('data\Sarcasm_Headlines_Dataset_v2.json',lines=True)
    df2 = pd.read_json('data\Sarcasm_Headlines_Dataset.json',lines=True)

    print(celan_sentences(["whats tehe ''#wtf #LOWL ##insta heck ? is  ankitrai326@gmail.com  ankitrai326.com hoing &^% "],stopwords=['is', 'this', 'it']))
