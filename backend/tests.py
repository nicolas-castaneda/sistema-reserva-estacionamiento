import unittest

from server import create_app
from models import setup_db
import json
import os

class TestSREApi(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = 'sre_test'
        self.database_path = 'postgresql://postgres:{}@localhost:5432/{}'.format(os.getenv('POST_PASS'), self.database_name)
        
        setup_db(self.app, self.database_path)
        
    def test_post_session_failed_correo(self):
        res = self.client().post('/session', json = {"correo": ""})
        data = json.loads(res.data)
        self.assertFalse(data['success'])
        self.assertEqual(data['error'], 400)
        self.assertIn('correo', data['message'])
    
    def test_post_session_failed_contrasena(self):
        res = self.client().post('/session', json = {"correo": "a@b.com", "contrasena": ""})
        data = json.loads(res.data)
        self.assertFalse(data['success'])
        self.assertEqual(data['error'], 400)
        self.assertIn('contraseña', data['message'])
        
    def test_post_session_success(self):
        res = self.client().post('/session', json = {"correo": "a@a.com", "contrasena": "1234"})
        data = json.loads(res.data)
        self.assertTrue(data['success'])
        self.assertIsNotNone(data['token'])
        self.assertEqual('REG', data['user']['estado'])
        self.assertIn('celular', data['user'])
        self.assertIn('correo', data['user'])
        self.assertIn('dni', data['user'])