# -*- coding: utf8 -*-
"""
Created by Leon on 2017/3/15.
"""
from flask import Flask, render_template, jsonify, request
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor

app = Flask(__name__)

app.config.from_pyfile("config.py")

mysql = MySQL()

mysql.init_app(app)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/api/iot')
def iot_api():
    start_time = request.args.get('start_time')
    end_time = request.args.get('end_time')
    time_format = "%Y-%m-%d %H:%M"
    cursor = mysql.get_db().cursor(DictCursor)
    result = []

    

    cursor.execute("select * from datasource "
                   "where sendtime<%s and sendtime>%s",
                   (end_time, start_time))
    for d in cursor.fetchall():
        result.append({"send_time": d['sendtime'].strftime(time_format),
                       "data1": int(d['data_1']), 'data2': int(d['data_2']),
                       "data3": int(d['data_3']), 'data4': int(d['data_4']),
                       'data5': int(d['data_5']),
                       })

    return jsonify({"status": 0, "result": result})


if __name__ == '__main__':
    app.run()
