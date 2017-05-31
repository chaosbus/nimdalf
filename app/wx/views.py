from flask import Flask, render_template, redirect, request, url_for, flash
from . import bp_wx


@bp_wx.route('/')
def index():
    print '__name__', __name__
    return render_template('api/index.html', subtitle='API::')


@bp_wx.route('/aqi')
def aqi():
    print '__name__', __name__
    return render_template('api/aqi.html', subtitle='AQI Stats')


@bp_wx.route('/pi')
def pi():
    print '__name__', __name__
    return render_template('api/pi.html', subtitle='RaspberryPi')


# import xxx as wx_parse
# import zzzz as wx_reply
#
#
# def wxmsg_process(xmlreq):
#     dat = wx_parse.parse_xml(xmlreq)
#     if not isinstance(dat, wx_parse.Msg):
#         print 'unsuported'
#         return wx_reply.Msg.send()
#
#     toUserName = dat.ToUserName
#     fromUserName = dat.FromUserName
#
#     if dat.MsgType.lower == 'text':
#         content = 'content...'
#         reply = wx_reply.TextMsg(toUserName, fromUserName, content)
#         return reply.send()
#     elif dat.MsgType.lower == 'image':
#         mediaId = dat.MediaId
#         reply = wx_reply.ImageMsg(toUserName, fromUserName, mediaId)
#         return reply.send()


