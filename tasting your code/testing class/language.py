from a_class_to_test import anonymous
#define a question and make a survey
question="what language did you first learn to speak?"
language_survey=anonymous(question)
#show the question and store responses to the question.
language_survey.show_question()
print("type q at any time to quit")  
while True:
    response=input("language: ")
    if response=="q":
        break
    language_survey.store_response(response)
#show the survey result:
print("here is the result of the survey:-")
language_survey.show_result()