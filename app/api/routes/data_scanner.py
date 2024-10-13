from fastapi import APIRouter, Depends, HTTPException, Response, status
router = APIRouter()
from app.db.conn import db

@router.post("/companies/", status_code=status.HTTP_201_CREATED)
def create_company(company_data: dict, db=Depends(lambda: db)):
    try:
        # Aquí insertamos la compañía en Firestore
        doc_ref = db.collection('companies').add(company_data)
        return {"message": "Company created successfully", "company_id": doc_ref[1].id}

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to create company: {str(e)}"
        )