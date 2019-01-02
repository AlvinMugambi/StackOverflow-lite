import unittest
import json

from app import create_app

class UserBaseTest(unittest.TestCase):
    def setUp(self):
        self.app= create_app()
        self.client=self.app.test_client()

        self.user1= {"Username":"Alvomug",
                    "Email":"alvo@gmail.com",
                    "Password":"Al20asdf",
                    "Confirm_Password":"Al20asdf"}

        self.user2= {"Username":"DarkVader",
                    "Email":"darkvader@gmail.com",
                    "Password":"LordVader1",
                    "Confirm_Password":"LordVader1"}

        self.user3= {"Username":"ObiWan",
                    "Email":"canobi@gmail.com",
                    "Password":"theForce1",
                    "Confirm_Password":"theForce1"}

        self.user_empty_data= {"Username":"",
                    "Email":"",
                    "Password":"",
                    "Confirm_Password":""}

        self.user_pass_dont_match= {"Username":"tash",
                    "Email":"tash@gmail.com",
                    "Password":"Tashito1",
                    "Confirm_Password":"Tash1"}

        self.user_invalid_email= {"Username":"alvo",
                    "Email":"alvo.com",
                    "Password":"A3adcsdcaa",
                    "Confirm_Password":"A3adcsdcaa"}

        self.user_invalid_email2= {"Username":"alvo",
                    "Email":"alvo@gmail",
                    "Password":"A3adcsdcaa",
                    "Confirm_Password":"A3adcsdcaa"}

        self.user_invalid_password= {"Username":"alvo",
                    "Email":"alvoefefS@gmail.com",
                    "Password":"A3a",
                    "Confirm_Password":"A3a"}

        self.user_invalid_password1= {"Username":"alvo",
                    "Email":"alvoqweda@gmail.com",
                    "Password":"122435645",
                    "Confirm_Password":"122435645"}

        self.user_invalid_password2= {"Username":"alvo",
                    "Email":"alvoefeef@gmail.com",
                    "Password":"123assdjsb",
                    "Confirm_Password":"123assdjsb"}

        self.user_invalid_password3= {"Username":"alvo",
                    "Email":"alvoaeedwa@gmail.com",
                    "Password":"AAdassdjsb",
                    "Confirm_Password":"AAdassdjsb"}


class TestUserSignUpandLogin(UserBaseTest):

    def test_user_can_sign_up(self):
        # test the endpoint that allows a user to successfully signup
        response= self.client.post('api/v1/auth/signup', data= json.dumps(self.user2), content_type="application/json")
        self.assertEqual(response.status_code, 201)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result["Message"], "Registered succesfully")

    def test_empty_data_on_signup(self):
        # test the response when a user fails to input data
        response= self.client.post('api/v1/auth/signup', data=json.dumps(self.user_empty_data), content_type="application/json")
        self.assertEqual(response.status_code, 400)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result["message"], "All fields are required")

    def test_email_already_taken(self):
        # test the response when a user signs up with an email already registered
        self.client.post('api/v1/auth/signup', data = json.dumps(self.user1), content_type="application/json")
        response= self.client.post('api/v1/auth/signup', data= json.dumps(self.user1), content_type="application/json")
        self.assertEqual(response.status_code, 400)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result["Message"], "Email already taken!")

    def test_user_passwords_dont_match(self):
        # test the response when a user does not confirm the entered password
        response=self.client.post('api/v1/auth/signup', data=json.dumps(self.user_pass_dont_match), content_type="application/json")
        self.assertEqual(response.status_code, 400)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result["message"], "Passwords do not match!")

    def test_user_invalid_email(self):
        # test the response if a user inputs an invalid email with no domain
        response=self.client.post('api/v1/auth/signup', data=json.dumps(self.user_invalid_email), content_type="application/json")
        self.assertEqual(response.status_code, 400)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result["message"], "Invalid Email")

    def test_user_invalid_email_1(self):
        # test the response if a user inputs an invalid email with no .com
        response=self.client.post('api/v1/auth/signup', data=json.dumps(self.user_invalid_email2), content_type="application/json")
        self.assertEqual(response.status_code, 400)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result["message"], "Invalid Email")

    def test_invalid_password_length(self):
        # test the response if a user inputs a short password i.e less than 6 chars
        response=self.client.post('api/v1/auth/signup', data=json.dumps(self.user_invalid_password), content_type="application/json")
        self.assertEqual(response.status_code, 400)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result["message"], "Password should not be less than 6 characters or exceed 12")

    def test_invalid_password_no_letters(self):
        # test the response if a user inputs a password with no letters
        response=self.client.post('api/v1/auth/signup', data=json.dumps(self.user_invalid_password1), content_type="application/json")
        self.assertEqual(response.status_code, 400)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result["message"], "Password should contain a letter between a-z")

    def test_invalid_password_no_capital_letter(self):
        # test the response if a user inputs a password with no capital letter
        response=self.client.post('api/v1/auth/signup', data=json.dumps(self.user_invalid_password2), content_type="application/json")
        self.assertEqual(response.status_code, 400)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result["message"], "Password should contain a capital letter")

    def test_invalid_password_no_int(self):
        # test the response if a user inputs a password with no integer
        response=self.client.post('api/v1/auth/signup', data=json.dumps(self.user_invalid_password3), content_type="application/json")
        self.assertEqual(response.status_code, 400)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result["message"], "Password should contain a number(0-9)")

    def test_user_can_log_in(self):
        # test the response if a user can log in successfully
        signup=self.client.post('api/v1/auth/signup', data= json.dumps(self.user3), content_type="application/json")
        self.assertEqual(signup.status_code, 201)
        response=self.client.post('api/v1/auth/login', data= json.dumps(self.user3), content_type="application/json")
        self.assertEqual(response.status_code, 200)

    def test_user_not_in_records(self):
        # test the response if a user inputs login information that is not contained in the db
        response=self.client.post('api/v1/auth/login', data= json.dumps(self.user2), content_type="application/json")
        self.assertEqual(response.status_code, 400)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result["message"], "Please Register First")





if __name__ == '__main__':
    unittest.main()
