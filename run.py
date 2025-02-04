from app import app
from app import db
from flask.cli import FlaskGroup

cli = FlaskGroup(app)

@cli.command("create_db")
def create_db():
    db.create_all()
    db.session.commit()

if __name__ == '__main__':
    cli()