from fastapi import FastAPI
import api.products as products
import api.sales as sales
import api.inventory as inventory
import api.revenue as revenue

app = FastAPI()

app.include_router(products.app)
app.include_router(sales.app)
app.include_router(inventory.app)
app.include_router(revenue.app)




if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=9000)






