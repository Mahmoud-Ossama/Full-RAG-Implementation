from .BaseDataModel import BaseDataModel
from .db_schemas import Project
from .enums.DataBaseEnums import DataBaseEnum

class ProjectModel(BaseDataModel):
    def __init__(self, db_client: object):
        super().__init__(db_client=db_client)
        self.collection = db_client[DataBaseEnum.COLLECTION_PROJECT_NAME.value]
    
    async def create_project(self, project: Project):
        
        result = await self.collection.insert_one(
            project.model_dump(by_alias=True, exclude_unset=True)
        )
        project.id = result.inserted_id
        
        return project
    
    # Retrieve a project by its ID or create it if not exitst
    async def get_project_or_create_one(self, project_id: str):
        project = await self.collection.find_one({"project_id": project_id})

        if not project:
            # Create a new project
            new_project = Project(project_id=project_id)
            return await self.create_project(new_project)
        return Project(**project)
    
    # Get all projects, Count them, then split into pages
    async def get_all_projects_paginated(self, page: int, page_size: int=10):
        
        total_docs = await self.collection.count_documents({})
        
        calc_docs = total_docs // page_size
        if total_docs % page_size > 0:
            calc_docs += 1

        skip = (page - 1) * page_size
        cursor = await self.collection.find().skip(skip).limit(page_size).to_list(length=page_size)
        # docs = list(cursor)
        projects = []
        async for docs in cursor:
            projects.append(Project(**docs))
        return projects, total_pages


