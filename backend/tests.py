import unittest

from server import create_app
from models import setup_db
from datetime import datetime, timedelta

import json
import jwt
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
        #self.assertEqual(data['count'], 1)
        
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

    # ESTACIONAMIENTO
    def test_get_estacionamientos_success(self):
        res = self.client().get('/estacionamiento')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertIsNotNone(data['estacionamientos'])
        self.assertTrue(data['success'])
        self.assertTrue(data['total_estacionamientos'])

    # RESERVA
    def test_post_reserva_failed_placa(self):
        token = jwt.encode({
            'id': '1',
            'correo': 'a@a.com',
            'iat': datetime.utcnow(),
            'exp': datetime.utcnow() + timedelta(minutes=30)
        }, '192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf',
        algorithm='HS256')
        
        res=self.client().post("/reserva", headers={"Authorization": "Bearer "+token, 
                                                    "Content-Type":"application/json"}, 
                                                json={  'lugar': 'A1', 
                                                        'inicioReserva': '2023-05-16T20:57', 
                                                        'finReserva': '2023-05-17T23:57', 
                                                        'costoReserva': '4.05', 
                                                        'costoTotal': '81', 
                                                        'placa': 'placamuylarga', 
                                                        'marca': 'a', 
                                                        'modelo': 'b', 
                                                        'color': 'c', 
                                                        'opcion': True, 
                                                    })
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertFalse(data['success'])
        self.assertTrue(data['message'])

    def test_post_reserva_failed_marca(self):
        token = jwt.encode({
            'id': '1',
            'correo': 'a@a.com',
            'iat': datetime.utcnow(),
            'exp': datetime.utcnow() + timedelta(minutes=30)
        }, '192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf',
        algorithm='HS256')
        
        res=self.client().post("/reserva", headers={"Authorization": "Bearer "+token, 
                                                    "Content-Type":"application/json"}, 
                                                json={  'lugar': 'A1', 
                                                        'inicioReserva': '2023-05-16T20:57', 
                                                        'finReserva': '2023-05-17T23:57', 
                                                        'costoReserva': '4.05', 
                                                        'costoTotal': '81', 
                                                        'placa': 'A7', 
                                                        'modelo': 'b', 
                                                        'color': 'c', 
                                                        'opcion': True, 
                                                    })
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertFalse(data['success'])
        self.assertIn('marca', data['message'])

    def test_post_reserva_failed_modelo(self):
        token = jwt.encode({
            'id': '1',
            'correo': 'a@a.com',
            'iat': datetime.utcnow(),
            'exp': datetime.utcnow() + timedelta(minutes=30)
        }, '192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf',
        algorithm='HS256')
        
        res=self.client().post("/reserva", headers={"Authorization": "Bearer "+token, 
                                                    "Content-Type":"application/json"}, 
                                                json={  'lugar': 'A1', 
                                                        'inicioReserva': '2023-05-16T20:57', 
                                                        'finReserva': '2023-05-17T23:57', 
                                                        'costoReserva': '4.05', 
                                                        'costoTotal': '81', 
                                                        'placa': 'A7', 
                                                        'marca': 'a', 
                                                        'color': 'c', 
                                                        'opcion': True, 
                                                    })
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertFalse(data['success'])
        self.assertIn('modelo', data['message'])

    def test_post_reserva_failed_color(self):
        token = jwt.encode({
            'id': '1',
            'correo': 'a@a.com',
            'iat': datetime.utcnow(),
            'exp': datetime.utcnow() + timedelta(minutes=30)
        }, '192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf',
        algorithm='HS256')
        
        res=self.client().post("/reserva", headers={"Authorization": "Bearer "+token, 
                                                    "Content-Type":"application/json"}, 
                                                json={  'lugar': 'A1', 
                                                        'inicioReserva': '2023-05-16T20:57', 
                                                        'finReserva': '2023-05-17T23:57', 
                                                        'costoReserva': '4.05', 
                                                        'costoTotal': '81', 
                                                        'placa': 'A7', 
                                                        'marca': 'a', 
                                                        'modelo':'b',
                                                        'opcion': True, 
                                                    })
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertFalse(data['success'])
        self.assertIn('color', data['message'])

    # PAGINA AUTOS

