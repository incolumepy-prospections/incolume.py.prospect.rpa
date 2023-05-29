from rocketry import Rocketry

app = Rocketry()


@app.task('minutely')
def a_cada_minuto():
    print('minuto a minuto')


@app.task('hourly')
def a_cada_hora():
    print('toda hora')


@app.task('daily')
def a_cada_dia():
    print('todo dia')


@app.task('weekly')
def a_cada_semana():
    print('toda semana')


@app.task('monthly')
def a_cada_mes():
    print('todo mes')


if __name__ == '__main__':
    app.run()
