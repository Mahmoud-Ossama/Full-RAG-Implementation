from .BaseDataModel import BaseDataModel
from .db_schemas import DataChunks
from .enums.DataBaseEnums import DataBaseEnum
from bson.objectid import ObjectId
from pymongo import InsertOne

class ChunkModel(BaseDataModel):
    def __init__(self, db_client: object):
        super().__init__(db_client=db_client)
        self.collection = db_client[DataBaseEnum.COLLECTION_CHUNKS_NAME.value]
        
    async def create_chunk(self, chunk: DataChunks):
        result = await self.collection.insert_one(
            chunk.model_dump(by_alias=True, exclude_unset=True)
        )
        chunk.id = result.inserted_id
        return chunk
    
    async def get_chunk(self, chunk_id: str):
        chunk = await self.collection.find_one({"_id": ObjectId(chunk_id)})
        if not chunk:
            return None
        return DataChunks(**chunk)
    
    async def update_chunk(self, chunk_id: str, chunk: DataChunks):
        result = await self.collection.replace_one(
            {"_id": ObjectId(chunk_id)},
            chunk.model_dump(by_alias=True, exclude_unset=True)
        )
        if not result.matched_count:
            return None
        return await self.get_chunk(chunk_id)
    
    async def insert_many_chunks(self, chunks: list, batch_size: int = 100):
        for i in range(0, len(chunks), batch_size):
            batch = chunks[i:i + batch_size]
            operations = [
                InsertOne(
                    chunk.model_dump(by_alias=True, exclude_unset=True)
                )
                for chunk in batch
            ]
            await self.collection.bulk_write(operations)
        return len(chunks)
    
    async def delet_chunk_by_project_id(self, project_id: str):
        result = await self.collection.delete_many(
            {
                "chunk_project_id": project_id,
                
            }
            )
        return result.deleted_count 