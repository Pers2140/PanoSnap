import sqlite3

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
        
        db_conn.commit()
        db_conn.close()
        
# expano = {'latLng': {'lat': 40.75822369999999, 'lng': -73.98540849999999}, 
# 'shortDescription': 'Times Square',
# 'description': 'Times Square',
# 'pano': 'CAoSK0FGMVFpcFAxRUtQcG1mZWZGMU4xS1hGZ3RxeTRLbm9COTk1UVZoV0NocTg.', 
# 'profileUrl': '//maps.google.com/maps/contrib/104359050004655709521'}

# mypano = favpano(expano)

# print ( mypano.latlng['lat'] )

