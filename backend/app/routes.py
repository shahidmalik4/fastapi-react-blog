from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas, database

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/blogs", response_model=list[schemas.Blog])
def list_blogs(db: Session = Depends(get_db)):
    return crud.get_blogs(db)

@router.get("/blogs/{blog_id}", response_model=schemas.Blog)
def read_blog(blog_id: int, db: Session = Depends(get_db)):
    blog = crud.get_blog(db, blog_id)
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    return blog

@router.post("/blogs", response_model=schemas.Blog)
def create(blog: schemas.BlogCreate, db: Session = Depends(get_db)):
    return crud.create_blog(db, blog)

@router.put("/blogs/{blog_id}", response_model=schemas.Blog)
def update(blog_id: int, blog: schemas.BlogUpdate, db: Session = Depends(get_db)):
    updated = crud.update_blog(db, blog_id, blog)
    if not updated:
        raise HTTPException(status_code=404, detail="Blog not found")
    return updated

@router.delete("/blogs/{blog_id}", response_model=schemas.Blog)
def delete(blog_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_blog(db, blog_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Blog not found")
    return deleted
