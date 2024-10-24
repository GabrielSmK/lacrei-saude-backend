from fastapi.testclient import TestClient
from lacrei_saude_backend.main import app

client = TestClient(app)

def test_create_profissional():
    response = client.post(
        "/profissionais/",
        json={
            "nome_completo": "Dr. Test",
            "nome_social": "Dr. T",
            "profissao": "Tester",
            "endereco": "123 Test St",
            "contato": "test@example.com"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["nome_completo"] == "Dr. Test"
    assert data["profissao"] == "Tester"
    assert "id" in data
