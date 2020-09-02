#!/usr/bin/python3
"""
script to start Flash web application
listens on 0.0.0.0, port 5000
uses storage to fetch data from storage engine
declares method to teardown SQLAlchemy session
routes:
/states_list: displays HTML page with State and list of all state objects
"""
if __name__ == '__main__':
    from flask import Flask
    from flask import render_template
    from models import storage
    app = Flask(__name__)

    @app.route('/states_list', strict_slashes=False)
    def states_list():
        """
        fetches data from storage engine and displays rendered HTML page
        """
        states_result = storage.all(State)
        return render_template('7-states_list', states_result=states_result)

    @app.teardown_appcontext
    def teardown():
        """
        removes current SQLAlchemy Session after each request
        """
        storage.close()

    app.run(host='0.0.0.0', port='5000')
