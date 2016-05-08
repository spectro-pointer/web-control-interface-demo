# Spectro pointer control interface

![Spectropointer Raspberry Pi control interface](https://github.com/sasha42/Spectropointer-server/raw/master/templates/spectropointer-video.gif)

The spectro pointer maps out the sky and orients itself automatically to any new bright objects, identifying them using an on-board spectrometer. It is controlled by 4 Raspberry Pi's. This git is the interface to manually pilot the motor driver, using a Flask microservice and a XML-RPC controller. For more information, please ask Gustavo or [Patrick](https://fixme.ch/wiki/User:Pherjung) from [FIXME](https://fixme.ch/).

## Running the app
```python
# Enter the URL of your server on line 7 in app.py
pip install -r requirements.txt
python app.py
```