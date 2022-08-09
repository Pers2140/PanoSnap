
# create SQL Model
class Users(db.Model):
    '''
        User class for signing up
    '''
    
    def __init__(self):
        
        self.id = db.Column(db.Integer, primary_key=True)
        self.first_name = db.Column(db.String(200), nullable=False)
        self.last_name = db.Column(db.String(200), nullable=False)
        self.username=db.Column(db.String(120), nullable=False, unique=True)
        self.email = db.Column(db.String(120), nullable=False, unique=True)
        self.data_added = db.Column(db.DateTime, default=datetime.utcnow)
    
        # On user creation submit information to DB
        # Connect to database
        db_conn = sqlite3.connect('test.db') 
        
        # Cursor to interact with DB
        c = db_conn.cursor()
        
        # submit pano 
        c.execute("INSERT INTO users ('first_name','last_name','username','password','email') VALUES (?,?,?,?,?)", ('Zeus','god','BigDadaZ','password123','Bigz@gmail.com'))
        print('New user submitted to DB new ')
        
        # close connection to DB
        db_conn.commit()
        db_conn.close()
    
 

    def __repr__(self):
        return '<Name %r> % self.name'
    
# create pano 360 class to submit to user's saves
class favpano:
    '''
        creates favpano obj from user submission to send to db
    '''
    def __init__(self,obj):
        
        self.des = obj['description']
        self.latlng = str(obj['latLng'])
        self.pano = obj['pano']
        self.profile_url = obj['profileUrl']
        
        # Connect to database
        db_conn = sqlite3.connect('test.db') 
        
        # Cursor to interact with DB
        c = db_conn.cursor()
        
        # submit pano 
        c.execute("INSERT INTO panos ('description','latlng','pano','profile_url') VALUES (?,?,?,?)", (self.des, self.latlng, self.pano, self.profile_url ))
        print('New pano submitted to DB new ')
        
        # close connection to DB
        db_conn.commit()
        db_conn.close()