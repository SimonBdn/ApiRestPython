from fastapi import FastAPI, HTTPException, Depends
from typing import List
import uvicorn
from database import database, products
from models import Product, ProductCreate, ProductUpdate

app = FastAPI(title="API REST avec Base de Données", version="1.0.0")

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/")
def read_root():
    return {"message": "Hello, World! API avec base de données"}

# Créer un produit
@app.post("/products/", response_model=Product)
async def create_product(product: ProductCreate):
    query = products.insert().values(
        name=product.name,
        description=product.description,
        price=product.price
    )
    last_record_id = await database.execute(query)
    
    # Récupérer le produit créé
    select_query = products.select().where(products.c.id == last_record_id)
    created_product = await database.fetch_one(select_query)
    return created_product

# Lire tous les produits
@app.get("/products/", response_model=List[Product])
async def get_products():
    query = products.select()
    return await database.fetch_all(query)

# Lire un produit par ID
@app.get("/products/{product_id}", response_model=Product)
async def get_product(product_id: int):
    query = products.select().where(products.c.id == product_id)
    product = await database.fetch_one(query)
    if product is None:
        raise HTTPException(status_code=404, detail="Produit non trouvé")
    return product

# Mettre à jour un produit
@app.put("/products/{product_id}", response_model=Product)
async def update_product(product_id: int, product: ProductUpdate):
    # Vérifier si le produit existe
    select_query = products.select().where(products.c.id == product_id)
    existing_product = await database.fetch_one(select_query)
    if existing_product is None:
        raise HTTPException(status_code=404, detail="Produit non trouvé")
    
    # Préparer les données à mettre à jour
    update_data = {}
    if product.name is not None:
        update_data["name"] = product.name
    if product.description is not None:
        update_data["description"] = product.description
    if product.price is not None:
        update_data["price"] = product.price
    
    if update_data:
        query = products.update().where(products.c.id == product_id).values(**update_data)
        await database.execute(query)
    
    # Retourner le produit mis à jour
    updated_product = await database.fetch_one(select_query)
    return updated_product

# Supprimer un produit
@app.delete("/products/{product_id}")
async def delete_product(product_id: int):
    query = products.select().where(products.c.id == product_id)
    product = await database.fetch_one(query)
    if product is None:
        raise HTTPException(status_code=404, detail="Produit non trouvé")
    
    delete_query = products.delete().where(products.c.id == product_id)
    await database.execute(delete_query)
    return {"message": "Produit supprimé avec succès"}

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)

