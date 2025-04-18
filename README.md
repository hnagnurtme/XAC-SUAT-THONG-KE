# Domicare API Documentation

## Overview
The **Domicare API** provides a comprehensive set of endpoints to manage users, roles, permissions, products, categories, bookings, reviews, and file uploads for the Domicare application. This API is designed for a service-oriented platform, likely focused on home care or e-commerce services. The API follows the **OpenAPI 3.0.1** specification and is licensed under **Apache 2.0**.

- **Base URL**: `http://localhost:8080` (development server)
- **Version**: 1.0.0
- **Purpose**: Facilitate user management, service bookings, product browsing, and administrative tasks with role-based access control (RBAC).

## Authentication
The API supports multiple authentication mechanisms:
- **Email/Password Login**: Use `POST /login` to obtain access and refresh tokens.
- **Token Refresh**: Use `POST /refresh-token` to refresh an access token.
- **OAuth2**: Use `GET /auth/callback` to exchange an authorization code.
- **Email Verification**: Required for new users via `GET /verify-email`.
- **Password Reset**: Supported via `POST /reset-password` and `GET /email/reset-password`.

**Note**: Most endpoints require authentication (e.g., Bearer tokens). Public endpoints (e.g., `/api/public/products`) are accessible without authentication.

## Key Endpoints
The API is organized into controllers, each handling specific functionalities. Below is a summary of the main endpoints grouped by controller.

### 1. User Controller
Manages user accounts and roles.

| Method | Endpoint                | Description                              | Request Body                     | Response                     |
|--------|-------------------------|------------------------------------------|----------------------------------|------------------------------|
| GET    | `/users`                | Retrieves a paginated list of users      | -                                | `ResultPagingDTO`            |
| PUT    | `/users`                | Updates user details                     | `UpdateUserRequest`              | `UserDTO`                    |
| PUT    | `/users/roles`          | Updates roles for a user                 | `UpdateRoleForUserRequest`       | `UserDTO`                    |
| GET    | `/users/{id}`           | Fetches a user by ID                     | -                                | `UserDTO`                    |
| DELETE | `/users/{id}`           | Deletes a user by ID                     | -                                | -                            |

**Query Parameters for GET /users**:
- `page` (optional, default: 1)
- `size` (optional, default: 20)
- `searchName` (optional)
- `sortBy` (optional, default: `id`)
- `sortDirection` (optional, default: `asc`)
- `spec` (required, `SpecificationUser`)
- `pageable` (required, `Pageable`)

### 2. Role Controller
Manages roles for access control.

| Method | Endpoint                | Description                              | Request Body                     | Response                     |
|--------|-------------------------|------------------------------------------|----------------------------------|------------------------------|
| GET    | `/roles`                | Retrieves all roles                      | -                                | Object                       |
| POST   | `/roles`                | Creates a new role                       | `RoleDTO`                        | `RoleDTO`                    |
| PUT    | `/roles`                | Updates a role                           | `RoleDTO`                        | `RoleDTO`                    |
| GET    | `/roles/{id}`           | Fetches a role by ID                     | -                                | Object                       |
| DELETE | `/roles/{id}`           | Deletes a role by ID                     | -                                | -                            |

### 3. Permission Controller
Manages permissions for RBAC.

| Method | Endpoint                | Description                              | Request Body                     | Response                     |
|--------|-------------------------|------------------------------------------|----------------------------------|------------------------------|
| GET    | `/permissions`          | Retrieves permissions                    | -                                | Object                       |
| POST   | `/permissions`          | Creates a new permission                 | `Permission`                     | `Permission`                 |
| PUT    | `/permissions`          | Updates a permission                     | `Permission`                     | `Permission`                 |
| GET    | `/permissions/{id}`     | Fetches a permission by ID               | -                                | Object                       |
| DELETE | `/permissions/{id}`     | Deletes a permission by ID               | -                                | -                            |

**Query Parameters for GET /permissions**:
- `search` (optional)
- `pageable` (required, `Pageable`)

### 4. Product Controller
Manages products and their images.

| Method | Endpoint                     | Description                              | Request Body                     | Response                     |
|--------|------------------------------|------------------------------------------|----------------------------------|------------------------------|
| POST   | `/api/products`              | Creates a new product                    | `AddProductRequest`              | Object                       |
| PUT    | `/api/products`              | Updates a product                        | `UpdateProductRequest`           | Object                       |
| DELETE | `/api/products/{id}`         | Deletes a product by ID                  | -                                | Object                       |
| PUT    | `/api/products/images`       | Uploads a product image                  | `AddProductImageRequest`         | Object                       |
| GET    | `/api/public/products`       | Retrieves a paginated list of products   | -                                | Object                       |
| GET    | `/api/public/products/{id}`  | Fetches a product by ID                  | -                                | Object                       |

**Query Parameters for GET /api/public/products**:
- `categoryId` (optional, default: 0)
- `page` (optional, default: 1)
- `size` (optional, default: 20)
- `searchName` (optional)
- `sortBy` (optional, default: `id`)
- `sortDirection` (optional, default: `asc`)
- `spec` (required, `SpecificationProduct`)
- `pageable` (required, `Pageable`)

### 5. Category Controller
Manages product categories.

| Method | Endpoint                     | Description                              | Request Body                     | Response                     |
|--------|------------------------------|------------------------------------------|----------------------------------|------------------------------|
| POST   | `/api/categories`            | Creates a new category                   | `AddCategoryRequest`             | Object                       |
| PUT    | `/api/categories`            | Updates a category                       | `UpdateCategoryRequest`          | Object                       |
| DELETE | `/api/categories/{id}`       | Deletes a category by ID                 | -                                | Object                       |
| GET    | `/api/public/categories`     | Retrieves a paginated list of categories | -                                | `ResultPagingDTO`            |
| GET    | `/api/public/categories/{id}`| Fetches a category by ID                 | -                                | Object                       |

**Query Parameters for GET /api/public/categories**:
- `page` (optional, default: 1)
- `size` (optional, default: 20)
- `sortBy` (optional, default: `id`)
- `sortDirection` (optional, default: `asc`)
- `spec` (required, `SpecificationCategory`)
- `pageable` (required, `Pageable`)

### 6. Booking Controller
Manages service bookings.

| Method | Endpoint                     | Description                              | Request Body                     | Response                     |
|--------|------------------------------|------------------------------------------|----------------------------------|------------------------------|
| POST   | `/api/bookings`              | Creates a new booking                    | `BookingRequest`                 | `BookingDTO`                 |
| PUT    | `/api/bookings`              | Updates a booking                        | `UpdateBookingRequest`           | `BookingDTO`                 |
| PUT    | `/api/bookings/status`       | Updates a booking status                 | `UpdateBookingStatusRequest`     | `BookingDTO`                 |
| GET    | `/api/bookings/{id}`         | Fetches a booking by ID                  | -                                | `BookingDTO`                 |
| DELETE | `/api/bookings/{id}`         | Deletes a booking by ID                  | -                                | -                            |

### 7. Review Controller
Manages product reviews.

| Method | Endpoint                     | Description                              | Request Body                     | Response                     |
|--------|------------------------------|------------------------------------------|----------------------------------|------------------------------|
| GET    | `/api/reviews`               | Retrieves a paginated list of reviews    | -                                | Object                       |
| POST   | `/api/reviews`               | Creates a new review                     | `ReviewRequest`                  | `ReviewDTO`                  |

**Query Parameters for GET /api/reviews**:
- `page` (optional, default: 1)
- `size` (optional, default: 20)
- `sortBy` (optional)
- `sortDirection` (optional, default: `asc`)
- `spec` (required, `SpecificationReview`)
- `pageable` (required, `Pageable`)

### 8. File Controller
Manages file uploads and retrieval via Cloudinary.

| Method | Endpoint                     | Description                              | Request Body                     | Response                     |
|--------|------------------------------|------------------------------------------|----------------------------------|------------------------------|
| POST   | `/api/cloudinary/files`      | Uploads a file                           | `{ "file": "binary" }`           | Object                       |
| GET    | `/api/cloudinary/files`      | Fetches a file by name                   | -                                | Object                       |
| GET    | `/api/cloudinary/files/{id}` | Fetches a file by ID                     | -                                | Object                       |
| DELETE | `/api/cloudinary/files/{id}` | Deletes a file by ID                     | -                                | Object                       |
| GET    | `/api/cloudinary/files/all`  | Retrieves all files                      | -                                | Object                       |

**Query Parameters for GET /api/cloudinary/files**:
- `name` (required)

### 9. Authentication Controller
Handles user authentication and registration.

| Method | Endpoint                     | Description                              | Request Body                     | Response                     |
|--------|------------------------------|------------------------------------------|----------------------------------|------------------------------|
| POST   | `/login`                     | Authenticates a user                     | `LoginRequest`                   | `LoginResponse`              |
| POST   | `/register`                  | Registers a new user                     | `RegisterRequest`                | `RegisterResponse`           |
| POST   | `/refresh-token`             | Refreshes an access token                | `RefreshTokenRequest`            | `RefreshTokenResponse`       |
| POST   | `/reset-password`            | Resets a user’s password                 | `UserDTO`                        | -                            |

### 10. Email Sending Controller
Manages email-related operations.

| Method | Endpoint                     | Description                              | Request Body                     | Response                     |
|--------|------------------------------|------------------------------------------|----------------------------------|------------------------------|
| GET    | `/email/verify`              | Sends an email verification link         | -                                | Object                       |
| GET    | `/email/reset-password`      | Sends a password reset email             | -                                | Object                       |

**Query Parameters**:
- `email` (required)

### 11. OAuth2 Controller
Handles OAuth2 authentication.

| Method | Endpoint                     | Description                              | Request Body                     | Response                     |
|--------|------------------------------|------------------------------------------|----------------------------------|------------------------------|
| GET    | `/auth/callback`             | Exchanges an authorization code           | -                                | Object                       |

**Query Parameters**:
- `code` (required)

### 12. View Controller
Handles email verification and password reset views.

| Method | Endpoint                     | Description                              | Request Body                     | Response                     |
|--------|------------------------------|------------------------------------------|----------------------------------|------------------------------|
| GET    | `/verify-email`              | Verifies a user’s email                  | -                                | String                       |
| GET    | `/forgot-password`           | Handles forgot password flow             | -                                | String                       |

**Query Parameters**:
- `token` (required)

## Schemas
The API defines several schemas for request and response bodies. Key schemas include:

- **UserDTO**: Represents a user with fields like `id`, `name`, `email`, `roles`, `gender`, and `dateOfBirth`.
- **RoleDTO**: Defines a role with `id`, `name`, and `description`.
- **Permission**: Represents a permission with `id`, `name`, `apiPath`, `method`, and `module`.
- **ProductDTO**: Describes a product with `id`, `name`, `price`, `discount`, and `reviewDTOs`.
- **CategoryDTO**: Represents a category with `id`, `name`, and associated `products`.
- **BookingDTO**: Defines a booking with `id`, `address`, `totalHours`, `bookingStatus`, and associated `products` and `userDTO`.
- **ReviewDTO**: Represents a review with `id`, `rating`, `comment`, and references to `userDTO` and `productId`.
- **ResultPagingDTO**: Used for paginated responses, containing `meta` (page, size, total) and `data`.

## Example Usage
### Register a New User
```bash
curl -X POST http://localhost:8080/register \
-H "Content-Type: application/json" \
-d '{
  "email": "user@example.com",
  "password": "Password123"
}'
```
**Response**:
```json
{
  "id": 1,
  "email": "user@example.com",
  "emailConfirmed": false,
  "emailConfirmationToken": "abc123",
  "roles": ["USER"]
}
```

### Login
```bash
curl -X POST http://localhost:8080/login \
-H "Content-Type: application/json" \
-d '{
  "email": "user@example.com",
  "password": "Password123"
}'
```
**Response**:
```json
{
  "accessToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "refreshToken": "xyz789",
  "user": {
    "id": 1,
    "email": "user@example.com",
    "name": "John Doe"
  }
}
```

### Create a Booking
```bash
curl -X POST http://localhost:8080/api/bookings \
-H "Content-Type: application/json" \
-H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..." \
-d '{
  "userId": 1,
  "productIds": [1, 2],
  "address": "123 Main St",
  "totalHours": 2.5,
  "isPeriodic": false,
  "note": "Please arrive by 9 AM"
}'
```
**Response**:
```json
{
  "id": 1,
  "address": "123 Main St",
  "totalHours": 2.5,
  "totalPrice": 50.0,
  "bookingStatus": "PENDING",
  "userDTO": { "id": 1, "name": "John Doe" },
  "products": [{ "id": 1, "name": "Cleaning Service" }]
}
```

## Notes
- **Pagination**: Use `page`, `size`, `sortBy`, and `sortDirection` for paginated endpoints.
- **File Uploads**: The `/api/cloudinary/files` POST endpoint expects `multipart/form-data` for file uploads (current schema may need correction).
- **Security**: Ensure proper authentication and authorization for private endpoints. Public endpoints should be used cautiously to avoid data exposure.
- **Error Handling**: The API spec does not define detailed error responses. Clients should handle standard HTTP status codes (e.g., 400, 401, 404).

## Contact
For further details or support, refer to the Domicare application documentation or contact the development team.
