from .entities.User import User 

class ModelUser():
    
    @classmethod
    def login(self,db,Users):
        try:
            cursor = db.connect.cursor()
            sql=""" SELECT Userid, email, password FROM user 
                    WHERE email = '{}'""".format(Users.email)
            cursor.execute(sql)
            row=cursor.fetchone()
            if row  != None:
                Users = User(row[0],row[1],User.check_password(row[2],Users.password))
                return Users
            else: 
                return None
        except Exception as ex:
            raise Exception(ex)
        
