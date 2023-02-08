import sqlite3
import random

def createTables():
    conn = sqlite3.connect("quiz.db")
    try:
        q = '''
        create table quiz(id integer primary key, 
                          title varchar(100) not null)
        '''
        conn.execute(q)
        conn.commit()

        q = '''
        create table question(id integer primary key, 
                          title varchar(100) not null,
                          option1 varchar(100) not null,
                          option2 varchar(100) not null,
                          answer varchar(1) not null,
                          quiz_id integer,
                          foreign key (quiz_id) references quiz(id))
        '''
        conn.execute(q)
        conn.commit()
        
        q = '''
        create table attempt(id integer primary key, 
                          quiz_id integer not null,
                          question_id integer not null,
                          answer varchar(1) not null,
                          foreign key (question_id) references question(id),
                          foreign key (quiz_id) references quiz(id))
        '''
        conn.execute(q)
        conn.commit()
        print("Success")
    except Exception as e:
        print(e)
        

def addQuiz(title):
    conn = sqlite3.connect("quiz.db")
    try:
        q = '''
            insert into quiz(title) values(?)
        '''
        conn.execute(q,[title])
        conn.commit()
        print("success")
    except Exception as e:
        print(e)
    finally:
        conn.close()
        
def getQuiz():
    conn = sqlite3.connect("quiz.db")
    try:
        q = '''
            select * from quiz
        '''
        quizes = conn.execute(q).fetchall()
        print("success")
        return quizes
    except Exception as e:
        print(e)
        return []
    finally:
        conn.close()
        


def addQuestion(quiz_id,title,option1,option2,answer):
    conn = sqlite3.connect("quiz.db")
    try:
        q = '''
            insert into question(quiz_id,title,option1,option2,answer) values(?,?,?,?,?)
        '''
        conn.execute(q,[quiz_id,title,option1,option2,answer])
        conn.commit()
        print("success")
    except Exception as e:
        print(e)
    finally:
        conn.close()
        
def getQuestion(quiz_id):
    conn = sqlite3.connect("quiz.db")
    try:
        q = '''
            select * from question where question.quiz_id = ?
        '''
        questions = conn.execute(q,[quiz_id]).fetchall()
        random.shuffle(questions)
        print("success")
        
        return questions

    except Exception as e:
        print(e)
        return []
    finally:
        conn.close()

if  __name__ == "__main__":
    # addQuiz("IBPS")
    # addQuiz("UPSZ")
    # addQuiz("ENG")
    # print(getQuiz())
    # addQuestion(1,"What is capital of India","Delhi","Islamabad","a")
    # addQuestion(1,"What is capital of Karnataka","Bengaluru","Hubli","a")
    # addQuestion(2,"What is capital of Pakistan","Delhi","Islamabad","b")
    # addQuestion(2,"What is capital of Bangladesh","Dhaka","Islamabad","a")
    # addQuestion(3,"Where is BVB","Hubli","Islamabad","a")
    # addQuestion(3,"Where is PESIT","Delhi","Bengalurur","b")

    print(getQuestion(1))