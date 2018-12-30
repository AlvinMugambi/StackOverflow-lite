import unittest
import os
import json
from app import create_app, db

class QuestionsTestcase(unittest.TestCase):

    def setUp(self):
        self.app= create_app(config_name="testing")
        self.client= self.app.test_client
        self.question= {
            'Question':"Are we working?",
            }

        with self.app.app_context():
            db.create_all()

    def test_question_creation(self):

        res= self.client().post('/api/v2/questions', data=self.question)
        self.assertEqual(res.status_code, 201)
        self.assertIn('Your question', str(res.data))

    def test_api_can_get_all_questions(self):

        res= self.client().post('/api/v2/questions', data=self.question)
        self.assertEqual(res.status_code, 201)
        res= self.client().get('/api/v2/questions')
        self.assertEqual(res.status_code, 200)
        self.assertIn('Are we working', str(res.data))

    def test_api_can_get_question_by_id(self):
        rv= self.client().post('/api/v2/questions', data= self.question)
        self.assertEqual(rv.status_code, 201)
        result_in_json= json.loads(rv.data.decode('utf-8').replace("'","\""))
        result= self.client().get('/api/v2/questions/{}'.format(result_in_json['id']))
        self.assertEqual(result.status_code, 201)

    def test_question_deletion(self):
        rv =self.client().post('/api/v2/questions', data=self.question)
        self.assertEqual(rv.status_code, 200)
        res= self.client().delete('/api/v2/questions/1')
        self.assertEqual(res.status_code, 200)
        result= self.client().get('/api/v2/questions/1')
        self.assertEqual(result.status_code, 404)

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

if __name__== '__main__':
    unittest.main()
