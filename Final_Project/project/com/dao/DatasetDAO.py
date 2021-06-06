from project.com.dao import con


class DatasetDAO:

    def insertDataset(self,datasetVO):

        try:
            connection = con()
            cursur = connection.cursor()

            cursur.execute(
                "INSERT INTO datasetmaster(datasetName,datasetPath,datasetDescription) VALUES ('" + datasetVO.datasetName + "','" + datasetVO.datasetPath + "','" + datasetVO.datasetDescription + " ') ")

            connection.commit()
            cursur.close()
            connection.close()
        except Exception:
            raise Exception

    def viewDataset(self):
        try:
            connection = con()
            cursur = connection.cursor()
            cursur.execute("SELECT * FROM datasetmaster WHERE datasetActiveStatus='active' ")
            data = cursur.fetchall()
            connection.commit()
            cursur.close()
            connection.close()
            return data
        except Exception:
            raise Exception

    def deleteDataset(self,datasetVO):
        try:
            connection = con()
            cursur = connection.cursor()
            cursur.execute("UPDATE datasetmaster SET datasetActiveStatus='deactive'  WHERE datasetId='" + datasetVO.datasetId + " '")
            #data = cursur.fetchall()
            connection.commit()
            cursur.close()
            connection.close()
        except Exception:
            raise Exception


