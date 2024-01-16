from flask import Flask


# Init flash APP
app = Flask(__name__)
# main
@app.route( '/', methods=['GET','POST'])
def main():
    return 'MON APPLICATION'

@app.route('/hetic', methods=['GET','POST'])
def main_hetic():
    return 'MON APPLICATIONd  DE TEST'
 
if __name__ == '__main__':
 app.run("0.0.0.0", port=80)