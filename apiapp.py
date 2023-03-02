from fastapi import FastAPI

app = FastAPI()

richest_list = {
    "Elon Musk":"280 Billion USD",
    "Jeff Bezos":"250 Billion USD",
    "Bill Gates":"190 Billion USD",
    "Mark Zuckerberg":"150 Billion USD"
}

@app.get("/richest-people")
def richest_people():
    return richest_list