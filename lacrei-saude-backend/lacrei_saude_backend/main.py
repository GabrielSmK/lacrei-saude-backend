from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas, security
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/profissionais/", response_model=schemas.Profissional)
def create_profissional(profissional: schemas.ProfissionalCreate, db: Session = Depends(get_db)):
    sanitized_profissional = schemas.ProfissionalCreate(
        nome_completo=security.sanitize_input(profissional.nome_completo),
        nome_social=security.sanitize_input(profissional.nome_social) if profissional.nome_social else None,
        profissao=security.sanitize_input(profissional.profissao),
        endereco=security.sanitize_input(profissional.endereco),
        contato=security.sanitize_input(profissional.contato)
    )
    return crud.create_profissional(db=db, profissional=sanitized_profissional)

@app.get("/profissionais/{profissional_id}", response_model=schemas.Profissional)
def read_profissional(profissional_id: int, db: Session = Depends(get_db)):
    db_profissional = crud.get_profissional(db, profissional_id=profissional_id)
    if db_profissional is None:
        raise HTTPException(status_code=404, detail="Profissional not found")
    return db_profissional

@app.put("/profissionais/{profissional_id}", response_model=schemas.Profissional)
def update_profissional(profissional_id: int, profissional: schemas.ProfissionalCreate, db: Session = Depends(get_db)):
    sanitized_profissional = schemas.ProfissionalCreate(
        nome_completo=security.sanitize_input(profissional.nome_completo),
        nome_social=security.sanitize_input(profissional.nome_social) if profissional.nome_social else None,
        profissao=security.sanitize_input(profissional.profissao),
        endereco=security.sanitize_input(profissional.endereco),
        contato=security.sanitize_input(profissional.contato)
    )
    db_profissional = crud.update_profissional(db, profissional_id, sanitized_profissional)
    if db_profissional is None:
        raise HTTPException(status_code=404, detail="Profissional not found")
    return db_profissional

@app.delete("/profissionais/{profissional_id}", response_model=schemas.Profissional)
def delete_profissional(profissional_id: int, db: Session = Depends(get_db)):
    db_profissional = crud.delete_profissional(db, profissional_id)
    if db_profissional is None:
        raise HTTPException(status_code=404, detail="Profissional not found")
    return db_profissional

@app.post("/consultas/", response_model=schemas.Consulta)
def create_consulta(consulta: schemas.ConsultaCreate, db: Session = Depends(get_db)):
    return crud.create_consulta(db=db, consulta=consulta)

@app.get("/consultas/{consulta_id}", response_model=schemas.Consulta)
def read_consulta(consulta_id: int, db: Session = Depends(get_db)):
    db_consulta = crud.get_consulta(db, consulta_id=consulta_id)
    if db_consulta is None:
        raise HTTPException(status_code=404, detail="Consulta not found")
    return db_consulta

@app.put("/consultas/{consulta_id}", response_model=schemas.Consulta)
def update_consulta(consulta_id: int, consulta: schemas.ConsultaCreate, db: Session = Depends(get_db)):
    db_consulta = crud.update_consulta(db, consulta_id, consulta)
    if db_consulta is None:
        raise HTTPException(status_code=404, detail="Consulta not found")
    return db_consulta

@app.delete("/consultas/{consulta_id}", response_model=schemas.Consulta)
def delete_consulta(consulta_id: int, db: Session = Depends(get_db)):
    db_consulta = crud.delete_consulta(db, consulta_id)
    if db_consulta is None:
        raise HTTPException(status_code=404, detail="Consulta not found")
    return db_consulta

@app.get("/profissionais/{profissional_id}/consultas/", response_model=list[schemas.Consulta])
def read_consultas_by_profissional(profissional_id: int, db: Session = Depends(get_db)):
    consultas = crud.get_consultas_by_profissional(db, profissional_id=profissional_id)
    return consultas