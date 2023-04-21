from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse

app = FastAPI()
app.title = "Mi Aplicacion con FastApi"
app.version = "0.0.3"

movies = [
    {
		"id": 1,
		"title": "Avatar",
		"overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
		"year": "2009",
		"rating": 7.8,
		"category": "ficcion"
	},
    {
		"id": 2,
		"title": "Avatar2",
		"overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
		"year": "2010",
		"rating": 7.8,
		"category": "Acción"
	}
]

@app.get("/", tags=['HOME'])
def messange():
    return HTMLResponse('<h1>Hello Wordl!</h1>')


@app.get('/movies', tags=['MOVIES'])
def getmovies():
    return movies


@app.get('/movies/{id}', tags=['MOVIES'])
def get_movie(id: int):
    for item in movies:
        if item["id"] == id:
            return item
    return []

@app.get('/movies/', tags=['MOVIES'])
def get_movies_by_category(category: str, year: int):
    return [ item for item in movies if item['category'] == category]

@app.post('/movies', tags=['MOVIES'])
def create_movie(id: int = Body(), title: str = Body(), overview:str = Body(), year:int = Body(), rating: float = Body(), category: str = Body()):
    movies.append({
        "id": id,
        "title": title,
        "overview": overview,
        "year": year,
        "rating": rating,
        "category": category
    })
    return movies

@app.put('/movies/{id}', tags=['MOVIES'])
def update_movie(id: int, title: str = Body(), overview:str = Body(), year:int = Body(), rating: float = Body(), category: str = Body()):
	for item in movies:
		if item["id"] == id:
			item['title'] = title,
			item['overview'] = overview,
			item['year'] = year,
			item['rating'] = rating,
			item['category'] = category
			return movies


@app.delete('/movies/{id}', tags=['MOVIES'])
def delete_movie(id: int):
    for item in movies:
        if item["id"] == id:
            movies.remove(item)
            return movies

