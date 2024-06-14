# BOOKMANAGER

## Description

**This project is a Python application for managing users, books, and reviews in a SQLite database. It provides functionalities to create, retrieve, update, and delete users, books, and reviews through a Command-Line Interface (CLI).**

### Features

    Users Management:
        Create a new user with name, email, and age.
        Retrieve user details by ID.
        Update user email.
        Delete a user.
        Get all users or users within a specified age range.

    Books Management:
        Create a new book with title, author, genre, year, and associated user ID.
        Retrieve book details by ID.
        Update book title.
        Delete a book.
        Get all books associated with a user ID.

    Reviews Management:
        Create a new review with user ID, book ID, review text, and rating.
        Retrieve review details by ID.
        Update review text and rating.
        Delete a review.
        Get all reviews written by a specific user.

## Installation

Clone the repository:
    
`git clone <repository-url>`

Navigate to the project directory:

`bash`

`cd project-directory`

Install dependencies using Pipenv 

`pipenv install`
`pipenv shell`

    
## Usage
1.Run config.py to setup the database
`Python config.py`

2.Run the CLI application:

`python cli.py`

    Follow the prompts to interact with the application:
        Choose options to manage users, books, and reviews.
        Enter data as prompted for creation, retrieval, update, and deletion operations.

## Project Structure

project/
│
├── lib/
│   ├── config.py       # Database connection setup
│   ├── user.py         # Users class for user management
│   ├── book.py         # Books class for book management
│   ├── review.py       # Reviews class for review management
│   
│── main.py             # contains test usage cases
├── cli.py              # Command-Line Interface script
├── Pipfile             # Pipenv configuration file
├── Pipfile.lock        # Pipenv lock file
├── README.md           # Project documentation
└── database.db         # SQLite database file

## Dependencies

    Python 3.8
    Pipenv (for managing dependencies)
    SQLite3 (for database operations)

## Contributing

    Fork the repository and clone it locally.
    Create a new branch for your feature or bug fix.
    Make changes and test thoroughly.
    Commit your changes and push to your fork.
    Submit a pull request with a clear description of your changes.

## License

[we are one big family, we are 808
instagram 808_zic
]

## Acknowledgements

    [ RHONA JOY:MENTOR AND TUTOR ]