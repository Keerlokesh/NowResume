from django.http import HttpResponse

from django.shortcuts import render
import inline as inline

from .models import Resumes, Suggesstions
# Setting style for bar graphs
import matplotlib.pyplot as plt

from .models import Templates


def sitemap(request):
    return render(request, 'NowOwnResume/sitemap.xml')


def admin(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        password = request.POST.get('password')
        if uname == 'lucky' and password == '123':
            return render(request, 'admin/admin.html', {'access': True})

    return render(request, 'admin/admin_login.html', {'aut': True})


def admin_loggedin(request):
    return render(request, 'admin/admin.html')


def admin_suggesstion(request):
    sugg = Suggesstions.objects.all()

    return render(request, 'admin/admin_suggesstion.html', {'suggess': sugg})


def admin_template(request):
    if request.method == 'POST':
        temp = request.POST.get('template', '')
        tempimg = request.POST.get('templateImage', '')
        t = Templates(templateFile=temp, image=tempimg)
        t.save()
    return render(request, 'admin/admin_template.html')


def admin_viewresumes(request):
    rdetails = Resumes.objects.all()
    return render(request, 'admin/admin_viewresumes.html', {'resumedetails': rdetails})


def home(request):
    thank = False
    if request.method == 'POST':
        n = request.POST.get('name', '')
        mob = request.POST.get('mobile', '')
        add = request.POST.get('address', '')
        email = request.POST.get('email', '')
        suggestion = request.POST.get('suggestion', '')
        sugg = Suggesstions(name=n, email=email, address=add, mob=mob, suggestion=suggestion)
        sugg.save()
        thank = True
    return render(request, 'NowOwnResume/index.html', {'thank': thank})


def aboutus(request):
    return render(request, 'NowOwnResume/about.html')


def preDesigned(request):
    temp = Templates.objects.all()
    return render(request, 'NowOwnResume/predesigned.html', {'template': temp})


def contactus(request):
    return render(request, 'NowOwnResume/contactus.html')


def donate(request):
    return render(request, 'NowOwnResume/donate.html')


def customized(request):
    naming = ''

    complete = False

    if request.method == 'POST':
        bg = request.POST.get('background')
        rbackground = request.POST.get('rightBackground')
        textcolor = request.POST.get('textColor')
        n = request.POST.get('name', 'none')
        dob = request.POST.get('DOB', '01/01/2000')
        mob = request.POST.get('mobile', '')
        add = request.POST.get('address', '')
        stt = request.POST.get('state', '')
        add = add + ' , ' + stt
        checks = request.POST.get('check', '')
        mob = 'Mobile No. ' + mob
        objective = request.POST.get('careerObjective', '')

        qclass1 = request.POST.get('Qualification1Class', '')
        qschool1 = request.POST.get('Qualification1School', '')
        qper1 = request.POST.get('Qualification1Percent', '')
        qdate1 = request.POST.get('Qualification1Date', '')
        q11 = '' + qclass1 + '\n' + qschool1 + '\n' + '( ' + qper1 + ' )  ' + qdate1

        qclass2 = request.POST.get('Qualification2Class', '')
        qschool2 = request.POST.get('Qualification2School', '')
        qper2 = request.POST.get('Qualification2Percent', '')
        qdate2 = request.POST.get('Qualification2Date', '')
        q22 = '' + qclass2 + '\n' + qschool2 + '\n' + '( ' + qper2 + ' )  ' + qdate2

        qclass3 = request.POST.get('Qualification3Class', '')
        qschool3 = request.POST.get('Qualification3College', '')
        qper3 = request.POST.get('Qualification3Percent', '')
        qdate3 = request.POST.get('Qualification3Date', '')
        q33 = '' + qclass3 + '\n' + qschool3 + '\n' + '( ' + qper3 + ' )  ' + qdate3

        interest11 = request.POST.get('interest1', '')
        interest22 = request.POST.get('interest2', '')
        interest33 = request.POST.get('interest3', '')
        interests1 = interest11 + '\n' + interest22 + '\n' + interest33

        skill1 = request.POST.get('skill1', '')
        skill2 = request.POST.get('skill2', '')
        skill3 = request.POST.get('skill3', '')
        skill4 = request.POST.get('skill3', '')
        skill5 = request.POST.get('skill3', '')
        skills = '' + skill1 + '\n' + skill2 + '\n' + skill3 + '\n' + skill4 + '\n' + skill5

        hobby1 = request.POST.get('hobby1', '')
        hobby2 = request.POST.get('hobby2', '')
        hobby3 = request.POST.get('hobby3', '')
        hobbies = '' + hobby1 + '\n' + hobby2 + '\n' + hobby3

        lang1 = request.POST.get('language', '')
        languages = '' + lang1

        str1 = request.POST.get('st1', '')
        str2 = request.POST.get('st2', '')
        str3 = request.POST.get('st3', '')
        strength = '' + str1 + '\n' + str2 + '\n' + str3

        header = ''
        name = 'Name - ' + n
        dob = 'DOB - ' + dob
        mobileno = 'Mob No. - ' + mob
        address = '' + add

        objective1 = 'Career Objective'
        careerobjective1 = objective

        interest = 'Interests'

        qualification = 'Qualifications'
        q1 = '' + q11
        q2 = '' + q22
        q3 = '' + q33

        language = 'Language Known'
        lang = '' + languages

        hobbies1 = 'Hobbies'

        skills1 = 'Skills'

        # set font
        plt.rcParams['font.family'] = 'sans-serif'
        plt.rcParams['font.sans-serif'] = 'STIXGeneral'
        fig, ax = plt.subplots(figsize=(8.5, 12))
        # Decorative Lines
        ax.axvline(x=.5, ymin=0, ymax=1, color='#94f3ff', alpha=0.0, linewidth=50)
        plt.axvline(x=.8, color=rbackground, alpha=0.5, linewidth=150)
        plt.axhline(y=1, xmin=0, xmax=1, color='#ffffff', linewidth=1)
        # set background color
        ax.set_facecolor(bg)
        # remove axes
        plt.axis('off')
        title = dob + '\n' + mob
        # add text
        plt.annotate(header, (.02, .98), weight='regular', fontsize=8, alpha=.75)
        plt.annotate(n, (.02, .94), weight='bold', fontsize=14)
        plt.annotate(title, (.02, .89), weight='regular', fontsize=9)

        plt.annotate('Career Objectives', (.02, .85), weight='bold', fontsize=10, color=textcolor)
        plt.annotate(careerobjective1, (.02, .825), weight='regular', fontsize=8)

        plt.annotate('Address', (.7, .970), weight='bold', fontsize=9, color=textcolor)

        if len(add) > 60:
            add = '' + add[0:29] + '\n' + add[30:59] + '\n' + add[60:]
        elif len(add) > 30:
            add = '' + add[0:29] + '\n' + add[29:]
        plt.annotate(add, (.7, .935), weight='regular', fontsize=8, color=textcolor)

        plt.annotate('Technical Skills', (.02, .765), weight='bold', fontsize=10, color=textcolor)
        plt.annotate(skills, (.04, .675), weight='regular', fontsize=7)

        plt.annotate(qualification, (.02, .645), weight='bold', fontsize=10, color=textcolor)
        plt.annotate(q1, (.04, .580), weight='regular', fontsize=7)
        plt.annotate(q2, (.04, .520), weight='regular', fontsize=7)
        plt.annotate(q3, (.04, .460), weight='regular', fontsize=7)

        plt.annotate(interest, (.02, .415), weight='bold', fontsize=10, color=textcolor)

        plt.annotate(interests1, (.04, .340), weight='regular', fontsize=7)

        plt.annotate(language, (.02, .290), weight='bold', fontsize=10, color=textcolor)
        plt.annotate(lang, (.04, .250), weight='regular', fontsize=7)

        plt.annotate('Strengths', (.02, .200), weight='bold', fontsize=10, color=textcolor)
        plt.annotate(strength, (.04, .130), weight='regular', fontsize=7)

        if len(hobbies) > 60:
            add = '' + add[0:20] + '\n' + add[21:41] + '\n' + add[41:]
        elif len(hobbies) > 30:
            add = '' + add[0:20] + '\n' + add[21:]
        plt.annotate('Hobbies', (.7, .820), weight='bold', fontsize=10, color=textcolor)
        plt.annotate(hobbies, (.7, .740), weight='regular', fontsize=7, color=textcolor)

        naming = 'static/Customized/' + n + '.png'
        complete = True
        plt.savefig(naming, dpi=300, bbox_inches='tight')
        naming = "/static/Customized/" + n + ".pdf"
        resume = Resumes(name=n, address=add, mob=mob, type='Customized Resume')
        resume.save()
    return render(request, 'NowOwnResume/customized.html', {'fname': naming, 'checks': complete})


def templates(request):
    return render(request, 'NowOwnResume/templates.html')


def basictemplate(request):
    return render(request, 'NowOwnResume/basictemplate.html')


def basictemplates(request):
    naming = ''

    complete = False
    if request.method == 'POST':
        n = request.POST.get('name', '')
        dob = request.POST.get('DOB', '01/01/2000')
        mob = request.POST.get('mobile', '')
        add = request.POST.get('address', '')
        stt = request.POST.get('state', '')
        add = add + ' , ' + stt
        checks = request.POST.get('check', '')

        objective = request.POST.get('careerObjective', '')

        qclass1 = request.POST.get('Qualification1Class', '')
        qschool1 = request.POST.get('Qualification1School', '')
        qper1 = request.POST.get('Qualification1Percent', '')
        qdate1 = request.POST.get('Qualification1Date', '')
        q11 = '' + qclass1 + '\n' + qschool1 + '\n' + '( ' + qper1 + ' )  ' + qdate1

        qclass2 = request.POST.get('Qualification2Class', '')
        qschool2 = request.POST.get('Qualification2School', '')
        qper2 = request.POST.get('Qualification2Percent', '')
        qdate2 = request.POST.get('Qualification2Date', '')
        q22 = '' + qclass2 + '\n' + qschool2 + '\n' + '( ' + qper2 + ' )  ' + qdate2

        qclass3 = request.POST.get('Qualification3Class', '')
        qschool3 = request.POST.get('Qualification3College', '')
        qper3 = request.POST.get('Qualification3Percent', '')
        qdate3 = request.POST.get('Qualification3Date', '')
        q33 = '' + qclass3 + '\n' + qschool3 + '\n' + '( ' + qper3 + ' )  ' + qdate3

        interest11 = request.POST.get('interest1', '')
        interest22 = request.POST.get('interest2', '')
        interest33 = request.POST.get('interest3', '')
        interests1 = interest11 + '\n' + interest22 + '\n' + interest33

        skill1 = request.POST.get('skill1', '')
        skill2 = request.POST.get('skill2', '')
        skill3 = request.POST.get('skill3', 'n')
        skills = '' + skill1 + '\n' + skill2 + '\n' + skill3

        hobby1 = request.POST.get('hobby1', '')
        hobby2 = request.POST.get('hobby2', '')
        hobby3 = request.POST.get('hobby3', '')
        hobbies = '' + hobby1 + '\n' + hobby2 + '\n' + hobby3

        lang1 = request.POST.get('language', '')
        languages = '' + lang1

        header = ''
        name = 'Name - ' + n
        dob = 'DOB - ' + dob
        mobb = mob
        mob = 'Mob No. - ' + mob
        address = '' + add

        objective1 = 'Career Objective'
        careerobjective1 = objective

        interest = 'Interests'

        qualification = 'Qualifications'
        q1 = '' + q11
        q2 = '' + q22
        q3 = '' + q33

        language = 'Language Known'
        lang = '' + languages

        hobbies1 = 'Hobbies'

        skills1 = 'Skills'

        # set font
        plt.rcParams['font.family'] = 'sans-serif'
        plt.rcParams['font.sans-serif'] = 'STIXGeneral'
        fig, ax = plt.subplots(figsize=(8.5, 11))

        # set font
        plt.rcParams['font.family'] = 'sans-serif'
        plt.rcParams['font.sans-serif'] = 'STIXGeneral'
        fig, ax = plt.subplots(figsize=(8.5, 11))

        # Decorative Lines
        ax.axvline(x=.5, ymin=0, ymax=1, color='#ffffff', alpha=0.0, linewidth=50)
        plt.axvline(x=.99, color='#ffffff', alpha=0.5, linewidth=1000)
        plt.axhline(y=.80, xmin=0, xmax=1, color='#000000', linewidth=3)
        # set background color
        ax.set_facecolor('white')
        # remove axes
        plt.axis('off')

        plt.annotate(header, (.02, .98), weight='regular', fontsize=8, alpha=.75)
        plt.annotate(name, (.02, .94), weight='bold', fontsize=20)
        plt.annotate(dob, (.02, .89), weight='regular', fontsize=12)
        plt.annotate(mob, (.02, .870), weight='regular', fontsize=12, color='#000000')
        plt.annotate(address, (.02, .820), weight='regular', fontsize=12, color='#000000')

        plt.annotate(objective, (.02, .75), weight='bold', fontsize=14, alpha=.75)
        plt.annotate(careerobjective1, (.02, .720), weight='regular', fontsize=9)

        plt.annotate(interest, (.02, .685), weight='bold', fontsize=14)
        plt.annotate(interests1, (.02, .610), weight='regular', fontsize=8, color='#000000')

        plt.annotate(qualification, (.02, .580), weight='bold', fontsize=14, color='#000000')
        plt.annotate(q1, (.02, .520), weight='regular', fontsize=8, color='#000000')
        plt.annotate(q2, (.02, .470), weight='regular', fontsize=8, color='#000000')
        plt.annotate(q3, (.02, .420), weight='regular', fontsize=8, color='#000000')

        plt.annotate(skills1, (.02, .370), weight='bold', fontsize=14, color='#000000')
        plt.annotate(skills, (.02, .300), weight='regular', fontsize=8, color='#000000')

        plt.annotate(hobbies1, (.02, .250), weight='bold', fontsize=14, color='#000000')
        plt.annotate(hobbies, (.02, .200), weight='regular', fontsize=8, color='#000000')

        plt.annotate(language, (.02, .140), weight='bold', fontsize=14, color='#000000')
        plt.annotate(lang, (.02, .090), weight='regular', fontsize=8, color='#000000')

        naming = 'static/BasicResume/' + n + '.png'
        complete = True
        plt.savefig(naming, dpi=300, bbox_inches='tight')
        naming = "/static/BasicResume/" + n + ".pdf"
        resume = Resumes(name=n, address=add, mob=mobb, type='Basic Resume')
        resume.save()
    return render(request, 'NowOwnResume/basicresume.html', {'fname': naming, 'checks': complete})


def suggestions(request):
    thank = False
    if request.method == 'POST':
        n = request.POST.get('name', '')
        mob = request.POST.get('mobile', '')
        add = request.POST.get('address', '')
        email = request.POST.get('email', '')
        suggestion = request.POST.get('suggestion', '')
        sugg = Suggesstions(name=n, email=email, address=add, mob=mob, suggestion=suggestion)
        sugg.save()
        thank = True
    return render(request, 'NowOwnResume/suggestions.html', {'thank': thank})


def basicResume(request):
    return render(request, 'NowOwnResume/basicresume.html')


def simpleResume(request):
    naming = ''

    complete = False

    if request.method == 'POST':
        n = request.POST.get('name', '')
        dob = request.POST.get('DOB', '01/01/2000')
        mob = request.POST.get('mobile', '')
        add = request.POST.get('address', '')
        stt = request.POST.get('state', '')
        add = add + ' , ' + stt
        checks = request.POST.get('check', '')

        objective = request.POST.get('careerObjective', '')

        qclass1 = request.POST.get('Qualification1Class', '')
        qschool1 = request.POST.get('Qualification1School', '')
        qper1 = request.POST.get('Qualification1Percent', '')
        qdate1 = request.POST.get('Qualification1Date', '')
        q11 = '' + qclass1 + '\n' + qschool1 + '\n' + '( ' + qper1 + ' )  ' + qdate1

        qclass2 = request.POST.get('Qualification2Class', '')
        qschool2 = request.POST.get('Qualification2School', '')
        qper2 = request.POST.get('Qualification2Percent', '')
        qdate2 = request.POST.get('Qualification2Date', '')
        q22 = '' + qclass2 + '\n' + qschool2 + '\n' + '( ' + qper2 + ' )  ' + qdate2

        qclass3 = request.POST.get('Qualification3Class', '')
        qschool3 = request.POST.get('Qualification3College', '')
        qper3 = request.POST.get('Qualification3Percent', '')
        qdate3 = request.POST.get('Qualification3Date', '')
        q33 = '' + qclass3 + '\n' + qschool3 + '\n' + '( ' + qper3 + ' )  ' + qdate3

        interest11 = request.POST.get('interest1', '')
        interest22 = request.POST.get('interest2', '')
        interest33 = request.POST.get('interest3', '')
        interests1 = interest11 + '\n' + interest22 + '\n' + interest33

        skill1 = request.POST.get('skill1', '')
        skill2 = request.POST.get('skill2', '')
        skill3 = request.POST.get('skill3', '')
        skills = '' + skill1 + '\n' + skill2 + '\n' + skill3

        hobby1 = request.POST.get('hobby1', '')
        hobby2 = request.POST.get('hobby2', '')
        hobby3 = request.POST.get('hobby3', '')
        hobbies = '' + hobby1 + '\n' + hobby2 + '\n' + hobby3

        lang1 = request.POST.get('language', '')
        languages = '' + lang1

        header = ''
        name = 'Name - ' + n
        dob = 'DOB - ' + dob
        mobileno = 'Mob No. - ' + mob
        address = '' + add

        objective1 = 'Career Objective'
        careerobjective1 = objective

        interest = 'Interests'

        qualification = 'Qualifications'
        q1 = '' + q11
        q2 = '' + q22
        q3 = '' + q33

        language = 'Language Known'
        lang = '' + languages

        hobbies1 = 'Hobbies'

        skills1 = 'Skills'

        # set font
        plt.rcParams['font.family'] = 'sans-serif'
        plt.rcParams['font.sans-serif'] = 'STIXGeneral'
        fig, ax = plt.subplots(figsize=(8.5, 11))

        # set font
        plt.rcParams['font.family'] = 'sans-serif'
        plt.rcParams['font.sans-serif'] = 'STIXGeneral'
        fig, ax = plt.subplots(figsize=(8.5, 11))

        # Decorative Lines
        ax.axvline(x=.5, ymin=0, ymax=1, color='#ffffff', alpha=0.0, linewidth=50)
        plt.axvline(x=.99, color='#ffffff', alpha=0.5, linewidth=1000)
        plt.axhline(y=1, xmin=0, xmax=1, color='#c7c5f0', linewidth=250)
        # set background color
        ax.set_facecolor('white')
        # remove axes
        plt.axis('off')

        plt.annotate(header, (.02, .98), weight='regular', fontsize=8, alpha=.75)
        plt.annotate(name, (.02, .94), weight='bold', fontsize=20)
        plt.annotate(dob, (.02, .89), weight='regular', fontsize=12)
        plt.annotate(mobileno, (.02, .870), weight='regular', fontsize=12, color='#000000')
        plt.annotate(address, (.02, .820), weight='regular', fontsize=12, color='#000000')

        plt.annotate(objective, (.02, .75), weight='bold', fontsize=14, alpha=.75)
        plt.annotate(careerobjective1, (.02, .720), weight='regular', fontsize=9)

        plt.annotate(interest, (.02, .675), weight='bold', fontsize=14)
        plt.annotate(interests1, (.02, .610), weight='regular', fontsize=8, color='#000000')

        plt.annotate(qualification, (.02, .580), weight='bold', fontsize=14, color='#000000')
        plt.annotate(q1, (.02, .520), weight='regular', fontsize=8, color='#000000')
        plt.annotate(q2, (.02, .470), weight='regular', fontsize=8, color='#000000')
        plt.annotate(q3, (.02, .420), weight='regular', fontsize=8, color='#000000')

        plt.annotate(skills1, (.02, .370), weight='bold', fontsize=14, color='#000000')
        plt.annotate(skills, (.02, .300), weight='regular', fontsize=8, color='#000000')

        plt.annotate(hobbies1, (.02, .250), weight='bold', fontsize=14, color='#000000')
        plt.annotate(hobbies, (.02, .200), weight='regular', fontsize=8, color='#000000')

        plt.annotate(language, (.02, .140), weight='bold', fontsize=14, color='#000000')
        plt.annotate(lang, (.02, .090), weight='regular', fontsize=8, color='#000000')

        naming = 'static/ResumeFiles/' + n + '.png'
        complete = True
        plt.savefig(naming, dpi=300, bbox_inches='tight')
        naming = "/static/ResumeFiles/" + n + ".pdf"
        resume = Resumes(name=n, address=add, mob=mob, type='Basic Resume')
        resume.save()

    return render(request, 'NowOwnResume/SimpleResume.html', {'fname': naming, 'checks': complete})


def attractive(request):
    naming = ''

    complete = False

    if request.method == 'POST':
        n = request.POST.get('name', '')
        dob = request.POST.get('DOB', '01/01/2000')
        mob = request.POST.get('mobile', '')
        add = request.POST.get('address', '')
        stt = request.POST.get('state', '')
        add = add + ' , ' + stt
        checks = request.POST.get('check', '')
        mob = 'Mobile No. ' + mob
        objective = request.POST.get('careerObjective', '')

        qclass1 = request.POST.get('Qualification1Class', '')
        qschool1 = request.POST.get('Qualification1School', '')
        qper1 = request.POST.get('Qualification1Percent', '')
        qdate1 = request.POST.get('Qualification1Date', '')
        q11 = '' + qclass1 + '\n' + qschool1 + '\n' + '( ' + qper1 + ' )  ' + qdate1

        qclass2 = request.POST.get('Qualification2Class', '')
        qschool2 = request.POST.get('Qualification2School', '')
        qper2 = request.POST.get('Qualification2Percent', '')
        qdate2 = request.POST.get('Qualification2Date', '')
        q22 = '' + qclass2 + '\n' + qschool2 + '\n' + '( ' + qper2 + ' )  ' + qdate2

        qclass3 = request.POST.get('Qualification3Class', '')
        qschool3 = request.POST.get('Qualification3College', '')
        qper3 = request.POST.get('Qualification3Percent', '')
        qdate3 = request.POST.get('Qualification3Date', '')
        q33 = '' + qclass3 + '\n' + qschool3 + '\n' + '( ' + qper3 + ' )  ' + qdate3

        interest11 = request.POST.get('interest1', '')
        interest22 = request.POST.get('interest2', '')
        interest33 = request.POST.get('interest3', 'n')
        interests1 = interest11 + '\n' + interest22 + '\n' + interest33

        skill1 = request.POST.get('skill1', '')
        skill2 = request.POST.get('skill2', '')
        skill3 = request.POST.get('skill3', '')
        skills = '' + skill1 + '\n' + skill2 + '\n' + skill3

        hobby1 = request.POST.get('hobby1', '')
        hobby2 = request.POST.get('hobby2', '')
        hobby3 = request.POST.get('hobby3', '')
        hobbies = '' + hobby1 + '\n' + hobby2 + '\n' + hobby3

        lang1 = request.POST.get('language', '')
        languages = '' + lang1

        str1 = request.POST.get('st1', '')
        str2 = request.POST.get('st2', '')
        str3 = request.POST.get('st3', '')
        strength = '' + str1 + '\n' + str2 + '\n' + str3

        header = ''
        name = 'Name - ' + n
        dob = 'DOB - ' + dob
        mobileno = 'Mob No. - ' + mob
        address = '' + add

        objective1 = 'Career Objective'
        careerobjective1 = objective

        interest = 'Interests'

        qualification = 'Qualifications'
        q1 = '' + q11
        q2 = '' + q22
        q3 = '' + q33

        language = 'Language Known'
        lang = '' + languages

        hobbies1 = 'Hobbies'

        skills1 = 'Skills'

        # set font
        plt.rcParams['font.family'] = 'sans-serif'
        plt.rcParams['font.sans-serif'] = 'STIXGeneral'
        fig, ax = plt.subplots(figsize=(8.5, 11))
        # Decorative Lines
        ax.axvline(x=.5, ymin=0, ymax=1, color='#007ACC', alpha=0.0, linewidth=50)
        plt.axvline(x=.99, color='#000000', alpha=0.5, linewidth=300)
        plt.axhline(y=.88, xmin=0, xmax=1, color='#ffffff', linewidth=3)
        # set background color
        ax.set_facecolor('white')
        # remove axes
        plt.axis('off')
        title = dob + '\n' + mob
        # add text
        plt.annotate(header, (.02, .98), weight='regular', fontsize=8, alpha=.75)
        plt.annotate(n, (.02, .94), weight='bold', fontsize=15)
        plt.annotate(title, (.02, .89), weight='regular', fontsize=9)

        plt.annotate('Career Objectives', (.02, .85), weight='bold', fontsize=10, color='#58C1B2')
        plt.annotate(careerobjective1, (.02, .825), weight='regular', fontsize=8)

        plt.annotate('Address', (.7, .965), weight='bold', fontsize=9, color='#58C1B2')
        plt.annotate(add, (.7, .935), weight='regular', fontsize=8, color='#ffffff')

        plt.annotate('Skills', (.02, .78), weight='bold', fontsize=10, color='#58C1B2')
        plt.annotate(skills, (.04, .720), weight='regular', fontsize=9)

        plt.annotate(qualification, (.02, .660), weight='bold', fontsize=10, color='#58C1B2')
        plt.annotate(q1, (.04, .580), weight='regular', fontsize=10)
        plt.annotate(q2, (.04, .520), weight='regular', fontsize=10)
        plt.annotate(q3, (.04, .460), weight='regular', fontsize=10)

        plt.annotate(interest, (.02, .425), weight='bold', fontsize=10, color='#58C1B2')

        plt.annotate(interests1, (.04, .360), weight='regular', fontsize=9)

        plt.annotate(language, (.02, .290), weight='bold', fontsize=10, color='#58C1B2')
        plt.annotate(lang, (.04, .250), weight='regular', fontsize=9)

        plt.annotate('Strengths', (.02, .200), weight='bold', fontsize=10, color='#58C1B2')
        plt.annotate(strength, (.04, .130), weight='regular', fontsize=9)

        plt.annotate('Hobbies', (.7, .820), weight='bold', fontsize=10, color='#ffffff')
        plt.annotate(hobbies, (.7, .740), weight='regular', fontsize=10, color='#ffffff')

        naming = 'static/AttractiveResumes/' + n + '.png'
        complete = True
        plt.savefig(naming, dpi=300, bbox_inches='tight')
        naming = "/static/AttractiveResumes/" + n + ".pdf"
        resume = Resumes(name=n, address=add, mob=mob, type='Basic Resume')
        resume.save()
    return render(request, 'NowOwnResume/AttraciveResume.html', {'fname': naming, 'checks': complete})


def softwareEngg(request):
    naming = ''

    complete = False

    if request.method == 'POST':
        n = request.POST.get('name', '')
        dob = request.POST.get('DOB', '01/01/2000')
        mob = request.POST.get('mobile', '')
        add = request.POST.get('address', '')
        stt = request.POST.get('state', '')
        add = add + ' , ' + stt
        checks = request.POST.get('check', 'none')
        mob = 'Mobile No. ' + mob
        objective = request.POST.get('careerObjective', '')

        qclass1 = request.POST.get('Qualification1Class', '')
        qschool1 = request.POST.get('Qualification1School', '')
        qper1 = request.POST.get('Qualification1Percent', '')
        qdate1 = request.POST.get('Qualification1Date', '')
        q11 = '' + qclass1 + '\n' + qschool1 + '\n' + '( ' + qper1 + ' )  ' + qdate1

        qclass2 = request.POST.get('Qualification2Class', '')
        qschool2 = request.POST.get('Qualification2School', '')
        qper2 = request.POST.get('Qualification2Percent', '')
        qdate2 = request.POST.get('Qualification2Date', '')
        q22 = '' + qclass2 + '\n' + qschool2 + '\n' + '( ' + qper2 + ' )  ' + qdate2

        qclass3 = request.POST.get('Qualification3Class', '')
        qschool3 = request.POST.get('Qualification3College', '')
        qper3 = request.POST.get('Qualification3Percent', '')
        qdate3 = request.POST.get('Qualification3Date', '')
        q33 = '' + qclass3 + '\n' + qschool3 + '\n' + '( ' + qper3 + ' )  ' + qdate3

        interest11 = request.POST.get('interest1', '')
        interest22 = request.POST.get('interest2', '')
        interest33 = request.POST.get('interest3', '')
        interests1 = interest11 + '\n' + interest22 + '\n' + interest33

        skill1 = request.POST.get('skill1', '')
        skill2 = request.POST.get('skill2', '')
        skill3 = request.POST.get('skill3', '')
        skill4 = request.POST.get('skill3', '')
        skill5 = request.POST.get('skill3', '')
        skills = '' + skill1 + '\n' + skill2 + '\n' + skill3 + '\n' + skill4 + '\n' + skill5

        hobby1 = request.POST.get('hobby1', '')
        hobby2 = request.POST.get('hobby2', '')
        hobby3 = request.POST.get('hobby3', '')
        hobbies = '' + hobby1 + '\n' + hobby2 + '\n' + hobby3

        lang1 = request.POST.get('language', '')
        languages = '' + lang1

        str1 = request.POST.get('st1', '')
        str2 = request.POST.get('st2', '')
        str3 = request.POST.get('st3', '')
        strength = '' + str1 + '\n' + str2 + '\n' + str3

        header = ''
        name = 'Name - ' + n
        dob = 'DOB - ' + dob
        mobileno = 'Mob No. - ' + mob
        address = '' + add

        objective1 = 'Career Objective'
        careerobjective1 = objective

        interest = 'Interests'

        qualification = 'Qualifications'
        q1 = '' + q11
        q2 = '' + q22
        q3 = '' + q33

        language = 'Language Known'
        lang = '' + languages

        hobbies1 = 'Hobbies'

        skills1 = 'Skills'

        # set font
        plt.rcParams['font.family'] = 'sans-serif'
        plt.rcParams['font.sans-serif'] = 'STIXGeneral'
        fig, ax = plt.subplots(figsize=(8.5, 12))
        # Decorative Lines
        ax.axvline(x=.5, ymin=0, ymax=1, color='#94f3ff', alpha=0.0, linewidth=50)
        plt.axvline(x=.99, color='#2ed3e8', alpha=0.5, linewidth=300)
        plt.axhline(y=.88, xmin=0, xmax=1, color='#ffffff', linewidth=3)
        # set background color
        ax.set_facecolor('white')
        # remove axes
        plt.axis('off')
        title = dob + '\n' + mob
        # add text
        plt.annotate(header, (.02, .98), weight='regular', fontsize=8, alpha=.75)
        plt.annotate(n, (.02, .94), weight='bold', fontsize=14)
        plt.annotate(title, (.02, .89), weight='regular', fontsize=9)

        plt.annotate('Career Objectives', (.02, .85), weight='bold', fontsize=10, color='#2ed3e8')
        plt.annotate(careerobjective1, (.02, .825), weight='regular', fontsize=8)

        plt.annotate('Address', (.7, .970), weight='bold', fontsize=9, color='#ffffff')

        if len(add) > 60:
            add = '' + add[0:29] + '\n' + add[30:59] + '\n' + add[60:]
        elif len(add) > 30:
            add = '' + add[0:29] + '\n' + add[29:]
        plt.annotate(add, (.7, .935), weight='regular', fontsize=8, color='#ffffff')

        plt.annotate('Technical Skills', (.02, .765), weight='bold', fontsize=10, color='#2ed3e8')
        plt.annotate(skills, (.04, .675), weight='regular', fontsize=7)

        plt.annotate(qualification, (.02, .645), weight='bold', fontsize=10, color='#2ed3e8')
        plt.annotate(q1, (.04, .580), weight='regular', fontsize=7)
        plt.annotate(q2, (.04, .520), weight='regular', fontsize=7)
        plt.annotate(q3, (.04, .460), weight='regular', fontsize=7)

        plt.annotate(interest, (.02, .415), weight='bold', fontsize=10, color='#2ed3e8')

        plt.annotate(interests1, (.04, .340), weight='regular', fontsize=7)

        plt.annotate(language, (.02, .290), weight='bold', fontsize=10, color='#2ed3e8')
        plt.annotate(lang, (.04, .250), weight='regular', fontsize=7)

        plt.annotate('Strengths', (.02, .200), weight='bold', fontsize=10, color='#2ed3e8')
        plt.annotate(strength, (.04, .130), weight='regular', fontsize=7)

        if len(hobbies) > 60:
            add = '' + add[0:20] + '\n' + add[21:41] + '\n' + add[41:]
        elif len(hobbies) > 30:
            add = '' + add[0:20] + '\n' + add[21:]
        plt.annotate('Hobbies', (.7, .820), weight='bold', fontsize=10, color='#ffffff')
        plt.annotate(hobbies, (.7, .740), weight='regular', fontsize=7, color='#ffffff')

        naming = 'static/Soft/' + n + '.pdf'
        complete = True
        plt.savefig(naming, dpi=300, bbox_inches='tight')
        naming = "/static/Soft/" + n + ".pdf"
        resume = Resumes(name=n, address=add, mob=mob, type='Software Engineer Resume')
        resume.save()
    return render(request, 'NowOwnResume/SoftwareEngineer.html', {'fname': naming, 'checks': complete})


def download(request, name):
    return render(request, 'NowOwnResume/download.html', name)


def simpleNew(request):
    naming = ''

    complete = False

    if request.method == 'POST':
        n = request.POST.get('name', '')
        dob = request.POST.get('DOB', '01/01/2000')
        mob = request.POST.get('mobile', '')
        add = request.POST.get('address', '')
        stt = request.POST.get('state', '')
        add = add + ' , ' + stt
        checks = request.POST.get('check', '')

        objective = request.POST.get('careerObjective', '')

        qclass1 = request.POST.get('Qualification1Class', '')
        qschool1 = request.POST.get('Qualification1School', '')
        qper1 = request.POST.get('Qualification1Percent', '')
        qdate1 = request.POST.get('Qualification1Date', '')
        q11 = '' + qclass1 + '\n' + qschool1 + '\n' + '( ' + qper1 + ' )  ' + qdate1

        qclass2 = request.POST.get('Qualification2Class', '')
        qschool2 = request.POST.get('Qualification2School', '')
        qper2 = request.POST.get('Qualification2Percent', '')
        qdate2 = request.POST.get('Qualification2Date', '')
        q22 = '' + qclass2 + '\n' + qschool2 + '\n' + '( ' + qper2 + ' )  ' + qdate2

        qclass3 = request.POST.get('Qualification3Class', '')
        qschool3 = request.POST.get('Qualification3College', '')
        qper3 = request.POST.get('Qualification3Percent', '')
        qdate3 = request.POST.get('Qualification3Date', '')
        q33 = '' + qclass3 + '\n' + qschool3 + '\n' + '( ' + qper3 + ' )  ' + qdate3

        interest11 = request.POST.get('interest1', '')
        interest22 = request.POST.get('interest2', '')
        interest33 = request.POST.get('interest3', '')
        interests1 = interest11 + '\n' + interest22 + '\n' + interest33

        skill1 = request.POST.get('skill1', '')
        skill2 = request.POST.get('skill2', '')
        skill3 = request.POST.get('skill3', '')
        skills = '' + skill1 + '\n' + skill2 + '\n' + skill3

        hobby1 = request.POST.get('hobby1', '')
        hobby2 = request.POST.get('hobby2', '')
        hobby3 = request.POST.get('hobby3', '')
        hobbies = '' + hobby1 + '\n' + hobby2 + '\n' + hobby3

        lang1 = request.POST.get('language', '')
        languages = '' + lang1

        header = ''
        name = 'Name - ' + n
        dob = 'DOB - ' + dob
        mobileno = 'Mob No. - ' + mob
        address = '' + add

        objective1 = 'Career Objective'
        careerobjective1 = objective

        interest = 'Interests'

        qualification = 'Qualifications'
        q1 = '' + q11
        q2 = '' + q22
        q3 = '' + q33

        language = 'Language Known'
        lang = '' + languages

        hobbies1 = 'Hobbies'

        skills1 = 'Skills'

        # set font
        plt.rcParams['font.family'] = 'sans-serif'
        plt.rcParams['font.sans-serif'] = 'STIXGeneral'
        fig, ax = plt.subplots(figsize=(8.5, 11))

        # set font
        plt.rcParams['font.family'] = 'sans-serif'
        plt.rcParams['font.sans-serif'] = 'STIXGeneral'
        fig, ax = plt.subplots(figsize=(8.5, 11))

        # Decorative Lines
        ax.axvline(x=.5, ymin=0, ymax=1, color='#ffffff', alpha=0.0, linewidth=50)
        plt.axvline(x=.99, color='#ffffff', alpha=0.5, linewidth=1000)
        plt.axhline(y=1, xmin=0, xmax=1, color='#fae3ff', linewidth=1250)
        # set background color
        ax.set_facecolor('white')
        # remove axes
        plt.axis('off')

        plt.annotate(header, (.02, .98), weight='regular', fontsize=8, alpha=.75)
        plt.annotate(name, (.02, .94), weight='bold', fontsize=20)
        plt.annotate(dob, (.02, .89), weight='regular', fontsize=12)
        plt.annotate(mobileno, (.02, .870), weight='regular', fontsize=12, color='#000000')
        plt.annotate(address, (.02, .820), weight='regular', fontsize=12, color='#000000')

        plt.annotate(objective, (.02, .75), weight='bold', fontsize=14, alpha=.75)
        plt.annotate(careerobjective1, (.02, .720), weight='regular', fontsize=9)

        plt.annotate(interest, (.02, .675), weight='bold', fontsize=14)
        plt.annotate(interests1, (.02, .610), weight='regular', fontsize=8, color='#000000')

        plt.annotate(qualification, (.02, .580), weight='bold', fontsize=14, color='#000000')
        plt.annotate(q1, (.02, .520), weight='regular', fontsize=8, color='#000000')
        plt.annotate(q2, (.02, .470), weight='regular', fontsize=8, color='#000000')
        plt.annotate(q3, (.02, .420), weight='regular', fontsize=8, color='#000000')

        plt.annotate(skills1, (.02, .370), weight='bold', fontsize=14, color='#000000')
        plt.annotate(skills, (.02, .300), weight='regular', fontsize=8, color='#000000')

        plt.annotate(hobbies1, (.02, .250), weight='bold', fontsize=14, color='#000000')
        plt.annotate(hobbies, (.02, .200), weight='regular', fontsize=8, color='#000000')

        plt.annotate(language, (.02, .140), weight='bold', fontsize=14, color='#000000')
        plt.annotate(lang, (.02, .090), weight='regular', fontsize=8, color='#000000')

        naming = 'static/simpleNew/' + n + '.png'
        complete = True
        plt.savefig(naming, dpi=300, bbox_inches='tight')
        naming = "/static/simpleNew/" + n + ".pdf"
        resume = Resumes(name=n, address=add, mob=mob, type='Basic Resume')
        resume.save()

    return render(request, 'NowOwnResume/simpleNew.html', {'fname': naming, 'checks': complete})


def simpleNewest(request):
    naming = ''

    complete = False

    if request.method == 'POST':
        n = request.POST.get('name', '')
        dob = request.POST.get('DOB', '01/01/2000')
        mob = request.POST.get('mobile', '')
        add = request.POST.get('address', '')
        stt = request.POST.get('state', '')
        add = add + ' , ' + stt
        checks = request.POST.get('check', '')

        objective = request.POST.get('careerObjective', '')

        qclass1 = request.POST.get('Qualification1Class', '')
        qschool1 = request.POST.get('Qualification1School', '')
        qper1 = request.POST.get('Qualification1Percent', '')
        qdate1 = request.POST.get('Qualification1Date', '')
        q11 = '' + qclass1 + '\n' + qschool1 + '\n' + '( ' + qper1 + ' )  ' + qdate1

        qclass2 = request.POST.get('Qualification2Class', '')
        qschool2 = request.POST.get('Qualification2School', '')
        qper2 = request.POST.get('Qualification2Percent', '')
        qdate2 = request.POST.get('Qualification2Date', '')
        q22 = '' + qclass2 + '\n' + qschool2 + '\n' + '( ' + qper2 + ' )  ' + qdate2

        qclass3 = request.POST.get('Qualification3Class', '')
        qschool3 = request.POST.get('Qualification3College', '')
        qper3 = request.POST.get('Qualification3Percent', '')
        qdate3 = request.POST.get('Qualification3Date', '')
        q33 = '' + qclass3 + '\n' + qschool3 + '\n' + '( ' + qper3 + ' )  ' + qdate3

        interest11 = request.POST.get('interest1', '')
        interest22 = request.POST.get('interest2', '')
        interest33 = request.POST.get('interest3', '')
        interests1 = interest11 + '\n' + interest22 + '\n' + interest33

        skill1 = request.POST.get('skill1', '')
        skill2 = request.POST.get('skill2', '')
        skill3 = request.POST.get('skill3', '')
        skills = '' + skill1 + '\n' + skill2 + '\n' + skill3

        hobby1 = request.POST.get('hobby1', '')
        hobby2 = request.POST.get('hobby2', '')
        hobby3 = request.POST.get('hobby3', '')
        hobbies = '' + hobby1 + '\n' + hobby2 + '\n' + hobby3

        lang1 = request.POST.get('language', '')
        languages = '' + lang1

        header = ''
        name = 'Name - ' + n
        dob = 'DOB - ' + dob
        mobileno = 'Mob No. - ' + mob
        address = '' + add

        objective1 = 'Career Objective'
        careerobjective1 = objective

        interest = 'Interests'

        qualification = 'Qualifications'
        q1 = '' + q11
        q2 = '' + q22
        q3 = '' + q33

        language = 'Language Known'
        lang = '' + languages

        hobbies1 = 'Hobbies'

        skills1 = 'Skills'

        # set font
        plt.rcParams['font.family'] = 'sans-serif'
        plt.rcParams['font.sans-serif'] = 'STIXGeneral'
        fig, ax = plt.subplots(figsize=(8.5, 11))

        # set font
        plt.rcParams['font.family'] = 'sans-serif'
        plt.rcParams['font.sans-serif'] = 'STIXGeneral'
        fig, ax = plt.subplots(figsize=(8.5, 11))

        # Decorative Lines
        ax.axvline(x=.5, ymin=0, ymax=1, color='#ffffff', alpha=0.0, linewidth=50)
        plt.axvline(x=.99, color='#ffffff', alpha=0.5, linewidth=1000)
        plt.axhline(y=1, xmin=0, xmax=1, color='#8ccfff', linewidth=250)
        # set background color
        ax.set_facecolor('white')
        # remove axes
        plt.axis('off')

        plt.annotate(header, (.02, .98), weight='regular', fontsize=8, alpha=.75)
        plt.annotate(name, (.02, .94), weight='bold', fontsize=20)
        plt.annotate(dob, (.02, .89), weight='regular', fontsize=12)
        plt.annotate(mobileno, (.02, .870), weight='regular', fontsize=12, color='#000000')
        plt.annotate(address, (.02, .820), weight='regular', fontsize=12, color='#000000')

        plt.annotate(objective, (.02, .75), weight='bold', fontsize=14, alpha=.75)
        plt.annotate(careerobjective1, (.02, .720), weight='regular', fontsize=9)

        plt.annotate(interest, (.02, .675), weight='bold', fontsize=14)
        plt.annotate(interests1, (.02, .610), weight='regular', fontsize=8, color='#000000')

        plt.annotate(qualification, (.02, .580), weight='bold', fontsize=14, color='#000000')
        plt.annotate(q1, (.02, .520), weight='regular', fontsize=8, color='#000000')
        plt.annotate(q2, (.02, .470), weight='regular', fontsize=8, color='#000000')
        plt.annotate(q3, (.02, .420), weight='regular', fontsize=8, color='#000000')

        plt.annotate(skills1, (.02, .370), weight='bold', fontsize=14, color='#000000')
        plt.annotate(skills, (.02, .300), weight='regular', fontsize=8, color='#000000')

        plt.annotate(hobbies1, (.02, .250), weight='bold', fontsize=14, color='#000000')
        plt.annotate(hobbies, (.02, .200), weight='regular', fontsize=8, color='#000000')

        plt.annotate(language, (.02, .140), weight='bold', fontsize=14, color='#000000')
        plt.annotate(lang, (.02, .090), weight='regular', fontsize=8, color='#000000')

        naming = 'static/simpleNewest/' + n + '.png'
        complete = True
        plt.savefig(naming, dpi=300, bbox_inches='tight')
        naming = "/static/simpleNewest/" + n + ".pdf"
        resume = Resumes(name=n, address=add, mob=mob, type='Basic Resume')
        resume.save()

    return render(request, 'NowOwnResume/SimpleNewest.html', {'fname': naming, 'checks': complete})
