import unittest
import json

from app import create_app

APP= create_app()

class BaseQuestions(unittest.TestCase):

    def setUp(self):
        self.app= create_app("testing")
        self.client=self.app.test_client()

        self.question_1 = {"Question":"What is programming",
                            "Title": "Programming",
                            "Category": "python"}

        self.question_2= {"Question":"What is flask",
                            "Title": "flask",
                            "Category": "python"}

        self.question_3= {"Question":"What is jquery",
                            "Title": "Jquery",
                            "Category": "Javascript"}

        self.question_4= {"Question":"",
                            "Title": "",
                            "Category": ""}

        self.answer_1= {"Answer":"Programming is the process of creating a set of instructions that tell a computer how to perform a task. Programming can be done using a variety of computer 'languages,' such as SQL, Java, Python, and C++."}

        self.questions= [{"Question":"What is programming",
                            "id": 1,
                            "Answers": []},
                            {"Question":"What is flask",
                            "id": 2,
                            "Answers": []},
                            {"Question":"What is jquery",
                            "id": 3,
                            "Answers": []}]
        self.answer_1= {"Answer":"Programming is the process of creating a set of instructions that tell a computer how to perform a task. Programming can be done using a variety of computer 'languages,' such as SQL, Java, Python, and C++." ,
                        "Answer_id": 1,
                        "Accepted":False}

        self.qtn_ans={"Question":"What is programming",
                            "id": 1,
                        "Answers": [{"Answer":"Programming is the process of creating a set of instructions that tell a computer how to perform a task. Programming can be done using a variety of computer 'languages,' such as SQL, Java, Python, and C++." ,
                                    "Answer_id":1,
                                    "Accepted":False}]}

    def tearDown(self):
        self.app.testing =False
        self.app= None

class TestQuestions(BaseQuestions):

    def test_if_no_data(self):
        response= self.client.post("/api/v1/questions", json=self.question_4, content_type= 'application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn("Ask a question", str(response.data))

    def test_user_can_post_question(self):
        response= self.client.post("api/v1/questions", json=self.question_1, content_type= 'application/json')
        self.assertEqual(response.status_code, 201)

    def test_user_can_answer_question(self):
        self.client.post("/api/v1/questions", json= self.question_1, content_type= 'application/json')
        self.client.post("/api/v1/questions/1/answers", json=self.answer_1, content_type= 'application/json')
        pass


if __name__ == '__main__':
    unittest.main()
