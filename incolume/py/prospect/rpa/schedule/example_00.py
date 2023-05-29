from rocketry import Rocketry

app = Rocketry()

@app.task('minutely')
def a_cada_minuto():
    print('minuto a minuto')

@app.task('hourly')
def a_cada_hora():
    print('toda hora')


if __name__ == '__main__':
    app.run()
