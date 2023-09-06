from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates('name')
    def validate_name(self, key, name):
        if len(name) == 0:
            raise ValueError('failed name')
        return name

    @validates('phone_number')
    def validate_number(self, key, number):
        if len(number) != 10:
            raise ValueError('Incorrect number of digits')
        return number

    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'

class Post(db.Model):
    __tablename__ = 'posts'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates('title')
    def validate_title(self, key, title):
        # clickbait = [
        #     "Won't Believe",
        #     "Secret",
        #     "Top[number]",
        #     "Guess"
        # ]
        if len(title) == 0:
            return title
            # for bait in clickbait:
            #     if bait in title:
            #         return title 
            # return ValueError('No clickbait')
        raise ValueError('No title')


    @validates('content')
    def validate_content_len(self, key, content):
        if len(content) < 250:
            raise ValueError('Not enough content')
        return content

    @validates('summary')
    def validate_summary_len(self, key, summary):
        if 249 < len(summary):
            raise ValueError('summary too long')
        return summary

    @validates('category')
    def validate_category(self, key, category):
        if category == 'Fiction' or category =='Non-Fiction':
            return category
        raise ValueError('no category')
    
    # @validates('title')
    # def validate_clickbait(self, key, title):
    #     clickbait = [
    #         "Won't Believe",
    #         "Secret",
    #         "Top[number]",
    #         "Guess"
    #     ]
    #     for bait in clickbait:
    #         if bait in title:
    #             return title
    #     raise ValueError('no bait')
    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'
