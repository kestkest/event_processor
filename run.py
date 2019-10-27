from event_processor.app import create_app
app = create_app('settings.py')

if __name__ == "__main__":
    app.run(port=5000, debug=True)
