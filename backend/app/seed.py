from faker import Faker
from sqlalchemy.orm import Session
from app import models, database

fake = Faker()

def seed_blogs(n=20):
    db: Session = database.SessionLocal()
    for _ in range(n):
        blog = models.Blog(
            title=fake.sentence(nb_words=6),
            content=fake.paragraph(nb_sentences=5)
        )
        db.add(blog)
    db.commit()
    db.close()
    print(f"{n} fake blog posts added.")

if __name__ == "__main__":
    models.Base.metadata.create_all(bind=database.engine)  # Ensure tables exist
    seed_blogs(20)  # Seed 10 dummy posts
