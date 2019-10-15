#Importing libraries
import nltk
from nltk.corpus import inaugural
from nltk.stem import PorterStemmer
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords
import xlwt
from xlwt import Workbook

def main():
    sample=inaugural.raw('2009-Obama.txt')
    tokens=nltk.word_tokenize(sample)
    words=[w.lower() for w in tokens if w.isalpha()]#remove punctuations and lowercase
    stop_words=set(stopwords.words('english'))
    filtered=[w for w in words if not w in stop_words]#remove stop words

    ps=PorterStemmer()
    ls=LancasterStemmer()
    sb=SnowballStemmer('english')

    porter=[]
    lancaster=[]
    snowball=[]
    for data in filtered:
        porter.append(ps.stem(data))
        lancaster.append(ls.stem(data))
        snowball.append(sb.stem(data))

    wb=Workbook()
    sheet=wb.add_sheet('Stemming')
    sheet.write(0,1,"Word")
    sheet.write(0,2,"Porter")
    sheet.write(0,3,"Lancaster")
    sheet.write(0,4,"Snowball")

    for i in range(len(filtered)):
        sheet.write(i+1,1,filtered[i])
        sheet.write(i+1,2,porter[i])
        sheet.write(i+1,3,lancaster[i])
        sheet.write(i+1,4,snowball[i])

    wb.save("ObamaStem.xls")

if __name__ == '__main__':
    main()
