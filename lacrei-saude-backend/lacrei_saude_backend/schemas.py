from pydantic import BaseModel, ConfigDict
from datetime import datetime

common_config = ConfigDict(
    from_attributes=True,
    populate_by_name=True
)

class ProfissionalBase(BaseModel):
    nome_completo: str
    nome_social: str | None = None
    profissao: str
    endereco: str
    contato: str

    model_config = common_config

class ProfissionalCreate(ProfissionalBase):
    pass

class Profissional(ProfissionalBase):
    id: int

    model_config = common_config

class ConsultaBase(BaseModel):
    date: datetime
    profissional_id: int

    model_config = common_config

class ConsultaCreate(ConsultaBase):
    pass

class Consulta(ConsultaBase):
    id: int

    model_config = common_config