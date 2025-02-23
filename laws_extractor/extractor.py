from PyPDF2 import PdfReader
from utils import pdfTextExtractor, extractQuestions
import pandas as pd

OAB38 = "oabTests/OAB-38-resolution.pdf"
filePath = OAB38
pdf = PdfReader(filePath)

##descomentar essa linha apenas para sobreescrever o arquivo de texto.
pdfTextExtractor(pdf, "extractedText/oab38extractedText.txt")
questionAndAnswerList = extractQuestions("extractedText/oab38extractedText.txt")

questionsList = []
commentList = []
legalPrinciples = []
for questionAndAnswer in questionAndAnswerList:
    questionsList.append(questionAndAnswer["question"])
    commentList.append(questionAndAnswer['comment'])
    legalPrinciples.append('Não preenchido')


df = pd.DataFrame({"question":questionsList, "comment":commentList, "legalPrinciples": legalPrinciples})
csvName = filePath.split('/')[1].split('.')[0]

df.to_csv(f'csv/{csvName}.csv', index=False)
df.to_excel(f'excel/{csvName}.xlsx', index=False, engine="openpyxl")

