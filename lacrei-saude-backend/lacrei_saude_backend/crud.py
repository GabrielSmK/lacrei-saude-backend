from sqlalchemy.orm import Session
from . import models, schemas

def create_profissional(db: Session, profissional: schemas.ProfissionalCreate):
    db_profissional = models.Profissional(**profissional.model_dump())
    db.add(db_profissional)
    db.commit()
    db.refresh(db_profissional)
    return db_profissional

def get_profissional(db: Session, profissional_id: int):
    return db.query(models.Profissional).filter(models.Profissional.id == profissional_id).first()

def update_profissional(db: Session, profissional_id: int, profissional: schemas.ProfissionalCreate):
    db_profissional = get_profissional(db, profissional_id)
    if db_profissional:
        for key, value in profissional.model_dump().items():
            setattr(db_profissional, key, value)
        db.commit()
        db.refresh(db_profissional)
    return db_profissional

def delete_profissional(db: Session, profissional_id: int):
    db_profissional = get_profissional(db, profissional_id)
    if db_profissional:
        db.delete(db_profissional)
        db.commit()
    return db_profissional

def create_consulta(db: Session, consulta: schemas.ConsultaCreate):
    db_consulta = models.Consulta(**consulta.model_dump())
    db.add(db_consulta)
    db.commit()
    db.refresh(db_consulta)
    return db_consulta

def get_consulta(db: Session, consulta_id: int):
    return db.query(models.Consulta).filter(models.Consulta.id == consulta_id).first()

def update_consulta(db: Session, consulta_id: int, consulta: schemas.ConsultaCreate):
    db_consulta = get_consulta(db, consulta_id)
    if db_consulta:
        for key, value in consulta.model_dump().items():
            setattr(db_consulta, key, value)
        db.commit()
        db.refresh(db_consulta)
    return db_consulta

def delete_consulta(db: Session, consulta_id: int):
    db_consulta = get_consulta(db, consulta_id)
    if db_consulta:
        db.delete(db_consulta)
        db.commit()
    return db_consulta

def get_consultas_by_profissional(db: Session, profissional_id: int):
    return db.query(models.Consulta).filter(models.Consulta.profissional_id == profissional_id).all()