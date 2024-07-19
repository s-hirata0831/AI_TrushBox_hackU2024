import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
import time

#------
#Firebase初期設定
#------
cred = credentials.Certificate("token.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
docCan = db.collection("stateTrashBox").document("can")
docPet = db.collection("stateTrashBox").document("pet")

docCan.update({"canNum": 24})
docPet.update({"petNum": 20})
