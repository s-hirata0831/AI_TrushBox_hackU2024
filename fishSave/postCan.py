import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
import time

#------
#Firebase初期設定
#------
def postC():
    cred = credentials.Certificate("fishSave/token.json")
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    docCan = db.collection("stateTrashBox").document("can")
    can = docCan.get().to_dict()
    can_num = can.get('canNum', 0)
    can_num += 1
    docCan.update({"canNum": can_num})    

def postPet():
    cred = credentials.Certificate("token.json")
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    docPet = db.collection("stateTrashBox").document("pet")
    pet = docPet.get().to_dict()
    pet_num=pet.get('petNum', 0)
    pet_num += 1
    docPet.update({"petNum": pet_num})
