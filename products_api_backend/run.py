from app import app

if __name__ == "__main__":
    # Development server; bind to 0.0.0.0 for container usage
    app.run(host="0.0.0.0", port=3001, debug=True)
