import os
from glob import iglob
from shutil import rmtree
from unittest import TestCase

from jsonstorage import JsonStorage, InvalidJsonStorage, VERSION

_KEY_FERRARI = 'cars.brands.ferrari'
_KEY_PORSCHE = 'cars.brands.porsche'

_MODELS_FERRARI = ['360 Modena', 'F40', 'F50', 'Enzo']
_MODELS_PORSCHE = ['911 Turbo', '911 Turbo S', '911 Carrera', 'Carrera', 'Tycan']


class _BasicTestCase(TestCase):
    _tests_base_path = os.path.dirname(os.path.abspath(__file__))
    _tests_fixture_path = os.path.join(_tests_base_path, 'fixtures')
    _tests_temp_path = os.path.join(_tests_base_path, 'temp')

    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)

    def get_fixture_file_path(self, file_name: str) -> str:
        return os.path.join(self._tests_fixture_path, file_name)

    def get_temp_file_path(self, file_name: str) -> str:
        return os.path.join(self._tests_temp_path, file_name)

    def get_fixture_content(self, fixture_file_name: str) -> str:
        with open(file=self.get_fixture_file_path(file_name=fixture_file_name), mode='r') as fixture:
            return fixture.read()

    def _cleanup_temp(self):
        if os.path.isdir(self._tests_temp_path):
            for item in iglob(pathname=os.path.join(self._tests_temp_path, "**")):
                if os.path.isdir(item):
                    rmtree(path=item)
                else:
                    os.remove(path=item)

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        if not os.path.isdir(cls._tests_temp_path):
            os.mkdir(cls._tests_temp_path)

    @classmethod
    def tearDownClass(cls) -> None:
        super().tearDownClass()
        if os.path.isdir(cls._tests_temp_path):
            rmtree(path=cls._tests_temp_path)

    def setUp(self) -> None:
        super().setUp()
        self._cleanup_temp()

    def tearDown(self) -> None:
        super().tearDown()
        self._cleanup_temp()


class TestJsonStorage(_BasicTestCase):

    def _get_data_file_path(self) -> str:
        return self.get_temp_file_path(file_name='data.json')

    def _get_invalid_data_file_path(self) -> str:
        return self.get_temp_file_path(file_name='data_invalid.json')

    def _get_storage(self) -> JsonStorage:
        return JsonStorage(path=self._get_data_file_path())

    def _create_invalid_json_file(self):
        with open(file=self._get_invalid_data_file_path(), encoding='utf8', mode='w') as file:
            file.writelines(_MODELS_FERRARI)
            file.writelines(_MODELS_PORSCHE)

    def test_version(self):
        self.assertEqual(VERSION, "0.1.0")

    def test_try_create_new_json_storage_with_empty_path(self):
        with self.assertRaises(ValueError):
            JsonStorage(path='')

    def test_try_create_new_json_storage_with_none_path(self):
        with self.assertRaises(ValueError):
            JsonStorage(path=None)

    def test_try_insert_value_with_empty_key(self):
        storage = self._get_storage()
        with self.assertRaises(ValueError):
            storage.set_value(key='', value=None)
        with self.assertRaises(ValueError):
            storage.set_value(key=None, value=None)

    def test_try_get_value_with_empty_key(self):
        storage = self._get_storage()
        with self.assertRaises(ValueError):
            storage.get_value(key='')
        with self.assertRaises(ValueError):
            storage.get_value(key=None)

    def _create_storage(self) -> JsonStorage:
        storage = self._get_storage()
        storage.set_value(_KEY_FERRARI, _MODELS_FERRARI)
        storage.set_value(_KEY_PORSCHE, _MODELS_PORSCHE)
        return storage

    def test_try_insert_value(self):
        storage = self._create_storage()
        self.assertIsNotNone(storage.data)
        self.assertIsInstance(storage.data, dict)
        self.assertIsInstance(storage.data['cars']['brands']['ferrari'], list)

    def test_try_insert_and_replace_value(self):
        storage = self._create_storage()
        self.assertIsNotNone(storage.data)
        self.assertIsInstance(storage.data, dict)
        self.assertIsInstance(storage.data['cars']['brands']['ferrari'], list)
        storage.set_value(_KEY_FERRARI, None)
        self.assertIsNone(storage.data['cars']['brands']['ferrari'])
        storage.set_value(_KEY_FERRARI, ['812 GTS', 'California', 'Challenge Stradale'])
        self.assertIsInstance(storage.data['cars']['brands']['ferrari'], list)

    def test_try_insert_and_get_value(self):
        storage = self._create_storage()
        self.assertIsInstance(storage.data, dict)
        self.assertIsInstance(storage.get_value('cars'), dict)
        self.assertIsInstance(storage.get_value('cars.brands'), dict)
        self.assertIsInstance(storage.get_value('cars.brands.ferrari'), list)

    def test_try_get_non_existent_value(self):
        storage = self._create_storage()
        self.assertIsNone(storage.get_value('cars.owners'))

    def test_try_create_and_save_file(self):
        storage = self._create_storage()
        storage.save()
        self.assertTrue(os.path.isfile(self._get_data_file_path()))
        storage2 = JsonStorage(path=self._get_data_file_path())
        self.assertTrue(isinstance(storage2.get_value(_KEY_FERRARI), list))
        self.assertTrue(isinstance(storage2.get_value(_KEY_PORSCHE), list))

    def test_try_load_invalid_json_file(self):
        self._create_invalid_json_file()
        with self.assertRaises(InvalidJsonStorage):
            JsonStorage(path=self._get_invalid_data_file_path())
