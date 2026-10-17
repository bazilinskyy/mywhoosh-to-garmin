import pytest
from services.mywhoosh_service import MyWhooshService

def test_mywhoosh_service_init():
    svc = MyWhooshService(email='test@example.com', password='secret')
    assert svc.email == 'test@example.com'
    assert svc.password == 'secret'

def test_device_id_is_stored_and_reused(tmp_path, monkeypatch):
    path = tmp_path / 'device_id'
    monkeypatch.setenv('MYWHOOSH_DEVICE_ID_FILE', str(path))

    first = MyWhooshService(email='test@example.com', password='secret')._load_device_id()
    second = MyWhooshService(email='test@example.com', password='secret')._load_device_id()

    assert first == second
    assert path.read_text().strip() == first
