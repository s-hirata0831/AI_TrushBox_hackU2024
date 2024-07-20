import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
#------
#Firebase初期設定
#------
cred = credentials.Certificate("fishSave/token.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
docCan = db.collection("stateTrashBox").document("can")
docPet = db.collection("stateTrashBox").document("pet")

#docCan.update({"canNum": 24})
#docPet.update({"petNum": 20})

can = docCan.get().to_dict()
pet = docPet.get().to_dict()
can_num = can.get('canNum', 0)
pet_num = pet.get('petNum', 0)

can_num += 1
docCan.update({"canNum": can_num})