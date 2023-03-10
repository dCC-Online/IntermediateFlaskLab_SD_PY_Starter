"""init

Revision ID: 46634a60c65b
Revises: 
Create Date: 2023-01-24 13:11:39.761118

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '46634a60c65b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('instructor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=255), nullable=False),
    sa.Column('last_name', sa.String(length=255), nullable=False),
    sa.Column('hire_date', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('student',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=255), nullable=False),
    sa.Column('last_name', sa.String(length=255), nullable=False),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.Column('gpa', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('course',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('instructor_id', sa.Integer(), nullable=True),
    sa.Column('credits', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['instructor_id'], ['instructor.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('student_course',
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.Column('course_id', sa.Integer(), nullable=True),
    sa.Column('grade', sa.String(length=5), nullable=True),
    sa.ForeignKeyConstraint(['course_id'], ['course.id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['student.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('student_course')
    op.drop_table('course')
    op.drop_table('student')
    op.drop_table('instructor')
    # ### end Alembic commands ###
