# Main Author: Luke Newman
# Date Created: Sept.20, 2021
# Date Last Modified: Sept.20, 2021

from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
