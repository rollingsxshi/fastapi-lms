# LMS API with FastAPI

## Poetry
- ensure poetry is installed in your system
- run `poetry init` in root of project
- install python packages with `poetry add {packageName}`

## FastAPI
- run server with `uvicorn main:app --reload`

## Alembic
- run `poetry add alembic`
- run `alembic init alembic`
- run `alembic revision --autogenerate` to generate migration file
- run `alembic upgrade head` to run migration to postgres db
- update migration file that contains enum:
```python
op.add_column('users', sa.Column('role', sa.Enum('teacher', 'student', name='role'), nullable=True))
```
- take note of sqlalchemy Enums in migration file
