# Transport Management API (Minimal)

## Setup
* use your env
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_data
python manage.py runserver
```

# TODO - maybe /api/v1/ etc.? 
# TODO - security? JWT

## Endpoints
- CRUD:
  - `GET/POST /api/vehicles/`
  - `GET/POST /api/drivers/`F
  - `GET/POST /api/orders/`
- Assignment:
  - `POST /api/orders/{id}/assign-optimal-vehicle/`

## Test
curl -X POST http://127.0.0.1:8000/api/orders/1/assign-vehicle/


Docs:
- OpenAPI schema: `/api/schema/`
- Swagger UI: `/api/docs/`
