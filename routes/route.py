from fastapi import APIRouter
from models.model import Allocation
from config.db import conn
from schemas.schema import allocation, allocations
from bson import ObjectId
from datetime import date

allo = APIRouter() #apirouter instance

#for fetching all allocations
@allo.get('/') 
async def get_allocations():
    return allocations(conn.local.allo.find())

#for creating new allocation
@allo.post('/')
async def create_allocation(newAllocation: Allocation):
    allocationDict = dict(newAllocation)
    
    if allocationDict['allocation_date'] > str(date.today()):
        conn.local.allo.insert_one(dict(newAllocation))
        return allocations(conn.local.allo.find())
    else:
        return {"error": "Invalid date"}

#for uptading an existing allocation
@allo.put('/{id}')
async def update_allocation(id):
    # updatedAllocationDict = dict(updatedAllocation)
    newUpdatedAllocationDict = dict(allocation(conn.local.allo.find_one({"_id": ObjectId(id)})))
    newUpdatedAllocationDict["allocation_date"] = str(date.today())
    # updatedAllocationDict['allocation_date'] = str(date.today())
    conn.local.allo.find_one_and_update({"_id": ObjectId(id)}, {"$set": newUpdatedAllocationDict})
    # conn.local.allo
    return allocation(conn.local.allo.find_one({"_id": ObjectId(id)}))
   
#for deleting an existing allocation
@allo.delete('/{id}')
async def delete_allocation(id):
    allocationToDelete = dict(allocation(conn.local.allo.find_one({"_id": ObjectId(id)})))
    if allocationToDelete["allocation_date"] > str(date.today()):
        conn.local.allo.find_one_and_delete({"_id": ObjectId(id)})
        return allocations(conn.local.allo.find())
    else:
        return {"error": "Allocation must be deleted before the allocated date"}