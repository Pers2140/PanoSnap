
# API key AIzaSyDuor625kNugbhknAmc4RtKUd5Z-PBulFk

# curl --request POST \
#     --url 'https://streetviewpublish.googleapis.com/v1/photo:startUpload?key=AIzaSyDuor625kNugbhknAmc4RtKUd5Z-PBulFk' \
#     --header 'authorization: Bearer YOUR_ACCESS_TOKEN' \
#     --header 'Content-Length: 0'

from google.streetview.publish_v1.proto import resources_pb2
from google.streetview.publish_v1 import street_view_publish_service_client as client
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.file import Storage
from oauth2client.tools import run_flow
import google.oauth2.credentials
import requests
import time
def 
def get_access_token():
  client_id = '914961849316-0ojb0sscc55v4c7ahsvhv0q5l7eqb478.apps.googleusercontent.com'
  client_secret = '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'
  flow = OAuth2WebServerFlow(client_id=client_id,
                             client_secret=client_secret,
                             scope='https://www.googleapis.com/auth/streetviewpublish',
                             redirect_uri='http://example.com/auth_return')
  storage = Storage('creds.data')
  # Open a web browser to ask the user for credentials.
  credentials = run_flow(flow, storage)
  assert credentials.access_token is not None
  return credentials.access_token

token = get_access_token()
credentials = google.oauth2.credentials.Credentials(token)

# Create a client and request an Upload URL.
streetview_client = client.StreetViewPublishServiceClient(credentials=credentials)
upload_ref = streetview_client.start_upload()
print("Created upload url: " + str(upload_ref))

# Upload the photo bytes to the Upload URL.
with open("/path/to/your/file.jpg", "rb") as f:
  print("Uploading file: " + f.name)
  raw_data = f.read()
  headers = {
      "Authorization": "Bearer " + token,
      "Content-Type": "image/jpeg",
      "X-Goog-Upload-Protocol": "raw",
      "X-Goog-Upload-Content-Length": str(len(raw_data)),
  }
  r = requests.post(upload_ref.upload_url, data=raw_data, headers=headers)
  print("Upload response: " + str(r))

# Upload the metadata of the photo.
photo = resources_pb2.Photo()
photo.upload_reference.upload_url = upload_ref.upload_url
photo.capture_time.seconds = int(time.time())
photo.pose.heading = 105.0
photo.pose.lat_lng_pair.latitude = 46.7512623
photo.pose.lat_lng_pair.longitude = -121.9376983
create_photo_response = streetview_client.create_photo(photo)
print("Create photo response: " + str(create_photo_response))
