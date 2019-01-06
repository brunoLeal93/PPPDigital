from pymongo import MongoClient

client = MongoClient("mongodb://admin:admin@cluster0-shard-00-00-umdst.mongodb.net:27017,cluster0-shard-00-01-umdst.mongodb.net:27017,cluster0-shard-00-02-umdst.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")
db = client.BasePPPDigital

class Cotacao():

    def cotVisuPrin(self):
        coll = db.Cotacao

        pipeline= [
            {
                "$group": {"_id": "$fonte", "mercados": {"$addToSet": "$mercado"}, "tp_instr": {"$addToSet": "$tp_instrumento"}}
            }
        ]

        vet = list(coll.aggregate(pipeline))
        return vet

#a = Cotacao().cotVisuPrin()

#print(a)
