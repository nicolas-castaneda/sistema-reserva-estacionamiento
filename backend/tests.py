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
    
    # Usuario
    def test_get_usuario(self):
        res = self.client().get('/usuario')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertIsNotNone(data['users'])
        self.assertTrue(data['success'])
        self.assertEqual(data['count'], 1)
        
    def test_post_usuario_failed_DNI(self):
        res = self.client().post('/usuario', json={'DNI':''})
        data = json.loads(res.data)
        self.assertFalse(data['success'])
        self.assertIn('DNI', data['message'])
        self.assertEqual(data['error'], 400)
        self.assertEqual(res.status_code, 400)
    
    def test_post_usuario_failed_celular(self):
        res = self.client().post('/usuario', json={'DNI': '12345678','celular':''})
        data = json.loads(res.data)
        self.assertFalse(data['success'])
        self.assertIn('celular', data['message'])
        self.assertEqual(data['error'], 400)
        self.assertEqual(res.status_code, 400)

    def test_post_usuario_failed_correo(self):
        res = self.client().post('/usuario', json={'DNI': '12345678',
                                                   'celular':'123456789',
                                                   'nombres': 'aaaa',
                                                   'correo': 'a@a.com'
                                                   })
        data = json.loads(res.data)
        self.assertFalse(data['success'])
        self.assertIn('correo', data['message'])
        self.assertEqual(data['error'], 400)
        self.assertEqual(res.status_code, 400)
        
    def test_post_usuario_failed_correo(self):
        res = self.client().post('/usuario', json={'DNI': '12345678',
                                                   'celular':'123456789',
                                                   'nombres': 'aaaa',
                                                   'correo': 'bcsd@a.com',
                                                   'contrasena': '12345'
                                                   })
        data = json.loads(res.data)
        self.assertFalse(data['success'])
        self.assertIn('contraseña', data['message'])
        self.assertEqual(data['error'], 400)
        self.assertEqual(res.status_code, 400)
        
    def test_post_usuario_success(self):
        res = self.client().post('/usuario', json={'DNI': '12345678',
                                                   'celular':'123456789',
                                                   'nombres': 'aaaa',
                                                   'correo': 'bcsd@a.com',
                                                   'contrasena': 'Ansdf234_S'
                                                   })
        data = json.loads(res.data)
        self.assertTrue(data['success'])
        self.assertEqual(res.status_code, 200)
        self.assertIsNotNone(data['user'])
        self.assertEqual(data['user']['estado'], 'REG')

    # SESSION    
    def test_post_session_failed_correo(self):
        res = self.client().post('/session', json = {"correo": ""})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertFalse(data['success'])
        self.assertEqual(data['error'], 400)
        self.assertIn('correo', data['message'])
    
    def test_post_session_failed_contrasena(self):
        res = self.client().post('/session', json = {"correo": "a@b.com", "contrasena": ""})
        data = json.loads(res.data)
        self.assertFalse(data['success'])
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['error'], 400)
        self.assertIn('contraseña', data['message'])
        
    def test_post_session_success(self):
        res = self.client().post('/session', json = {"correo": "a@a.com", "contrasena": "1234"})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertIsNotNone(data['token'])
        self.assertEqual('REG', data['user']['estado'])
        self.assertIn('celular', data['user'])
        self.assertIn('correo', data['user'])
        self.assertIn('dni', data['user'])

    
    def home_test(self):
        res = self.client().get('/')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)