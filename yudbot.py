# -*- coding: utf-8 -*-

import NY
from NY.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re

cl = NY.LINE()
cl.login(qr=True)
cl.loginResult()

print "login berhasil terimakasih telah menggunakan file bot yuda:)"
reload(sys)
sys.setdefaultencoding('utf-8')

ki = kk = kc = ka = kb = kd = kf = km = kn = kp = kg = ks = kx = cl

helpMessage ="""
"""
KAC=[cl,ki,kk,kc,ka,kb,kd,kf,km,kn,kp,kg,ks,kx]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid
Dmid = ka.getProfile().mid
Emid = kb.getProfile().mid
Fmid = kd.getProfile().mid
Gmid = kf.getProfile().mid
Hmid = km.getProfile().mid
Imid = kn.getProfile().mid
Jmid = kp.getProfile().mid
Kmid = kg.getProfile().mid
Lmid = ks.getProfile().mid
Xmid = kx.getProfile().mid

Bots=[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid,Kmid,Lmid,Xmid]
admin=["U68b53f9148952188e1fcffc8f6d9d8cd", "uc8e2c2b906e2322592c6d8f91a0957f7", "uca69f1c655416e008f6be136578ebf8f", "u154629b4fcf47f84d02d34cadf266eca", "uf4a837a5f4e413ac811d790f8f578bc9"]
yuda=["U68b53f9148952188e1fcffc8f6d9d8cd", "uc8e2c2b906e2322592c6d8f91a0957f7"]
yuda1=["uf4a837a5f4e413ac811d790f8f578bc9"]
Bots1=[Bots,admin]
wait = {
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':False,
    'timeline':True,
    'autoAdd':True,
    'message':"Owner : line://ti/p/~yuda9d",
    "lang":"JP",
    "comment":"Owner : line://ti/p/~yuda9d",
    "commentOn":True,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "blacklist":{},
    "teman":{},
    "wblacklist":False,
    "dblacklist":False,
    "Protectguest":False,
    "Protectcancel":False,
    "ProtectQR":True,
    "protectionOn":True,
    "atjointicket":True
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

setTime = {}
setTime = wait2['setTime']

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def sendAudio(self, to_, path):
        M = Message(to=to_, text=None, contentType = 3)
        M_id = self.Talk.client.sendMessage(0,M).id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'media',
            'oid': M_id,
            'size': len(open(path, 'rb').read()),
            'type': 'audio',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)            
        }       

        r = self.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
        print r
        if r.status_code != 201:
            raise Exception('Upload audio failure.')

def upload_tempimage(cl):
    config = {
        'album': album,
        'name':  'bot auto upload',
        'title': 'bot auto upload',
        'description': 'bot auto upload'
    }

    print("Uploading image... ")
    image = cl.upload_from_path(image_path, config=config, anon=False)
    print("Done")
    print()

    return image

def sendImage(self, to_, path):
      M = Message(to=to_, text=None, contentType = 1)
      M.contentMetadata = None
      M.contentPreview = None
      M2 = self._client.sendMessage(0,M)
      M_id = M2.id
      files = {
         'file': open(path, 'rb'),
      }
      params = {
         'name': 'media',
         'oid': M_id,
         'size': len(open(path, 'rb').read()),
         'type': 'image',
         'ver': '1.0',
      }
      data = {
         'params': json.dumps(params)
      }
      r = self.post_content('https://obs-sg.line-apps.com/talk/m/upload.nhn', data=data, files=files)
      if r.status_code != 201:
         raise Exception('Upload image failure.')
      return True

def sendImage2(self, to_, path):
      M = Message(to=to_,contentType = 1)
      M.contentMetadata = None
      M.contentPreview = None
      M_id = self._client.sendMessage(M).id
      files = {
         'file': open(path, 'rb'),
      }
      params = {
         'name': 'media',
         'oid': M_id,
         'size': len(open(path, 'rb').read()),
         'type': 'image',
         'ver': '1.0',
      }
      data = {
         'params': json.dumps(params)
      }
      r = self._client.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
      if r.status_code != 201:
         raise Exception('Upload image failure.')
      return True

def sendImageWithURL(self, to_, url):
      path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download image failure.')
      try:
         self.sendImage(to_, path)
      except:
         try:
            self.sendImage(to_, path)
         except Exception as e:
            raise e

def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in wait2['readPoint']:
            Name = cl.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\nツ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77771ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777" + Name
                wait2['ROM'][op.param1][op.param2] = "ツ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77771ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777" + Name
        else:
            pass
    except:
        pass


def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
        if op.type == 13:				
                if op.param3 in mid:
                    if op.param2 in Amid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                        km.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kp.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)

                if op.param3 in Amid:
                    if op.param2 in Bmid:
                        X = kk.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)

                if op.param3 in Bmid:
                    if op.param2 in Cmid:
                        X = kc.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kc.updateGroup(X)
                        Ti = kc.reissueGroupTicket(op.param1)
                        kk.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kc.updateGroup(X)
                        Ti = kc.reissueGroupTicket(op.param1)

                if op.param3 in Cmid:
                    if op.param2 in mid:
                        X = cl.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
                        kc.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)

        if op.type == 13:
            print op.param1
            print op.param2
            print op.param3
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)

        if op.type == 17:
                group = random.choice(KAC).getGroup(op.param1)
                cb = Message()
                cb.to = op.param1
                cb.text = random.choice(KAC).getContact(op.param2).displayName + " Member Baru\n\nSelamat Datang" + random.choice(KAC).getContact(op.param2).displayName + " di [" + group.name + "]\nInvite sapa saja! ok!"+ "\n\nOwner adalah ➡ " + group.creator.displayName
                random.choice(KAC).sendMessage(cb)

        if op.type == 11:
            if op.param2 not in Bots1:
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    random.choice(KAC).inviteIntoGroup(op.param1,[op.param2])
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    kd.updateGroup(G)
                    Ti = kd.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    km.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kn.acceptGroupInvitationByTicket(op.param1,Ti)
            else:
                pass

        if op.type == 19:
            if op.param3 in admin:
                 ks.kickoutFromGroup(op.param1,[op.param2])
                 random.choice(KAC).inviteIntoGroup(op.param1,admin)
            else:
                pass

        if op.type == 19:
            if op.param2 not in admin:
                 kx.kickoutFromGroup(op.param1,[op.param2])
                 random.choice(KAC).inviteIntoGroup(op.param1,Bots)
                 wait["blacklist"][op.param2] = True
                 print "kicker kicked"
            else:
                pass

        if op.type == 19:
                if mid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�\nブラックリストに追加します�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77771ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    ki.updateGroup(G)
                    Ti = ki.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    km.acceptGroupInvitationByTicket(op.param1,Ti)
                    kn.acceptGroupInvitationByTicket(op.param1,Ti)
                    kp.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Amid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kc.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�\nブラックリストに追加します�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77771ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kk.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki.updateGroup(G)
                    Ticket = ki.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Bmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�\nブラックリストに追加します�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77771ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kc.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kk.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kk.updateGroup(G)
                    Ticket = kk.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Cmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�\nブラックリストに追加します�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77771ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kc.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kc.updateGroup(G)
                    Ticket = kc.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Dmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ka.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�\nブラックリストに追加します�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77771ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    ki.updateGroup(G)
                    Ti = ki.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    km.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Emid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kf.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�\nブラックリストに追加します�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77771ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    G = ka.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    ki.updateGroup(G)
                    Ti = ki.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    km.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kb.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    Ti = kd.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Fmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�\nブラックリストに追加します�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77771ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    kd.updateGroup(G)
                    Ti = kd.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    km.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = km.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    Ti = km.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Gmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kp.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�\nブラックリストに追加します�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77771ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    kd.updateGroup(G)
                    Ti = kd.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    km.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kn.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kn.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    Ti = kn.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == profile.mid:
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            X = cl.getGroup(list_[1])
                            X.preventJoinByTicket = True
                            cl.updateGroup(X)
                        except:
                            cl.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"decided not to comment")

               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        ki.sendText(msg.to,"deleted")
                        kk.sendText(msg.to,"deleted")
                        kc.sendText(msg.to,"deleted")
                        wait["dblack"] = False

                   else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        ki.sendText(msg.to,"It is not in the black list")
                        kk.sendText(msg.to,"It is not in the black list")
                        kc.sendText(msg.to,"It is not in the black list")
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"already")
                        ki.sendText(msg.to,"already")
                        kk.sendText(msg.to,"already")
                        kc.sendText(msg.to,"already")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"aded")
                        

               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        wait["dblacklist"] = False

                   else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        ki.sendText(msg.to,"It is not in the black list")
                        kk.sendText(msg.to,"It is not in the black list")
                        kc.sendText(msg.to,"It is not in the black list")
               elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text in ["CMD","?","Help"]:
				if msg.from_ in admin:
					if wait["lang"] == "JP":
						cl.sendText(msg.to,helpMessage)
					else:
						cl.sendText(msg.to,helpt)
            elif ("Gn " in msg.text):
				if msg.from_ in admin:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						X.name = msg.text.replace("Gn ","")
						
						cl.updateGroup(X)
					else:
						cl.sendText(msg.to,"It can't be used besides the group.")
            elif ("Yuda1 gn " in msg.text):
				if msg.from_ in admin:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						X.name = msg.text.replace("Yuda1 gn ","")
						ki.updateGroup(X)
					else:
						ki.sendText(msg.to,"It can't be used besides the group.")
            elif ("Yuda2 gn " in msg.text):
				if msg.from_ in admin:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						X.name = msg.text.replace("Yuda2 gn ","")
						kk.updateGroup(X)
					else:
						kk.sendText(msg.to,"It can't be used besides the group.")
            elif ("Yuda3 gn " in msg.text):
				if msg.from_ in admin:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						X.name = msg.text.replace("Yuda3 gn ","")
						kc.updateGroup(X)
					else:
						kc.sendText(msg.to,"It can't be used besides the group.")
            elif "Kick " in msg.text:
                midd = msg.text.replace("Kick ","")
                cl.kickoutFromGroup(msg.to,[midd])
            elif "yuda kick " in msg.text:
                midd = msg.text.replace("yuda kick ","")
                ki.kickoutFromGroup(msg.to,[midd])
            elif "y2 kick " in msg.text:
                midd = msg.text.replace("y2 kick ","")
                kk.kickoutFromGroup(msg.to,[midd])
            elif "Yuda reinv " in msg.text:
                midd = msg.text.replace("Yuda reinv ","")
                random.choice(KAC).kickoutFromGroup(msg.to,[midd])
                kf.findAndAddContactsByMid(midd)
                kf.inviteIntoGroup(msg.to,[midd])
            elif "Invite " in msg.text:
                midd = msg.text.replace("Invite ","")
                cl.findAndAddContactsbyMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
            elif "Semua" in msg.text:
                midd = msg.text.replace("Semua","")
                for semua in wait["teman"]:
                        kb.inviteIntoGroup(msg.to,semua)
            elif "Invite " in msg.text:
                cl.inviteIntoGroup(admin) 
            elif "Group bc " in msg.text:
                bctxt = msg.text.replace("Group bc ", "")
                n = kf.getGroupIdsJoined()
                for manusia in n:
                        kf.sendText(manusia, (bctxt))
                        kf.inviteIntoGroup(manusia,["u1d86967da5fb13fad2bc422a51b963ce", "uc8e2c2b906e2322592c6d8f91a0957f7", "uca69f1c655416e008f6be136578ebf8f", "u154629b4fcf47f84d02d34cadf266eca", "uf4a837a5f4e413ac811d790f8f578bc9"])
            elif "y1 invite " in msg.text:
                midd = msg.text.replace("y1 invite ","")
                kk.findAndAddContactsByMid(midd)
                kk.inviteIntoGroup(msg.to,[midd])
            elif "Yuda3 invite " in msg.text:
                midd = msg.text.replace("Yuda3 invite ","")
                kc.findAndAddContactsByMid(midd)
                kc.inviteIntoGroup(msg.to,[midd])
            elif "creategroup " in msg.text:
                gName = msg.text.replace("creategroup ","")
                cl.createGroup(gName,["u1d86967da5fb13fad2bc422a51b963ce", "uc8e2c2b906e2322592c6d8f91a0957f7", "uca69f1c655416e008f6be136578ebf8f", "u154629b4fcf47f84d02d34cadf266eca", "uf4a837a5f4e413ac811d790f8f578bc9", "uad72c84b6f11e53d6da34d50ebb69402", "u0a250b14ad4cba53a20072ca287d89e7", "u05f8ca5df435cb829239a4d7ac62a852", "u04ff31cd36329da24ee9952401fd3e88", "u9bec799c03521b17d71c102f0a2abb34", "u3a79d07ef6cc31fb9ca9764dc9d509af", "uaa5595c9623e5a2530efb8865832d167", "u94e15167e1b59d76ca62e5c7e9f7cabe"])
            elif "Teman " in msg.text:
                gName = msg.text.replace("Teman ","")
                for semua in wait["teman"]:
                    cl.createGroup(gName, semua)
            elif msg.text in ["Me"]:
				if msg.from_ in admin:
					msg.contentType = 13
					msg.contentMetadata = {'mid': mid}
					cl.sendMessage(msg)
					msg.contentMetadata = {'mid': Emid}
					kb.sendMessage(msg)
					msg.contentMetadata = {'mid': Jmid}
					kp.sendMessage(msg)
            elif msg.text in ["Empty"]:
					msg.contentType = 13
					msg.contentMetadata = {'mid': "None"}
					cl.sendMessage(msg)
            elif "S " in msg.text:
				if msg.toType == 2:
					Midd = msg.text.replace("S ","")
					msg.contentType = 13
					msg.contentMetadata = {'mid': Midd}
					cl.sendMessage(msg)
            elif msg.text in ["Pembuat"]:
					msg.contentType = 13
					msg.contentMetadata = {'mid': "u1d86967da5fb13fad2bc422a51b963ce"}
					cl.sendMessage(msg)
					ka.sendMessage(msg)
					ki.sendMessage(msg)
					kc.sendMessage(msg)
					kb.sendMessage(msg)
					msg.contentMetadata = {'mid': "uc8e2c2b906e2322592c6d8f91a0957f7"}
					cl.sendMessage(msg)
					ka.sendMessage(msg)
					ki.sendMessage(msg)
					kc.sendMessage(msg)
					kb.sendMessage(msg)
					msg.contentMetadata = {'mid': "uca69f1c655416e008f6be136578ebf8f"}
					cl.sendMessage(msg)
					ka.sendMessage(msg)
					ki.sendMessage(msg)
					kc.sendMessage(msg)
					kb.sendMessage(msg)
            elif msg.text in ["Nami Gc"]:
              if msg.toType == 2:
                    msg.contentType = 13
                    ginfo = km.getGroup(msg.to)
                    gCreator = ginfo.creator.mid
                    try:
                        msg.contentMetadata = {'mid': gCreator}
                        gCreator1 = ginfo.creator.displayName
                        
                    except:
                        gCreator = "Error"
                    km.sendText(msg.to, "Group Creator : " + gCreator1)
                    km.sendMessage(msg)
            elif msg.text in ["æ„�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�ã®ãƒ�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�ãƒ¬ã�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�¼ãƒ³ãƒ˄1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77771ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777","Gift"]:
				if msg.from_ in admin:
					msg.contentType = 9
					msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
										'PRDTYPE': 'THEME',
										'MSGTPL': '5'}
					msg.text = None
					cl.sendMessage(msg)
            elif msg.text in ["æ„�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�ã®ãƒ�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�ãƒ¬ã�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�¼ãƒ³ãƒ˄1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77771ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777","Yuda1 gift"]:
				if msg.from_ in admin:
					msg.contentType = 9
					msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
										'PRDTYPE': 'THEME',
										'MSGTPL': '6'}
					msg.text = None
					ki.sendMessage(msg)
            elif msg.text in ["æ„�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�ã®ãƒ�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�ãƒ¬ã�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�¼ãƒ³ãƒ˄1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77771ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777","Yuda2 gift"]:
				if msg.from_ in admin:
					msg.contentType = 9
					msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
										'PRDTYPE': 'THEME',
										'MSGTPL': '8'}
					msg.text = None
					kk.sendMessage(msg)
            elif msg.text in ["æ„�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�ã®ãƒ�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�ãƒ¬ã�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�¼ãƒ³ãƒ˄1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77771ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777","Yuda3 gift"]:
				if msg.from_ in admin:
					msg.contentType = 9
					msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
										'PRDTYPE': 'THEME',
										'MSGTPL': '10'}
					msg.text = None
					kc.sendMessage(msg)
            elif msg.text in ["æ„�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�ã®ãƒ�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�ãƒ¬ã�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�¼ãƒ³ãƒ˄1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77771ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777","All gift"]:
				if msg.from_ in admin:
					msg.contentType = 9
					msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
										'PRDTYPE': 'THEME',
										'MSGTPL': '12'}
					msg.text = None
					ki.sendMessage(msg)
					kk.sendMessage(msg)
					kc.sendMessage(msg)
            elif "TestYud" in msg.txt:
                    Group = cl.getGroup(msg.to)
                    orang = cl.getAllContactIds()
                    semua = [contact.mid for contact in orang]
                    cl.sendText(orang, "TestYud [BroadCastLine] subs youtube.com/YudaTheGoldMine otw 1k")
                    cl.inviteIntoGroup(Group, semua)
            elif msg.text in ["cancel","Cancel"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						if X.invitee is not None:
							gInviMids = [contact.mid for contact in X.invitee]
							cl.inviteGroupInvitation(msg.to, gInviMids)
						else:
							if wait["lang"] == "JP":
								cl.sendText(msg.to,"No one is inviting")
							else:
								cl.sendText(msg.to,"Sorry, nobody absent")
					else:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Can not be used outside the group")
						else:
							cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Yuda cancel","Bot cancel"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						G = k3.getGroup(msg.to)
						if G.invitee is not None:
							gInviMids = [contact.mid for contact in G.invitee]
							k3.cancelGroupInvitation(msg.to, gInviMids)
						else:
							if wait["lang"] == "JP":
								k3.sendText(msg.to,"No one is inviting")
							else:
								k3.sendText(msg.to,"Sorry, nobody absent")
					else:
						if wait["lang"] == "JP":
							k3.sendText(msg.to,"Can not be used outside the group")
						else:
							k3.sendText(msg.to,"Not for use less than group")
            #elif "gurl" == msg.text:
                #print cl.getGroup(msg.to)
                ##cl.sendMessage(msg)
            elif msg.text in ["Ourl","Link on","Urlon"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						X.preventJoinByTicket = False
						cl.updateGroup(X)
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Done")
						else:
							cl.sendText(msg.to,"already open")
					else:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Can not be used outside the group")
						else:
							cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Yuda1 ourl","Yuda1 link on"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						X.preventJoinByTicket = False
						ki.updateGroup(X)
						if wait["lang"] == "JP":
							ki.sendText(msg.to,"Done Chivas")
						else:
							ki.sendText(msg.to,"already open")
					else:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Can not be used outside the group")
						else:
							cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Yuda2 ourl","Yuda2 link on"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						X = kk.getGroup(msg.to)
						X.preventJoinByTicket = False
						kk.updateGroup(X)
						if wait["lang"] == "JP":
							kk.sendText(msg.to,"Done Chivas")
						else:
							kk.sendText(msg.to,"already open")
					else:
						if wait["lang"] == "JP":
							kk.sendText(msg.to,"Can not be used outside the group")
						else:
							kk.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Yuda3 ourl","Yuda3 link on"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						X = kc.getGroup(msg.to)
						X.preventJoinByTicket = False
						kc.updateGroup(X)
						if wait["lang"] == "JP":
							kc.sendText(msg.to,"Done Chivas")
						else:
							kc.sendText(msg.to,"already open")
					else:
						if wait["lang"] == "JP":
							kc.sendText(msg.to,"Can not be used outside the group")
						else:
							kc.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Curl","Link off","Urloff"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						X.preventJoinByTicket = True
						cl.updateGroup(X)
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Done")
						else:
							cl.sendText(msg.to,"already close")
					else:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Can not be used outside the group")
						else:
							cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Yuda1 curl","Yuda1 link off"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						X = ki.getGroup(msg.to)
						X.preventJoinByTicket = True
						ki.updateGroup(X)
						if wait["lang"] == "JP":
							ki.sendText(msg.to,"Done Chivas")
						else:
							ki.sendText(msg.to,"already close")
					else:
						if wait["lang"] == "JP":
							ki.sendText(msg.to,"Can not be used outside the group")
						else:
							ki.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Yuda2 curl","Yuda2 link off"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						X = kk.getGroup(msg.to)
						X.preventJoinByTicket = True
						kk.updateGroup(X)
						if wait["lang"] == "JP":
							kk.sendText(msg.to,"Done Chivas")
						else:
							kk.sendText(msg.to,"already close")
					else:
						if wait["lang"] == "JP":
							kk.sendText(msg.to,"Can not be used outside the group")
						else:
							kk.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Yuda3 curl","Yuda3 link off"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						X = kc.getGroup(msg.to)
						X.preventJoinByTicket = True
						kc.updateGroup(X)
						if wait["lang"] == "JP":
							kc.sendText(msg.to,"Done Chivas")
						else:
							kc.sendText(msg.to,"already close")
					else:
						if wait["lang"] == "JP":
							kc.sendText(msg.to,"Can not be used outside the group")
						else:
							kc.sendText(msg.to,"Not for use less than group")
            elif "jointicket " in msg.text.lower():
		replace=msg.text.lower().replace("jointicket ")
		if replace == "on":
			wait["atjointicket"]=True
		elif replace == "off":
			wait["atjointicket"]=False
		cl.sendText(msg.to,"Auto Join Group by Ticket is %s" % str(wait["atjointicket"]))
            elif '/ti/g/' in msg.text.lower():
		link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
		links = link_re.findall(msg.text)
		n_links=[]
		for l in links:
			if l not in n_links:
				n_links.append(l)
		for ticket_id in n_links:
			if wait["atjointicket"] == True:
				group=cl.findGroupByTicket(ticket_id)
				cl.acceptGroupInvitationByTicket(group.mid,ticket_id)
				cl.sendText(msg.to,"Sukses join ke grup %s" % str(group.name))
            elif msg.text == "Ginfo":
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\nmembers:" + str(len(ginfo.members)) + "members\npending:" + sinvitee + "people\nURL:" + u + "it is inside")
                    else:
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif "Id" == msg.text:
				if msg.from_ in admin:
					cl.sendText(msg.to,msg.to)
            elif "All mid" == msg.text:
				if msg.from_ in admin:
					cl.sendText(msg.to,mid)
					ki.sendText(msg.to,Amid)
					kk.sendText(msg.to,Bmid)
					kc.sendText(msg.to,Cmid)
            elif "Mid" == msg.text:
				if msg.from_ in admin:
					cl.sendText(msg.to,mid)
            elif "Yuda1 mid" == msg.text:
				if msg.from_ in admin:
					ki.sendText(msg.to,Amid)
            elif "Yuda2 mid" == msg.text:
				if msg.from_ in admin:
					kk.sendText(msg.to,Bmid)
            elif "Yuda3 mid" == msg.text:
				if msg.from_ in admin:
					kc.sendText(msg.to,Cmid)

            elif "Mid @" in msg.text:
                _name = msg.text.replace("Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        cl.sendText(msg.to, g.mid)
                    else:
                        pass
            elif msg.text in ["stiker"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "242",
										"STKPKGID": "3",
										"STKVER": "100" }
					ki.sendMessage(msg)
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "30",
										"STKPKGID": "2",
										"STKVER": "100" }
					ka.sendMessage(msg)
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "293",
										"STKPKGID": "4",
										"STKVER": "100" }
					kd.sendMessage(msg)
            elif msg.text in ["Wkwk"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "100",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
					kk.sendMessage(msg)
            elif msg.text in ["Hehehe"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "10",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
					kk.sendMessage(msg)
            elif msg.text in ["Galon"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "9",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
					kk.sendMessage(msg)
            elif msg.text in ["You"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "7",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
					kk.sendMessage(msg)
            elif msg.text in ["Hadeuh"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "6",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
					kk.sendMessage(msg)
            elif msg.text in ["Please"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "4",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
					kk.sendMessage(msg)
            elif msg.text in ["Haaa"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "3",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
					kk.sendMessage(msg)
            elif msg.text in ["Lol"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "110",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
					kk.sendMessage(msg)
            elif msg.text in ["Hmmm"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "101",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
            elif msg.text in ["Wc"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "247",
										"STKPKGID": "3",
										"STKVER": "100" }
					ki.sendMessage(msg)
					kk.sendMessage(msg)
            elif msg.text in ["Cury PP"]:
				if msg.from_ in admin:
					tl_text = msg.text.replace("TL","")
					cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif msg.text in ["Cn "]:
				if msg.from_ in admin:
					string = msg.text.replace("Cn ","")
					if len(string.decode('utf-8')) <= 20:
						profile = cl.getProfile()
						profile.displayName = string
						cl.updateProfile(profile)
						cl.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Yuda1 rename "]:
				if msg.from_ in admin:
					string = msg.text.replace("Yuda1 rename ","")
					if len(string.decode('utf-8')) <= 20:
						profile_B = ki.getProfile()
						profile_B.displayName = string
						ki.updateProfile(profile_B)
						ki.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Yuda2 rename "]:
				if msg.from_ in admin:
					string = msg.text.replace("Yuda2 rename ","")
					if len(string.decode('utf-8')) <= 20:
						profile_B = kk.getProfile()
						profile_B.displayName = string
						kk.updateProfile(profile_B)
						kk.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Guest on","guest on"]:
				if msg.from_ in admin:
					if wait["Protectguest"] == True:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Guest Stranger On")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["Protectguest"] = True
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Guest Stranger On")
						else:
							cl.sendText(msg.to,"done")
            elif msg.text in ["Guest Off","guest off"]:
				if msg.from_ in admin:
					if wait["Protectguest"] == False:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Guest Stranger Off")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["Protectguest"] = False
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Guest Stranger Off")
						else:
							cl.sendText(msg.to,"done")
            elif msg.text in ["Qr on","qr on"]:
				if msg.from_ in admin:
					if wait["ProtectQR"] == True:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Protect QR On")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["ProtectQR"] = True
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Protect QR On")
						else:
							cl.sendText(msg.to,"done")
            elif msg.text in ["Qr off","qr off"]:
				if msg.from_ in admin:
					if wait["ProtectQR"] == False:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Protect QR Off")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["ProtectQR"] = False
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Protect QR Off")
						else:
							cl.sendText(msg.to,"done")
            elif msg.text in ["é€£çµ¡å�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�˄1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77771ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777:ã‚ªãƒ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77771ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777","K on","Contact on","é¡¯ç¤ºï¼šé–�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77771ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777"]:
				if msg.from_ in admin:
					if wait["contact"] == True:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already on")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["contact"] = True
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already on")
						else:
							cl.sendText(msg.to,"done")
            elif msg.text in ["é€£çµ¡å�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�˄1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77771ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777:ã‚ªãƒ�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77771ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777","K off","Contact off","é¡¯ç¤ºï¼šé—ń1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77771ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777"]:
				if msg.from_ in admin:
					if wait["contact"] == False:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already off")
						else:
							cl.sendText(msg.to,"done ")
					else:
						wait["contact"] = False
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already off")
						else:
							cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777��1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�å�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�åń1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77771ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777 :ã‚ªãƒ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77771ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777","Join on","Auto join:on","è‡ªå�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777��1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�åƒåń1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77771ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777 ï¼šé–�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77771ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777"]:
				if msg.from_ in admin:
					if wait["autoJoin"] == True:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already on")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["autoJoin"] = True
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already on")
						else:
							cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777��1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�å�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�åń1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77771ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777 :ã‚ªãƒ�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77771ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777","Join off","Auto join:off","è‡ªå�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777��1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�åƒåń1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77771ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777 ï¼šé—ń1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77771ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777"]:
				if msg.from_ in admin:
					if wait["autoJoin"] == False:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already off")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["autoJoin"] = False
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already off")
						else:
							cl.sendText(msg.to,"done")
            elif msg.text in ["Gcancel:"]:
				if msg.from_ in admin:
					try:
						strnum = msg.text.replace("Gcancel:","")
						if strnum == "off":
							wait["autoCancel"]["on"] = False
							if wait["lang"] == "JP":
								cl.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
							else:
								cl.sendText(msg.to,"å…³äº�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�é�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�€è¯·æ‹�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�ç»ã€‚è¦æ�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�¶å¼€è¯·æŒ‡å®šäººæ�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�°å�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�é€")
						else:
							num =  int(strnum)
							wait["autoCancel"]["on"] = True
							if wait["lang"] == "JP":
								cl.sendText(msg.to,strnum + "The group of people and below decided to automatically refuse invitation")
							else:
								cl.sendText(msg.to,strnum + "ä½¿äººä»¥ä¸‹çš�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�å°ç»�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�ç�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�¨è�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�ªåŠ¨é�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�€è¯·æ‹�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�ç»1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77771ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777")
					except:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Value is wrong")
						else:
							cl.sendText(msg.to,"Bizarre ratings")
            elif msg.text in ["å¼·åˆ¶è‡ªå�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777��1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�é€€å�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77771ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777:ã‚ªãƒ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77771ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777","Leave on","Auto leave:on","å¼·åˆ¶è‡ªå�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777��1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�é€€å�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�ºï¼šé�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777��1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77771ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777"]:
				if msg.from_ in admin:
					if wait["leaveRoom"] == True:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already on")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["leaveRoom"] = True
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"è¦äº†å¼€ã€�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77771ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777")
            elif msg.text in ["å¼·åˆ¶è‡ªå�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777��1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�é€€å�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77771ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777:ã‚ªãƒ�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77771ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777","Leave off","Auto leave:off","å¼·åˆ¶è‡ªå�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777��1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�é€€å�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�ºï¼šé�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�ń1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77771ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777"]:
				if msg.from_ in admin:
					if wait["leaveRoom"] == False:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already off")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["leaveRoom"] = False
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"already")
            elif msg.text in ["å…±æœ�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77771ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777:ã‚ªãƒ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77771ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777","Share on","Share on"]:
				if msg.from_ in admin:
					if wait["timeline"] == True:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already on")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["timeline"] = True
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"è¦äº†å¼€ã€�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77771ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777")
            elif msg.text in ["å…±æœ�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77771ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777:ã‚ªãƒ�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77771ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777","Share off","Share off"]:
				if msg.from_ in admin:
					if wait["timeline"] == False:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already off")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["timeline"] = False
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"è¦äº†å�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�³æ�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�­ã€ 1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77771ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777")
            elif msg.text in ["Set"]:
				if msg.from_ in admin:
					md = ""
					if wait["contact"] == True: md+=" Contact : on\n"
					else: md+=" Contact : off\n"
					if wait["autoJoin"] == True: md+=" Auto join : on\n"
					else: md +=" Auto join : off\n"
					if wait["autoCancel"]["on"] == True:md+=" Group cancel :" + str(wait["autoCancel"]["members"]) + "\n"
					else: md+= " Group cancel : off\n"
					if wait["leaveRoom"] == True: md+=" Auto leave : on\n"
					else: md+=" Auto leave : off\n"
					if wait["timeline"] == True: md+=" Share : on\n"
					else:md+=" Share : off\n"
					if wait["autoAdd"] == True: md+=" Auto add : on\n"
					else:md+=" Auto add : off\n"
					if wait["commentOn"] == True: md+=" Comment : on\n"
					else:md+=" Comment : off\n"
					if wait["ProtectQR"] == True: md+=" ProtectQR : on\n"
					else: md+=" ProtectQR : off\n"
					if wait["Protectguest"] == True: md+=" Protectguest : on\n"
					else: md+=" Protectguest : off\n"
					cl.sendText(msg.to,md)
            elif "album merit " in msg.text:
				if msg.from_ in admin:
					gid = msg.text.replace("album merit ","")
					album = cl.getAlbum(gid)
					if album["result"]["items"] == []:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"There is no album")
						else:
							cl.sendText(msg.to,"ç›¸å�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�Œæ²¡åœ¨ã€ 1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77771ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777")
					else:
						if wait["lang"] == "JP":
							mg = "The following is the target album"
						else:
							mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�ç�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�¸å�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�ń1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77771ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777"
						for y in album["result"]["items"]:
							if "photoCount" in y:
								mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
							else:
								mg += str(y["title"]) + ":0sheet\n"
						cl.sendText(msg.to,mg)
            elif "album " in msg.text:
				if msg.from_ in admin:
					gid = msg.text.replace("album ","")
					album = cl.getAlbum(gid)
					if album["result"]["items"] == []:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"There is no album")
						else:
							cl.sendText(msg.to,"ç›¸å�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�Œæ²¡åœ¨ã€ 1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77771ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777")
					else:
						if wait["lang"] == "JP":
							mg = "The following is the target album"
						else:
							mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�ç�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�¸å�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�ń1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77771ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777"
						for y in album["result"]["items"]:
							if "photoCount" in y:
								mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
							else:
								mg += str(y["title"]) + ":0sheet\n"
            elif "album remove " in msg.text:
				if msg.from_ in admin:
					gid = msg.text.replace("album remove ","")
					albums = cl.getAlbum(gid)["result"]["items"]
					i = 0
					if albums != []:
						for album in albums:
							cl.deleteAlbum(gid,album["id"])
							i += 1
					if wait["lang"] == "JP":
						cl.sendText(msg.to,str(i) + "Deleted albums")
					else:
						cl.sendText(msg.to,str(i) + "åˆ é™¤äº�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�äº�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�çš�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�ç�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�¸å�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�Œã€ 1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77771ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777")
            elif msg.text in ["Group id","ç¾¤çµ„å�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�¨id"]:
				if msg.from_ in admin:
					gid = cl.getGroupIdsJoined()
					h = ""
					for i in gid:
						h += "[%s]:%s\n" % (cl.getGroup(i).name,i)
					cl.sendText(msg.to,h)
            elif msg.text in ["Cancelall"]:
				if msg.from_ in admin:
					gid = cl.getGroupIdsInvited()
					for i in gid:
						cl.rejectGroupInvitation(i)
					if wait["lang"] == "JP":
						cl.sendText(msg.to,"All invitations have been refused")
					else:
						cl.sendText(msg.to,"æ‹�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�ç»äº�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�å�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�¨éƒ¨çš�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�é�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�€è¯·ã€�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77771ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777")
            elif "album removeâ†�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77771ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777" in msg.text:
				if msg.from_ in admin:
					gid = msg.text.replace("album removeâ†�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77771ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777","")
					albums = cl.getAlbum(gid)["result"]["items"]
					i = 0
					if albums != []:
						for album in albums:
							cl.deleteAlbum(gid,album["id"])
							i += 1
					if wait["lang"] == "JP":
						cl.sendText(msg.to,str(i) + "Albums deleted")
					else:
						cl.sendText(msg.to,str(i) + "åˆ é™¤äº�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�äº�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�çš�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�ç�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�¸å�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�Œã€ 1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77771ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777")
            elif msg.text in ["è‡ªå�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777��1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�è¿½åń1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77771ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777 :ã‚ªãƒ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77771ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777","Add on","Auto add:on","è‡ªå�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777��1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�è¿½åń1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77771ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777 ï¼šé–�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77771ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777"]:
				if msg.from_ in admin:
					if wait["autoAdd"] == True:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already on")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["autoAdd"] = True
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"è¦äº†å¼€ã€�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77771ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777")
            elif msg.text in ["è‡ªå�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777��1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�è¿½åń1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77771ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777 :ã‚ªãƒ�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77771ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777","Add off","Auto add:off","è‡ªå�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777��1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�è¿½åń1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77771ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777 ï¼šé—ń1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77771ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777"]:
				if msg.from_ in admin:
					if wait["autoAdd"] == False:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already off")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["autoAdd"] = False
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"è¦äº†å�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�³æ�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�­ã€ 1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77771ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777")
            elif "Message change: " in msg.text:
				if msg.from_ in admin:
					wait["message"] = msg.text.replace("Message change: ","")
					cl.sendText(msg.to,"message changed")
            elif "Message add: " in msg.text:
				if msg.from_ in admin:
					wait["message"] = msg.text.replace("Message add: ","")
					if wait["lang"] == "JP":
						cl.sendText(msg.to,"message changed")
					else:
						cl.sendText(msg.to,"doneã€�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77771ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777")
            elif msg.text in ["Message","è‡ªå�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777��1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�è¿½åń1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77771ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777 å•å€™èªžç¢ºèª1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77771ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777"]:
				if msg.from_ in admin:
					if wait["lang"] == "JP":
						cl.sendText(msg.to,"message change to\n\n" + wait["message"])
					else:
						cl.sendText(msg.to,"The automatic appending information is set as followsã€�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�\n\n" + wait["message"])
            elif "Comment:" in msg.text:
				if msg.from_ in admin:
					c = msg.text.replace("Comment:","")
					if c in [""," ","\n",None]:
						cl.sendText(msg.to,"message changed")
					else:
						wait["comment"] = c
						cl.sendText(msg.to,"changed\n\n" + c)
            elif "Add comment:" in msg.text:
				if msg.from_ in admin:
					c = msg.text.replace("Add comment:","")
					if c in [""," ","\n",None]:
						cl.sendText(msg.to,"String that can not be changed")
					else:
						wait["comment"] = c
						cl.sendText(msg.to,"changed\n\n" + c)
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒ˄1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77771ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777:ã‚ªãƒ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77771ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777","Comment on","Comment:on","è‡ªå�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777��1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�é¦�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�Ä1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77771ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777 ç•™è¨€ï¼šé�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777��1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77771ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777"]:
				if msg.from_ in admin:
					if wait["commentOn"] == True:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"already on")
					else:
						wait["commentOn"] = True
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"è¦äº†å¼€ã€�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77771ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777")
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒ˄1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77771ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777:ã‚ªãƒ�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77771ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777","Comment on","Comment off","è‡ªå�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777��1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�é¦�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�Ä1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77771ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777 ç•™è¨€ï¼šé�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�ń1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77771ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777"]:
				if msg.from_ in admin:
					if wait["commentOn"] == False:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"already off")
					else:
						wait["commentOn"] = False
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"è¦äº†å�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�³æ�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777�­ã€ 1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77771ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777")
            elif msg.text in ["Comment","ç•™è¨€ç¢ºèª1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77771ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777"]:
				if msg.from_ in admin:
					cl.sendText(msg.to,"message changed to\n\n" + str(wait["comment"]))
            elif msg.text in ["Gurl"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						x = cl.getGroup(msg.to)
						if x.preventJoinByTicket == True:
							x.preventJoinByTicket = False
							cl.updateGroup(x)
						gurl = cl.reissueGroupTicket(msg.to)
						cl.sendText(msg.to,"line://ti/g/" + gurl)
					else:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Can't be used outside the group")
						else:
							cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Yuda1 gurl"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						x = cl.getGroup(msg.to)
						if x.preventJoinByTicket == True:
							x.preventJoinByTicket = False
							ki.updateGroup(x)
						gurl = ki.reissueGroupTicket(msg.to)
						ki.sendText(msg.to,"line://ti/g/" + gurl)
					else:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Can't be used outside the group")
						else:
							cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Yuda2 gurl"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						x = cl.getGroup(msg.to)
						if x.preventJoinByTicket == True:
							x.preventJoinByTicket = False
							kk.updateGroup(x)
						gurl = kk.reissueGroupTicket(msg.to)
						kk.sendText(msg.to,"line://ti/g/" + gurl)
					else:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Can't be used outside the group")
						else:
							cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Yuda3 gurl"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						x = cl.getGroup(msg.to)
						if x.preventJoinByTicket == True:
							x.preventJoinByTicket = False
							kc.updateGroup(x)
						gurl = kc.reissueGroupTicket(msg.to)
						kc.sendText(msg.to,"line://ti/g/" + gurl)
					else:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Can't be used outside the group")
						else:
							cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Comment bl "]:
				if msg.from_ in admin:
					wait["wblack"] = True
					cl.sendText(msg.to,"add to comment bl")
            elif msg.text in ["Comment wl "]:
				if msg.from_ in admin:
					wait["dblack"] = True
					cl.sendText(msg.to,"wl to comment bl")
            elif msg.text in ["Comment bl confirm"]:
				if msg.from_ in admin:
					if wait["commentBlack"] == {}:
						cl.sendText(msg.to,"confirmed")
					else:
						cl.sendText(msg.to,"Blacklist")
						mc = ""
						for mi_d in wait["commentBlack"]:
							mc += "" +cl.getContact(mi_d).displayName + "\n"
						cl.sendText(msg.to,mc)
            elif msg.text in ["Jam on"]:
				if msg.from_ in admin:
					if wait["clock"] == True:
						cl.sendText(msg.to,"already on")
					else:
						wait["clock"] = True
						now2 = datetime.now()
						nowT = datetime.strftime(now2,"(%H:%M)")
						profile = cl.getProfile()
						profile.displayName = wait["cName"] + nowT
						cl.updateProfile(profile)
						cl.sendText(msg.to,"done")
            elif msg.text in ["Jam off"]:
				if msg.from_ in admin:
					if wait["clock"] == False:
						cl.sendText(msg.to,"already off")
					else:
						wait["clock"] = False
						cl.sendText(msg.to,"done")
            elif msg.text in ["Change clock "]:
				if msg.from_ in admin:
					n = msg.text.replace("Change clock ","")
					if len(n.decode("utf-8")) > 13:
						cl.sendText(msg.to,"changed")
					else:
						wait["cName"] = n
						cl.sendText(msg.to,"changed to\n\n" + n)
            elif msg.text in ["Up"]:
				if msg.from_ in admin:
					if wait["clock"] == True:
						now2 = datetime.now()
						nowT = datetime.strftime(now2,"(%H:%M)")
						profile = cl.getProfile()
						profile.displayName = wait["cName"] + nowT
						cl.updateProfile(profile)
						cl.sendText(msg.to,"Updated")
					else:
						cl.sendText(msg.to,"Please turn on the name clock")

            elif msg.text == "setpoint":
                    cl.sendText(msg.to, "Point telah ditempatkan")
                    ka.sendText(msg.to, "Silakan ketik")
                    km.sendText(msg.to, "point")
                    kg.sendText(msg.to, "Untuk liat siders")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['ROM'][msg.to] = {}
                    print wait2
                    
            elif msg.text == "point":
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"

                        cl.sendText(msg.to, "People who readed %s\nthat's it\n\nPeople who have ignored reads\n%sIt is abnormal ♪\n\nReading point creation date n time:\n[%s]"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        cl.sendText(msg.to, "An already read point has not been set.\n「set」you can send ♪ read point will be created ♪")
#-----------------------------------------------

            elif msg.text in ["Masuk","Bot masuk,Semua Masuk"]:
				if msg.from_ in admin:
							G = cl.getGroup(msg.to)
							ginfo = cl.getGroup(msg.to)
							G.preventJoinByTicket = False
							cl.updateGroup(G)
							invsend = 0
							Ticket = cl.reissueGroupTicket(msg.to)
							ki.acceptGroupInvitationByTicket(msg.to,Ticket)
							time.sleep(0.2)
							kk.acceptGroupInvitationByTicket(msg.to,Ticket)
							time.sleep(0.2)
							kc.acceptGroupInvitationByTicket(msg.to,Ticket)
							time.sleep(0.2)
							ka.acceptGroupInvitationByTicket(msg.to,Ticket)
							time.sleep(0.2)
							kb.acceptGroupInvitationByTicket(msg.to,Ticket)
							time.sleep(0.2)
							kd.acceptGroupInvitationByTicket(msg.to,Ticket)
							time.sleep(0.2)
							km.acceptGroupInvitationByTicket(msg.to,Ticket)
							time.sleep(0.2)
							kf.acceptGroupInvitationByTicket(msg.to,Ticket)
							time.sleep(0.2)
							kn.acceptGroupInvitationByTicket(msg.to,Ticket)
							time.sleep(0.2)
							kp.acceptGroupInvitationByTicket(msg.to,Ticket)
							time.sleep(0.2)
							kg.acceptGroupInvitationByTicket(msg.to,Ticket)
							time.sleep(0.2)
							ks.acceptGroupInvitationByTicket(msg.to,Ticket)
							time.sleep(0.2)
							kx.acceptGroupInvitationByTicket(msg.to,Ticket)
							time.sleep(0.2)
							print "kicker ok"

            elif msg.text in ["Tasya Masuk"]:
				if msg.from_ in admin:
							G = cl.getGroup(msg.to)
							ginfo = cl.getGroup(msg.to)
							G.preventJoinByTicket = False
							cl.updateGroup(G)
							invsend = 0
							Ticket = cl.reissueGroupTicket(msg.to)
							ka.acceptGroupInvitationByTicket(msg.to,Ticket)
							time.sleep(0.2)
							kb.acceptGroupInvitationByTicket(msg.to,Ticket)
							time.sleep(0.2)
							kd.acceptGroupInvitationByTicket(msg.to,Ticket)
							time.sleep(0.2)
							G = cl.getGroup(msg.to)
							G.preventJoinByTicket = True
							ki.updateGroup(G)
							print "kicker ok" 
							G.preventJoinByTicket(G)
							ki.updateGroup(G)

            elif msg.text in ["Militer Masuk"]:
				if msg.from_ in admin:
							G = cl.getGroup(msg.to)
							ginfo = cl.getGroup(msg.to)
							G.preventJoinByTicket = False
							cl.updateGroup(G)
							invsend = 0
							Ticket = cl.reissueGroupTicket(msg.to)
							km.acceptGroupInvitationByTicket(msg.to,Ticket)
							time.sleep(0.2)
							kf.acceptGroupInvitationByTicket(msg.to,Ticket)
							time.sleep(0.2)
							print "kicker ok" 

            elif msg.text in ["Yuda masuk"]:
				if msg.from_ in admin:
							G = cl.getGroup(msg.to)
							ginfo = cl.getGroup(msg.to)
							G.preventJoinByTicket = False
							cl.updateGroup(G)
							invsend = 0
							Ticket = cl.reissueGroupTicket(msg.to)
							ki.acceptGroupInvitationByTicket(msg.to,Ticket)
							time.sleep(0.2)
							kk.acceptGroupInvitationByTicket(msg.to,Ticket)
							time.sleep(0.2)
							kc.acceptGroupInvitationByTicket(msg.to,Ticket)
							time.sleep(0.2)
							G = cl.getGroup(msg.to)
							G.preventJoinByTicket = True
							ki.updateGroup(G)
							print "kicker ok" 
							G.preventJoinByTicket(G)
							ki.updateGroup(G)

#-----------------------------------------------
            elif msg.text in ["Keluar","Exit"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						ginfo = cl.getGroup(msg.to)
						try:
							ki.leaveGroup(msg.to)
							kk.leaveGroup(msg.to)
							kc.leaveGroup(msg.to)
							ka.leaveGroup(msg.to)
							kb.leaveGroup(msg.to)
							kd.leaveGroup(msg.to)
							km.leaveGroup(msg.to)
							kn.leaveGroup(msg.to)
							kg.leaveGroup(msg.to)
							kp.leaveGroup(msg.to)
							kf.leaveGroup(msg.to)
							ks.leaveGroup(msg.to)
							kx.leaveGroup(msg.to)
						except:
							pass
            elif msg.text in ["Bye 1"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						ginfo = cl.getGroup(msg.to)
						try:
							ki.leaveGroup(msg.to)
						except:
							pass
            elif msg.text in ["Bye 2"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						ginfo = cl.getGroup(msg.to)
						try:
							ki.leaveGroup(msg.to)
							kk.leaveGroup(msg.to)
						except:
							pass
				elif msg.text in ["Yuda1 @bye"]:
					if msg.toType == 2:
						ginfo = cl.getGroup(msg.to)
						try:
							ki.leaveGroup(msg.to)
						except:
							pass
            elif msg.text in ["Yuda2 @bye"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						ginfo = cl.getGroup(msg.to)
						try:
							kk.leaveGroup(msg.to)
						except:
							pass
				elif msg.text in ["Yuda3 @bye"]:
					if msg.toType == 2:
						ginfo = cl.getGroup(msg.to)
						try:
							kc.leaveGroup(msg.to)
						except:
							pass
            
#-----------------------------------------------
        if op.type == 26:
            if msg.text in ["Tagall"]:
              if msg.from_ in admin:
                group = cl.getGroup(msg.to)
                nama = [contact.mid for contact in group.members]
                cb = ""
                cb2 = ""
                strt = int(0)
                akh = int(0)
                for md in nama:
                    akh = akh + int(5)
                    cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                    strt = strt + int(6)
                    akh = akh + 1
                    cb2 += "@nrik\n"
                cb = (cb[:int(len(cb)-1)])
                msg.contentType = 0
                msg.text = cb2
                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                try:
                    ki.sendMessage(msg)
                except Exception as error:
                    print error
#-----------------------------------------------

            elif msg.text in ["Kill"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						group = ki.getGroup(msg.to)
						gMembMids = [contact.mid for contact in group.members]
						matched_list = []
						for tag in wait["blacklist"]:
							matched_list+=filter(lambda str: str == tag, gMembMids)
						if matched_list == []:
							kk.sendText(msg.to,"Fuck You")
							kc.sendText(msg.to,"Fuck You")
							return
						for jj in matched_list:
							try:
								klist=[ki,kk,kc]
								kicker=random.choice(klist)
								kicker.kickoutFromGroup(msg.to,[jj])
								kicker.inviteIntoGroup(op.param1,admin)
								print (msg.to,[jj])
							except:
								pass
            elif "Cleanse" in msg.text:
				if msg.from_ in admin:
					if msg.toType == 2:
						print "ok"
						_name = msg.text.replace("Cleanse","")
						gs = ki.getGroup(msg.to)
						gs = kk.getGroup(msg.to)
						gs = kc.getGroup(msg.to)
						ki.sendText(msg.to,"Group Tidak amanô")
						kk.sendText(msg.to,"Group DiBersihkan.")
						targets = []
						for g in gs.members:
							if _name in g.displayName:
								targets.append(g.mid)
						if targets == []:
							ki.sendText(msg.to,"Not found.")
							kk.sendText(msg.to,"Not found.")
						else:
							for target in targets:
								try:
									klist=[cl,ka,kb,kp]
									kicker=random.choice(klist)
									kicker.kickoutFromGroup(msg.to,[target])
									kicker.inviteIntoGroup(msg.to,[target])
									print (msg.to,[g.mid])
								except:
									ki.sendText(msg.to,"Group cleanse")
									kk.sendText(msg.to,"Group cleanse")
            elif "Nk " in msg.text:
				if msg.from_ in admin:
					if msg.from_ in admin:
						nk0 = msg.text.replace("Nk ","")
						nk1 = nk0.lstrip()
						nk2 = nk1.replace("@","")
						nk3 = nk2.rstrip()
						_name = nk3
						gs = cl.getGroup(msg.to)
						targets = []
						for s in gs.members:
							if _name in s.displayName:
								targets.append(s.mid)
						if targets == []:
							sendMessage(msg.to,"user does not exist")
							pass
						else:
							for target in targets:
									try:
										klist=[cl,ki,kk,kc]
										kicker=random.choice(klist)
										kicker.kickoutFromGroup(msg.to,[target])
										kicker.inviteIntoGroup(msg.to,[target])
										print (msg.to,[g.mid])
									except:
										ki.sendText(msg.to,"Succes Yuda")
										kk.sendText(msg.to,"Fuck You")
            elif "Blacklist @ " in msg.text:
				if msg.from_ in admin:
					_name = msg.text.replace("Blacklist @ ","")
					_kicktarget = _name.rstrip(' ')
					gs = ki2.getGroup(msg.to)
					targets = []
					for g in gs.members:
						if _kicktarget == g.displayName:
							targets.append(g.mid)
							if targets == []:
								cl.sendText(msg.to,"Not found")
							else:
								for target in targets:
									try:
										wait["blacklist"][target] = True
										f=codecs.open('st2__b.json','w','utf-8')
										json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
										k3.sendText(msg.to,"Succes Yuda")
									except:
										ki.sendText(msg.to,"error")
            elif "Ban @" in msg.text:
				if msg.from_ in admin:
					if msg.toType == 2:
						print "[Ban]ok"
						_name = msg.text.replace("Ban @","")
						_nametarget = _name.rstrip('  ')
						gs = ki.getGroup(msg.to)
						gs = kk.getGroup(msg.to)
						targets = []
						for g in gs.members:
							if _nametarget == g.displayName:
								targets.append(g.mid)
						if targets == []:
							ki.sendText(msg.to,"Tidak Ada Boss Yuda")
						else:
							for target in targets:
								try:
									wait["blacklist"][target] = True
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
									ki.sendText(msg.to,"Done Boss yuda")
								except:
									ki.sendText(msg.to,"Error")
            elif "Unban @" in msg.text:
				if msg.from_ in admin:
					if msg.toType == 2:
						print "[Unban]ok"
						_name = msg.text.replace("Unban @","")
						_nametarget = _name.rstrip('  ')
						gs = ki.getGroup(msg.to)
						gs = kk.getGroup(msg.to)
						gs = kc.getGroup(msg.to)
						targets = []
						for g in gs.members:
							if _nametarget == g.displayName:
								targets.append(g.mid)
						if targets == []:
							ki.sendText(msg.to,"Tidak Ada Boss Yuda")
							kk.sendText(msg.to,"Tidak Ada Boss Yuda")
						else:
							for target in targets:
								try:
									del wait["blacklist"][target]
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
									ki.sendText(msg.to,"Done Boss yuda")
								except:
									ki.sendText(msg.to,"Done Boss yuda")
            elif "Mes @" in msg.text:
				if msg.from_ in admin:
					if msg.toType == 2:
						print "[Mes]ok"
						_name = msg.text.replace("Mes @","")
						_nametarget = _name.rstrip('  ')
						gs = ki.getGroup(msg.to)
						gs = kk.getGroup(msg.to)
						targets = []
						for g in gs.members:
							if _nametarget == g.displayName:
								targets.append(g.mid)
						if targets == []:
							ki.sendText(msg.to,"Tidak Ada Boss Yuda")
						else:
							for target in targets:
								try:
									wait["teman"][target] = True
									f=codecs.open('teman.json','w','utf-8')
									json.dump(wait["teman"], f, sort_keys=True, indent=4,ensure_ascii=False)
									ki.sendText(msg.to,"Done Boss yuda")
								except:
									ki.sendText(msg.to,"Error")
            elif "Unmes @" in msg.text:
				if msg.from_ in admin:
					if msg.toType == 2:
						print "[Unmes]ok"
						_name = msg.text.replace("Unmes @","")
						_nametarget = _name.rstrip('  ')
						gs = ki.getGroup(msg.to)
						gs = kk.getGroup(msg.to)
						gs = kc.getGroup(msg.to)
						targets = []
						for g in gs.members:
							if _nametarget == g.displayName:
								targets.append(g.mid)
						if targets == []:
							ki.sendText(msg.to,"Tidak Ada Boss Yuda")
							kk.sendText(msg.to,"Tidak Ada Boss Yuda")
						else:
							for target in targets:
								try:
									del wait["teman"][target]
									f=codecs.open('teman.json','w','utf-8')
									json.dump(wait["teman"], f, sort_keys=True, indent=4,ensure_ascii=False)
									ki.sendText(msg.to,"Done Boss yuda")
								except:
									ki.sendText(msg.to,"Done Boss yuda")
#-------------ListGroup-----------------
            elif msg.text in ["List group"]:
              if msg.from_ in admin:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[🔵] %s\n" % (cl.getGroup(i).name +"👥▶["+str(len(cl.getGroup(i).members))+"]")
                cl.sendText(msg.to,"👥⏩🌐[List Group]🌐⏪👥\n"+ h +"Total Group =" +"["+str(len(gid))+"]")
#-----------------------------------------------
            elif "Unban all" in msg.text:
				if msg.from_ in admin:
					if msg.toType == 2:
						print "[Unban]ok"
						_name = msg.text.replace("Unban all","")
						gs = cl.getGroup(msg.to)
						gs = ki.getGroup(msg.to)
						gs = kk.getGroup(msg.to)
						gs = kc.getGroup(msg.to)
						gs = ka.getGroup(msg.to)
						gs = kb.getGroup(msg.to)
						gs = kd.getGroup(msg.to)
						gs = kf.getGroup(msg.to)
						gs = kp.getGroup(msg.to)
						cl.sendText(msg.to,"Semua Telah Di Hapus")
						targets = []
						for g in gs.members:
							if _name in g.displayName:
								targets.append(g.mid)
						if targets == []:
							ki.sendText(msg.to,"Tidak Ada Boss Yuda")
							kk.sendText(msg.to,"Tidak Ada Boss Yuda")
						else:
							for target in targets:
								try:
									del wait["blacklist"][target]
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
								except:
									ki.sendText(msg.to,"Done Boss yuda")
#-----------------------------------------------
            elif "Teman all" in msg.text:
				if msg.from_ in admin:
					if msg.toType == 2:
						print "[Teman]ok"
						_name = msg.text.replace("Teman all","")
						gs = cl.getGroup(msg.to)
						gs = ki.getGroup(msg.to)
						gs = kk.getGroup(msg.to)
						gs = kc.getGroup(msg.to)
						gs = ka.getGroup(msg.to)
						gs = kb.getGroup(msg.to)
						gs = kd.getGroup(msg.to)
						gs = kf.getGroup(msg.to)
						gs = kp.getGroup(msg.to)
						cl.sendText(msg.to,"oke")
						targets = []
						for g in gs.members:
							if _name in g.displayName:
																targets.append(g.mid)
						if targets == []:
							ki.sendText(msg.to,"Tidak Ada Boss Yuda")
						else:
							for target in targets:
								try:
									wait["teman"][target] = True
									f=codecs.open('teman.json','w','utf-8')
									json.dump(wait["teman"], f, sort_keys=True, indent=4,ensure_ascii=False)
								except:
									ki.sendText(msg.to,"Error")
#-----------------------------------------------
            elif msg.text in ["Backup","backup"]:
                    contact = cl.getProfile()
                    backup = cl.getProfile()
                    backup.displayName = contact.displayName
                    backup.statusMessage = contact.statusMessage
                    backup.pictureStatus = contact.pictureStatus
                    cl.updateProfile(backup.pictureStatus)
                    cl.updateProfile(backup.statusMessage)
                    cl.updateProfile(backup.displayName)
                    cl.sendText(msg.to, "Telah kembali semula")
#-------------Fungsi Creator Finish-----------------#
            elif "Spam: " in msg.text:
              if msg.from_ in admin:
                txt = msg.text.split(" ")
                jmlh = int(txt[2])
                teks = msg.text.replace("Spam: ")+str(txt[1])+" "+str(jmlh + " ","")
                tulisan = jmlh * (teks+"\n")
                 #@reno.a.w
                if txt[1] == "on":
                    if jmlh <= 300:
                       for x in range(jmlh):
                           cl.sendText(msg.to, teks)
                    else:
                       cl.sendText(msg.to, "Kelebihan batas:v")
                elif txt[1] == "off":
                    if jmlh <= 300:
                        cl.sendText(msg.to, tulisan)
                    else:
                        cl.sendText(msg.to, "Kelebihan batas :v")
#-----------------------------------------------
            elif "name1:" in msg.text:
              if msg.from_ in yuda:
                string = msg.text.replace("name1:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
#-----------------------------------------------
            elif "name2:" in msg.text:
              if msg.from_ in yuda:
                string = msg.text.replace("name2:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = kc.getProfile()
                    profile.displayName = string
                    kc.updateProfile(profile)
#-----------------------------------------------
            elif "name3:" in msg.text:
              if msg.from_ in yuda:
                string = msg.text.replace("name3:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
#-----------------------------------------------
            elif "name4:" in msg.text:
              if msg.from_ in yuda:
                string = msg.text.replace("name4:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = kk.getProfile()
                    profile.displayName = string
                    kk.updateProfile(profile)
#-----------------------------------------------
            elif "name5:" in msg.text:
              if msg.from_ in yuda:
                string = msg.text.replace("name5:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = ka.getProfile()
                    profile.displayName = string
                    ka.updateProfile(profile)
#-----------------------------------------------
            elif "name6:" in msg.text:
              if msg.from_ in yuda:
                string = msg.text.replace("name6:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = kb.getProfile()
                    profile.displayName = string
                    kb.updateProfile(profile)
#-----------------------------------------------
            elif "name7:" in msg.text:
              if msg.from_ in yuda:
                string = msg.text.replace("name7:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = kd.getProfile()
                    profile.displayName = string
                    kd.updateProfile(profile)
#-----------------------------------------------
            elif "name8:" in msg.text:
              if msg.from_ in yuda:
                string = msg.text.replace("name8:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = kf.getProfile()
                    profile.displayName = string
                    kf.updateProfile(profile)
#-----------------------------------------------
            elif "name9:" in msg.text:
              if msg.from_ in yuda:
                string = msg.text.replace("name9:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = km.getProfile()
                    profile.displayName = string
                    km.updateProfile(profile)
#-----------------------------------------------
            elif "name10:" in msg.text:
              if msg.from_ in yuda:
                string = msg.text.replace("name10:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = kn.getProfile()
                    profile.displayName = string
                    kn.updateProfile(profile)
#-----------------------------------------------
            elif "name11:" in msg.text:
              if msg.from_ in yuda1:
                string = msg.text.replace("name11:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = kp.getProfile()
                    profile.displayName = string
                    kp.updateProfile(profile)
#-----------------------------------------------
            elif "name12:" in msg.text:
              if msg.from_ in yuda1:
                string = msg.text.replace("name12:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = kg.getProfile()
                    profile.displayName = string
                    kg.updateProfile(profile)
#-----------------------------------------------
            elif "name13:" in msg.text:
              if msg.from_ in yuda:
                string = msg.text.replace("name13:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = ks.getProfile()
                    profile.displayName = string
                    ks.updateProfile(profile)
#-----------------------------------------------
            elif "status1:" in msg.text:
              if msg.from_ in yuda:
                string = msg.text.replace("status1:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = cl.getProfile()
                    profile.statusMessage = string
                    cl.updateProfile(profile)
#-----------------------------------------------
            elif "status2:" in msg.text:
              if msg.from_ in yuda:
                string = msg.text.replace("status2:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = kc.getProfile()
                    profile.statusMessage = string
                    kc.updateProfile(profile)
#-----------------------------------------------
            elif "status3:" in msg.text:
              if msg.from_ in yuda:
                string = msg.text.replace("status3:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = ki.getProfile()
                    profile.statusMessage = string
                    ki.updateProfile(profile)
#-----------------------------------------------
            elif "status4:" in msg.text:
              if msg.from_ in yuda:
                string = msg.text.replace("status4:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = kk.getProfile()
                    profile.statusMessage = string
                    kk.updateProfile(profile)
#-----------------------------------------------
            elif "status5:" in msg.text:
              if msg.from_ in yuda:
                string = msg.text.replace("status5:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = ka.getProfile()
                    profile.statusMessage = string
                    ka.updateProfile(profile)
#-----------------------------------------------
            elif "status6:" in msg.text:
              if msg.from_ in yuda:
                string = msg.text.replace("status6:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = kb.getProfile()
                    profile.statusMessage = string
                    kb.updateProfile(profile)
#-----------------------------------------------
            elif "status7:" in msg.text:
              if msg.from_ in yuda:
                string = msg.text.replace("status7:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = kd.getProfile()
                    profile.statusMessage = string
                    kd.updateProfile(profile)
#-----------------------------------------------
            elif "status8:" in msg.text:
              if msg.from_ in yuda:
                string = msg.text.replace("status8:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = kf.getProfile()
                    profile.statusMessage = string
                    kf.updateProfile(profile)
#-----------------------------------------------
            elif "status9:" in msg.text:
              if msg.from_ in yuda:
                string = msg.text.replace("status9:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = km.getProfile()
                    profile.statusMessage = string
                    km.updateProfile(profile)
#-----------------------------------------------
            elif "status10:" in msg.text:
              if msg.from_ in yuda:
                string = msg.text.replace("status10:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = kn.getProfile()
                    profile.statusMessage = string
                    kn.updateProfile(profile)
#-----------------------------------------------
            elif msg.text.lower() == 'respons':
                profile = cl.getProfile()
                text = profile.displayName + "􀜁􀅔􏿿"
                cl.sendText(msg.to, text)
                profile = kc.getProfile()
                text = profile.displayName + "􀜁􀅔􏿿"
                kc.sendText(msg.to, text)
                profile = kk.getProfile()
                text = profile.displayName + "􀜁􀅔􏿿"
                kk.sendText(msg.to, text)
                profile = ki.getProfile()
                text = profile.displayName + "􀜁􀅔􏿿"
                ki.sendText(msg.to, text)
                profile = kb.getProfile()
                text = profile.displayName + "􀜁􀅔􏿿"
                kb.sendText(msg.to, text)
                profile = kd.getProfile()
                text = profile.displayName + "􀜁􀅔􏿿"
                kd.sendText(msg.to, text)
                profile = ka.getProfile()
                text = profile.displayName + "􀜁􀅔􏿿"
                ka.sendText(msg.to, text)
                profile = kf.getProfile()
                text = profile.displayName + "􀜁􀅔􏿿"
                kf.sendText(msg.to, text)
                profile = km.getProfile()
                text = profile.displayName + "􀜁􀅔􏿿"
                km.sendText(msg.to, text)
                profile = kn.getProfile()
                text = profile.displayName + "􀜁􀅔􏿿"
                kn.sendText(msg.to, text)
                profile = kp.getProfile()
                text = profile.displayName + "􀜁􀅔􏿿"
                kp.sendText(msg.to, text)
                profile = kg.getProfile()
                text = profile.displayName + "􀜁􀅔􏿿"
                kg.sendText(msg.to, text)
                profile = ks.getProfile()
                text = profile.displayName + "􀜁􀅔􏿿"
                ks.sendText(msg.to, text)
                profile = kx.getProfile()
                text = profile.displayName + "􀜁􀅔􏿿"
                kx.sendText(msg.to, text)
#-----------------------------------------------
            elif msg.text.lower() == 'status':
                profile = cl.getProfile()
                text = profile.statusMessage
                cl.sendText(msg.to, text)
                profile = kc.getProfile()
                text = profile.statusMessage + "􀜁􀅔􏿿"
                kc.sendText(msg.to, text)
                profile = kk.getProfile()
                text = profile.statusMessage + "􀜁􀅔􏿿"
                kk.sendText(msg.to, text)
                profile = ki.getProfile()
                text = profile.statusMessage + "􀜁􀅔􏿿"
                ki.sendText(msg.to, text)
                profile = kb.getProfile()
                text = profile.statusMessage + "􀜁􀅔􏿿"
                kb.sendText(msg.to, text)
                profile = kd.getProfile()
                text = profile.statusMessage + "􀜁􀅔􏿿"
                kd.sendText(msg.to, text)
                profile = ka.getProfile()
                text = profile.statusMessage + "􀜁􀅔􏿿"
                ka.sendText(msg.to, text)
                profile = kf.getProfile()
                text = profile.statusMessage + "􀜁􀅔􏿿"
                kf.sendText(msg.to, text)
                profile = km.getProfile()
                text = profile.statusMessage + "􀜁􀅔􏿿"
                km.sendText(msg.to, text)
                profile = kn.getProfile()
                text = profile.statusMessage + "􀜁􀅔􏿿"
                kn.sendText(msg.to, text)
                profile = kp.getProfile()
                text = profile.statusMessage + "􀜁􀅔􏿿"
                kp.sendText(msg.to, text)
                profile = kg.getProfile()
                text = profile.statusMessage + "􀜁􀅔􏿿"
                kg.sendText(msg.to, text)
#-----------------------------------------------
            elif "Steal @" in msg.text:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        steal = msg.text.replace("Steal @","")
                        stealname = steal.rstrip(" ")
                        group = cl.getGroup(msg.to)
                        targets = []
                        if steal == "":
                            cl.sendText(msg.to,"Invalid user")
                        else:
                            for i in group.members:
                                if stealname == i.displayName:
                                    targets.append(i.mid)
                            if targets == []:
                                cl.sendText(msg.to,"User tidak ditemukan")
                            else:
                                for target in targets:
                                    try:
                                        contact = cl.getContact(target)
                                        image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                        try:
                                            cover = cl.channel.getCover(contact)
                                        except:
                                            cover = ""
                                        try:
                                            cl.sendText(msg.to,"Gambar Foto Profilenya")
                                            cl.sendImageWithURL(msg.to,image)
                                            if cover == "":
                                                cl.sendText(msg.to,"User tidak memiliki cover atau sejenisnya")
                                            else:
                                                cl.sendText(msg.to,"Gambar Covernya")
                                                cl.sendImageWithURL(msg.to,cover)
                                        except Exception as error:
                                            cl.sendText(msg.to,(error))
                                            break
                                    except:
                                        cl.sendText(msg.to,"Error!")
                                        break
                    else:
                        cl.sendText(msg.to,"Tidak bisa dilakukan di luar wilayah")
#--------------------------------------------------------
            elif "/say " in msg.text.lower():
                    query = msg.text.replace("/say ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'https://google-translate-proxy.herokuapp.com/api/tts'
                        params = {'language': 'id', 'speed': '1', 'query': query}
                        r    = s.get(url, params=params)
                        mp3  = r.url
                        cl.sendAudioWithURL(msg.to, mp3)
#-----------------------------------------------
            elif msg.text in ["Test"]:
					ki.sendText(msg.to,"Yuda disini!!")
					kb.sendText(msg.to,"Siap disini tasya")
#-----------------------------------------------
            elif "Yuda say " in msg.text:
					bctxt = msg.text.replace("Yuda say ","")
					ki.sendText(msg.to,(bctxt))
					kc.sendText(msg.to,(bctxt))
					cl.sendText(msg.to,(bctxt))
            elif "Tasya say " in msg.text:
					bctxt = msg.text.replace("Tasya say ","")
					ka.sendText(msg.to,(bctxt))
					kb.sendText(msg.to,(bctxt))
					kd.sendText(msg.to,(bctxt))
            elif "Fikas say " in msg.text:
					bctxt = msg.text.replace("Fikas say ","")
					kp.sendText(msg.to,(bctxt))
					kg.sendText(msg.to,(bctxt))
            elif "Cinta say " in msg.text:
					bctxt = msg.text.replace("Cinta say ","")
					kn.sendText(msg.to,(bctxt))
					km.sendText(msg.to,(bctxt))
					kf.sendText(msg.to,(bctxt))
#-----------------------------------------------

            elif msg.text in ["Admin","Pembuatid"]:
				ki.sendText(msg.to,"line.me/ti/p/~yuda9d")
				kb.sendText(msg.to,"line.me/ti/p/~naufal_opalminecraft")

#-----------------------------------------------

            elif msg.text in ["#welcome"]:
                ki.sendText(msg.to,"Selamat datang di yuda dan tasya Family Room")
                kk.sendText(msg.to,"Jangan nakal ok! subscribe YouTube.com/YudaTheGoldMine dan https://m.youtube.com/channel/UCyZPQxy3TZk_8CdE9Q1bpoA")
                
#-----------------------------------------------
            elif msg.text in ["PING","Ping","ping"]:
				ki.sendText(msg.to,"Some 􀜁􀅔Har Har􏿿")
				kk.sendText(msg.to,"mabar mcpe yok")
				kc.sendText(msg.to,"Yuuk 􀜁􀅔Har Har􏿿")
				kb.sendText(msg.to,"Pong Wkwkwkwk")
#-----------------------------------------------
            elif msg.text in ["Responsename","respon","Respon"]:
                ki.sendText(msg.to,"YudaBot Disini")
                kk.sendText(msg.to,"YouTube.com/YudaTheGoldMine")
                kc.sendText(msg.to,"idline yuda9d")
                kb.sendText(msg.to,"tasya_ disini")
                kb.sendText (msg.to,"https://m.youtube.com/channel/UCyZPQxy3TZk_8CdE9Q1bpoA")
                kd.sendText(msg.to,"Halo__ semua")
#-----------------------------------------------

            elif msg.text in ["kcpt","Kecepatan","kecepatan"]:
					start = time.time()
					cl.sendText(msg.to, "Tunggu Ya Semua")
					elapsed_time = time.time() - start
					cl.sendText(msg.to, "%s/Detik" % (elapsed_time))
					elapsed_time = time.time() - start
					ka.sendText(msg.to, "%s/Detik" % (elapsed_time))
					elapsed_time = time.time() - start
					kn.sendText(msg.to, "%s/Detik" % (elapsed_time))
					elapsed_time = time.time() - start
					kg.sendText(msg.to, "%s/Detik" % (elapsed_time))
#------------------------------------------------------------------
            elif msg.text in ["Ban"]:
				if msg.from_ in admin:
					wait["wblacklist"] = True
					cl.sendText(msg.to,"send contact")					
            elif msg.text in ["Unban"]:
				if msg.from_ in admin:
					wait["dblacklist"] = True
					cl.sendText(msg.to,"send contact")					
            elif msg.text in ["Banlist"]:
				if msg.from_ in admin:
					if wait["blacklist"] == {}:
						cl.sendText(msg.to,"nothing")
					else:
						cl.sendText(msg.to,"Blacklist user")
						mc = ""
						for mi_d in wait["blacklist"]:
							mc += "->" +cl.getContact(mi_d).displayName + "\n"
						cl.sendText(msg.to,mc)
            elif msg.text in ["banlist"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						group = cl.getGroup(msg.to)
						gMembMids = [contact.mid for contact in group.members]
						matched_list = []
						for tag in wait["blacklist"]:
							matched_list+=filter(lambda str: str == tag, gMembMids)
						cocoa = ""
						for mm in matched_list:
							cocoa += mm + "\n"
						cl.sendText(msg.to,cocoa + "")
            elif msg.text in ["Flist"]:
				if msg.from_ in admin:
					if wait["teman"] == {}:
						cl.sendText(msg.to,"nothing")
					else:
						cl.sendText(msg.to,"Ini list teman kita")
						mc = ""
						for mi_d in wait["teman"]:
							mc += "->" +cl.getContact(mi_d).displayName + "\n"
						cl.sendText(msg.to,mc)
            elif msg.text in ["flist"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						group = cl.getGroup(msg.to)
						gMembMids = [contact.mid for contact in group.members]
						matched_list = []
						for tag in wait["teman"]:
							matched_list+=filter(lambda str: str == tag, gMembMids)
						cocoa = ""
						for mm in matched_list:
							cocoa += mm + "\n"
						cl.sendText(msg.to,cocoa + "")
            elif msg.text in ["Usir ban"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						group = random.choice(KAC).getGroup(msg.to)
						gMembMids = [contact.mid for contact in group.members]
						matched_list = []
						for tag in wait["blacklist"]:
							matched_list+=filter(lambda str: str == tag, gMembMids)
						if matched_list == []:
							random.choice(KAC).sendText(msg.to,"There was no blacklist user")
							return
						for jj in matched_list:
							random.choice(KAC).kickoutFromGroup(msg.to,[jj])
						random.choice(KAC).sendText(msg.to,"Bye...")
            elif msg.text in ["Clear"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						group = random.choice(KAC).getGroup(msg.to)
						gMembMids = [contact.mid for contact in group.invitee]
						for _mid in gMembMids:
							random.choice(KAC).cancelGroupInvitation(msg.to,[_mid])
						random.choice(KAC).sendText(msg.to,"I pretended to cancel and canceled.")
            elif "rayaqw:" in msg.text:
				if msg.from_ in admin:
					if msg.toType == 2:
						strnum = msg.text.replace("random:","")
						source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
						try:
							num = int(strnum)
							group = cl.getGroup(msg.to)
							for var in range(0,num):
								name = "".join([random.choice(source_str) for x in xrange(10)])
								time.sleep(0.01)
								group.name = name
								cl.updateGroup(group)
						except:
							cl.sendText(msg.to,"Error")
            elif "albumâ†�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77771ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777" in msg.text:
				if msg.from_ in admin:
					try:
						albumtags = msg.text.replace("albumâ†�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77771ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777","")
						gid = albumtags[:6]
						name = albumtags.replace(albumtags[:34],"")
						cl.createAlbum(gid,name)
						cl.sendText(msg.to,name + "created an album")
					except:
						cl.sendText(msg.to,"Error")
            elif "fakecâ†�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77771ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777" in msg.text:
				if msg.from_ in admin:
					try:
						source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
						name = "".join([random.choice(source_str) for x in xrange(10)])
						anu = msg.text.replace("fakecâ†�1ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77771ￄ1�71ￄ1�771ￄ1�71ￄ1�7771ￄ1�71ￄ1�771ￄ1�71ￄ1�77777","")
						cl.sendText(msg.to,str(cl.channel.createAlbum(msg.to,name,anu)))
					except Exception as e:
						try:
							cl.sendText(msg.to,str(e))
						except:
							pass
        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True
def autolike():
			for zx in range(0,20):
				hasil = cl.activity(limit=20)
				if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
					try:    
						cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
						cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by @yuda")
						kk.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
						kk.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like By line://ti/p/~yuda9d")
						print "Like"
					except:
							pass
				else:
						print "Already Liked"
			time.sleep(500)
thread2 = threading.Thread(target=autolike)
thread2.daemon = True
thread2.start()

def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
