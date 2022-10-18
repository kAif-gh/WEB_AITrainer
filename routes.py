from flask import Flask, render_template, Response, request
import cv2
from Models.improvedCode import utils as u
import numpy as np

from Models.shoulders.overheadpress import *
from Models.shoulders.dips import *
from Models.shoulders.pikepress import *
from Models.shoulders.renegadeRow import *
from Models.shoulders.snatchGripLowPull import *

from Models.legs.squats import *
from Models.legs.SinglelegGlute import *
from Models.legs.Reverselunges import *
from Models.legs.RomanionSquats import *
from Models.legs.LateralLegRaisesRightSIDE import LateralLegRaisesRightSIDE

from Models.chest.BarbellBenchPress import *
from Models.chest.dips import *
from Models.chest.DumbbellBenchPress import *
from Models.chest.pushups import *
from Models.chest.Widepushups import *
from Models.chest.Diamondpushups import *
from Models.chest.ChestFly import *

from Models.back.BentoverRow import *
from Models.back.Deadlift import *
from Models.back.DumbbellSingleArmRow import *
from Models.back.LatPullDown import *
from Models.back.Pullups import *


from Models.others.Newcurl import *
from Models.others.Plank import *



from Models.improvedCode.camera import Camera
app = Flask(__name__)
# from seconderoute import second
# app.register_blueprint(second, url_prefix='/test')

@app.route('/')
@app.route('/index')
def home_page():
    return render_template('index.html')

@app.route('/Exercises')
def exercices_page():
    return render_template('Exercises.html')

@app.route('/page-user')
def user_page():
     return render_template('page-user.html')


# /////////////////////////////////////
# ///////////////////// shoulder Cycle Routes//////////////////////////////

@app.route('/shoulder')
def shoulder_page():
    return render_template('shoulder_cycle.html')

@app.route('/pikePressCycle')
def pikePressCycle():
    return render_template('pikePressCycle.html')

@app.route('/DipsShoulderCycle')
def DipsShoulderCycle():
    return render_template('DipsShoulderCycle.html')
@app.route('/renegadeRowCycle')
def renegadeRowCycle():
    return render_template('renegadeRowCycle.html')
@app.route('/snatchgripCycle')
def snatchgripCycle():
    return render_template('snatchgripCycle.html')

# ///////////////////// legs Cycle Routes//////////////////////////////


@app.route('/legs')
def legs_page():
    return render_template('legs_cycle.html')

@app.route('/LateralLegCycle')
def LateralLegCycle():
    return render_template('laterallegCycle.html')

@app.route('/reverselungesCycle')
def reverselungesCycle():
    return render_template('reverselungesCycle.html')
@app.route('/romanionsquatCycle')
def romanionsquatCycle():
    return render_template('romanionsquatCycle.html')
@app.route('/singleleggluteCycle')
def singleleggluteCycle():
    return render_template('singleleggluteCycle.html')

# ///////////////////// Chest Cycle Routes//////////////////////////////


@app.route('/chest')
def chest_page():
    return render_template('chest_cycle.html')

@app.route('/BarbellBenchPressCycle')
def BarbellBenchPressCycle():
    return render_template('BarbellBenchPressCycle.html')
@app.route('/ChestflyCycle')
def ChestflyCycle():
    return render_template('ChestflyCycle.html')
@app.route('/DipsChestCycle')
def DipsChestCycle():
    return render_template('DipsChestCycle.html')
@app.route('/pushupCycle')
def pushupCycle():
    return render_template('pushupCycle.html')
@app.route('/widePushupCycle')
def widePushupCycle():
    return render_template('widePushupCycle.html')
@app.route('/DiamondPushupCycle')
def DiamondPushupCycle():
    return render_template('DiamondPushupCycle.html')

# ///////////////////// Back Cycle Routes//////////////////////////////

@app.route('/back')
def back_page():
    return render_template('back_cycle.html')
@app.route('/BentOverrowCycle')
def BentOverrowCycle():
    return render_template('BentOverrowCycle.html')

@app.route('/LatPulldowncycle')
def LatPulldowncycle():
    return render_template('LatPulldowncycle.html')
@app.route('/pullupsCycle')
def pullupsCycle():
    return render_template('pullupsCycle.html')
@app.route('/DumbbellsinglearmCycle')
def DumbbellsinglearmCycle():
    return render_template('DumbbellsinglearmCycle.html')


# ///////////////////////////////////
#  legs routes
@app.route('/exercise01')
def ex01_page():
    return render_template('exercise01.html')
@app.route('/exercise02')
def ex02_page():
    return render_template('exercise02.html')
@app.route('/exercise03')
def ex03_page():
    return render_template('exercise03.html')
@app.route('/exercise04')
def ex04_page():
    return render_template('exercise04.html')
@app.route('/exercise05')
def ex05_page():
    return render_template('exercise05.html')

@app.route('/squats')
def squats():
    return Response(Squats(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/laterallegraiseleft')
def laterallegraiseleft():
    return Response(LateralLegRaisesRightSIDE(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/singlelegglute')
def singlelegglute():
    return Response(SingleLegGlute(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/Romanionsquats')
def Romanionsquats():
    return Response(RomanionSquats(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/reverselunges')
def reverselunges():
    return Response(ReverseLungs(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

#  chest routes
@app.route('/exercise11')
def ex11_page():
    return render_template('exercise11.html')
@app.route('/exercise12')
def ex12_page():
    return render_template('exercise12.html')
@app.route('/exercise13')
def ex13_page():
    return render_template('exercise13.html')
@app.route('/exercise14')
def ex14_page():
    return render_template('exercise14.html')
@app.route('/exercise15')
def ex15_page():
    return render_template('exercise15.html')
@app.route('/exercise16')
def ex16_page():
    return render_template('exercise16.html')
@app.route('/exercise17')
def ex17_page():
    return render_template('exercise17.html')

@app.route('/Dumbbellbenchpress')
def Dumbbellbenchpress():
    return Response(DumbbellBenchPress(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/Barbellbenchpress')
def Barbellbenchpress():
    return Response(BarbellBenchPress(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/Chestfly')
def Chestfly():
    return Response(ChestFly(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/dips')
def dips():
    return Response(Dips(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/PushUps')
def PushUps():
    return Response(Pushups(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
@app.route('/WidePushUps')
def WidePushUps():
    return Response(WidePushups(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/DiamondPushUps')
def DiamondPushUps():
    return Response(DiamondPushups(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

#  shoulder routes
@app.route('/exercise21')
def ex21_page():
    return render_template('exercise21.html')
@app.route('/exercise22')
def ex22_page():
    return render_template('exercise22.html')

@app.route('/exercise24')
def ex24_page():
    return render_template('exercise24.html')
@app.route('/exercise25')
def ex25_page():
    return render_template('exercise25.html')

@app.route('/overheadpress')
def overheadpress():

    return Response(Overheadpress(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/Pikepress')
def Pikepress():
    return Response(PikePress(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/Renegaderow')
def Renegaderow():
    return Response(RenegadeRow(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/Snatchgriplowpull')
def Snatchgriplowpull():
    return Response(SnatchGripLowPull(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

#  Back routes
@app.route('/exercise31')
def ex31_page():
    return render_template('exercise31.html')
@app.route('/exercise32')
def ex32_page():
    return render_template('exercise32.html')
@app.route('/exercise33')
def ex33_page():
    return render_template('exercise33.html')
@app.route('/exercise34')
def ex34_page():
    return render_template('exercise34.html')
@app.route('/exercise35')
def ex35_page():
    return render_template('exercise35.html')

@app.route('/pullups')
def pullups():
    return Response(Pullups(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/LatpullDown')
def LatpullDown():
    return Response(LatPullDown(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/deadlift')
def deadlift():
    return Response(Deadlift(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/BentOverrow')
def BentOverrow():
    return Response(BentOverRow(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/DumbbellSinglearmrow')
def DumbbellSinglearmrow():
    return Response(DumbbellSingleArmRow(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

# ////////////////////////////////////////////////////////
@app.route('/exercise40')
def ex40_page():
    return render_template('exercise40.html')
@app.route('/exercise41')
def ex41_page():
    return render_template('exercise41.html')

@app.route('/plank')
def plank():
    return Response(Plank(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/curl')
def curl():
    return Response(Curl(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')



# @app.route('/video_feed')
# def video_feed():
#       return Response(Overheadpress(Camera()),
#                     mimetype='multipart/x-mixed-replace; boundary=frame')
#

# @app.route('/video_feed/{string:username}', methods=['GET', 'POST'])
# def video_feed(username):
#     if username == "overheadpress":
#       return Response(Overheadpress(Camera()),
#                     mimetype='multipart/x-mixed-replace; boundary=frame')
#     else:
#         return Response(Squats(Camera()),
#                         mimetype='multipart/x-mixed-replace; boundary=frame')


# @app.route('/<variable>/overheadpress', methods=['GET', 'POST'])
# def overheadpress(variable):
#       return Response(Overheadpress(Camera()),
#                     mimetype='multipart/x-mixed-replace; boundary=frame')
#
# @app.route('/<variable>/squats', methods=['GET', 'POST'])
# def squats(variable):
#       return Response(Squats(Camera()),
#                     mimetype='multipart/x-mixed-replace; boundary=frame')
