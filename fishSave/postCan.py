import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials

#------
#Firebase初期設定
#------
cred = credentials.Certificate("token.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
docCan = db.collection("stateTrashBox").document("can")

docCan.update({"canNum": 0})