'''
  @description platform for hackatren 2018
  @author Daniel Sarabusing
'''

'''
 @description all imports for flask, threading, socket
'''
from threading import Lock
from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, Namespace, emit, join_room, leave_room, close_room, rooms, disconnect

'''
 @description variable declarations and initializations
'''

# @description for async_mode
async_mode=None

# @description init for flask app
app = Flask(__name__)
# @description setting flask app config secret key
app.config['SECRET_KEY'] = 'secret!'
# @description init for sockets wrap into the flask app
socketio = SocketIO(app, async_mode=async_mode)
# @description for thread
thread = None
# @description init for thread lock
thread_lock = Lock()

'''
 @description routes
'''
@app.route('/')
def index():
  return render_template('index.html', async_mode=socketio.async_mode)

'''
  @class TrainLocatorSpace
  @description all events for train locator
'''
class TrainLocatorSpace(Namespace):
    def on_connect(self):
        emit('server_response', {'data': 'Hello, world'})

'''
  @class TrainStatusSpace
  @description all events for train status
'''
class TrainStatusSpace(Namespace):
    def on_connect(self):
        pass

'''
  @class TrainMyTravelSpace
  @description all events for train my travel
'''
class TrainMyTravelSpace(Namespace):
    def on_connect(self):
        pass

'''
  Register namepsace
'''
socketio.on_namespace(TrainLocatorSpace('/train/locator'))

if __name__ == '__main__':
  socketio.run(app, debug=True)
