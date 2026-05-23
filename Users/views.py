import re

from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from Users.models import UserRegister_Model, Phishing_Model, SendMailModel, PhishingThread_Model, FeedbackModel


def userlogin(request):
    pawd = ''
    usname = ''
    li = ''
    ans = ''
    cl = []
    serh = []
    prm = []
    splt = ''
    if request.method == "POST":
        usname = request.POST.get('email')
        pawd = request.POST.get('password')
        try:

            check = UserRegister_Model.objects.get(email=usname, password=pawd)
            request.session['userid'] = check.id
            return redirect('userpage')
        except:
            splt = (re.findall(r"[\w']+", str(usname)))
            for a in splt:
                if a in ('http'):
                    serh.append(a)
                elif a in ('com', 'in', 'info', 'edu'):
                    prm.append(a)
                else:
                    li = list(usname)
                    for f in li:

                        if f in ('0', '1', '2', '3', '4', '5', '6', '8', '9'):
                            cl.append(f)
                        else:
                            ans = 'Whaling Phishing Email'

            if len(cl):
                ans = 'Spear Phishing Email'
            elif len(prm):
                ans = 'Pharming Phishing Email'
            elif len(serh):
                ans = ' Search Engine Phishing Attack'
    Phishing_Model.objects.create(attack_type=ans, text=usname)


    return render(request,'users/userlogin.html',{'a':ans,'b':usname})

def userregister(request):
    if request.method=="POST":
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        userid=request.POST.get('userid')
        password=request.POST.get('password')
        gender=request.POST.get('gender')
        UserRegister_Model.objects.create(fname=fname,lname=lname,email=email,userid=userid,password=password,gender=gender)
        return redirect('userlogin')


    return render(request,'users/userregister.html')

def mydetails(request):

    return render(request,'users/mydetails.html')

def userpage(request):
    uid = request.session['userid']
    request_obj = UserRegister_Model.objects.get(id=uid)
    se = ''
    pos = []
    neg = []
    oth = []
    mm = ''
    sa = ''
    ro = 0
    cat = ''
    ss = ''
    cos = []
    sos = []
    tos = []
    vos = []

    edcount, bcount, scount, fcount, acount, ecount, hcount, ocount = 0, 0, 0, 0, 0, 0, 0, 0
    edw, bw, sw, fw, aw, ew, hw, oth = [], [], [], [], [], [], [], []
    if request.method == "POST":
        to1 = request.POST.get('to')
        sub = request.POST.get('subject')
        cht = request.POST.get('chat')
        to_mail = request_obj.email
        c = (re.findall(r"[\w']+", str(cht)))
        for f in c:

            if f in ('agitate', 'argue', 'clamor', 'combat', 'contend', 'contest', 'dispute', 'feud', 'oppugn',
                     'skirmish', 'strive', 'tug', 'wrestle', 'clamor', 'contest', 'dispute', 'feud', 'oppugn',
                     'skirmish', 'agitate', 'argue', 'clamor', 'combat', 'contend', 'carnage', 'purge', 'slaughter',
                     'argue', 'battle', 'brawl', 'buckcombat', 'conflict', 'contend', 'crossswords', 'differ',
                     'disagree',
                     'encounter', 'feud', 'fret', 'gall', 'grapple', 'grate', 'quarrel', 'wrangle', 'buck', 'clash',
                     'contend',
                     'contest', 'cope', 'defy', 'dispute', 'battle', ' duel', 'engage', 'fight', 'oppose', 'repel',
                     'bom', 'attack',):

                pos.append(f)
            elif f in (
            'weapon', 'doomsday ', 'machine', 'mininuke', 'mirv', 'nuke', 'H-bomb', 'nuke', 'Dagger', 'Falchion',
            'Katana', 'Knife', 'Longsword', 'Shortsword', 'Ulfberht', 'Estoc', 'Rapier', 'Club', 'Flail', 'Mace',
            'Pernach', 'Shestophor', 'Maul', 'Quarterstaff', 'Bludgeon', 'Ahlspiess', 'Bardiche', 'Bill', 'Glaive',
            'Guisarme', 'Lance', 'hammer', 'Partisan', 'Pike', 'Ranseur', 'Sovnya', 'Spetum', 'Swordstaff', 'Voulge',
            'War-scythe', 'hammer', 'Bow', 'Longbow', 'Crossbow', 'Arbalest', 'Ballista', 'crossbow', 'Sling',
            'weapons', 'Chakram', 'Francisca', 'Kunai', 'Spear', 'Shuriken', 'Culverin', 'cannon', 'Arquebus', 'Musket',
            'Ranged',):

                neg.append(f)
            elif f in (
                    'brutal', 'crazy', 'cruel', 'fierce', 'homicidal', 'hysterical', 'murderous', 'passionate',
                    'potent',
                    'powerful', 'savage', 'uncontrollable', 'vicious', 'agitated', 'aroused', 'berserk', 'bloodthirsty',
                    'coercive', 'demoniac', 'desperate', 'distraught', 'disturbed', 'enraged', 'fiery', 'forceful',
                    'forcible',
                    'frantic', 'fuming', 'furious', 'great', 'headstrong', 'hotheaded', 'impassioned', 'impetuous',
                    'inflamed',
                    'intemperate', 'mad', 'maddened', 'maniacal', 'mighty', 'raging', 'riotous', 'rough', 'strong',
                    'ungovernable', 'unrestrained', 'urgent', 'vehement', 'wild', 'acute', 'cutting', 'distressing',
                    'excruciating', 'exquisite', 'fierce', 'keen', 'overpowering', 'overwhelming', 'piercing',
                    'poignant',
                    'powerful', 'racking', 'severe', 'sharp', 'shooting', 'stabbing', 'sudden', 'violent', 'agonizing',
                    'disturbing', 'excruciating', 'extreme', 'fierce', 'harrowing', 'intense', 'racking', 'struggling',
                    'tearing', 'tormenting', 'tortuous', 'torturing', 'vehement',):
                cos.append(f)
            elif f in (
                    'threateningly', 'threateners', 'threatening', 'threatener', 'threatened', 'threating', 'threatens',
                    'threaten', 'threated', 'threats', 'counterthreat', 'blackmail', 'hazard', 'intimidation', 'menace',
                    'peril', 'risk', 'bluff', 'commination', 'fix', 'foreboding', 'foreshadowing', 'fulmination',
                    'impendence', 'omen', 'portent', 'presage', 'thunder', 'bugbear', 'apprehension', 'bogey', 'bogy',
                    'boogeyman', 'bugaboo', 'dread', 'fear', 'goblin', 'gremlin', 'hobgoblin', 'loup-garou', 'ogre',
                    'problem', 'scare', 'specter', 'terror', 'threat', 'wraith', 'dare', 'defiance', 'demanding',
                    'demur', 'ultimatum', 'remonstrance', 'summons to contest', 'coercion', 'browbeating',):
                sos.append(f)
            elif f in (
                    'corrupt', 'deplorable', 'illegal', 'illegitimate', 'illicit', 'immoral', 'scandalous', 'senseless',
                    'unlawful', 'vicious', 'bent', 'heavy', 'racket', 'wildcat', 'wrong', 'caught', 'crooked',
                    'culpable',
                    'dirty', 'hung up', 'indictable', 'iniquitous', 'nefarious', 'peccant', 'shady', 'unrighteous',
                    'villainous', 'wicked', 'banned', 'criminal', 'illicit', 'unconstitutional', 'unlawful', 'base',
                    'corrupt',
                    'criminal', 'delinquent', 'evil', 'iniquitous', 'mean', 'reprobate', 'sinful', 'vicious', 'vile',
                    'villainous', 'wicked', 'wrong', 'brigand', 'criminal', 'crook', 'desperado', 'forager', 'gangster',
                    'gunperson', 'highwayperson',):
                tos.append(f)
            elif f in (
                    'smuggling', 'rum-running', 'stealing', 'prostitution', 'slavery', 'bootlegging', 'counterfeiting',
                    'dealing', 'goods', 'moonshine', 'piracy', 'plunder', 'poaching', 'rum-running',
                    'smuggling', 'stuff', 'swag', 'theft', 'trafficking', 'violation', 'wetbacking',
                    'hijacking''infringement', 'plagiarism', 'theft', 'bootlegging', 'buccaneering', 'rapine',
                    'stealing', 'swashbuckling', 'commandeering', 'freebooting', 'marauding', 'pirating', 'bootlegging',
                    'counterfeiting', 'moonshine', 'piracy', 'plunder', 'poaching', 'rum-running', 'smuggling',
                    'stuff', 'swag', 'theft', 'trafficking', 'violation', 'wetbacking', 'carjack', 'commandeer',
                    'kidnap', 'steal', 'shanghai', 'skyjack', 'annex', 'borrow', 'clap', 'confiscate', 'cop',
                    'embezzle', 'filch', 'grab', 'hijack', 'liberate', 'lift', 'misappropriate', 'pilfer',):
                vos.append(f)

        if len(pos) > len(neg) and len(pos) > len(cos) and len(pos) > len(sos) and len(pos) > len(tos) and len(
                pos) > len(vos):
            cat = "EmailOnline Services"
        elif len(neg) > len(pos) and len(neg) > len(cos) and len(neg) > len(sos) and len(neg) > len(tos) and len(
                neg) > len(vos):
            cat = "Financial"
        elif len(cos) > len(pos) and len(cos) > len(neg) and len(cos) > len(sos) and len(cos) > len(tos) and len(
                cos) > len(vos):
            cat = "Payment Services"
        elif len(sos) > len(pos) and len(sos) > len(neg) and len(sos) > len(cos) and len(sos) > len(tos) and len(
                sos) > len(vos):
            cat = "Cloud Storage File Hosting"
        elif len(tos) > len(pos) and len(tos) > len(neg) and len(tos) > len(cos) and len(tos) > len(sos) and len(
                tos) > len(vos):
            cat = "Softwares A-Services"
        elif len(vos) > len(pos) and len(vos) > len(neg) and len(vos) > len(cos) and len(vos) > len(sos) and len(
                vos) > len(tos):
            cat = "Social Networking"
        else:
            cat = "other"
        ss = len(pos)

    if (len(pos) > 0):
        sa = 'spam'
    elif (len(neg) > 0):
        sa = 'spam'
    elif (len(cos) > 0):
        sa = 'spam'
    elif (len(sos) > 0):
        sa = 'spam'
    elif (len(tos) > 0):
        sa = 'spam'
    elif (len(vos) > 0):
        sa = 'spam'
    else:
        sa = 'inbox'
    if request.method == "POST":
        to1 = request.POST.get('to')
        sub = request.POST.get('subject')
        cht = request.POST.get('chat')

        to_mail = request_obj.email
        SendMailModel.objects.create(sendermail=to_mail, to=to1, subject=sub, chat=cht, spam=sa, category=cat)

    return render(request,'users/userpage.html',{'obj':ss,'a':cat,'ji':sa,})



def mydetails(request):
    usid=request.session['userid']
    us_id=UserRegister_Model.objects.get(id=usid)
    return render(request,'users/mydetails.html',{'obje':us_id})




def viewmailpage(request):
    uid = request.session['userid']
    request_obj = UserRegister_Model.objects.get(id=uid)
    to_mail = request_obj.email
    obj=SendMailModel.objects.filter(spam='inbox')
    return render(request,'users/viewmailpage.html',{'form':obj})


def spampage(request):
    uid = request.session['userid']
    request_obj = UserRegister_Model.objects.get(id=uid)
    to_mail = request_obj.email
    obj = SendMailModel.objects.filter( spam='spam')
    return render(request,'users/spampage.html',{'objects':obj})


def checking(request):
    userid = request.session['userid']
    objec = UserRegister_Model.objects.get(id=userid)
    cate1 = []
    cate2, cate3, cate4, cate5, cate6, cate7, cate8, cate9, cate10, cate11, cate12, cate13, cate14, cate15, cate16, cate17, = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
    s = ''
    txt = ''
    c = ''
    malware = ''
    nu = ''
    ans = ''

    if request.method == "POST":
        txt = request.POST.get("name")

        c = (re.findall(r"[\w']+", str(txt)))
        malware = (
        'secret,cloudsecure,phonemodel,bankid,keyid,apikey,iosid,networkoperator,privateid,decid,yourname,panid,hidedata')
        s = malware.split(',')
        for attack in s:
            for url in c:
                if url == attack:
                    nu = nu + url
        if len(nu) > 0:
            ans = "Phishing Is Detected"
        else:
            ans = 'legitimate'
        PhishingThread_Model.objects.create(usid=objec,website=txt,atk=ans)


    return render(request,'users/checking.html',{'ans':ans})


def checking_attack(request):
    userid = request.session['userid']
    objec = UserRegister_Model.objects.get(id=userid)
    obj=PhishingThread_Model.objects.filter(usid=objec)
    return render(request,'users/checking_attack.html',{'obj':obj})

def deleteobj(request,pk):
    obj = get_object_or_404(SendMailModel, pk=pk)
    obj.delete()
    return redirect('viewmailpage')

def spamdeleteobj(request,pk):
    obj = get_object_or_404(SendMailModel, pk=pk)
    obj.delete()
    return redirect('spampage')

def feedback(request):
    uid = request.session['userid']
    objec = UserRegister_Model.objects.get(id=uid)
    if request.method == "POST":
        feed = request.POST.get('feedback')
        FeedbackModel.objects.create(username=objec, feedback=feed)
    return render(request,'users/feedback.html')
