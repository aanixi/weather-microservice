# Weather Microservice

This is a FastAPI based microservice that fetches the weather data for given city from OpenWeatherMap.

## Start
1. Ensure Python 3.9+ and 'pip' are installed.
2. Install requied libraries (if not yet installed):
```
pip install fastapi uvicorn requests
```
3. Start the server:
```
uvicorn main:app --host 0.0.0.0 --port 8080 --reload
```
## Testing
**Test in browser (Swagger UI):**
http://localhost:8080/docs

**Test in terminal:**
curl "http://localhost:8080/weather?city=Helsinki"

## Example result
```json
{
  "city": "Helsinki",
  "temperature": 2.5,
  "description": "clear sky"
}
