
# create pano 360 class to submit to user's saves

class favpano:
    '''
        creates favpano obj from user submission to send to db
    '''
    def __init__(self,obj):
        
        self.des = obj['description']
        self.latlng = obj['latLng']
        self.pano = obj['pano']
        self.profile_url = obj['profileUrl']
        
  
        
# expano = {'latLng': {'lat': 40.75822369999999, 'lng': -73.98540849999999}, 
# 'shortDescription': 'Times Square',
# 'description': 'Times Square',
# 'pano': 'CAoSK0FGMVFpcFAxRUtQcG1mZWZGMU4xS1hGZ3RxeTRLbm9COTk1UVZoV0NocTg.', 
# 'profileUrl': '//maps.google.com/maps/contrib/104359050004655709521'}

# mypano = favpano(expano)

# print ( mypano.latlng['lat'] )

