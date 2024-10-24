from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Profissional(Base):
    __tablename__ = "profissionais"

    id = Column(Integer, primary_key=True, index=True)
    nome_completo = Column(String, index=True)
    nome_social = Column(String, nullable=True)
    profissao = Column(String)
    endereco = Column(String)
    contato = Column(String)

    consultas = relationship("Consulta", back_populates="profissional")

class Consulta(Base):
    __tablename__ = "Consultas"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime)
    profissional_id = Column(Integer, ForeignKey("profissionais.id"))

    profissional = relationship("Profissional", back_populates="consultas")