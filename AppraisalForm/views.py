from AppraisalForm.models import AppraisalForm, AppraisalForm2, AppraisalForm3, BackupApiScores, GrandApiScores
from django.shortcuts import render, redirect
from django.contrib import messages
from faculty.models import *

# Create your views here.

def AppraisalForm_create(request):
    if request.session.get('faculty', False):
        Staff_ID = request.session['faculty']
        check = PersonalDetail.objects.get(Staff_ID=Staff_ID)
        staff = PersonalDetail.objects.get(Staff_ID=Staff_ID)
        context = {'check':check,
                    'staff':staff,
                    'staff_id':Staff_ID }
       
        if PersonalDetail.objects.filter(Staff_ID=Staff_ID).exists():
             try:
                if AppraisalForm.objects.filter(user=Staff_ID).exists():
                    staffedit = AppraisalForm.objects.get(user=Staff_ID)
                    staff = PersonalDetail.objects.get(Staff_ID=Staff_ID)
                    contextedit = {
                        'staffedit':staffedit,
                        'staff' : staff
                    }
                    if request.method == "GET":
                        return render(request, "AppraisalForm/appraisalformedit.html",contextedit)
                    if request.method == "POST":
                        if check.Department == "Basic Science and Humanities":
                                sub1 = request.POST['sub1']
                                sub2 = request.POST['sub2']
                                sub3 = request.POST['sub3']
                                sub4 = request.POST['sub4']
                                sub5 = request.POST['sub5']
                                sub6 = request.POST['sub6']
                                sub7 = request.POST['sub7']
                                sub8 = request.POST['sub8']
                                pfile = request.FILES['pfile']
                                s1 = request.POST['s1']
                                s2 = request.POST['s2']
                                s3 = request.POST['s3']
                                s4 = request.POST['s4']
                                s5 = request.POST['s5']
                                s6 = request.POST['s6']
                                s7 = request.POST['s7']
                                s8 = request.POST['s8']
                                p1 = int(float(request.POST['pass1']))
                                p2 = int(float(request.POST['pass2']))
                                p3 = int(float(request.POST['pass3']))
                                p4 = int(float(request.POST['pass4']))
                                p5 = int(float(request.POST['pass5']))
                                p6 = int(float(request.POST['pass6']))
                                p7 = int(float(request.POST['pass7']))
                                p8 = int(float(request.POST['pass8']))
                                p61 = int(float(request.POST['pass61']))
                                p62 = int(float(request.POST['pass62']))
                                p63 = int(float(request.POST['pass63']))
                                p64 = int(float(request.POST['pass64']))
                                p65 = int(float(request.POST['pass65']))
                                p66 = int(float(request.POST['pass66']))
                                p67 = int(float(request.POST['pass67']))
                                p68 = int(float(request.POST['pass68']))
                                c7_sf = request.POST['student_feedback']
                                a9_cw = request.POST['a9']
                                b9_ict = request.POST['b9']
                                c9_cw = request.POST['c9']
                                a9file = request.FILES['a9file']
                                c9file = request.FILES['c9file']
                                a8b = request.POST['a8b']
                                b8b = request.POST['b8b']
                                c8b = request.POST['c8b']
                                d8b = request.POST['d8b']
                                a8bfile = request.FILES['a8bfile']
                                b8bfile = request.FILES['b8bfile']
                                c8bfile = request.FILES['c8bfile']
                                d8bfile = request.FILES['d8bfile']
                                
                                staffedit.Sub_code1 = sub1
                                staffedit.Sub_code2 = sub2
                                staffedit.Sub_code3 = sub3
                                staffedit.Sub_code4 = sub4
                                staffedit.Sub_code5 = sub5
                                staffedit.Sub_code6 = sub6
                                staffedit.Sub_code7 = sub7
                                staffedit.Sub_code8 = sub8
                                staffedit.percent = pfile
                                staffedit.No_of_students1 = s1
                                staffedit.No_of_students2 = s2
                                staffedit.No_of_students3 = s3
                                staffedit.No_of_students4 = s4
                                staffedit.No_of_students5 = s5
                                staffedit.No_of_students6 = s6
                                staffedit.No_of_students7 = s7
                                staffedit.No_of_students8 = s8
                                staffedit.Percentage_of_pass1 = p1
                                staffedit.Percentage_of_pass2 = p2
                                staffedit.Percentage_of_pass3 = p3
                                staffedit.Percentage_of_pass4 = p4
                                staffedit.Percentage_of_pass5 = p5
                                staffedit.Percentage_of_pass6 = p6
                                staffedit.Percentage_of_pass7 = p7
                                staffedit.Percentage_of_pass8 = p8
                                staffedit.Percent_over_601 = p61
                                staffedit.Percent_over_602 = p62
                                staffedit.Percent_over_603 = p63
                                staffedit.Percent_over_604 = p64
                                staffedit.Percent_over_605 = p65
                                staffedit.Percent_over_606 = p66
                                staffedit.Percent_over_607 = p67
                                staffedit.Percent_over_608 = p68
                                staffedit.Percentage_of_pass1_hod = p1
                                staffedit.Percentage_of_pass2_hod = p2
                                staffedit.Percentage_of_pass3_hod = p3
                                staffedit.Percentage_of_pass4_hod = p4
                                staffedit.Percentage_of_pass5_hod = p5
                                staffedit.Percentage_of_pass6_hod = p6
                                staffedit.Percentage_of_pass7_hod = p7
                                staffedit.Percentage_of_pass8_hod = p8
                                staffedit.Percent_over_601_hod = p61
                                staffedit.Percent_over_602_hod = p62
                                staffedit.Percent_over_603_hod = p63
                                staffedit.Percent_over_604_hod = p64
                                staffedit.Percent_over_605_hod = p65
                                staffedit.Percent_over_606_hod = p66
                                staffedit.Percent_over_607_hod = p67
                                staffedit.Percent_over_608_hod = p68
                                staffedit.c7_Student_Feedback = c7_sf
                                staffedit.a9_No_of_conferences_or_workshops_or_Seminars_or_training_programs_or_etc_FDPs_attended_score = a9_cw
                                staffedit.b9_Use_of_ICT_in_TLP_score = b9_ict
                                staffedit.c9_No_of_conferences_or_workshops_or_Seminars_or_training_or_programs_or_etc_or_FDPs_conducted_or_coordinated_score = c9_cw
                                staffedit.a9file = a9file
                                staffedit.c9file = c9file
                                staffedit.a8B_No_of_Topper_in_1st_year_of_study_under_your_mentorship_score = a8b
                                staffedit.b8B_No_of_students_achieved_vertical_progression_to_2nd_Year_under_your_mentorship_score = b8b
                                staffedit.c8B_No_of_FCD_in_1st_year_of_study_under_your_mentorship_score = c8b
                                staffedit.d8B_No_of_UG_or_PG_projects_Co_guided_score = d8b
                                staffedit.a8bfile = a8bfile
                                staffedit.b8bfile = b8bfile
                                staffedit.c8bfile = c8bfile
                                staffedit.d8bfile = d8bfile

                                staffedit.save()
                                return render(request, "AppraisalForm/appraisalformedit.html",contextedit)
                            
                        else:
                                sub1 = request.POST['sub1']
                                sub2 = request.POST['sub2']
                                sub3 = request.POST['sub3']
                                sub4 = request.POST['sub4']
                                sub5 = request.POST['sub5']
                                sub6 = request.POST['sub6']
                                sub7 = request.POST['sub7']
                                sub8 = request.POST['sub8']
                                s5 = request.POST['s5']
                                s6 = request.POST['s6']
                                s7 = request.POST['s7']
                                s8 = request.POST['s8']
                                pfile = request.FILES['pfile']
                                s1 = request.POST['s1']
                                s2 = request.POST['s2']
                                s3 = request.POST['s3']
                                s4 = request.POST['s4']
                                s5 = request.POST['s5']
                                s6 = request.POST['s6']
                                s7 = request.POST['s7']
                                s8 = request.POST['s8']
                                p1 = int(float(request.POST['pass1']))
                                p2 = int(float(request.POST['pass2']))
                                p3 = int(float(request.POST['pass3']))
                                p4 = int(float(request.POST['pass4']))
                                p5 = int(float(request.POST['pass5']))
                                p6 = int(float(request.POST['pass6']))
                                p7 = int(float(request.POST['pass7']))
                                p8 = int(float(request.POST['pass8']))
                                p61 = int(float(request.POST['pass61']))
                                p62 = int(float(request.POST['pass62']))
                                p63 = int(float(request.POST['pass63']))
                                p64 = int(float(request.POST['pass64']))
                                p65 = int(float(request.POST['pass65']))
                                p66 = int(float(request.POST['pass66']))
                                p67 = int(float(request.POST['pass67']))
                                p68 = int(float(request.POST['pass68']))
                                c7_sf = request.POST['student_feedback']
                                a9_cw = request.POST['a9']
                                b9_ict = request.POST['b9']
                                c9_cw = request.POST['c9']
                                a9file = request.FILES['a9file']
                                c9file = request.FILES['c9file']
                                a8 = request.POST['a8']
                                b8 = request.POST['b8']
                                c8 = request.POST['c8']
                                b8file = request.FILES['b8file']
                                c8file = request.FILES['c8file']
                                
                                staffedit.Sub_code1 = sub1
                                staffedit.Sub_code2 = sub2
                                staffedit.Sub_code3 = sub3
                                staffedit.Sub_code4 = sub4
                                staffedit.Sub_code5 = sub5
                                staffedit.Sub_code6 = sub6
                                staffedit.Sub_code7 = sub7
                                staffedit.Sub_code8 = sub8
                                staffedit.percent = pfile
                                staffedit.No_of_students1 = s1
                                staffedit.No_of_students2 = s2
                                staffedit.No_of_students3 = s3
                                staffedit.No_of_students4 = s4
                                staffedit.No_of_students5 = s5
                                staffedit.No_of_students6 = s6
                                staffedit.No_of_students7 = s7
                                staffedit.No_of_students8 = s8
                                staffedit.Percentage_of_pass1 = p1
                                staffedit.Percentage_of_pass2 = p2
                                staffedit.Percentage_of_pass3 = p3
                                staffedit.Percentage_of_pass4 = p4
                                staffedit.Percentage_of_pass5 = p5
                                staffedit.Percentage_of_pass6 = p6
                                staffedit.Percentage_of_pass7 = p7
                                staffedit.Percentage_of_pass8 = p8
                                staffedit.Percent_over_601 = p61
                                staffedit.Percent_over_602 = p62
                                staffedit.Percent_over_603 = p63
                                staffedit.Percent_over_604 = p64
                                staffedit.Percent_over_605 = p65
                                staffedit.Percent_over_606 = p66
                                staffedit.Percent_over_607 = p67
                                staffedit.Percent_over_608 = p68
                                staffedit.Percentage_of_pass1_hod = p1
                                staffedit.Percentage_of_pass2_hod = p2
                                staffedit.Percentage_of_pass3_hod = p3
                                staffedit.Percentage_of_pass4_hod = p4
                                staffedit.Percentage_of_pass5_hod = p5
                                staffedit.Percentage_of_pass6_hod = p6
                                staffedit.Percentage_of_pass7_hod = p7
                                staffedit.Percentage_of_pass8_hod = p8
                                staffedit.Percent_over_601_hod = p61
                                staffedit.Percent_over_602_hod = p62
                                staffedit.Percent_over_603_hod = p63
                                staffedit.Percent_over_604_hod = p64
                                staffedit.Percent_over_605_hod = p65
                                staffedit.Percent_over_606_hod = p66
                                staffedit.Percent_over_607_hod = p67
                                staffedit.Percent_over_608_hod = p68
                                staffedit.c7_Student_Feedback = c7_sf
                                staffedit.a9_No_of_conferences_or_workshops_or_Seminars_or_training_programs_or_etc_FDPs_attended_score = a9_cw
                                staffedit.b9_Use_of_ICT_in_TLP_score = b9_ict
                                staffedit.c9_No_of_conferences_or_workshops_or_Seminars_or_training_or_programs_or_etc_or_FDPs_conducted_or_coordinated_score = c9_cw
                                staffedit.a9file = a9file
                                staffedit.c9file = c9file
                                staffedit.a8_No_of_projects_guided_score = a8
                                staffedit.b8_No_of_Best_Projects_Awarded_OR_Student_Project_Exhibited_in_competitions_or_Symposiums_OR_Funded_by_external_agency_OR_Student_Project_Paper_Publication_s_score = b8
                                staffedit.c8_No_of_students_achieved_vertical_progression_under_your_mentorship = c8
                                staffedit.b8file = b8file
                                staffedit.c8file = c8file

                                staffedit.save()
                                return render(request, "AppraisalForm/appraisalformedit.html",contextedit)
                else:    
                    if request.method == "GET":
                        return render(request, "AppraisalForm/appraisalform.html",context)
                    if request.method == "POST":
                        user = Staff_ID
        
                        if check.Department == "Basic Science and Humanities":
                                ay = request.POST['a_year']
                                sub1 = request.POST['sub1']
                                sub2 = request.POST['sub2']
                                sub3 = request.POST['sub3']
                                sub4 = request.POST['sub4']
                                sub5 = request.POST['sub5']
                                sub6 = request.POST['sub6']
                                sub7 = request.POST['sub7']
                                sub8 = request.POST['sub8']
                                pfile = request.FILES['pfile']
                                s1 = request.POST['s1']
                                s2 = request.POST['s2']
                                s3 = request.POST['s3']
                                s4 = request.POST['s4']
                                s5 = request.POST['s5']
                                s6 = request.POST['s6']
                                s7 = request.POST['s7']
                                s8 = request.POST['s8']
                                p1 = int(float(request.POST['pass1']))
                                p2 = int(float(request.POST['pass2']))
                                p3 = int(float(request.POST['pass3']))
                                p4 = int(float(request.POST['pass4']))
                                p5 = int(float(request.POST['pass5']))
                                p6 = int(float(request.POST['pass6']))
                                p7 = int(float(request.POST['pass7']))
                                p8 = int(float(request.POST['pass8']))
                                p61 = int(float(request.POST['pass61']))
                                p62 = int(float(request.POST['pass62']))
                                p63 = int(float(request.POST['pass63']))
                                p64 = int(float(request.POST['pass64']))
                                p65 = int(float(request.POST['pass65']))
                                p66 = int(float(request.POST['pass66']))
                                p67 = int(float(request.POST['pass67']))
                                p68 = int(float(request.POST['pass68']))
                                c7_sf = request.POST['student_feedback']
                                a9_cw = request.POST['a9']
                                b9_ict = request.POST['b9']
                                c9_cw = request.POST['c9']
                                a9file = request.FILES['a9file']
                                c9file = request.FILES['c9file']
                                a8b = request.POST['a8b']
                                b8b = request.POST['b8b']
                                c8b = request.POST['c8b']
                                d8b = request.POST['d8b']
                                a8bfile = request.FILES['a8bfile']
                                b8bfile = request.FILES['b8bfile']
                                c8bfile = request.FILES['c8bfile']
                                d8bfile = request.FILES['d8bfile']

                                apf = AppraisalForm(user=Staff_ID,department=check.Department,designation=check.Present_Designation,academic_year=ay,name=check.Name,submitted_Faculty=True,No_of_students1=s1, No_of_students2=s2, No_of_students3=s3, No_of_students4=s4,No_of_students5=s5, No_of_students6=s6, No_of_students7=s7, No_of_students8=s8,
                                            Sub_code1=sub1, Sub_code2=sub2, Sub_code3=sub3, Sub_code4=sub4,Sub_code5=sub5, Sub_code6=sub6, Sub_code7=sub7, Sub_code8=sub8,
                                            Percentage_of_pass1=p1, Percentage_of_pass2=p2, Percentage_of_pass3=p3, Percentage_of_pass4=p4,Percentage_of_pass5=p5, Percentage_of_pass6=p6, Percentage_of_pass7=p7, Percentage_of_pass8=p8,
                                            Percent_over_601=p61, Percent_over_602=p62, Percent_over_603=p63, Percent_over_604=p64,Percent_over_605=p65, Percent_over_606=p66, Percent_over_607=p67, Percent_over_608=p68,
                                            Percentage_of_pass1_hod=p1, Percentage_of_pass2_hod=p2, Percentage_of_pass3_hod=p3, Percentage_of_pass4_hod=p4,Percentage_of_pass5_hod=p5, Percentage_of_pass6_hod=p6, Percentage_of_pass7_hod=p7, Percentage_of_pass8_hod=p8,
                                            Percent_over_601_hod=p61, Percent_over_602_hod=p62, Percent_over_603_hod=p63, Percent_over_604_hod=p64,Percent_over_605_hod=p65, Percent_over_606_hod=p66, Percent_over_607_hod=p67, Percent_over_608_hod=p68,
                                            c7_Student_Feedback = c7_sf, a9_No_of_conferences_or_workshops_or_Seminars_or_training_programs_or_etc_FDPs_attended_score = a9_cw,
                                            b9_Use_of_ICT_in_TLP_score = b9_ict, c9_No_of_conferences_or_workshops_or_Seminars_or_training_or_programs_or_etc_or_FDPs_conducted_or_coordinated_score = c9_cw, a8B_No_of_Topper_in_1st_year_of_study_under_your_mentorship_score=a8b,
                                            b8B_No_of_students_achieved_vertical_progression_to_2nd_Year_under_your_mentorship_score=b8b, c8B_No_of_FCD_in_1st_year_of_study_under_your_mentorship_score=c8b,
                                            d8B_No_of_UG_or_PG_projects_Co_guided_score=d8b,percent=pfile,a9file=a9file,c9file=c9file,a8bfile=a8bfile,b8bfile=b8bfile,c8bfile=c8bfile,d8bfile=d8bfile)
                                apf.save()
                                return render(request, "AppraisalForm/appraisalform2.html",context)   
                        else:
                                ay = request.POST['a_year']
                                sub1 = request.POST['sub1']
                                sub2 = request.POST['sub2']
                                sub3 = request.POST['sub3']
                                sub4 = request.POST['sub4']
                                sub5 = request.POST['sub5']
                                sub6 = request.POST['sub6']
                                sub7 = request.POST['sub7']
                                sub8 = request.POST['sub8']
                                pfile = request.FILES['pfile']
                                s1 = request.POST['s1']
                                s2 = request.POST['s2']
                                s3 = request.POST['s3']
                                s4 = request.POST['s4']
                                s5 = request.POST['s5']
                                s6 = request.POST['s6']
                                s7 = request.POST['s7']
                                s8 = request.POST['s8']
                                p1 = int(float(request.POST['pass1']))
                                p2 = int(float(request.POST['pass2']))
                                p3 = int(float(request.POST['pass3']))
                                p4 = int(float(request.POST['pass4']))
                                p5 = int(float(request.POST['pass5']))
                                p6 = int(float(request.POST['pass6']))
                                p7 = int(float(request.POST['pass7']))
                                p8 = int(float(request.POST['pass8']))
                                p61 = int(float(request.POST['pass61']))
                                p62 = int(float(request.POST['pass62']))
                                p63 = int(float(request.POST['pass63']))
                                p64 = int(float(request.POST['pass64']))
                                p65 = int(float(request.POST['pass65']))
                                p66 = int(float(request.POST['pass66']))
                                p67 = int(float(request.POST['pass67']))
                                p68 = int(float(request.POST['pass68']))
                                c7_sf = request.POST['student_feedback']
                                a9_cw = request.POST['a9']
                                b9_ict = request.POST['b9']
                                c9_cw = request.POST['c9']
                                a9file = request.FILES['a9file']
                                c9file = request.FILES['c9file']
                                a8 = request.POST['a8']
                                b8 = request.POST['b8']
                                c8 = request.POST['c8']
                                b8file = request.FILES['b8file']
                                c8file = request.FILES['c8file']

                                apf = AppraisalForm(user=Staff_ID,department=check.Department,designation=check.Present_Designation,academic_year=ay,name=check.Name,submitted_Faculty=True,No_of_students1=s1, No_of_students2=s2, No_of_students3=s3, No_of_students4=s4,No_of_students5=s5, No_of_students6=s6, No_of_students7=s7, No_of_students8=s8,
                                            Sub_code1=sub1, Sub_code2=sub2, Sub_code3=sub3, Sub_code4=sub4,Sub_code5=sub5, Sub_code6=sub6, Sub_code7=sub7, Sub_code8=sub8,
                                            Percentage_of_pass1=p1, Percentage_of_pass2=p2, Percentage_of_pass3=p3, Percentage_of_pass4=p4,Percentage_of_pass5=p5, Percentage_of_pass6=p6, Percentage_of_pass7=p7, Percentage_of_pass8=p8,
                                            Percent_over_601=p61, Percent_over_602=p62, Percent_over_603=p63, Percent_over_604=p64,Percent_over_605=p65, Percent_over_606=p66, Percent_over_607=p67, Percent_over_608=p68,
                                            Percentage_of_pass1_hod=p1, Percentage_of_pass2_hod=p2, Percentage_of_pass3_hod=p3, Percentage_of_pass4_hod=p4,Percentage_of_pass5_hod=p5, Percentage_of_pass6_hod=p6, Percentage_of_pass7_hod=p7, Percentage_of_pass8_hod=p8,
                                            Percent_over_601_hod=p61, Percent_over_602_hod=p62, Percent_over_603_hod=p63, Percent_over_604_hod=p64,Percent_over_605_hod=p65, Percent_over_606_hod=p66, Percent_over_607_hod=p67, Percent_over_608_hod=p68,
                                            c7_Student_Feedback = c7_sf, a9_No_of_conferences_or_workshops_or_Seminars_or_training_programs_or_etc_FDPs_attended_score = a9_cw,
                                            b9_Use_of_ICT_in_TLP_score = b9_ict, c9_No_of_conferences_or_workshops_or_Seminars_or_training_or_programs_or_etc_or_FDPs_conducted_or_coordinated_score = c9_cw,a8_No_of_projects_guided_score=a8,
                                            b8_No_of_Best_Projects_Awarded_OR_Student_Project_Exhibited_in_competitions_or_Symposiums_OR_Funded_by_external_agency_OR_Student_Project_Paper_Publication_s_score=b8,
                                            c8_No_of_students_achieved_vertical_progression_under_your_mentorship=c8, percent=pfile,a9file=a9file,c9file=c9file,
                                            b8file=b8file,c8file=c8file)
                                apf.save()
                                return render(request, "AppraisalForm/appraisalform2.html",context)
             except:
                messages.warning(request, 'You need to upload all files before submission.')
                return redirect('/AppraisalForm/appraisalform/') 
        else:
            return redirect('/log-in')
    else:
        return redirect('/log-in')

    # return render(request, 'AppraisalForm/appraisalform.html',context)

def AppraisalForm2_create(request):
    if request.session.get('faculty', False):
        Staff_ID = request.session['faculty']
        check = PersonalDetail.objects.get(Staff_ID=Staff_ID)
        staff = PersonalDetail.objects.get(Staff_ID=Staff_ID)
        context = {'check':check,
                    'staff': staff,
                    'staff_id':Staff_ID }
        
        if PersonalDetail.objects.filter(Staff_ID=Staff_ID).exists():
            try:
                if AppraisalForm2.objects.filter(user=Staff_ID).exists():
                    staffedit = AppraisalForm2.objects.get(user=Staff_ID)
                    staff = PersonalDetail.objects.get(Staff_ID=Staff_ID)
                    contextedit = {
                        'staffedit':staffedit,
                        'staff' : staff
                    }
                    if request.method == "GET":
                        return render(request, "AppraisalForm/appraisalformedit2.html",contextedit)
                    if request.method == "POST":
                                a10 = request.POST['a10']
                                b10 = request.POST['b10']
                                c10 = request.POST['c10']
                                a11 = request.POST['a11']
                                b11 = request.POST['b11']
                                a12 = request.POST['a12']
                                b12 = request.POST['b12']
                                a10file = request.FILES['a10file']
                                b10file = request.FILES['b10file']
                                c10file = request.FILES['c10file']
                                a11file = request.FILES['a11file']
                                b11file = request.FILES['b11file']
                                a12file = request.FILES['a12file']
                                b12file = request.FILES['b12file']

                                staffedit.a10_No_of_papers_published_in_journals_score = a10
                                staffedit.b10_No_of_papers_presented_in_conferences_score = b10
                                staffedit.c10_No_of_papers_indexed_in_In_Scopus_or_Web_of_Science_or_UGC_care_list_OR_No_of_book_chapters_authored_OR_No_of_Books_Authored_score = c10
                                staffedit.a11_No_of_Research_Project_proposals_submitted_score = a11
                                staffedit.b11_No_of_Research_projects_Received_and_Amount_score = b11
                                staffedit.a12_No_of_Consultancy_projects_received_OR_ongoing_score = a12
                                staffedit.b12_No_of_patents_applied_awarded_score = b12
                                staffedit.a10file = a10file
                                staffedit.b10file = b10file
                                staffedit.c10file = c10file
                                staffedit.a11file = a11file
                                staffedit.b11file = b11file
                                staffedit.a12file = a12file
                                staffedit.b12file = b12file

                                staffedit.save()
                                return render(request, "AppraisalForm/appraisalformedit2.html",contextedit)
                else:
                    if request.method == "GET":
                        return render(request, "AppraisalForm/appraisalform2.html",context)
                    if request.method == "POST":
                                ay = request.POST['a_year']
                                a10 = request.POST['a10']
                                b10 = request.POST['b10']
                                c10 = request.POST['c10']
                                a11 = request.POST['a11']
                                b11 = request.POST['b11']
                                a12 = request.POST['a12']
                                b12 = request.POST['b12']
                                a10file = request.FILES['a10file']
                                b10file = request.FILES['b10file']
                                c10file = request.FILES['c10file']
                                a11file = request.FILES['a11file']
                                b11file = request.FILES['b11file']
                                a12file = request.FILES['a12file']
                                b12file = request.FILES['b12file']

                                apf2 = AppraisalForm2(user=Staff_ID,department=check.Department,designation=check.Present_Designation,name=check.Name,academic_year=ay,submitted_Faculty=True,a10_No_of_papers_published_in_journals_score=a10,b10_No_of_papers_presented_in_conferences_score=b10,
                                            c10_No_of_papers_indexed_in_In_Scopus_or_Web_of_Science_or_UGC_care_list_OR_No_of_book_chapters_authored_OR_No_of_Books_Authored_score=c10,
                                            a11_No_of_Research_Project_proposals_submitted_score=a11,b11_No_of_Research_projects_Received_and_Amount_score=b11,
                                            a12_No_of_Consultancy_projects_received_OR_ongoing_score=a12,b12_No_of_patents_applied_awarded_score=b12,
                                            a10file=a10file,b10file=b10file,c10file=c10file,
                                            a11file=a11file,b11file=b11file,a12file=a12file,b12file=b12file)
                                apf2.save()
                                return render(request, "AppraisalForm/appraisalform3.html",context)
            except:
                messages.warning(request, 'You need to upload all files before submission.')
                return redirect('/AppraisalForm/appraisalform2/')
        else:
            return redirect('/log-in')
    else:
        return redirect('/log-in')

    # return render(request, 'AppraisalForm/appraisalform2.html',context)

def AppraisalForm3_create(request):
    if request.session.get('faculty', False):
        Staff_ID = request.session['faculty']
        check = PersonalDetail.objects.get(Staff_ID=Staff_ID)
        staff = PersonalDetail.objects.get(Staff_ID=Staff_ID)
        context = {'check':check, 'staff':staff,
                    'staff_id':Staff_ID }
        
        if PersonalDetail.objects.filter(Staff_ID=Staff_ID).exists():
            try:
                if AppraisalForm3.objects.filter(user=Staff_ID).exists():
                    staffedit = AppraisalForm3.objects.get(user=Staff_ID)
                    staff = PersonalDetail.objects.get(Staff_ID=Staff_ID)
                    contextedit = {
                        'staffedit':staffedit,
                        'staff' : staff
                    }
                    if request.method == "GET":
                        return render(request, "AppraisalForm/appraisalformedit3.html",contextedit)
                    if request.method == "POST":
                        a13 = request.POST['a13']
                        b13 = request.POST['b13']
                        c13 = request.POST['c13']
                        d13 = request.POST['d13']
                        e13 = request.POST['e13']
                        f13 = request.POST['f13']
                        a14 = request.POST['a14']
                        b14 = request.POST['b14']
                        c14 = request.POST['c14']
                        a15 = request.POST['a15']
                        c14file = request.FILES['c14file']
                        a15file = request.FILES['a15file'] 

                        staffedit.a13 = a13
                        staffedit.b13 = b13
                        staffedit.c13 = c13
                        staffedit.d13 = d13
                        staffedit.e13 = e13
                        staffedit.f13 = f13
                        staffedit.a14 = a14
                        staffedit.b14 = b14
                        staffedit.c14 = c14
                        staffedit.a15 = a15
                        staffedit.c14file = c14file
                        staffedit.a15file = a15file   

                        staffedit.save()
                        return grandscorecalc(request)                  
                else:
                    if request.method == "GET":
                        return render(request, "AppraisalForm/appraisalform3.html",context)
                    if request.method == "POST":
                        ay = request.POST['a_year']
                        a13 = request.POST['a13']
                        b13 = request.POST['b13']
                        c13 = request.POST['c13']
                        d13 = request.POST['d13']
                        e13 = request.POST['e13']
                        f13 = request.POST['f13']
                        a14 = request.POST['a14']
                        b14 = request.POST['b14']
                        c14 = request.POST['c14']
                        a15 = request.POST['a15']
                        c14file = request.FILES['c14file']
                        a15file = request.FILES['a15file']

                        apf3 = AppraisalForm3(user=Staff_ID,department=check.Department,designation=check.Present_Designation,name=check.Name,academic_year=ay,submitted_Faculty=True,a13=a13,b13=b13,c13=c13,d13=d13,e13=e13,
                                            f13=f13,a14=a14,b14=b14,c14=c14,a15=a15,c14file=c14file,a15file=a15file)
                        apf3.save()
                        return grandscorecalc(request)
            except:
                messages.warning(request, 'You need to upload all files before submission.')
                return redirect('/AppraisalForm/appraisalform3/') 
        else:
            return redirect('/log-in')
    else:
        return redirect('/log-in')
    # return render(request, 'AppraisalForm/appraisalform3.html',context)

def grandscorecalc(request):
    staff = request.session['faculty']
    if PersonalDetail.objects.filter(Staff_ID=staff).exists():
        if GrandApiScores.objects.filter(user=staff).exists():
            pd = PersonalDetail.objects.get(Staff_ID=staff)
            apf = AppraisalForm.objects.get(user=staff)
            apf2 = AppraisalForm2.objects.get(user=staff)
            apf3 = AppraisalForm3.objects.get(user=staff)
            gapi = GrandApiScores.objects.get(user=staff)
            if int(pd.total_years) <= 5:
                grand = (((apf.Part1APIscore/350)*0.70)+((apf2.part2APIscore/170)*0.20)+((apf3.part3APIscore/180)*0.10))*100
                gapi.GrandScore = grand
                gapi.save()
                
            elif int(pd.total_years) > 5 and int(pd.total_years) < 10:
                grand = (((apf.Part1APIscore/350)*0.60)+((apf2.part2APIscore/170)*0.25)+((apf3.part3APIscore/180)*0.15))*100
                gapi.GrandScore = grand
                gapi.save()

            elif int(pd.total_years) >= 10:
                grand = (((apf.Part1APIscore/350)*0.50)+((apf2.part2APIscore/170)*0.30)+((apf3.part3APIscore/180)*0.20))*100
                gapi.GrandScore = grand
                gapi.save()
            return redirect('/log-out')
        else:
            pd = PersonalDetail.objects.get(Staff_ID=staff)
            apf = AppraisalForm.objects.get(user=staff)
            apf2 = AppraisalForm2.objects.get(user=staff)
            apf3 = AppraisalForm3.objects.get(user=staff)
            if int(pd.total_years) <= 5:
                grand = (((apf.Part1APIscore/350)*0.70)+((apf2.part2APIscore/170)*0.20)+((apf3.part3APIscore/180)*0.10))*100
                gapi = GrandApiScores(user=staff,department=pd.Department,designation=pd.Present_Designation,name=pd.Name,submitted_Faculty=True,Part1APIscore=apf.Part1APIscore,
                                part2APIscore=apf2.part2APIscore,part3APIscore=apf3.part3APIscore,GrandScore=grand,academic_year=apf.academic_year)
                gapi.save()
                
            elif int(pd.total_years) > 5 and int(pd.total_years) < 10:
                grand = (((apf.Part1APIscore/350)*0.60)+((apf2.part2APIscore/170)*0.25)+((apf3.part3APIscore/180)*0.15))*100
                gapi = GrandApiScores(user=staff,department=pd.Department,designation=pd.Present_Designation,name=pd.Name,submitted_Faculty=True,Part1APIscore=apf.Part1APIscore,
                                part2APIscore=apf2.part2APIscore,part3APIscore=apf3.part3APIscore,GrandScore=grand,academic_year=apf.academic_year)
                gapi.save()
            elif int(pd.total_years) >= 10:
                grand = (((apf.Part1APIscore/350)*0.50)+((apf2.part2APIscore/170)*0.30)+((apf3.part3APIscore/180)*0.20))*100
                gapi = GrandApiScores(user=staff,department=pd.Department,designation=pd.Present_Designation,name=pd.Name,submitted_Faculty=True,Part1APIscore=apf.Part1APIscore,
                                part2APIscore=apf2.part2APIscore,part3APIscore=apf3.part3APIscore,GrandScore=grand,academic_year=apf.academic_year)
                gapi.save()
            return redirect('/log-out')


#Hod_createform

def AppraisalForm_HODcreate(request):
    if request.session.get('hod', False):
        Staff_ID = request.session['hod']
        check = PersonalDetail.objects.get(Staff_ID=Staff_ID)
        staff = PersonalDetail.objects.get(Staff_ID=Staff_ID)
        context = {'check':check, 'staff':staff,
                    'staff_id':Staff_ID }

        if PersonalDetail.objects.filter(Staff_ID=Staff_ID).exists():
            try:
                if AppraisalForm.objects.filter(user=Staff_ID).exists():
                    staffedit = AppraisalForm.objects.get(user=Staff_ID)
                    staff = PersonalDetail.objects.get(Staff_ID=Staff_ID)
                    contextedit = {
                        'staffedit':staffedit,
                        'staff' : staff
                    }
                    if request.method == "GET":
                        return render(request, "AppraisalForm/appraisalformedithod.html",contextedit)
                    if request.method == "POST":
                        if check.Department == "Basic Science and Humanities":
                                sub1 = request.POST['sub1']
                                sub2 = request.POST['sub2']
                                sub3 = request.POST['sub3']
                                sub4 = request.POST['sub4']
                                sub5 = request.POST['sub5']
                                sub6 = request.POST['sub6']
                                sub7 = request.POST['sub7']
                                sub8 = request.POST['sub8']
                                pfile = request.FILES['pfile']
                                s1 = request.POST['s1']
                                s2 = request.POST['s2']
                                s3 = request.POST['s3']
                                s4 = request.POST['s4']
                                s5 = request.POST['s5']
                                s6 = request.POST['s6']
                                s7 = request.POST['s7']
                                s8 = request.POST['s8']
                                p1 = int(float(request.POST['pass1']))
                                p2 = int(float(request.POST['pass2']))
                                p3 = int(float(request.POST['pass3']))
                                p4 = int(float(request.POST['pass4']))
                                p5 = int(float(request.POST['pass5']))
                                p6 = int(float(request.POST['pass6']))
                                p7 = int(float(request.POST['pass7']))
                                p8 = int(float(request.POST['pass8']))
                                p61 = int(float(request.POST['pass61']))
                                p62 = int(float(request.POST['pass62']))
                                p63 = int(float(request.POST['pass63']))
                                p64 = int(float(request.POST['pass64']))
                                p65 = int(float(request.POST['pass65']))
                                p66 = int(float(request.POST['pass66']))
                                p67 = int(float(request.POST['pass67']))
                                p68 = int(float(request.POST['pass68']))
                                c7_sf = request.POST['student_feedback']
                                a9_cw = request.POST['a9']
                                b9_ict = request.POST['b9']
                                c9_cw = request.POST['c9']
                                a9file = request.FILES['a9file']
                                c9file = request.FILES['c9file']
                                a8b = request.POST['a8b']
                                b8b = request.POST['b8b']
                                c8b = request.POST['c8b']
                                d8b = request.POST['d8b']
                                a8bfile = request.FILES['a8bfile']
                                b8bfile = request.FILES['b8bfile']
                                c8bfile = request.FILES['c8bfile']
                                d8bfile = request.FILES['d8bfile']
                                
                                staffedit.Sub_code1 = sub1
                                staffedit.Sub_code2 = sub2
                                staffedit.Sub_code3 = sub3
                                staffedit.Sub_code4 = sub4
                                staffedit.Sub_code5 = sub5
                                staffedit.Sub_code6 = sub6
                                staffedit.Sub_code7 = sub7
                                staffedit.Sub_code8 = sub8
                                staffedit.percent = pfile
                                staffedit.No_of_students1 = s1
                                staffedit.No_of_students2 = s2
                                staffedit.No_of_students3 = s3
                                staffedit.No_of_students4 = s4
                                staffedit.No_of_students5 = s5
                                staffedit.No_of_students6 = s6
                                staffedit.No_of_students7 = s7
                                staffedit.No_of_students8 = s8
                                staffedit.Percentage_of_pass1 = p1
                                staffedit.Percentage_of_pass2 = p2
                                staffedit.Percentage_of_pass3 = p3
                                staffedit.Percentage_of_pass4 = p4
                                staffedit.Percentage_of_pass5 = p5
                                staffedit.Percentage_of_pass6 = p6
                                staffedit.Percentage_of_pass7 = p7
                                staffedit.Percentage_of_pass8 = p8
                                staffedit.Percent_over_601 = p61
                                staffedit.Percent_over_602 = p62
                                staffedit.Percent_over_603 = p63
                                staffedit.Percent_over_604 = p64
                                staffedit.Percent_over_605 = p65
                                staffedit.Percent_over_606 = p66
                                staffedit.Percent_over_607 = p67
                                staffedit.Percent_over_608 = p68
                                staffedit.c7_Student_Feedback = c7_sf
                                staffedit.a9_No_of_conferences_or_workshops_or_Seminars_or_training_programs_or_etc_FDPs_attended_score = a9_cw
                                staffedit.b9_Use_of_ICT_in_TLP_score = b9_ict
                                staffedit.c9_No_of_conferences_or_workshops_or_Seminars_or_training_or_programs_or_etc_or_FDPs_conducted_or_coordinated_score = c9_cw
                                staffedit.a9file = a9file
                                staffedit.c9file = c9file
                                staffedit.a8B_No_of_Topper_in_1st_year_of_study_under_your_mentorship_score = a8b
                                staffedit.b8B_No_of_students_achieved_vertical_progression_to_2nd_Year_under_your_mentorship_score = b8b
                                staffedit.c8B_No_of_FCD_in_1st_year_of_study_under_your_mentorship_score = c8b
                                staffedit.d8B_No_of_UG_or_PG_projects_Co_guided_score = d8b
                                staffedit.a8bfile = a8bfile
                                staffedit.b8bfile = b8bfile
                                staffedit.c8bfile = c8bfile
                                staffedit.d8bfile = d8bfile

                                staffedit.save()
                                return render(request, "AppraisalForm/appraisalformedithod.html",contextedit)
                            
                        else:
                                sub1 = request.POST['sub1']
                                sub2 = request.POST['sub2']
                                sub3 = request.POST['sub3']
                                sub4 = request.POST['sub4']
                                sub5 = request.POST['sub5']
                                sub6 = request.POST['sub6']
                                sub7 = request.POST['sub7']
                                sub8 = request.POST['sub8']
                                pfile = request.FILES['pfile']
                                s1 = request.POST['s1']
                                s2 = request.POST['s2']
                                s3 = request.POST['s3']
                                s4 = request.POST['s4']
                                s5 = request.POST['s5']
                                s6 = request.POST['s6']
                                s7 = request.POST['s7']
                                s8 = request.POST['s8']
                                p1 = int(float(request.POST['pass1']))
                                p2 = int(float(request.POST['pass2']))
                                p3 = int(float(request.POST['pass3']))
                                p4 = int(float(request.POST['pass4']))
                                p5 = int(float(request.POST['pass5']))
                                p6 = int(float(request.POST['pass6']))
                                p7 = int(float(request.POST['pass7']))
                                p8 = int(float(request.POST['pass8']))
                                p61 = int(float(request.POST['pass61']))
                                p62 = int(float(request.POST['pass62']))
                                p63 = int(float(request.POST['pass63']))
                                p64 = int(float(request.POST['pass64']))
                                p65 = int(float(request.POST['pass65']))
                                p66 = int(float(request.POST['pass66']))
                                p67 = int(float(request.POST['pass67']))
                                p68 = int(float(request.POST['pass68']))
                                c7_sf = request.POST['student_feedback']
                                a9_cw = request.POST['a9']
                                b9_ict = request.POST['b9']
                                c9_cw = request.POST['c9']
                                a9file = request.FILES['a9file']
                                c9file = request.FILES['c9file']
                                a8 = request.POST['a8']
                                b8 = request.POST['b8']
                                c8 = request.POST['c8']
                                b8file = request.FILES['b8file']
                                c8file = request.FILES['c8file']
                                
                                staffedit.Sub_code1 = sub1
                                staffedit.Sub_code2 = sub2
                                staffedit.Sub_code3 = sub3
                                staffedit.Sub_code4 = sub4
                                staffedit.Sub_code5 = sub5
                                staffedit.Sub_code6 = sub6
                                staffedit.Sub_code7 = sub7
                                staffedit.Sub_code8 = sub8
                                staffedit.percent = pfile
                                staffedit.No_of_students1 = s1
                                staffedit.No_of_students2 = s2
                                staffedit.No_of_students3 = s3
                                staffedit.No_of_students4 = s4
                                staffedit.No_of_students5 = s5
                                staffedit.No_of_students6 = s6
                                staffedit.No_of_students7 = s7
                                staffedit.No_of_students8 = s8
                                staffedit.Percentage_of_pass1 = p1
                                staffedit.Percentage_of_pass2 = p2
                                staffedit.Percentage_of_pass3 = p3
                                staffedit.Percentage_of_pass4 = p4
                                staffedit.Percentage_of_pass5 = p5
                                staffedit.Percentage_of_pass6 = p6
                                staffedit.Percentage_of_pass7 = p7
                                staffedit.Percentage_of_pass8 = p8
                                staffedit.Percent_over_601 = p61
                                staffedit.Percent_over_602 = p62
                                staffedit.Percent_over_603 = p63
                                staffedit.Percent_over_604 = p64
                                staffedit.Percent_over_605 = p65
                                staffedit.Percent_over_606 = p66
                                staffedit.Percent_over_607 = p67
                                staffedit.Percent_over_608 = p68
                                staffedit.c7_Student_Feedback = c7_sf
                                staffedit.a9_No_of_conferences_or_workshops_or_Seminars_or_training_programs_or_etc_FDPs_attended_score = a9_cw
                                staffedit.b9_Use_of_ICT_in_TLP_score = b9_ict
                                staffedit.c9_No_of_conferences_or_workshops_or_Seminars_or_training_or_programs_or_etc_or_FDPs_conducted_or_coordinated_score = c9_cw
                                staffedit.a9file = a9file
                                staffedit.c9file = c9file
                                staffedit.a8_No_of_projects_guided_score = a8
                                staffedit.b8_No_of_Best_Projects_Awarded_OR_Student_Project_Exhibited_in_competitions_or_Symposiums_OR_Funded_by_external_agency_OR_Student_Project_Paper_Publication_s_score = b8
                                staffedit.c8_No_of_students_achieved_vertical_progression_under_your_mentorship = c8
                                staffedit.b8file = b8file
                                staffedit.c8file = c8file

                                staffedit.save()
                                return render(request, "AppraisalForm/appraisalformedithod.html",contextedit)
                else:    
                    if request.method == "GET":
                        return render(request, "AppraisalForm/appraisalform_hod.html",context)
                    if request.method == "POST":
                        user = Staff_ID
        
                        if check.Department == "Basic Science and Humanities":
                                ay = request.POST['a_year']
                                sub1 = request.POST['sub1']
                                sub2 = request.POST['sub2']
                                sub3 = request.POST['sub3']
                                sub4 = request.POST['sub4']
                                sub5 = request.POST['sub5']
                                sub6 = request.POST['sub6']
                                sub7 = request.POST['sub7']
                                sub8 = request.POST['sub8']
                                pfile = request.FILES['pfile']
                                s1 = request.POST['s1']
                                s2 = request.POST['s2']
                                s3 = request.POST['s3']
                                s4 = request.POST['s4']
                                s5 = request.POST['s5']
                                s6 = request.POST['s6']
                                s7 = request.POST['s7']
                                s8 = request.POST['s8']
                                p1 = int(float(request.POST['pass1']))
                                p2 = int(float(request.POST['pass2']))
                                p3 = int(float(request.POST['pass3']))
                                p4 = int(float(request.POST['pass4']))
                                p5 = int(float(request.POST['pass5']))
                                p6 = int(float(request.POST['pass6']))
                                p7 = int(float(request.POST['pass7']))
                                p8 = int(float(request.POST['pass8']))
                                p61 = int(float(request.POST['pass61']))
                                p62 = int(float(request.POST['pass62']))
                                p63 = int(float(request.POST['pass63']))
                                p64 = int(float(request.POST['pass64']))
                                p65 = int(float(request.POST['pass65']))
                                p66 = int(float(request.POST['pass66']))
                                p67 = int(float(request.POST['pass67']))
                                p68 = int(float(request.POST['pass68']))
                                c7_sf = request.POST['student_feedback']
                                a9_cw = request.POST['a9']
                                b9_ict = request.POST['b9']
                                c9_cw = request.POST['c9']
                                a9file = request.FILES['a9file']
                                c9file = request.FILES['c9file']
                                a8b = request.POST['a8b']
                                b8b = request.POST['b8b']
                                c8b = request.POST['c8b']
                                d8b = request.POST['d8b']
                                a8bfile = request.FILES['a8bfile']
                                b8bfile = request.FILES['b8bfile']
                                c8bfile = request.FILES['c8bfile']
                                d8bfile = request.FILES['d8bfile']

                                apf = AppraisalForm(user=Staff_ID,department=check.Department,designation=check.Present_Designation,academic_year=ay,name=check.Name,submitted_Faculty=True,submitted_HOD=True,whether_HOD=True,No_of_students1=s1, No_of_students2=s2, No_of_students3=s3, No_of_students4=s4,No_of_students5=s5, No_of_students6=s6, No_of_students7=s7, No_of_students8=s8,
                                            Sub_code1=sub1, Sub_code2=sub2, Sub_code3=sub3, Sub_code4=sub4,Sub_code5=sub5, Sub_code6=sub6, Sub_code7=sub7, Sub_code8=sub8,
                                            Percentage_of_pass1=p1, Percentage_of_pass2=p2, Percentage_of_pass3=p3, Percentage_of_pass4=p4,Percentage_of_pass5=p5, Percentage_of_pass6=p6, Percentage_of_pass7=p7, Percentage_of_pass8=p8,
                                            Percent_over_601=p61, Percent_over_602=p62, Percent_over_603=p63, Percent_over_604=p64,Percent_over_605=p65, Percent_over_606=p66, Percent_over_607=p67, Percent_over_608=p68,
                                            Percentage_of_pass1_hod=p1, Percentage_of_pass2_hod=p2, Percentage_of_pass3_hod=p3, Percentage_of_pass4_hod=p4,Percentage_of_pass5_hod=p5, Percentage_of_pass6_hod=p6, Percentage_of_pass7_hod=p7, Percentage_of_pass8_hod=p8,
                                            Percent_over_601_hod=p61, Percent_over_602_hod=p62, Percent_over_603_hod=p63, Percent_over_604_hod=p64,Percent_over_605_hod=p65, Percent_over_606_hod=p66, Percent_over_607_hod=p67, Percent_over_608_hod=p68,
                                            c7_Student_Feedback = c7_sf, a9_No_of_conferences_or_workshops_or_Seminars_or_training_programs_or_etc_FDPs_attended_score = a9_cw,
                                            b9_Use_of_ICT_in_TLP_score = b9_ict, c9_No_of_conferences_or_workshops_or_Seminars_or_training_or_programs_or_etc_or_FDPs_conducted_or_coordinated_score = c9_cw, a8B_No_of_Topper_in_1st_year_of_study_under_your_mentorship_score=a8b,
                                            b8B_No_of_students_achieved_vertical_progression_to_2nd_Year_under_your_mentorship_score=b8b, c8B_No_of_FCD_in_1st_year_of_study_under_your_mentorship_score=c8b,
                                            d8B_No_of_UG_or_PG_projects_Co_guided_score=d8b,percent=pfile,a9file=a9file,c9file=c9file,a8bfile=a8bfile,b8bfile=b8bfile,c8bfile=c8bfile,d8bfile=d8bfile)
                                apf.save()
                                return render(request, "AppraisalForm/appraisalform2_hod.html",context)   
                        else:
                                ay = request.POST['a_year']
                                sub1 = request.POST['sub1']
                                sub2 = request.POST['sub2']
                                sub3 = request.POST['sub3']
                                sub4 = request.POST['sub4']
                                sub5 = request.POST['sub5']
                                sub6 = request.POST['sub6']
                                sub7 = request.POST['sub7']
                                sub8 = request.POST['sub8']
                                pfile = request.FILES['pfile']
                                s1 = request.POST['s1']
                                s2 = request.POST['s2']
                                s3 = request.POST['s3']
                                s4 = request.POST['s4']
                                s5 = request.POST['s5']
                                s6 = request.POST['s6']
                                s7 = request.POST['s7']
                                s8 = request.POST['s8']
                                p1 = int(float(request.POST['pass1']))
                                p2 = int(float(request.POST['pass2']))
                                p3 = int(float(request.POST['pass3']))
                                p4 = int(float(request.POST['pass4']))
                                p5 = int(float(request.POST['pass5']))
                                p6 = int(float(request.POST['pass6']))
                                p7 = int(float(request.POST['pass7']))
                                p8 = int(float(request.POST['pass8']))
                                p61 = int(float(request.POST['pass61']))
                                p62 = int(float(request.POST['pass62']))
                                p63 = int(float(request.POST['pass63']))
                                p64 = int(float(request.POST['pass64']))
                                p65 = int(float(request.POST['pass65']))
                                p66 = int(float(request.POST['pass66']))
                                p67 = int(float(request.POST['pass67']))
                                p68 = int(float(request.POST['pass68']))
                                c7_sf = request.POST['student_feedback']
                                a9_cw = request.POST['a9']
                                b9_ict = request.POST['b9']
                                c9_cw = request.POST['c9']
                                a9file = request.FILES['a9file']
                                c9file = request.FILES['c9file']
                                a8 = request.POST['a8']
                                b8 = request.POST['b8']
                                c8 = request.POST['c8']
                                b8file = request.FILES['b8file']
                                c8file = request.FILES['c8file']

                                apf = AppraisalForm(user=Staff_ID,department=check.Department,designation=check.Present_Designation,name=check.Name,academic_year=ay,submitted_Faculty=True,submitted_HOD=True,whether_HOD=True,No_of_students1=s1, No_of_students2=s2, No_of_students3=s3, No_of_students4=s4,No_of_students5=s5, No_of_students6=s6, No_of_students7=s7, No_of_students8=s8,
                                            Sub_code1=sub1, Sub_code2=sub2, Sub_code3=sub3, Sub_code4=sub4,Sub_code5=sub5, Sub_code6=sub6, Sub_code7=sub7, Sub_code8=sub8,
                                            Percentage_of_pass1=p1, Percentage_of_pass2=p2, Percentage_of_pass3=p3, Percentage_of_pass4=p4,Percentage_of_pass5=p5, Percentage_of_pass6=p6, Percentage_of_pass7=p7, Percentage_of_pass8=p8,
                                            Percent_over_601=p61, Percent_over_602=p62, Percent_over_603=p63, Percent_over_604=p64,Percent_over_605=p65, Percent_over_606=p66, Percent_over_607=p67, Percent_over_608=p68,
                                            Percentage_of_pass1_hod=p1, Percentage_of_pass2_hod=p2, Percentage_of_pass3_hod=p3, Percentage_of_pass4_hod=p4,Percentage_of_pass5_hod=p5, Percentage_of_pass6_hod=p6, Percentage_of_pass7_hod=p7, Percentage_of_pass8_hod=p8,
                                            Percent_over_601_hod=p61, Percent_over_602_hod=p62, Percent_over_603_hod=p63, Percent_over_604_hod=p64,Percent_over_605_hod=p65, Percent_over_606_hod=p66, Percent_over_607_hod=p67, Percent_over_608_hod=p68,
                                            c7_Student_Feedback = c7_sf, a9_No_of_conferences_or_workshops_or_Seminars_or_training_programs_or_etc_FDPs_attended_score = a9_cw,
                                            b9_Use_of_ICT_in_TLP_score = b9_ict, c9_No_of_conferences_or_workshops_or_Seminars_or_training_or_programs_or_etc_or_FDPs_conducted_or_coordinated_score = c9_cw,a8_No_of_projects_guided_score=a8,
                                            b8_No_of_Best_Projects_Awarded_OR_Student_Project_Exhibited_in_competitions_or_Symposiums_OR_Funded_by_external_agency_OR_Student_Project_Paper_Publication_s_score=b8,
                                            c8_No_of_students_achieved_vertical_progression_under_your_mentorship=c8, percent=pfile,a9file=a9file,c9file=c9file,
                                            b8file=b8file,c8file=c8file)
                                apf.save()
                                return render(request, "AppraisalForm/appraisalform2_hod.html",context)
            except:
                messages.warning(request, 'You need to upload all files before submission.')
                return redirect('/AppraisalForm/appraisalform_hodcreate/') 
        else:
            return redirect('/log-in')
    else:
        return redirect('/log-in')
def AppraisalForm2_hodcreate(request):
    if request.session.get('hod', False):
        Staff_ID = request.session['hod']
        check = PersonalDetail.objects.get(Staff_ID=Staff_ID)
        staff = PersonalDetail.objects.get(Staff_ID=Staff_ID)
        context = {'check':check, 'staff':staff,
                    'staff_id':Staff_ID }

        if PersonalDetail.objects.filter(Staff_ID=Staff_ID).exists():
            try:
                if AppraisalForm2.objects.filter(user=Staff_ID).exists():
                    staffedit = AppraisalForm2.objects.get(user=Staff_ID)
                    staff = PersonalDetail.objects.get(Staff_ID=Staff_ID)
                    contextedit = {
                        'staffedit':staffedit,
                        'staff' : staff
                    }
                    if request.method == "GET":
                        return render(request, "AppraisalForm/appraisalformedit2hod.html",contextedit)
                    if request.method == "POST":
                                a10 = request.POST['a10']
                                b10 = request.POST['b10']
                                c10 = request.POST['c10']
                                a11 = request.POST['a11']
                                b11 = request.POST['b11']
                                a12 = request.POST['a12']
                                b12 = request.POST['b12']
                                a10file = request.FILES['a10file']
                                b10file = request.FILES['b10file']
                                c10file = request.FILES['c10file']
                                a11file = request.FILES['a11file']
                                b11file = request.FILES['b11file']
                                a12file = request.FILES['a12file']
                                b12file = request.FILES['b12file']

                                staffedit.a10_No_of_papers_published_in_journals_score = a10
                                staffedit.b10_No_of_papers_presented_in_conferences_score = b10
                                staffedit.c10_No_of_papers_indexed_in_In_Scopus_or_Web_of_Science_or_UGC_care_list_OR_No_of_book_chapters_authored_OR_No_of_Books_Authored_score = c10
                                staffedit.a11_No_of_Research_Project_proposals_submitted_score = a11
                                staffedit.b11_No_of_Research_projects_Received_and_Amount_score = b11
                                staffedit.a12_No_of_Consultancy_projects_received_OR_ongoing_score = a12
                                staffedit.b12_No_of_patents_applied_awarded_score = b12
                                staffedit.a10file = a10file
                                staffedit.b10file = b10file
                                staffedit.c10file = c10file
                                staffedit.a11file = a11file
                                staffedit.b11file = b11file
                                staffedit.a12file = a12file
                                staffedit.b12file = b12file

                                staffedit.save()
                                return render(request, "AppraisalForm/appraisalformedit2hod.html",contextedit)
                else:
                    if request.method == "GET":
                        return render(request, "AppraisalForm/appraisalform2_hod.html",context)
                    if request.method == "POST":
                                ay = request.POST['a_year']
                                a10 = request.POST['a10']
                                b10 = request.POST['b10']
                                c10 = request.POST['c10']
                                a11 = request.POST['a11']
                                b11 = request.POST['b11']
                                a12 = request.POST['a12']
                                b12 = request.POST['b12']
                                a10file = request.FILES['a10file']
                                b10file = request.FILES['b10file']
                                c10file = request.FILES['c10file']
                                a11file = request.FILES['a11file']
                                b11file = request.FILES['b11file']
                                a12file = request.FILES['a12file']
                                b12file = request.FILES['b12file']

                                apf2 = AppraisalForm2(user=Staff_ID,department=check.Department,designation=check.Present_Designation,academic_year=ay,name=check.Name,submitted_Faculty=True,submitted_HOD=True,whether_HOD=True,a10_No_of_papers_published_in_journals_score=a10,b10_No_of_papers_presented_in_conferences_score=b10,
                                            c10_No_of_papers_indexed_in_In_Scopus_or_Web_of_Science_or_UGC_care_list_OR_No_of_book_chapters_authored_OR_No_of_Books_Authored_score=c10,
                                            a11_No_of_Research_Project_proposals_submitted_score=a11,b11_No_of_Research_projects_Received_and_Amount_score=b11,
                                            a12_No_of_Consultancy_projects_received_OR_ongoing_score=a12,b12_No_of_patents_applied_awarded_score=b12,
                                            a10file=a10file,b10file=b10file,c10file=c10file,
                                            a11file=a11file,b11file=b11file,a12file=a12file,b12file=b12file)
                                apf2.save()
                                return render(request, "AppraisalForm/appraisalform3_hod.html",context)
            except:
                messages.warning(request, 'You need to upload all files before submission.')
                return redirect('/AppraisalForm/appraisalform2_hodcreate/')  
        else:
            return redirect('/log-in')
    else:
        return redirect('/log-in')

    # return render(request, 'AppraisalForm/appraisalform2_hod.html',context)

def AppraisalForm3_hodcreate(request):
    if request.session.get('hod', False):
        Staff_ID = request.session['hod']
        check = PersonalDetail.objects.get(Staff_ID=Staff_ID)
        staff = PersonalDetail.objects.get(Staff_ID=Staff_ID)
        context = {'check':check, 'staff':staff,
                    'staff_id':Staff_ID }

        if PersonalDetail.objects.filter(Staff_ID=Staff_ID).exists():
            try:
                if AppraisalForm3.objects.filter(user=Staff_ID).exists():
                    staffedit = AppraisalForm3.objects.get(user=Staff_ID)
                    staff = PersonalDetail.objects.get(Staff_ID=Staff_ID)
                    contextedit = {
                        'staffedit':staffedit,
                        'staff' : staff
                    }
                    if request.method == "GET":
                        return render(request, "AppraisalForm/appraisalformedit3hod.html",contextedit)
                    if request.method == "POST":
                        a13 = request.POST['a13']
                        b13 = request.POST['b13']
                        c13 = request.POST['c13']
                        d13 = request.POST['d13']
                        e13 = request.POST['e13']
                        f13 = request.POST['f13']
                        a14 = request.POST['a14']
                        b14 = request.POST['b14']
                        c14 = request.POST['c14']
                        a15 = request.POST['a15']
                        c14file = request.FILES['c14file']
                        a15file = request.FILES['a15file'] 

                        staffedit.a13 = a13
                        staffedit.b13 = b13
                        staffedit.c13 = c13
                        staffedit.d13 = d13
                        staffedit.e13 = e13
                        staffedit.f13 = f13
                        staffedit.a14 = a14
                        staffedit.b14 = b14
                        staffedit.c14 = c14
                        staffedit.a15 = a15
                        staffedit.c14file = c14file
                        staffedit.a15file = a15file   

                        staffedit.save()
                        return grandscorecalcH(request)                  
                else:
                    if request.method == "GET":
                        return render(request, "AppraisalForm/appraisalform3_hod.html",context)
                    if request.method == "POST":
                        ay = request.POST['a_year']
                        a13 = request.POST['a13']
                        b13 = request.POST['b13']
                        c13 = request.POST['c13']
                        d13 = request.POST['d13']
                        e13 = request.POST['e13']
                        f13 = request.POST['f13']
                        a14 = request.POST['a14']
                        b14 = request.POST['b14']
                        c14 = request.POST['c14']
                        a15 = request.POST['a15']
                        c14file = request.FILES['c14file']
                        a15file = request.FILES['a15file']

                        apf3 = AppraisalForm3(user=Staff_ID,department=check.Department,designation=check.Present_Designation,name=check.Name,academic_year=ay,submitted_Faculty=True,submitted_HOD=True,whether_HOD=True,a13=a13,b13=b13,c13=c13,d13=d13,e13=e13,
                                            f13=f13,a14=a14,b14=b14,c14=c14,a15=a15,c14file=c14file,a15file=a15file)
                        apf3.save()
                        return grandscorecalcH(request)
            except:
                messages.warning(request, 'You need to upload all files before submission.')
                return redirect('/AppraisalForm/appraisalform3_hodcreate/')  
        else:
            return redirect('/log-in')
    else:
        return redirect('/log-in')
    # return render(request, 'AppraisalForm/appraisalform3_hod.html',context)

def grandscorecalcH(request):
    staff = request.session['hod']
    if PersonalDetail.objects.filter(Staff_ID=staff).exists():
        if GrandApiScores.objects.filter(user=staff).exists():
            pd = PersonalDetail.objects.get(Staff_ID=staff)
            apf = AppraisalForm.objects.get(user=staff)
            apf2 = AppraisalForm2.objects.get(user=staff)
            apf3 = AppraisalForm3.objects.get(user=staff)
            gapi = GrandApiScores.objects.get(user=staff)
            if int(pd.total_years) <= 5:
                grand = (((apf.Part1APIscore/350)*0.70)+((apf2.part2APIscore/170)*0.20)+((apf3.part3APIscore/180)*0.10))*100
                gapi.GrandScore = grand
                gapi.save()
                
            elif int(pd.total_years) > 5 and int(pd.total_years) < 10:
                grand = (((apf.Part1APIscore/350)*0.60)+((apf2.part2APIscore/170)*0.25)+((apf3.part3APIscore/180)*0.15))*100
                gapi.GrandScore = grand
                gapi.save()

            elif int(pd.total_years) >= 10:
                grand = (((apf.Part1APIscore/350)*0.50)+((apf2.part2APIscore/170)*0.30)+((apf3.part3APIscore/180)*0.20))*100
                gapi.GrandScore = grand
                gapi.save()
            return redirect('/hod')
        else:
            pd = PersonalDetail.objects.get(Staff_ID=staff)
            apf = AppraisalForm.objects.get(user=staff)
            apf2 = AppraisalForm2.objects.get(user=staff)
            apf3 = AppraisalForm3.objects.get(user=staff)
            if int(pd.total_years) <= 5:
                grand = (((apf.Part1APIscore/350)*0.70)+((apf2.part2APIscore/170)*0.20)+((apf3.part3APIscore/180)*0.10))*100
                gapi = GrandApiScores(user=staff,department=pd.Department,designation=pd.Present_Designation,name=pd.Name,submitted_Faculty=True,submitted_HOD=True,whether_HOD=True,Part1APIscore=apf.Part1APIscore,
                                part2APIscore=apf2.part2APIscore,part3APIscore=apf3.part3APIscore,GrandScore=grand,GrandScoreHOD=grand,academic_year=apf.academic_year)
                gapi.save()
                
            elif int(pd.total_years) > 5 and int(pd.total_years) < 10:
                grand = (((apf.Part1APIscore/350)*0.60)+((apf2.part2APIscore/170)*0.25)+((apf3.part3APIscore/180)*0.15))*100
                gapi = GrandApiScores(user=staff,department=pd.Department,designation=pd.Present_Designation,name=pd.Name,submitted_Faculty=True,submitted_HOD=True,whether_HOD=True,Part1APIscore=apf.Part1APIscore,
                                part2APIscore=apf2.part2APIscore,part3APIscore=apf3.part3APIscore,GrandScore=grand,GrandScoreHOD=grand,academic_year=apf.academic_year)
                gapi.save()
            elif int(pd.total_years) >= 10:
                grand = (((apf.Part1APIscore/350)*0.50)+((apf2.part2APIscore/170)*0.30)+((apf3.part3APIscore/180)*0.20))*100
                gapi = GrandApiScores(user=staff,department=pd.Department,designation=pd.Present_Designation,name=pd.Name,submitted_Faculty=True,submitted_HOD=True,whether_HOD=True,Part1APIscore=apf.Part1APIscore,
                                part2APIscore=apf2.part2APIscore,part3APIscore=apf3.part3APIscore,GrandScore=grand,GrandScoreHOD=grand,academic_year=apf.academic_year)
                gapi.save()
            return redirect('/hod')

    

#hod_faculty_edit

def AppraisalForm_HODscores(request, user):
    if request.session.get('hod', False):
        Staff_ID = request.session['hod']
        dept = PersonalDetail.objects.get(Staff_ID=Staff_ID)
        if PersonalDetail.objects.filter(Staff_ID=Staff_ID).exists():
            if AppraisalForm.objects.filter(user=user).exists():
                form = AppraisalForm.objects.get(user=user)
                staff = PersonalDetail.objects.get(Staff_ID=Staff_ID)
                context = {"form" : form, 'staff':staff }
                if request.method == "GET":
                    return render(request, 'AppraisalForm/hod_faculty_score.html', context)
                if request.method == "POST":
                    if dept.Department == "Basic Science and Humanities":
                        p1 = int(float(request.POST['pass1']))
                        p2 = int(float(request.POST['pass2']))
                        p3 = int(float(request.POST['pass3']))
                        p4 = int(float(request.POST['pass4']))
                        p5 = int(float(request.POST['pass5']))
                        p6 = int(float(request.POST['pass6']))
                        p7 = int(float(request.POST['pass7']))
                        p8 = int(float(request.POST['pass8']))
                        p61 = int(float(request.POST['pass61']))
                        p62 = int(float(request.POST['pass62']))
                        p63 = int(float(request.POST['pass63']))
                        p64 = int(float(request.POST['pass64']))
                        p65 = int(float(request.POST['pass65']))
                        p66 = int(float(request.POST['pass66']))
                        p67 = int(float(request.POST['pass67']))
                        p68 = int(float(request.POST['pass68']))
                        c7HOD = request.POST['c7HOD']
                        a9HOD = request.POST['a9HOD']
                        b9HOD = request.POST['b9HOD']
                        c9HOD = request.POST['c9HOD']
                        a8bHOD = request.POST['a8bHOD']
                        b8bHOD = request.POST['b8bHOD']
                        c8bHOD = request.POST['c8bHOD']
                        d8bHOD = request.POST['d8bHOD']

                        form.Percentage_of_pass1_hod = p1
                        form.Percentage_of_pass2_hod = p2
                        form.Percentage_of_pass3_hod = p3
                        form.Percentage_of_pass4_hod = p4
                        form.Percentage_of_pass5_hod = p5
                        form.Percentage_of_pass6_hod = p6
                        form.Percentage_of_pass7_hod = p7
                        form.Percentage_of_pass8_hod = p8
                        form.Percent_over_601_hod = p61
                        form.Percent_over_602_hod = p62
                        form.Percent_over_603_hod = p63
                        form.Percent_over_604_hod = p64
                        form.Percent_over_605_hod = p65
                        form.Percent_over_606_hod = p66
                        form.Percent_over_607_hod = p67
                        form.Percent_over_608_hod = p68
                        form.c7HOD_Student_Feedback = c7HOD
                        form.c7P_Student_Feedback = c7HOD
                        form.a9HOD_score = a9HOD
                        form.a9P_score = a9HOD
                        form.b9HOD_score = b9HOD
                        form.b9P_score = b9HOD
                        form.c9HOD_score = c9HOD
                        form.c9P_score = c9HOD
                        form.a8BHOD_score = a8bHOD
                        form.a8BP_score = a8bHOD
                        form.b8BHOD_score = b8bHOD
                        form.b8BP_score = b8bHOD
                        form.c8BHOD_score = c8bHOD
                        form.c8BP_score = c8bHOD
                        form.d8BHOD_score = d8bHOD
                        form.d8BP_score = d8bHOD
                        form.submitted_HOD = True

                        form.save()
                        return render(request, 'AppraisalForm/hod_faculty_score.html',context)
                        
                    else:
                        p1 = int(float(request.POST['pass1']))
                        p2 = int(float(request.POST['pass2']))
                        p3 = int(float(request.POST['pass3']))
                        p4 = int(float(request.POST['pass4']))
                        p5 = int(float(request.POST['pass5']))
                        p6 = int(float(request.POST['pass6']))
                        p7 = int(float(request.POST['pass7']))
                        p8 = int(float(request.POST['pass8']))
                        p61 = int(float(request.POST['pass61']))
                        p62 = int(float(request.POST['pass62']))
                        p63 = int(float(request.POST['pass63']))
                        p64 = int(float(request.POST['pass64']))
                        p65 = int(float(request.POST['pass65']))
                        p66 = int(float(request.POST['pass66']))
                        p67 = int(float(request.POST['pass67']))
                        p68 = int(float(request.POST['pass68']))
                        c7HOD = request.POST['c7HOD']
                        a9HOD = request.POST['a9HOD']
                        b9HOD = request.POST['b9HOD']
                        c9HOD = request.POST['c9HOD']
                        a8HOD = request.POST['a8HOD']
                        b8HOD = request.POST['b8HOD']
                        c8HOD = request.POST['c8HOD']

                        form.Percentage_of_pass1_hod = p1
                        form.Percentage_of_pass2_hod = p2
                        form.Percentage_of_pass3_hod = p3
                        form.Percentage_of_pass4_hod = p4
                        form.Percentage_of_pass5_hod = p5
                        form.Percentage_of_pass6_hod = p6
                        form.Percentage_of_pass7_hod = p7
                        form.Percentage_of_pass8_hod = p8
                        form.Percent_over_601_hod = p61
                        form.Percent_over_602_hod = p62
                        form.Percent_over_603_hod = p63
                        form.Percent_over_604_hod = p64
                        form.Percent_over_605_hod = p65
                        form.Percent_over_606_hod = p66
                        form.Percent_over_607_hod = p67
                        form.Percent_over_608_hod = p68
                        form.c7HOD_Student_Feedback = c7HOD
                        form.c7P_Student_Feedback = c7HOD
                        form.a9HOD_score = a9HOD
                        form.a9P_score = a9HOD
                        form.b9HOD_score = b9HOD
                        form.b9P_score = b9HOD
                        form.c9HOD_score = c9HOD
                        form.c9P_score = c9HOD
                        form.a8HOD_score = a8HOD
                        form.a8P_score = a8HOD
                        form.b8HOD_score = b8HOD
                        form.b8P_score = b8HOD
                        form.c8HOD_No_of_students_achieved_vertical_progression_under_your_mentorship = c8HOD
                        form.c8P_No_of_students_achieved_vertical_progression_under_your_mentorship = c8HOD
                        form.submitted_HOD = True

                        form.save()
                        return render(request, 'AppraisalForm/hod_faculty_score.html',context)
            else:
                return redirect('/faculty_list')
        else:
            return redirect('/log-in')
    else:
        return redirect('/log-in')
          
    

def AppraisalForm2_HODscores(request, user):
    if request.session.get('hod', False):
        Staff_ID = request.session['hod']
        if PersonalDetail.objects.filter(Staff_ID=Staff_ID).exists():
            if AppraisalForm2.objects.filter(user=user).exists():
                form = AppraisalForm2.objects.get(user=user)
                staff = PersonalDetail.objects.get(Staff_ID=Staff_ID)
                context = {"form" : form, 'staff':staff }
                if request.method == "GET":
                    return render(request, 'AppraisalForm/hod_faculty_score2.html', context)
                if request.method == "POST":
                    a10HOD = request.POST['a10HOD']
                    b10HOD = request.POST['b10HOD']
                    c10HOD = request.POST['c10HOD']
                    a11HOD = request.POST['a11HOD']
                    b11HOD = request.POST['b11HOD']
                    a12HOD = request.POST['a12HOD']
                    b12HOD = request.POST['b12HOD']

                    form.a10HOD_score = a10HOD
                    form.a10P_score = a10HOD
                    form.b10HOD_score = b10HOD
                    form.b10P_score = b10HOD
                    form.c10HOD_score = c10HOD
                    form.c10P_score = c10HOD
                    form.a11HOD_score = a11HOD
                    form.a11P_score = a11HOD
                    form.b11HOD_score = b11HOD
                    form.b11P_score = b11HOD
                    form.a12HOD_score = a12HOD
                    form.a12P_score = a12HOD
                    form.b12HOD_score = b12HOD
                    form.b12P_score = b12HOD
                    form.submitted_HOD = True

                    form.save()
                    return render(request, 'AppraisalForm/hod_faculty_score2.html', context)
            else:
                return redirect('/faculty_list')
        else:
            return redirect('/log-in')
    else:
        return redirect('/log-in')

def AppraisalForm3_HODscores(request, user):
    if request.session.get('hod', False):
        Staff_ID = request.session['hod']
        if PersonalDetail.objects.filter(Staff_ID=Staff_ID).exists():
            if AppraisalForm3.objects.filter(user=user).exists():
                form = AppraisalForm3.objects.get(user=user)
                staff = PersonalDetail.objects.get(Staff_ID=Staff_ID)
                context = {"form" : form, 'staff':staff }
                if request.method == "GET":
                    return render(request, 'AppraisalForm/hod_faculty_score3.html', context)
                if request.method == "POST":
                    a13HOD = request.POST['a13HOD']
                    b13HOD = request.POST['b13HOD']
                    c13HOD = request.POST['c13HOD']
                    d13HOD = request.POST['d13HOD']
                    e13HOD = request.POST['e13HOD']
                    f13HOD = request.POST['f13HOD']
                    a14HOD = request.POST['a14HOD']
                    b14HOD = request.POST['b14HOD']
                    c14HOD = request.POST['c14HOD']
                    a15HOD = request.POST['a15HOD']

                    form.HOD_a13 = a13HOD
                    form.P_a13 = a13HOD
                    form.HOD_b13 = b13HOD
                    form.P_b13 = b13HOD
                    form.HOD_c13 = c13HOD
                    form.P_c13 = c13HOD
                    form.HOD_d13 = d13HOD
                    form.P_d13 = d13HOD
                    form.HOD_e13 = e13HOD
                    form.P_e13 = e13HOD
                    form.HOD_f13 = f13HOD
                    form.P_f13 = f13HOD
                    form.HOD_a14 = a14HOD
                    form.P_a14 = a14HOD
                    form.HOD_b14 = b14HOD
                    form.P_b14 = b14HOD
                    form.HOD_c14 = c14HOD
                    form.P_c14 = c14HOD
                    form.HOD_a15 = a15HOD
                    form.P_a15 = a15HOD
                    form.submitted_HOD = True

                    form.save()
                    return grandscorecalcHOD(request,user)
            else:
                return redirect('/faculty_list')
        else:
            return redirect('/log-in')
    else:
        return redirect('/log-in')


def grandscorecalcHOD(request,user):
    staff = request.session['hod']
    if PersonalDetail.objects.filter(Staff_ID=staff).exists():
        if GrandApiScores.objects.filter(user=user).exists():
            pd = PersonalDetail.objects.get(Staff_ID=user)
            apf = AppraisalForm.objects.get(user=user)
            apf2 = AppraisalForm2.objects.get(user=user)
            apf3 = AppraisalForm3.objects.get(user=user)
            gapi = GrandApiScores.objects.get(user=user)
            if int(pd.total_years) <= 5:
                grandhod = (((apf.Part1HODAPIscore/350)*0.70)+((apf2.part2HODAPIscore/170)*0.20)+((apf3.part3HODAPIscore/180)*0.10))*100
                grandp = (((apf.Part1PAPIscore/350)*0.70)+((apf2.part2PAPIscore/170)*0.20)+((apf3.part3PAPIscore/180)*0.10))*100
                
                if grandhod >= 70 and grandhod <= 100:
                    gapi.Part1HODAPIscore = apf.Part1HODAPIscore
                    gapi.part2HODAPIscore = apf2.part2HODAPIscore
                    gapi.part3HODAPIscore = apf3.part3HODAPIscore
                    gapi.Part1PAPIscore = apf.Part1PAPIscore
                    gapi.part2PAPIscore = apf2.part2PAPIscore
                    gapi.part3PAPIscore = apf3.part3PAPIscore
                    gapi.GrandScoreHOD = grandhod
                    gapi.submitted_HOD = True
                    gapi.GrandScoreP = grandp
                    gapi.grade = 'A'
                    gapi.save()
                elif grandhod >= 60 and grandhod < 70:
                    gapi.Part1HODAPIscore = apf.Part1HODAPIscore
                    gapi.part2HODAPIscore = apf2.part2HODAPIscore
                    gapi.part3HODAPIscore = apf3.part3HODAPIscore
                    gapi.Part1PAPIscore = apf.Part1PAPIscore
                    gapi.part2PAPIscore = apf2.part2PAPIscore
                    gapi.part3PAPIscore = apf3.part3PAPIscore
                    gapi.GrandScoreHOD = grandhod
                    gapi.submitted_HOD = True
                    gapi.GrandScoreP = grandp
                    gapi.grade = 'B'
                    gapi.save()
                elif grandhod >= 55 and grandhod < 60:
                    gapi.Part1HODAPIscore = apf.Part1HODAPIscore
                    gapi.part2HODAPIscore = apf2.part2HODAPIscore
                    gapi.part3HODAPIscore = apf3.part3HODAPIscore
                    gapi.Part1PAPIscore = apf.Part1PAPIscore
                    gapi.part2PAPIscore = apf2.part2PAPIscore
                    gapi.part3PAPIscore = apf3.part3PAPIscore
                    gapi.GrandScoreHOD = grandhod
                    gapi.submitted_HOD = True
                    gapi.GrandScoreP = grandp
                    gapi.grade = 'C'
                    gapi.save()
                elif grandhod >= 50 and grandhod < 55:
                    gapi.Part1HODAPIscore = apf.Part1HODAPIscore
                    gapi.part2HODAPIscore = apf2.part2HODAPIscore
                    gapi.part3HODAPIscore = apf3.part3HODAPIscore
                    gapi.Part1PAPIscore = apf.Part1PAPIscore
                    gapi.part2PAPIscore = apf2.part2PAPIscore
                    gapi.part3PAPIscore = apf3.part3PAPIscore
                    gapi.GrandScoreHOD = grandhod
                    gapi.submitted_HOD = True
                    gapi.GrandScoreP = grandp
                    gapi.grade = 'D'
                    gapi.save()
                elif grandhod >= 40 and grandhod < 50:
                    gapi.Part1HODAPIscore = apf.Part1HODAPIscore
                    gapi.part2HODAPIscore = apf2.part2HODAPIscore
                    gapi.part3HODAPIscore = apf3.part3HODAPIscore
                    gapi.Part1PAPIscore = apf.Part1PAPIscore
                    gapi.part2PAPIscore = apf2.part2PAPIscore
                    gapi.part3PAPIscore = apf3.part3PAPIscore
                    gapi.GrandScoreHOD = grandhod
                    gapi.submitted_HOD = True
                    gapi.GrandScoreP = grandp
                    gapi.grade = 'E'
                    gapi.save()
                elif grandhod < 40:
                    gapi.Part1HODAPIscore = apf.Part1HODAPIscore
                    gapi.part2HODAPIscore = apf2.part2HODAPIscore
                    gapi.part3HODAPIscore = apf3.part3HODAPIscore
                    gapi.Part1PAPIscore = apf.Part1PAPIscore
                    gapi.part2PAPIscore = apf2.part2PAPIscore
                    gapi.part3PAPIscore = apf3.part3PAPIscore
                    gapi.GrandScoreHOD = grandhod
                    gapi.submitted_HOD = True
                    gapi.GrandScoreP = grandp
                    gapi.grade = 'F'
                    gapi.save()
            elif int(pd.total_years) > 5 and int(pd.total_years) < 10:
                grandhod = (((apf.Part1HODAPIscore/350)*0.60)+((apf2.part2HODAPIscore/170)*0.25)+((apf3.part3HODAPIscore/180)*0.15))*100
                grandp = (((apf.Part1PAPIscore/350)*0.60)+((apf2.part2PAPIscore/170)*0.25)+((apf3.part3PAPIscore/180)*0.15))*100

                if grandhod >= 70 and grandhod <= 100:
                    gapi.Part1HODAPIscore = apf.Part1HODAPIscore
                    gapi.part2HODAPIscore = apf2.part2HODAPIscore
                    gapi.part3HODAPIscore = apf3.part3HODAPIscore
                    gapi.Part1PAPIscore = apf.Part1PAPIscore
                    gapi.part2PAPIscore = apf2.part2PAPIscore
                    gapi.part3PAPIscore = apf3.part3PAPIscore
                    gapi.GrandScoreHOD = grandhod
                    gapi.submitted_HOD = True
                    gapi.GrandScoreP = grandp
                    gapi.grade = 'A'
                    gapi.save()
                elif grandhod >= 60 and grandhod < 70:
                    gapi.Part1HODAPIscore = apf.Part1HODAPIscore
                    gapi.part2HODAPIscore = apf2.part2HODAPIscore
                    gapi.part3HODAPIscore = apf3.part3HODAPIscore
                    gapi.Part1PAPIscore = apf.Part1PAPIscore
                    gapi.part2PAPIscore = apf2.part2PAPIscore
                    gapi.part3PAPIscore = apf3.part3PAPIscore
                    gapi.GrandScoreHOD = grandhod
                    gapi.submitted_HOD = True
                    gapi.GrandScoreP = grandp
                    gapi.grade = 'B'
                    gapi.save()
                elif grandhod >= 55 and grandhod < 60:
                    gapi.Part1HODAPIscore = apf.Part1HODAPIscore
                    gapi.part2HODAPIscore = apf2.part2HODAPIscore
                    gapi.part3HODAPIscore = apf3.part3HODAPIscore
                    gapi.Part1PAPIscore = apf.Part1PAPIscore
                    gapi.part2PAPIscore = apf2.part2PAPIscore
                    gapi.part3PAPIscore = apf3.part3PAPIscore
                    gapi.GrandScoreHOD = grandhod
                    gapi.submitted_HOD = True
                    gapi.GrandScoreP = grandp
                    gapi.grade = 'C'
                    gapi.save()
                elif grandhod >= 50 and grandhod < 55:
                    gapi.Part1HODAPIscore = apf.Part1HODAPIscore
                    gapi.part2HODAPIscore = apf2.part2HODAPIscore
                    gapi.part3HODAPIscore = apf3.part3HODAPIscore
                    gapi.Part1PAPIscore = apf.Part1PAPIscore
                    gapi.part2PAPIscore = apf2.part2PAPIscore
                    gapi.part3PAPIscore = apf3.part3PAPIscore
                    gapi.GrandScoreHOD = grandhod
                    gapi.submitted_HOD = True
                    gapi.GrandScoreP = grandp
                    gapi.grade = 'D'
                    gapi.save()
                elif grandhod >= 40 and grandhod < 50:
                    gapi.Part1HODAPIscore = apf.Part1HODAPIscore
                    gapi.part2HODAPIscore = apf2.part2HODAPIscore
                    gapi.part3HODAPIscore = apf3.part3HODAPIscore
                    gapi.Part1PAPIscore = apf.Part1PAPIscore
                    gapi.part2PAPIscore = apf2.part2PAPIscore
                    gapi.part3PAPIscore = apf3.part3PAPIscore
                    gapi.GrandScoreHOD = grandhod
                    gapi.submitted_HOD = True
                    gapi.GrandScoreP = grandp
                    gapi.grade = 'E'
                    gapi.save()
                elif grandhod < 40:
                    gapi.Part1HODAPIscore = apf.Part1HODAPIscore
                    gapi.part2HODAPIscore = apf2.part2HODAPIscore
                    gapi.part3HODAPIscore = apf3.part3HODAPIscore
                    gapi.Part1PAPIscore = apf.Part1PAPIscore
                    gapi.part2PAPIscore = apf2.part2PAPIscore
                    gapi.part3PAPIscore = apf3.part3PAPIscore
                    gapi.GrandScoreHOD = grandhod
                    gapi.submitted_HOD = True
                    gapi.GrandScoreP = grandp
                    gapi.grade = 'F'
                    gapi.save()
            elif int(pd.total_years) >= 10:
                grandhod = (((apf.Part1HODAPIscore/350)*0.50)+((apf2.part2HODAPIscore/170)*0.30)+((apf3.part3HODAPIscore/180)*0.20))*100
                grandp = (((apf.Part1PAPIscore/350)*0.50)+((apf2.part2PAPIscore/170)*0.30)+((apf3.part3PAPIscore/180)*0.20))*100

                if grandhod >= 70 and grandhod <= 100:
                    gapi.Part1HODAPIscore = apf.Part1HODAPIscore
                    gapi.part2HODAPIscore = apf2.part2HODAPIscore
                    gapi.part3HODAPIscore = apf3.part3HODAPIscore
                    gapi.Part1PAPIscore = apf.Part1PAPIscore
                    gapi.part2PAPIscore = apf2.part2PAPIscore
                    gapi.part3PAPIscore = apf3.part3PAPIscore
                    gapi.GrandScoreHOD = grandhod
                    gapi.submitted_HOD = True
                    gapi.GrandScoreP = grandp
                    gapi.grade = 'A'
                    gapi.save()
                elif grandhod >= 60 and grandhod < 70:
                    gapi.Part1HODAPIscore = apf.Part1HODAPIscore
                    gapi.part2HODAPIscore = apf2.part2HODAPIscore
                    gapi.part3HODAPIscore = apf3.part3HODAPIscore
                    gapi.Part1PAPIscore = apf.Part1PAPIscore
                    gapi.part2PAPIscore = apf2.part2PAPIscore
                    gapi.part3PAPIscore = apf3.part3PAPIscore
                    gapi.GrandScoreHOD = grandhod
                    gapi.submitted_HOD = True
                    gapi.GrandScoreP = grandp
                    gapi.grade = 'B'
                    gapi.save()
                elif grandhod >= 55 and grandhod < 60:
                    gapi.Part1HODAPIscore = apf.Part1HODAPIscore
                    gapi.part2HODAPIscore = apf2.part2HODAPIscore
                    gapi.part3HODAPIscore = apf3.part3HODAPIscore
                    gapi.Part1PAPIscore = apf.Part1PAPIscore
                    gapi.part2PAPIscore = apf2.part2PAPIscore
                    gapi.part3PAPIscore = apf3.part3PAPIscore
                    gapi.GrandScoreHOD = grandhod
                    gapi.submitted_HOD = True
                    gapi.GrandScoreP = grandp
                    gapi.grade = 'C'
                    gapi.save()
                elif grandhod >= 50 and grandhod < 55:
                    gapi.Part1HODAPIscore = apf.Part1HODAPIscore
                    gapi.part2HODAPIscore = apf2.part2HODAPIscore
                    gapi.part3HODAPIscore = apf3.part3HODAPIscore
                    gapi.Part1PAPIscore = apf.Part1PAPIscore
                    gapi.part2PAPIscore = apf2.part2PAPIscore
                    gapi.part3PAPIscore = apf3.part3PAPIscore
                    gapi.GrandScoreHOD = grandhod
                    gapi.submitted_HOD = True
                    gapi.GrandScoreP = grandp
                    gapi.grade = 'D'
                    gapi.save()
                elif grandhod >= 40 and grandhod < 50:
                    gapi.Part1HODAPIscore = apf.Part1HODAPIscore
                    gapi.part2HODAPIscore = apf2.part2HODAPIscore
                    gapi.part3HODAPIscore = apf3.part3HODAPIscore
                    gapi.Part1PAPIscore = apf.Part1PAPIscore
                    gapi.part2PAPIscore = apf2.part2PAPIscore
                    gapi.part3PAPIscore = apf3.part3PAPIscore
                    gapi.GrandScoreHOD = grandhod
                    gapi.submitted_HOD = True
                    gapi.GrandScoreP = grandp
                    gapi.grade = 'E'
                    gapi.save()
                elif grandhod < 40:
                    gapi.Part1HODAPIscore = apf.Part1HODAPIscore
                    gapi.part2HODAPIscore = apf2.part2HODAPIscore
                    gapi.part3HODAPIscore = apf3.part3HODAPIscore
                    gapi.Part1PAPIscore = apf.Part1PAPIscore
                    gapi.part2PAPIscore = apf2.part2PAPIscore
                    gapi.part3PAPIscore = apf3.part3PAPIscore
                    gapi.GrandScoreHOD = grandhod
                    gapi.submitted_HOD = True
                    gapi.GrandScoreP = grandp
                    gapi.grade = 'F'
                    gapi.save()
        
    return redirect('/faculty_list')

#principal_faculty_edit

def AppraisalForm_Pscores(request, user):
    if request.session.get('principal', False):
        Staff_ID = request.session['principal']
        dept = PersonalDetail.objects.get(Staff_ID=user)
        if PersonalDetail.objects.filter(Staff_ID=Staff_ID).exists():
            if AppraisalForm.objects.filter(user=user).exists():
                form = AppraisalForm.objects.get(user=user)
                staff = PersonalDetail.objects.get(Staff_ID=Staff_ID)
                context = {"form" : form, 'staff':staff }
                if request.method == "GET":
                    return render(request, 'AppraisalForm/principal_faculty_score.html', context)
                if request.method == "POST":
                    if dept.Department == "Basic Science and Humanities":
                        a7P = request.POST['a7P']
                        b7P = request.POST['b7P']
                        c7P = request.POST['c7P']
                        a9P = request.POST['a9P']
                        b9P = request.POST['b9P']
                        c9P = request.POST['c9P']
                        a8bP = request.POST['a8bP']
                        b8bP = request.POST['b8bP']
                        c8bP = request.POST['c8bP']
                        d8bP = request.POST['d8bP']

                        form.a7P_score = a7P
                        form.b7P_score = b7P
                        form.c7P_Student_Feedback = c7P
                        form.a9P_score = a9P
                        form.b9P_score = b9P
                        form.c9P_score = c9P
                        form.a8BP_score = a8bP
                        form.b8BP_score = b8bP
                        form.c8BP_score = c8bP
                        form.d8BP_score = d8bP
                        form.submitted_Principal = True

                        form.save()
                        return render(request, 'AppraisalForm/principal_faculty_score.html',context)
                        
                    else:
                        a7P = request.POST['a7P']
                        b7P = request.POST['b7P']
                        c7P = request.POST['c7P']
                        a9P = request.POST['a9P']
                        b9P = request.POST['b9P']
                        c9P = request.POST['c9P']
                        a8P = request.POST['a8P']
                        b8P = request.POST['b8P']
                        c8P = request.POST['c8P']

                        form.a7P_score = a7P
                        form.b7P_score = b7P
                        form.c7P_Student_Feedback = c7P
                        form.a9P_score = a9P
                        form.b9P_score = b9P
                        form.c9P_score = c9P
                        form.a8P_score = a8P
                        form.b8P_score = b8P
                        form.c8P_No_of_students_achieved_vertical_progression_under_your_mentorship = c8P
                        form.submitted_Principal = True

                        form.save()
                        return render(request, 'AppraisalForm/principal_faculty_score.html',context)
                
            else:
                return redirect('/faculty_list_P')
        else:
            return redirect('/log-in')
    else:
        return redirect('/log-in')
                        
        

def AppraisalForm2_Pscores(request, user):
    if request.session.get('principal', False):
        Staff_ID = request.session['principal']
        if PersonalDetail.objects.filter(Staff_ID=Staff_ID).exists():
            if AppraisalForm2.objects.filter(user=user).exists():
                form = AppraisalForm2.objects.get(user=user)
                staff = PersonalDetail.objects.get(Staff_ID=Staff_ID)
                context = {"form" : form, 'staff':staff }
                if request.method == "GET":
                    return render(request, 'AppraisalForm/principal_faculty_score2.html', context)
                if request.method == "POST":
                    a10P = request.POST['a10P']
                    b10P = request.POST['b10P']
                    c10P = request.POST['c10P']
                    a11P = request.POST['a11P']
                    b11P = request.POST['b11P']
                    a12P = request.POST['a12P']
                    b12P = request.POST['b12P']

                    form.a10P_score = a10P
                    form.b10P_score = b10P
                    form.c10P_score = c10P
                    form.a11P_score = a11P
                    form.b11P_score = b11P
                    form.a12P_score = a12P
                    form.b12P_score = b12P
                    form.submitted_Principal = True

                    form.save()
                    return render(request, 'AppraisalForm/principal_faculty_score2.html', context)
            else:
                return redirect('/faculty_list_P')
        else:
            return redirect('/log-in')
    else:
        return redirect('/log-in')


def AppraisalForm3_Pscores(request, user):
    if request.session.get('principal', False):
        Staff_ID = request.session['principal']
        if PersonalDetail.objects.filter(Staff_ID=Staff_ID).exists():
            if AppraisalForm3.objects.filter(user=user).exists():
                form = AppraisalForm3.objects.get(user=user)
                staff = PersonalDetail.objects.get(Staff_ID=Staff_ID)
                context = {"form" : form, 'staff':staff }
                if request.method == "GET":
                    return render(request, 'AppraisalForm/principal_faculty_score3.html', context)
                if request.method == "POST":
                    a13P = request.POST['a13P']
                    b13P = request.POST['b13P']
                    c13P = request.POST['c13P']
                    d13P = request.POST['d13P']
                    e13P = request.POST['e13P']
                    f13P = request.POST['f13P']
                    a14P = request.POST['a14P']
                    b14P = request.POST['b14P']
                    c14P = request.POST['c14P']
                    a15P = request.POST['a15P']

                    form.P_a13 = a13P
                    form.P_b13 = b13P
                    form.P_c13 = c13P
                    form.P_d13 = d13P
                    form.P_e13 = e13P
                    form.P_f13 = f13P
                    form.P_a14 = a14P
                    form.P_b14 = b14P
                    form.P_c14 = c14P
                    form.P_a15 = a15P
                    form.submitted_Principal = True

                    form.save()
                    return grandscorecalcP(request,user)
            else:
                return redirect('/faculty_list_P')
        else:
            return redirect('/log-in')
    else:
        return redirect('/log-in')


def grandscorecalcP(request,user):
    staff = request.session['principal']
    if PersonalDetail.objects.filter(Staff_ID=staff).exists():
        if GrandApiScores.objects.filter(user=user).exists():
            pd = PersonalDetail.objects.get(Staff_ID=user)
            apf = AppraisalForm.objects.get(user=user)
            apf2 = AppraisalForm2.objects.get(user=user)
            apf3 = AppraisalForm3.objects.get(user=user)
            gapi = GrandApiScores.objects.get(user=user)
            if int(pd.total_years) <= 5:
                grandp = (((apf.Part1PAPIscore/350)*0.70)+((apf2.part2PAPIscore/170)*0.20)+((apf3.part3PAPIscore/180)*0.10))*100
                
                if grandp >= 70 and grandp <= 100:
                    gapi.Part1PAPIscore = apf.Part1PAPIscore
                    gapi.part2PAPIscore = apf2.part2PAPIscore
                    gapi.part3PAPIscore = apf3.part3PAPIscore
                    gapi.GrandScoreP = grandp
                    gapi.submitted_Principal = True
                    gapi.grade = 'A'
                    gapi.save()
                elif grandp >= 60 and grandp < 70:
                    gapi.Part1PAPIscore = apf.Part1PAPIscore
                    gapi.part2PAPIscore = apf2.part2PAPIscore
                    gapi.part3PAPIscore = apf3.part3PAPIscore
                    gapi.GrandScoreP = grandp
                    gapi.submitted_Principal = True
                    gapi.grade = 'B'
                    gapi.save()
                elif grandp >= 55 and grandp < 60:
                    gapi.Part1PAPIscore = apf.Part1PAPIscore
                    gapi.part2PAPIscore = apf2.part2PAPIscore
                    gapi.part3PAPIscore = apf3.part3PAPIscore
                    gapi.GrandScoreP = grandp
                    gapi.submitted_Principal = True
                    gapi.grade = 'C'
                    gapi.save()
                elif grandp >= 50 and grandp < 55:
                    gapi.Part1PAPIscore = apf.Part1PAPIscore
                    gapi.part2PAPIscore = apf2.part2PAPIscore
                    gapi.part3PAPIscore = apf3.part3PAPIscore
                    gapi.GrandScoreP = grandp
                    gapi.submitted_Principal = True
                    gapi.grade = 'D'
                    gapi.save()
                elif grandp >= 40 and grandp < 50:
                    gapi.Part1PAPIscore = apf.Part1PAPIscore
                    gapi.part2PAPIscore = apf2.part2PAPIscore
                    gapi.part3PAPIscore = apf3.part3PAPIscore
                    gapi.GrandScoreP = grandp
                    gapi.submitted_Principal = True
                    gapi.grade = 'E'
                    gapi.save()
                elif grandp < 40:
                    gapi.Part1PAPIscore = apf.Part1PAPIscore
                    gapi.part2PAPIscore = apf2.part2PAPIscore
                    gapi.part3PAPIscore = apf3.part3PAPIscore
                    gapi.GrandScoreP = grandp
                    gapi.submitted_Principal = True
                    gapi.grade = 'F'
                    gapi.save()
            elif int(pd.total_years) > 5 and int(pd.total_years) < 10:
                grandp = (((apf.Part1PAPIscore/350)*0.60)+((apf2.part2PAPIscore/170)*0.25)+((apf3.part3PAPIscore/180)*0.15))*100

                if grandp >= 70 and grandp <= 100:
                    gapi.Part1PAPIscore = apf.Part1PAPIscore
                    gapi.part2PAPIscore = apf2.part2PAPIscore
                    gapi.part3PAPIscore = apf3.part3PAPIscore
                    gapi.GrandScoreP = grandp
                    gapi.submitted_Principal = True
                    gapi.grade = 'A'
                    gapi.save()
                elif grandp >= 60 and grandp < 70:
                    gapi.Part1PAPIscore = apf.Part1PAPIscore
                    gapi.part2PAPIscore = apf2.part2PAPIscore
                    gapi.part3PAPIscore = apf3.part3PAPIscore
                    gapi.GrandScoreP = grandp
                    gapi.submitted_Principal = True
                    gapi.grade = 'B'
                    gapi.save()
                elif grandp >= 55 and grandp < 60:
                    gapi.Part1PAPIscore = apf.Part1PAPIscore
                    gapi.part2PAPIscore = apf2.part2PAPIscore
                    gapi.part3PAPIscore = apf3.part3PAPIscore
                    gapi.GrandScoreP = grandp
                    gapi.submitted_Principal = True
                    gapi.grade = 'C'
                    gapi.save()
                elif grandp >= 50 and grandp < 55:
                    gapi.Part1PAPIscore = apf.Part1PAPIscore
                    gapi.part2PAPIscore = apf2.part2PAPIscore
                    gapi.part3PAPIscore = apf3.part3PAPIscore
                    gapi.GrandScoreP = grandp
                    gapi.submitted_Principal = True
                    gapi.grade = 'D'
                    gapi.save()
                elif grandp >= 40 and grandp < 50:
                    gapi.Part1PAPIscore = apf.Part1PAPIscore
                    gapi.part2PAPIscore = apf2.part2PAPIscore
                    gapi.part3PAPIscore = apf3.part3PAPIscore
                    gapi.GrandScoreP = grandp
                    gapi.submitted_Principal = True
                    gapi.grade = 'E'
                    gapi.save()
                elif grandp < 40:
                    gapi.Part1PAPIscore = apf.Part1PAPIscore
                    gapi.part2PAPIscore = apf2.part2PAPIscore
                    gapi.part3PAPIscore = apf3.part3PAPIscore
                    gapi.GrandScoreP = grandp
                    gapi.submitted_Principal = True
                    gapi.grade = 'F'
                    gapi.save()
            elif int(pd.total_years) >= 10:
                grandp = (((apf.Part1PAPIscore/350)*0.50)+((apf2.part2PAPIscore/170)*0.30)+((apf3.part3PAPIscore/180)*0.20))*100

                if grandp >= 70 and grandp <= 100:
                    gapi.Part1PAPIscore = apf.Part1PAPIscore
                    gapi.part2PAPIscore = apf2.part2PAPIscore
                    gapi.part3PAPIscore = apf3.part3PAPIscore
                    gapi.GrandScoreP = grandp
                    gapi.submitted_Principal = True
                    gapi.grade = 'A'
                    gapi.save()
                elif grandp >= 60 and grandp < 70:
                    gapi.Part1PAPIscore = apf.Part1PAPIscore
                    gapi.part2PAPIscore = apf2.part2PAPIscore
                    gapi.part3PAPIscore = apf3.part3PAPIscore
                    gapi.GrandScoreP = grandp
                    gapi.submitted_Principal = True
                    gapi.grade = 'B'
                    gapi.save()
                elif grandp >= 55 and grandp < 60:
                    gapi.Part1PAPIscore = apf.Part1PAPIscore
                    gapi.part2PAPIscore = apf2.part2PAPIscore
                    gapi.part3PAPIscore = apf3.part3PAPIscore
                    gapi.GrandScoreP = grandp
                    gapi.submitted_Principal = True
                    gapi.grade = 'C'
                    gapi.save()
                elif grandp >= 50 and grandp < 55:
                    gapi.Part1PAPIscore = apf.Part1PAPIscore
                    gapi.part2PAPIscore = apf2.part2PAPIscore
                    gapi.part3PAPIscore = apf3.part3PAPIscore
                    gapi.GrandScoreP = grandp
                    gapi.submitted_Principal = True
                    gapi.grade = 'D'
                    gapi.save()
                elif grandp >= 40 and grandp < 50:
                    gapi.Part1PAPIscore = apf.Part1PAPIscore
                    gapi.part2PAPIscore = apf2.part2PAPIscore
                    gapi.part3PAPIscore = apf3.part3PAPIscore
                    gapi.GrandScoreP = grandp
                    gapi.submitted_Principal = True
                    gapi.grade = 'E'
                    gapi.save()
                elif grandp < 40:
                    gapi.Part1PAPIscore = apf.Part1PAPIscore
                    gapi.part2PAPIscore = apf2.part2PAPIscore
                    gapi.part3PAPIscore = apf3.part3PAPIscore
                    gapi.GrandScoreP = grandp
                    gapi.submitted_Principal = True
                    gapi.grade = 'F'
                    gapi.save()
        
    return redirect('/faculty_list_P')
