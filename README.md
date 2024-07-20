# Lease Document Abstractor

Lease Document Abstractor is a web application that automates the process of extracting key information from lease documents. This application allows users to upload PDF files of lease documents, processes the files to extract relevant clauses, and stores the extracted information in a database. Users can then view the uploaded documents and extracted clauses through the application.

## Features

- Automated PDF processing
- Accurate clause extraction
- Organized lease information storage
- Easy data retrieval

## Technologies Used

- Python
- Flask
- MySQL
- PyPDF2
- HTML/CSS

## Getting Started

### Prerequisites

- Python 3.x
- MySQL
- pip (Python package installer)

### Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/your-username/lease-document-abstractor.git
    cd lease-document-abstractor
    ```

2. **Create a virtual environment and activate it:**
    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up the MySQL database:**
    ```sh
    mysql -u yourusername -p
    mysql> SOURCE /path/to/leasedb.sql;
    ```

5. **Set environment variables:**

    On Windows (PowerShell):
    ```powershell
    $env:MYSQL_HOST="localhost"
    $env:MYSQL_USER="yourusername"
    $env:MYSQL_PASSWORD="yourpassword"
    $env:MYSQL_DATABASE="leasedb"
    ```

    On macOS/Linux:
    ```sh
    export MYSQL_HOST="localhost"
    export MYSQL_USER="yourusername"
    export MYSQL_PASSWORD="yourpassword"
    export MYSQL_DATABASE="leasedb"
    ```

### Running the Application

1. **Start the Flask application:**
    ```sh
    python -m flask run
    ```

2. **Open your web browser and navigate to:**
    ```
    http://127.0.0.1:5000
    ```

### Project Structure

lease-document-abstractor/
│
├── app.py # Main Flask application
├── requirements.txt # Python dependencies
├── templates/
│ ├── upload.html # Upload page template
│ └── view.html # View abstracts page template
└── static/
└── styles.css # CSS styles




### Usage

1. **Upload a Lease Document:**
    - Navigate to the upload page.
    - Select a PDF file and click the "Upload" button.

2. **View Extracted Information:**
    - Navigate to the view abstracts page to see the list of uploaded documents and the extracted clauses.

### Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

### Contact

For any inquiries or support, please contact [ritamjash8@gmail.com.com].

