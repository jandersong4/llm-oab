import re

def pdfTextExtractor(pdf, txtFilePath):
    allText = ''
    pageIndex = 0

    for page in pdf.pages:
        if pageIndex > 1:
            allText += page.extract_text()
        pageIndex += 1

    with open(txtFilePath, "w", encoding="utf-8") as f:
        f.write(allText)


def extractQuestions(textFilePath):

    text = open(textFilePath, "r").read()

    pattern = r"(QUESTÃO\s+\d+\.?\s+.*?)(Comentários\s+.*?)(?=(QUESTÃO\s+\d+\.?|$))"

    matches = re.findall(pattern, text, re.DOTALL)
    
    questions = [
        {"question": match[0].strip(), "comment": match[1].strip()}
        for match in matches
    ]
    return questions
