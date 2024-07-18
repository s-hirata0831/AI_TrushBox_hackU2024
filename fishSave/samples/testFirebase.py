import os
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials

#------
#Firebase初期設定
#------
cred = credentials.Certificate("token.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
document = db.collection("stateTrashBox").document("can")

canState = ['canNum']
can = document.get(field_paths=canState).to_dict()
can_s=can['canNum']
print(can_s)