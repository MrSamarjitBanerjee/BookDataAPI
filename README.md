# BookDataAPI  📚

This is a Django-based RESTful API for managing books, reviews, and genres. The API allows authenticated users to view and create reviews, search for books, and admins to manage books and genres. The API is secured with JWT authentication and supports rate-limiting for both anonymous and authenticated users.

Features
View and Search Books: Anyone can view the list of books and search by title, author, or genre.

Book Reviews: Authenticated users can post reviews, and all users can view reviews for any book.

Admin Permissions: Only admin users can create, update, or delete books and genres.

Rate Limiting: Custom rate limiting for both anonymous and authenticated users to prevent abuse.

JWT Authentication: Secured endpoints using JWT tokens.

Pagination: Paged results for books.

## API Endpoints 🌐

### Authentication & Account
| Endpoint                | Description           | Method |
|------------------------|-----------------------|--------|
| `/account/register/`   | User registration      | `POST` |
| `/account/login/`      | User login             | `POST` |
| `/account/logout/`     | User logout            | `POST` |

---

### Books API
| Endpoint                                | Description                       | Method                   | Authorization   | Rate Limit                     |
|-----------------------------------------|-----------------------------------|--------------------------|------------------|---------------------------------|
| `/api/books/`                          | List all books                   | `GET`                    | Public           | Anon: 10/min, User: 15/min    |
| `/api/books/create/`                   | Add a new book                   | `POST`                   | Admin Only       | None                            |
| `/api/books/<BOOK_ID>/edit/`          | View, update, or delete a book   | `GET`, `PUT`, `POST`, `DELETE` | Admin Only       | None                            |
| `/api/books/<BOOK_ID>/`                | View a specific book by ID       | `GET`                    | Authorized Users  | Anon: 10/min, User: 15/min    |
| `/api/books/<BOOK_ID>/reviews/`       | View all reviews for a book      | `GET`                    | Authorized Users  | Anon: 10/min, User: 15/min    |

---

### Genres API (Admin Only)
| Endpoint                       | Description                     | Method  |
|--------------------------------|---------------------------------|---------|
| `/api/genres/`                | List all genres                | `GET`   |
| `/api/genres/<ID>/`           | Retrieve a specific genre      | `GET`   |
| `/api/genres/`                | Create a new genre             | `POST`  |
| `/api/genres/<ID>/`           | Update a genre completely      | `PUT`   |
| `/api/genres/<ID>/`           | Partially update a genre       | `PATCH` |
| `/api/genres/<ID>/`           | Delete a genre                 | `DELETE`|

---

### Reviews API
| Endpoint                         | Description               | Method                   | Authorization      | Rate Limit                     |
|----------------------------------|---------------------------|--------------------------|---------------------|---------------------------------|
| `/api/reviews/`                 | List all reviews          | `GET`                    | Public              | Anon: 10/min, User: 15/min    |
| `/api/reviews/<ID>/`            | View a specific review    | `GET`                    | Authenticated Users  | Anon: 10/min, User: 15/min    |
| `/api/reviews/<ID>/edit/`       | Update or delete a review | `PUT`, `PATCH`, `DELETE` | Admin Only          | None                            |
| `/api/reviews/create/`          | Create a new review       | `POST`                   | Authenticated Users   | Anon: 10/min, User: 15/min    |

---

### Admin Panel
| Endpoint           | Description                
|--------------------|------------------------
| `/adminpanel/`     | Access the admin panel     


## USAGE

Setup Instructions
1. Clone the repository
bash
Copy code
git clone https://github.com/your-username/book-data-api.git
cd book-data-api
2. Install dependencies
bash
Copy code
pip install -r requirements.txt
3. Run migrations
bash
Copy code
python manage.py migrate
4. Create a superuser (admin)
bash
Copy code
python manage.py createsuperuser
5. Run the development server
bash
Copy code
python manage.py runserver
