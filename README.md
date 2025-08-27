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
  - `GET/POST /api/drivers/`
  - `GET/POST /api/orders/`
- Assignment:
  - `POST /api/orders/{id}/assign-optimal-vehicle/`

Docs:
- OpenAPI schema: `/api/schema/`
- Swagger UI: `/api/docs/`
