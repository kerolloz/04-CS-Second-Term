import re


def format_mcq(arr, ans):
    ans = ans.strip()[-1]
    indexOfAnswer = ord(ans) - ord('a')
    arr[indexOfAnswer] = "**{0}**".format(arr[indexOfAnswer])
    arr = "  \n  ".join([re.sub(r'\)', '.', i) for i in arr])
    return arr


def format_question(q):
    return re.sub('QUESTION: ', '', q)


def make_question(q):
    q["mcq"] = format_mcq(q['mcq'], q['answer'])
    q["question"] = format_question(q['question'])
    return """- {question}

  {mcq}

  ```
  {answer}
  {explanation}
  ```
""".format(question=q['question'], mcq=q['mcq'], answer=q['answer'], explanation=q['explanation'])


with open('text.txt') as file:
    i = 0
    questions = []
    questionData = {"mcq": []}
    mcqAnswerPattern = re.compile(r'^[a-z]\) .*$')  # a) answer 1
    for line in file:
        line = line.strip()
        if line.startswith('QUESTION'):
            questionData['question'] = line
        elif line.startswith('ANSWER'):
            questionData['answer'] = line
        elif line.startswith('EXPLANATION'):
            questionData['explanation'] = line
            # add the data to the questions array
            questions.append(questionData)
            questionData = {"mcq": []}  # new question
            i += 1
        elif mcqAnswerPattern.match(line):
            questionData['mcq'].append(line)

    for q in questions:
        # print(q)
        print(make_question(q))

    # print(len(questions))
