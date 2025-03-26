from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from pydantic import BaseModel
from typing import List

#pip install pymysql
#.\.venv\Scripts\activate  # Windows
#uvicorn main:app --reload

# Configuración de la base de datos
DATABASE_URL = "mysql+pymysql://root:@localhost:3306/BDCitas"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# MODELO: Paciente
class Paciente(Base):
    __tablename__ = "Paciente"
    id = Column(String(50), primary_key=True, index=True)
    nom = Column(String(100))
    ape = Column(String(100))
    tel = Column(Integer)
    img = Column(String(255))

# Crear tablas
Base.metadata.create_all(bind=engine)

# Esquema Pydantic
class PacienteSchema(BaseModel):
    id: str
    nom: str
    ape: str
    tel: int
    img: str

    class Config:
        from_attributes = True

# Dependencia

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Instancia FastAPI
app = FastAPI()

# CRUD Paciente

# Crear Paciente
@app.post("/paciente/", response_model=PacienteSchema)
def crear_paciente(paciente: PacienteSchema, db: Session = Depends(get_db)):
    db_paciente = Paciente(**paciente.model_dump())
    db.add(db_paciente)
    db.commit()
    db.refresh(db_paciente)
    return db_paciente

# Obtener Paciente por ID
@app.get("/paciente/{paciente_id}", response_model=PacienteSchema)
def obtener_paciente(paciente_id: str, db: Session = Depends(get_db)):
    paciente = db.query(Paciente).filter(Paciente.id == paciente_id).first()
    if not paciente:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    return paciente

# Listar todos los Pacientes
@app.get("/pacientes/", response_model=List[PacienteSchema])
def listar_pacientes(db: Session = Depends(get_db)):
    pacientes = db.query(Paciente).all()
    return pacientes

# Actualizar Paciente
@app.put("/paciente/{paciente_id}", response_model=PacienteSchema)
def actualizar_paciente(paciente_id: str, paciente: PacienteSchema, db: Session = Depends(get_db)):
    db_paciente = db.query(Paciente).filter(Paciente.id == paciente_id).first()
    if not db_paciente:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    for key, value in paciente.model_dump().items():
        if key != "id":
            setattr(db_paciente, key, value)
    db.commit()
    db.refresh(db_paciente)
    return db_paciente

# Eliminar Paciente
@app.delete("/paciente/{paciente_id}")
def eliminar_paciente(paciente_id: str, db: Session = Depends(get_db)):
    db_paciente = db.query(Paciente).filter(Paciente.id == paciente_id).first()
    if not db_paciente:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    db.delete(db_paciente)
    db.commit()
    return {"mensaje": "Paciente eliminado exitosamente"}

# Ejecutar FastAPI con Uvicorn
if __name__ == "__main__":
    import uvicorn
    #uvicorn.run(app, host="127.0.0.1", port=8000)
    uvicorn.run(app, host="172.56.0.22", port=8000)
