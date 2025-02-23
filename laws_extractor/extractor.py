from PyPDF2 import PdfReader
from utils import pdfTextExtractor, extractQuestions
import pandas as pd

OAB38 = "oabTests/OAB-38-resolution.pdf"
OAB39 = "oabTests/OAB-39-resolution.pdf"
OAB40 = "oabTests/OAB-40-resolution.pdf"
OAB41 = "oabTests/OAB-41-resolution.pdf"

filePath = OAB41
pdf = PdfReader(filePath)
oabTextNumber = filePath.split('/')[1].split('-')[1]

pdfTextExtractor(pdf, f"extractedText/oab{oabTextNumber}extractedText.txt")
questionAndAnswerList = extractQuestions(f"extractedText/oab{oabTextNumber}extractedText.txt")

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
