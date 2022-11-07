from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

class Chat_T:
    chatbot: None

    def __init__(self):
        self.chatbot = ChatBot("ChatBot")
    # Training with Personal Ques & Ans
        conversation = [
            "Hello",
            "Hi there!",
            "How are you doing?",
            "I'm doing great.",
            "You're welcome.",
            "who Developed you",
            "NLP class",
            "Wonderful, How's the weather today",
            "It's lovely outside"
            "Can you look for a good Sushi place in zip code 46285?"
            "Ofcourse. I found one on Washington St. with great reviews."      
        ]
        trainer = ListTrainer(self.chatbot)
        trainer.train(conversation)

    def chat(self, t1):
        response = self.chatbot.get_response(t1)
        return response