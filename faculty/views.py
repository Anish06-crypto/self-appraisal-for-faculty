from reportlab.lib import pagesizes
from AppraisalForm.models import AppraisalForm, AppraisalForm2, AppraisalForm3, BackupApiScores, DatesToTrack, EXPDate, GrandApiScores
from django.shortcuts import redirect, render
from .resources import PersonDetailsResource
from .models import PersonalDetail
from django.contrib import messages
from tablib import Dataset
from django.http import HttpResponse
from .filters import BackupFilter, DepartmentFilter, GradedDeptFilter
from datetime import date, datetime

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


# Create your views here.

def grade_pdf(request):
     if request.session.get('principal',False):
        principal_id = request.session['principal']
        if PersonalDetail.objects.filter(Staff_ID=principal_id).exists():
            tle = GrandApiScores.objects.all()
            template_path = 'Users/pdfreport.html'
            context = { 'tle' : tle }
            
            response = HttpResponse(content_type='applicaton/pdf')

            response['Content-Disposition'] = 'attachment; filename="grade_report.pdf"'

            template = get_template(template_path)
            html = template.render(context)

            pisa_status = pisa.CreatePDF(
                html, dest=response
            )

            if pisa_status.err:
                return HttpResponse('We had some errors <pre>' + html + '</pre>')
            return response

def export(request):
    person_resource = PersonDetailsResource()
    dataset = person_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="persons.xls"'
    return response

def simple_upload(request):
    if request.method == 'POST':
        person_resource = PersonDetailsResource()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_persons.read(),format='xlsx')
        #print(imported_data)
        for data in imported_data:
        	print(data[1])
        	value = PersonalDetail(
        		data[0],
        		data[1],
        		 data[2],
        		 data[3],
                 data[4],
                 data[5],
                 data[6],
                 data[7],
                 data[8],
                 data[9],
                 data[10],
                 data[11],
                 data[12],
                 data[13],
        		)
        	value.save()       
        
        #result = person_resource.import_data(dataset, dry_run=True)  # Test the data import

        #if not result.has_errors():
        #    person_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'Users/input.html')


def login(request):
    if request.method == "GET":
        return render(request, 'Users/login.html')
    if request.method == "POST":
        staff_id = request.POST['Staff_ID']
        password = request.POST['Password']
        if PersonalDetail.objects.filter(Staff_ID=staff_id).exists():
            faculty = PersonalDetail.objects.filter(Staff_ID=staff_id)[0]
            if faculty.Password == password and (PersonalDetail.objects.filter(Staff_ID=staff_id,Present_Designation='Assistant Professor').exists() 
                or PersonalDetail.objects.filter(Staff_ID=staff_id,Present_Designation='Associate Professor').exists()):  
                if GrandApiScores.objects.filter(user=staff_id).exists():
                    request.session['faculty'] = faculty.Staff_ID
                    faculty = PersonalDetail.objects.get(Staff_ID=request.session['faculty'])
                    apf = AppraisalForm.objects.get(user=staff_id)
                    apf2 = AppraisalForm2.objects.get(user=staff_id)
                    apf3 = AppraisalForm3.objects.get(user=staff_id)
                    gapi = GrandApiScores.objects.get(user=staff_id)
                    context = { "apf" : apf,
                                "apf2" : apf2,
                                "apf3" : apf3,
                                "gapi" : gapi,
                                "faculty":faculty }
                    return render(request,'Users/score.html',context)
                else:
                    request.session['faculty'] = faculty.Staff_ID
                    request.session.set_expiry(3000)
                    return redirect('/AppraisalForm/appraisalform/')
            elif faculty.Password == password and PersonalDetail.objects.filter(Staff_ID=staff_id,Whether_HOD=True).exists():
                request.session['hod'] = faculty.Staff_ID
                request.session.set_expiry(3000)
                return redirect('/faculty_list')
            elif faculty.Password == password and PersonalDetail.objects.filter(Staff_ID=staff_id,Present_Designation='Principal').exists():
                request.session['principal'] = faculty.Staff_ID
                return redirect('/faculty_list_P')
            elif faculty.Password == password and PersonalDetail.objects.filter(Staff_ID=staff_id,Present_Designation='Admin').exists():
                request.session['admin'] = faculty.Staff_ID
                return redirect('/adminmit')
            else:
                return_obj = {"isPasswordInvalid": True, "email": staff_id}
                return render(request, "Users/login.html", return_obj)
        else:
            return_obj = {"isEmailInvalid": True}
            return render(request, "Users/login.html", return_obj)
        return redirect('/')

def logOut(request):
    request.session.flush()
    return redirect('/log-in')

def facultydashboard(request):
    if request.session.get('faculty',False):
        faculty = request.session['faculty']
        context= {"faculty":faculty}
        if PersonalDetail.objects.filter(Staff_ID=faculty).exists():
            staff = PersonalDetail.objects.get(Staff_ID=faculty)
            context= {"staff":staff}
            return render(request, 'Users/faculty.html',context)

def hoddashboard(request):
    if request.session.get('hod',False):
        hod_id = request.session['hod']
        if PersonalDetail.objects.filter(Staff_ID=hod_id).exists():
            staff = PersonalDetail.objects.get(Staff_ID=hod_id)
            context= {"staff":staff}
            return render(request, 'Users/hod.html',context)

def principaldashboard(request):
    if request.session.get('principal',False):
        principal_id = request.session['principal']
        context= {"principal":principal_id}
        if PersonalDetail.objects.filter(Staff_ID=principal_id).exists():
            staff = PersonalDetail.objects.get(Staff_ID=principal_id)
            context= {"staff":staff}
            return render(request, 'Users/princi.html',context)

def admindashboard(request):
    if request.session.get('admin',False):
        admin = request.session['admin']
        context= {"admin":admin}
        if PersonalDetail.objects.filter(Staff_ID=admin).exists():
            pd = PersonalDetail.objects.all().count()
            pdd = PersonalDetail.objects.all()
            context = { 'pd' : pd,
                        'pdd' : pdd }
            return render(request, 'Users/admin_index.html',context)

def staff_list(request):
    if request.session.get('hod',False):
        hod_id = request.session['hod']
        if PersonalDetail.objects.filter(Staff_ID=hod_id).exists():
            hod = PersonalDetail.objects.filter(Staff_ID=hod_id)[0]
            staffs = PersonalDetail.objects.all()
            tle = AppraisalForm.objects.all()
            staff = PersonalDetail.objects.get(Staff_ID=hod_id)
            tlecount = AppraisalForm.objects.filter(department=hod.Department, submitted_Faculty=True).count()
            context = {'staffs': staffs, 
                        'hod': hod,
                        'tle' : tle,
                        'tlecount' : tlecount,
                        "staff":staff}
            return render(request, 'Users/faculty_list.html', context)

def staff_list_hod_score(request):
    if request.session.get('hod',False):
        hod_id = request.session['hod']
        if PersonalDetail.objects.filter(Staff_ID=hod_id).exists():
            hod = PersonalDetail.objects.filter(Staff_ID=hod_id)[0]
            staff = PersonalDetail.objects.get(Staff_ID=hod_id)
            tle = GrandApiScores.objects.all()
            context = { 'hod': hod,
                        'tle' : tle, 'staff':staff}
            return render(request, 'Users/hod_dept_faculty_scores.html', context)

def staff_list_P(request):
    if request.session.get('principal',False):
        principal_id = request.session['principal']
        if PersonalDetail.objects.filter(Staff_ID=principal_id).exists():
            principal = PersonalDetail.objects.filter(Staff_ID=principal_id)[0]
            staffs = PersonalDetail.objects.all()
            tle = AppraisalForm.objects.all()
            staff = PersonalDetail.objects.get(Staff_ID=principal_id)
            myFilter = DepartmentFilter(request.GET, queryset=tle)
            tle = myFilter.qs
            context = {'staffs': staffs, 
                        'principal': principal,
                        'tle' : tle,
                        'myFilter' : myFilter, 'staff':staff  }
            return render(request, 'Users/faculty_list_P.html', context)

def grade_dept_filter_P(request):
    if request.session.get('principal',False):
        principal_id = request.session['principal']
        if PersonalDetail.objects.filter(Staff_ID=principal_id).exists():
            principal = PersonalDetail.objects.filter(Staff_ID=principal_id)[0]
            staffs = PersonalDetail.objects.all()
            tle = GrandApiScores.objects.all()
            staff = PersonalDetail.objects.get(Staff_ID=principal_id)
            myFilter = GradedDeptFilter(request.GET, queryset=tle)
            tle = myFilter.qs
            context = {'staffs': staffs, 
                        'principal': principal,
                        'tle' : tle,
                        'myFilter' : myFilter, 'staff':staff  }
            return render(request, 'Users/graded_department.html', context)

def backup_filter_P(request):
    if request.session.get('principal',False):
        principal_id = request.session['principal']
        if PersonalDetail.objects.filter(Staff_ID=principal_id).exists():
            principal = PersonalDetail.objects.filter(Staff_ID=principal_id)[0]
            staffs = PersonalDetail.objects.all()
            tle = BackupApiScores.objects.all()
            staff = PersonalDetail.objects.get(Staff_ID=principal_id)
            myFilter = BackupFilter(request.GET, queryset=tle)
            tle = myFilter.qs
            context = {'staffs': staffs, 
                        'principal': principal,
                        'tle' : tle,
                        'myFilter' : myFilter, 'staff':staff  }
            return render(request, 'Users/backup_scores.html', context)

def grade_list_P(request):
    if request.session.get('principal',False):
        principal_id = request.session['principal']
        if PersonalDetail.objects.filter(Staff_ID=principal_id).exists():
            principal = PersonalDetail.objects.filter(Staff_ID=principal_id)[0]
            staffs = PersonalDetail.objects.all()
            tle = GrandApiScores.objects.all()
            staff = PersonalDetail.objects.get(Staff_ID=principal_id)
            context = {'staffs': staffs, 
                        'principal': principal,
                        'tle' : tle, 'staff':staff }
            return render(request, 'Users/graded_faculty.html', context)

def staff_list_total(request):
    if request.session.get('hod',False):
        hod_id = request.session['hod']
        if PersonalDetail.objects.filter(Staff_ID=hod_id).exists():
            hod = PersonalDetail.objects.filter(Staff_ID=hod_id)[0]
            staffs = PersonalDetail.objects.all()
            staff = PersonalDetail.objects.get(Staff_ID=hod_id)
            staffcount = PersonalDetail.objects.filter(Department=hod.Department, Whether_HOD=False).count()
            
            context = {'staffs': staffs, 
                        'staffcount': staffcount,
                        'hod': hod, 'staff':staff }
            return render(request, 'Users/just_faculty.html', context)

def admin_staff_list(request):
    if request.session.get('admin',False):
        admin = request.session['admin']
        if PersonalDetail.objects.filter(Staff_ID=admin).exists():
            staffs = PersonalDetail.objects.all()
            ds = DatesToTrack.objects.all()
            es = EXPDate.objects.all()
            
            context = {'staffs': staffs, 'ds':ds, 'es':es }
            return render(request, 'Users/admin_faculty_list.html', context)

def forgot_password(request,user):
    if request.session.get('admin',False):
        admin = request.session['admin']
        staff = PersonalDetail.objects.get(Staff_ID=user)
        context = {'staff':staff}
        if PersonalDetail.objects.filter(Staff_ID=admin).exists():
            if request.method == "GET":
                return render(request, 'Users/forgot_password.html', context)
            if request.method == "POST": 
                name = request.POST['Name'] 
                Staff_id = request.POST['Staff_id'] 
                name = request.POST['Name'] 
                Department = request.POST['Department'] 
                ph_num = request.POST['ph_num'] 
                email = request.POST['email'] 
                Designation = request.POST['Designation'] 
                joining_date = request.POST['Designation_date'] 
                # Joining_mit = request.POST['Joining_mit'] 
                Pre_exp = request.POST['Pre_exp'] 
                Qualification = request.POST['Qualification'] 
                Specialization = request.POST['Specialization'] 
                # optionsRadios = request.POST['optionsRadios'] 
                # candidates = request.POST['candidates'] 
                firstPassword = request.POST['firstPassword']
                staff.Password = firstPassword
                staff.Name = name
                staff.Staff_ID = Staff_id
                staff.Department = Department
                staff.Contact_No = ph_num
                staff.Mail_Id = email
                staff.Present_Designation = Designation
                staff.Date_of_joining = joining_date
                staff.total_years = Pre_exp
                staff.Highest_Qualification = Qualification
                staff.Specialization = Specialization
                staff.save()
                return redirect('/admin_faculty')
        else:
            return redirect('/log-in')
    else:
        return redirect('/log-in')
    return render(request, 'Users/forgot_password.html', context)

def changePassword(request):
    if request.session.get('faculty', False):
        Staff_ID = request.session['faculty']
        if PersonalDetail.objects.filter(Staff_ID=Staff_ID).exists():
            faculty = PersonalDetail.objects.filter(Staff_ID=Staff_ID)[0]
            password = request.POST['password']
            faculty.Password = password
            faculty.save()
            faculty = PersonalDetail.objects.get(Staff_ID=request.session['faculty'])
            apf = AppraisalForm.objects.get(user=Staff_ID)
            apf2 = AppraisalForm2.objects.get(user=Staff_ID)
            apf3 = AppraisalForm3.objects.get(user=Staff_ID)
            gapi = GrandApiScores.objects.get(user=Staff_ID)
            context = { "apf" : apf,
                                "apf2" : apf2,
                                "apf3" : apf3,
                                "gapi" : gapi,
                                "faculty":faculty }
            return render(request,'Users/score.html',context)
        else:
            return redirect('/log-in')
    else:
        return redirect('/log-in')

def changePasswordD(request):
    if request.session.get('faculty', False):
        Staff_ID = request.session['faculty']
        if PersonalDetail.objects.filter(Staff_ID=Staff_ID).exists():
            faculty = PersonalDetail.objects.filter(Staff_ID=Staff_ID)[0]
            password = request.POST['password']
            faculty.Password = password
            faculty.save()
            return redirect("/log-in")
        else:
            return redirect('/log-in')
    else:
        return redirect('/log-in')

def changePasswordhod(request):
    if request.session.get('hod', False):
        Staff_ID = request.session['hod']
        if PersonalDetail.objects.filter(Staff_ID=Staff_ID).exists():
            faculty = PersonalDetail.objects.filter(Staff_ID=Staff_ID)[0]
            password = request.POST['password']
            faculty.Password = password
            faculty.save()
            return redirect("/hod")
        else:
            return redirect('/log-in')
    else:
        return redirect('/log-in')

def changePasswordprincipal(request):
    if request.session.get('principal', False):
        Staff_ID = request.session['principal']
        if PersonalDetail.objects.filter(Staff_ID=Staff_ID).exists():
            faculty = PersonalDetail.objects.filter(Staff_ID=Staff_ID)[0]
            password = request.POST['password']
            faculty.Password = password
            faculty.save()
            return redirect("/principal")
        else:
            return redirect('/log-in')
    else:
        return redirect('/log-in')

def changePasswordadmin(request):
    if request.session.get('admin', False):
        Staff_ID = request.session['admin']
        if PersonalDetail.objects.filter(Staff_ID=Staff_ID).exists():
            faculty = PersonalDetail.objects.filter(Staff_ID=Staff_ID)[0]
            password = request.POST['password']
            faculty.Password = password
            faculty.save()
            return redirect("/adminmit")
        else:
            return redirect('/log-in')
    else:
        return redirect('/log-in')


def register(request):
    if request.session.get('admin',False):
        admin = request.session['admin']
        if PersonalDetail.objects.filter(Staff_ID=admin).exists():
            if request.method == "GET":
                return render(request, 'Users/register.html')
            if request.method == "POST":
                name = request.POST['Name'] 
                Staff_id = request.POST['Staff_id'] 
                name = request.POST['Name'] 
                Department = request.POST['Department'] 
                ph_num = request.POST['ph_num'] 
                email = request.POST['email'] 
                Designation = request.POST['Designation'] 
                joining_date = request.POST['Designation_date'] 
                Joining_mit = request.POST['Joining_mit'] 
                Pre_exp = request.POST['Pre_exp'] 
                Qualification = request.POST['Qualification'] 
                Specialization = request.POST['Specialization'] 
                optionsRadios = request.POST['optionsRadios'] 
                candidates = request.POST['candidates'] 
                firstPassword = request.POST['firstPassword'] 
                pd = PersonalDetail(Name=name,Department=Department,Staff_ID=Staff_id,
                                    Contact_No=ph_num,Mail_Id=email,Present_Designation=Designation,
                                    Date_on_which_Acquired=joining_date,Years_of_Service_at_MITM=Joining_mit,
                                    total_years=Pre_exp,Highest_Qualification=Qualification,Specialization=Specialization,
                                    Recognized_as_a_Research_Guide=optionsRadios,If_yes_Number_of_candidates_being_supervised=candidates,
                                    Password=firstPassword)
                pd.save()
        else:
            return redirect('/log-in')
    else:
        return redirect('/log-in')

    return render(request,'Users/register.html')


def exp_increment(request):
    if request.session.get('admin',False):
        admin = request.session['admin']
        if PersonalDetail.objects.filter(Staff_ID=admin).exists():
            exps = PersonalDetail.objects.all()
            for exp in exps:
                exp.total_years += 1
                currentDate = datetime.now()
                join = datetime.strptime(str(exp.Date_of_joining), "%Y-%m-%d %H:%M:%S")
                daysLeft = currentDate - join

                years = ((daysLeft.total_seconds())/(365.242*24*3600))
                yearsInt=int(years)

                months=(years-yearsInt)*12
                monthsInt=int(months)

                exp.Years_of_Service_at_MITM = str(yearsInt) + ":" + str(monthsInt)
                exp.save()
            
            return expdate(request)
        else:
            return redirect('/log-in')
    else:
        return redirect('/log-in')

def backupapiscore(request):
    if request.session.get('admin',False):
        admin = request.session['admin']
        if PersonalDetail.objects.filter(Staff_ID=admin).exists():
            staffs = GrandApiScores.objects.all()
            for staff in staffs:
                backup = BackupApiScores(user=staff,department=staff.department,designation=staff.designation,name=staff.name,submitted_Faculty=staff.submitted_Faculty,submitted_HOD=staff.submitted_HOD,submitted_Principal=staff.submitted_Principal,whether_HOD=staff.whether_HOD,
                Part1APIscore=staff.Part1APIscore,part2APIscore=staff.part2APIscore,part3APIscore=staff.part3APIscore,Part1HODAPIscore=staff.Part1HODAPIscore,part2HODAPIscore=staff.part2HODAPIscore,part3HODAPIscore=staff.part3HODAPIscore,Part1PAPIscore=staff.Part1PAPIscore,
                part2PAPIscore=staff.part2PAPIscore,part3PAPIscore=staff.part3PAPIscore,GrandScore=staff.GrandScore,GrandScoreHOD=staff.GrandScoreHOD,GrandScoreP=staff.GrandScoreP,grade=staff.grade,academic_year=staff.academic_year)
                backup.save()

            return backupdate(request)
        else:
            return redirect('/log-in')
    else:
        return redirect('/log-in')

def backupdate(request):
    if request.session.get('admin',False):
        admin = request.session['admin']
        if PersonalDetail.objects.filter(Staff_ID=admin).exists():
            d = DatesToTrack(backupdate=date.today())
            d.save()
            messages.success(request,'Backup Updated on ' + str(date.today()))
            return redirect('/admin_faculty')
        else:
            return redirect('/log-in')
    else:
        return redirect('/log-in')

def expdate(request):
    if request.session.get('admin',False):
        admin = request.session['admin']
        if PersonalDetail.objects.filter(Staff_ID=admin).exists():
            e = EXPDate(expdate=date.today())
            e.save()
            messages.success(request,'Total Experience Updated on ' + str(date.today()))
            return redirect('/admin_faculty')
        else:
            return redirect('/log-in')
    else:
        return redirect('/log-in')

def delete_faculty(request,user):
    if request.session.get('admin',False):
        admin = request.session['admin']
        if PersonalDetail.objects.filter(Staff_ID=admin).exists():
            if PersonalDetail.objects.filter(Staff_ID=user).exists():
                faculty = PersonalDetail.objects.filter(Staff_ID=user)
                faculty.delete()
                messages.success(request,'Faculty deleted.')
                return redirect('/admin_faculty')
            else:
                return redirect('/admin_faculty')
        else:
            return redirect('/log-in')
    else:
        return redirect('/log-in')

def delete_allforms(request):
    if request.session.get('admin',False):
        admin = request.session['admin']
        if PersonalDetail.objects.filter(Staff_ID=admin).exists():
            apf1 = AppraisalForm.objects.all()
            apf2 = AppraisalForm2.objects.all()
            apf3 = AppraisalForm3.objects.all()
            gapi = GrandApiScores.objects.all()
            for a1 in apf1:
                a1.delete()
            for a2 in apf2:
                a2.delete()
            for a3 in apf3:
                a3.delete()
            for g in gapi:
                g.delete()
            messages.success(request,'All forms deleted.')
            return redirect('/admin_faculty') 
        else:
            return redirect('/log-in')
    else:
        return redirect('/log-in')

def delete_backup_date(request,pk):
    if request.session.get('admin',False):
        admin = request.session['admin']
        if PersonalDetail.objects.filter(Staff_ID=admin).exists():
            backup = DatesToTrack.objects.filter(id=pk)
            backup.delete()
            messages.success(request,'Old date deleted.')
            return redirect('/admin_faculty')
        else:
            return redirect('/log-in')
    else:
        return redirect('/log-in')

def delete_exp_date(request,pk):
    if request.session.get('admin',False):
        admin = request.session['admin']
        if PersonalDetail.objects.filter(Staff_ID=admin).exists():
            exp = EXPDate.objects.filter(id=pk)
            exp.delete()
            messages.success(request,'Old date deleted.')
            return redirect('/admin_faculty')
        else:
            return redirect('/log-in')
    else:
        return redirect('/log-in')