from survey import AnonymousSurvey

#Define a question, and make a survey.
question = "What language did you first learn to speak?"
langugage_survey = AnonymousSurvey(question)

#Show the question, and store the responses to the question.
langugage_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response.lower() == 'q':
        break
    langugage_survey.store_response(response)

#Show the survey results.
print("\nThank you to everyone who participated in the survey!")
langugage_survey.show_results()