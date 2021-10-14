from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from faculty.models import *

# Create your models here.

class AppraisalForm(models.Model):

    CATEGORY = (
			('Humanities', 'Humanities'),
            ('Physics', 'Physics'),
            ('Chemistry', 'Chemistry'),
            ('Mathematics', 'Mathematics'),
			('Mechanical Engineering', 'Mechanical Engineering'),
            ('Civil Engineering', 'Civil Engineering'),
            ('Computer Science and Engineering', 'Computer Science and Engineering'),
            ('Information Science and Engineering', 'Information Science and Engineering'),
            ('Electronics and Communication Engineering', 'Electronics and Communication Engineering'),
            ('Master of Business Administration', 'Master of Business Administration'),
            ('Master of Computer Applications', 'Master of Computer Applications'),
			) 

    ROLES = (
            ('Assistant Professor', 'Assistant Professor'),
            ('Associate Professor', 'Associate Professor'),
            ('Professor', 'Professor'),
    )


    user = models.CharField(max_length=10, null=True)
    department = models.CharField(max_length=200, null=True, choices=CATEGORY)
    designation = models.CharField(max_length=200, null=True, choices=ROLES)
    name = models.CharField(max_length=200, null=True)
    whether_HOD = models.BooleanField(default=False)
    submitted_Faculty = models.BooleanField(default=False)
    submitted_HOD = models.BooleanField(default=False)
    submitted_Principal = models.BooleanField(default=False)
    academic_year = models.IntegerField(null=True)

    #part1

    No_of_students1 = models.IntegerField(null=True)
    Percentage_of_pass1 = models.IntegerField(null=True)
    Percent_over_601 = models.IntegerField(null=True)
    Sub_code1 = models.CharField(max_length=200, null=True)

    No_of_students2 = models.IntegerField(null=True, default=0)
    Percentage_of_pass2 = models.IntegerField(null=True, default=0)
    Percent_over_602 = models.IntegerField(null=True, default=0)
    Sub_code2 = models.CharField(max_length=200, null=True, default=0)

    No_of_students3 = models.IntegerField(null=True, default=0)
    Percentage_of_pass3 = models.IntegerField(null=True, default=0)  
    Percent_over_603 = models.IntegerField(null=True, default=0)
    Sub_code3 = models.CharField(max_length=200, null=True, default=0)

    No_of_students4 = models.IntegerField(null=True, default=0)
    Percentage_of_pass4 = models.IntegerField(null=True, default=0)
    Percent_over_604 = models.IntegerField(null=True, default=0)
    Sub_code4 = models.CharField(max_length=200, null=True, default=0)

    No_of_students5 = models.IntegerField(null=True)
    Percentage_of_pass5 = models.IntegerField(null=True)
    Percent_over_605 = models.IntegerField(null=True)
    Sub_code5 = models.CharField(max_length=200, null=True)

    No_of_students6 = models.IntegerField(null=True, default=0)
    Percentage_of_pass6 = models.IntegerField(null=True, default=0)
    Percent_over_606 = models.IntegerField(null=True, default=0)
    Sub_code6 = models.CharField(max_length=200, null=True, default=0)

    No_of_students7 = models.IntegerField(null=True, default=0)
    Percentage_of_pass7 = models.IntegerField(null=True, default=0)  
    Percent_over_607 = models.IntegerField(null=True, default=0)
    Sub_code7 = models.CharField(max_length=200, null=True, default=0)

    No_of_students8 = models.IntegerField(null=True, default=0)
    Percentage_of_pass8 = models.IntegerField(null=True, default=0)
    Percent_over_608 = models.IntegerField(null=True, default=0)
    Sub_code8 = models.CharField(max_length=200, null=True, default=0)

    Percentage_of_pass1_hod = models.IntegerField(null=True)
    Percent_over_601_hod = models.IntegerField(null=True)

    Percentage_of_pass2_hod = models.IntegerField(null=True, default=0)
    Percent_over_602_hod = models.IntegerField(null=True, default=0)

    Percentage_of_pass3_hod = models.IntegerField(null=True, default=0)  
    Percent_over_603_hod = models.IntegerField(null=True, default=0)

    Percentage_of_pass4_hod = models.IntegerField(null=True, default=0)
    Percent_over_604_hod = models.IntegerField(null=True, default=0)

    Percentage_of_pass5_hod = models.IntegerField(null=True)
    Percent_over_605_hod = models.IntegerField(null=True)

    Percentage_of_pass6_hod = models.IntegerField(null=True, default=0)
    Percent_over_606_hod = models.IntegerField(null=True, default=0)

    Percentage_of_pass7_hod = models.IntegerField(null=True, default=0)  
    Percent_over_607_hod = models.IntegerField(null=True, default=0)

    Percentage_of_pass8_hod = models.IntegerField(null=True, default=0)
    Percent_over_608_hod = models.IntegerField(null=True, default=0)

    a7_Sub_Code_of_theory_Subjects_taught_and_No_of_Students_score = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(30), MinValueValidator(0)])
    percent = models.FileField(upload_to='passpercents', null=True)
    a7HOD_score = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(30), MinValueValidator(0)])
    a7P_score = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(30), MinValueValidator(0)])

    b7_Percentage_of_Students_scoring_gt_60_score = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(40), MinValueValidator(0)])
    b7HOD_score = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(40), MinValueValidator(0)])
    b7P_score = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(40), MinValueValidator(0)])
    c7_Student_Feedback = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(40), MinValueValidator(0)])
    c7HOD_Student_Feedback = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(40), MinValueValidator(0)])
    c7P_Student_Feedback = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(40), MinValueValidator(0)])
    a9_No_of_conferences_or_workshops_or_Seminars_or_training_programs_or_etc_FDPs_attended_score = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(45), MinValueValidator(0)])
    a9file = models.FileField(upload_to='part1', null=True) 
    a9HOD_score = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(45), MinValueValidator(0)]) 
    a9P_score = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(45), MinValueValidator(0)]) 
    b9_Use_of_ICT_in_TLP_score = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(35), MinValueValidator(0)])
    b9HOD_score = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(35), MinValueValidator(0)])
    b9P_score = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(35), MinValueValidator(0)])
    c9_No_of_conferences_or_workshops_or_Seminars_or_training_or_programs_or_etc_or_FDPs_conducted_or_coordinated_score = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(30), MinValueValidator(0)])
    c9file = models.FileField(upload_to='part1', null=True)
    c9HOD_score = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(30), MinValueValidator(0)])
    c9P_score = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(30), MinValueValidator(0)])

    def avg_of_passpercent_hod(self):

            if self.Percentage_of_pass2_hod == 0 and self.Percentage_of_pass3_hod == 0 and self.Percentage_of_pass4_hod == 0 and self.Percentage_of_pass5_hod == 0 and self.Percentage_of_pass6_hod == 0 and self.Percentage_of_pass7_hod == 0 and self.Percentage_of_pass8_hod == 0:
                p1 = ((self.Percentage_of_pass1_hod*0.01)*30)
                self.a7HOD_score = p1 
                self.a7P_score = self.a7HOD_score
            elif self.Percentage_of_pass3_hod == 0 and self.Percentage_of_pass4_hod == 0 and self.Percentage_of_pass5_hod == 0 and self.Percentage_of_pass6_hod == 0 and self.Percentage_of_pass7_hod == 0 and self.Percentage_of_pass8_hod == 0:
                p1 = ((self.Percentage_of_pass1_hod*0.01)*30)
                p2 = ((self.Percentage_of_pass2_hod*0.01)*30)
                self.a7HOD_score = (p1 + p2) / 2
                self.a7P_score = self.a7HOD_score
            elif self.Percentage_of_pass4_hod == 0 and self.Percentage_of_pass5_hod == 0 and self.Percentage_of_pass6_hod == 0 and self.Percentage_of_pass7_hod == 0 and self.Percentage_of_pass8_hod == 0:
                p1 = ((self.Percentage_of_pass1_hod*0.01)*30)
                p2 = ((self.Percentage_of_pass2_hod*0.01)*30) 
                p3 = ((self.Percentage_of_pass3_hod*0.01)*30)
                self.a7HOD_score = (p1 + p2 + p3) / 3
                self.a7P_score = self.a7HOD_score
            elif self.Percentage_of_pass5_hod == 0 and self.Percentage_of_pass6_hod == 0 and self.Percentage_of_pass7_hod == 0 and self.Percentage_of_pass8_hod == 0:
                p1 = ((self.Percentage_of_pass1_hod*0.01)*30)
                p2 = ((self.Percentage_of_pass2_hod*0.01)*30) 
                p3 = ((self.Percentage_of_pass3_hod*0.01)*30) 
                p4 = ((self.Percentage_of_pass4_hod*0.01)*30)
                self.a7HOD_score = (p1 + p2 + p3 + p4) / 4
                self.a7P_score = self.a7HOD_score
            elif self.Percentage_of_pass6_hod == 0 and self.Percentage_of_pass7_hod == 0 and self.Percentage_of_pass8_hod == 0:
                p1 = ((self.Percentage_of_pass1_hod*0.01)*30)
                p2 = ((self.Percentage_of_pass2_hod*0.01)*30) 
                p3 = ((self.Percentage_of_pass3_hod*0.01)*30) 
                p4 = ((self.Percentage_of_pass4_hod*0.01)*30)
                p5 = ((self.Percentage_of_pass5_hod*0.01)*30)
                self.a7HOD_score = (p1 + p2 + p3 + p4 + p5) / 5
                self.a7P_score = self.a7HOD_score
            elif self.Percentage_of_pass7_hod == 0 and self.Percentage_of_pass8_hod == 0:
                p1 = ((self.Percentage_of_pass1_hod*0.01)*30)
                p2 = ((self.Percentage_of_pass2_hod*0.01)*30) 
                p3 = ((self.Percentage_of_pass3_hod*0.01)*30) 
                p4 = ((self.Percentage_of_pass4_hod*0.01)*30)
                p5 = ((self.Percentage_of_pass5_hod*0.01)*30)
                p6 = ((self.Percentage_of_pass6_hod*0.01)*30)
                self.a7HOD_score = (p1 + p2 + p3 + p4 + p5 + p6) / 6
                self.a7P_score = self.a7HOD_score
            elif self.Percentage_of_pass8_hod == 0:
                p1 = ((self.Percentage_of_pass1_hod*0.01)*30)
                p2 = ((self.Percentage_of_pass2_hod*0.01)*30) 
                p3 = ((self.Percentage_of_pass3_hod*0.01)*30) 
                p4 = ((self.Percentage_of_pass4_hod*0.01)*30)
                p5 = ((self.Percentage_of_pass5_hod*0.01)*30)
                p6 = ((self.Percentage_of_pass6_hod*0.01)*30)
                p7 = ((self.Percentage_of_pass7_hod*0.01)*30)
                self.a7HOD_score = (p1 + p2 + p3 + p4 + p5 + p6 + p7) / 7
                self.a7P_score = self.a7HOD_score
            else:
                p1 = ((self.Percentage_of_pass1_hod*0.01)*30)
                p2 = ((self.Percentage_of_pass2_hod*0.01)*30) 
                p3 = ((self.Percentage_of_pass3_hod*0.01)*30) 
                p4 = ((self.Percentage_of_pass4_hod*0.01)*30)
                p5 = ((self.Percentage_of_pass5_hod*0.01)*30)
                p6 = ((self.Percentage_of_pass6_hod*0.01)*30)
                p7 = ((self.Percentage_of_pass7_hod*0.01)*30)
                p8 = ((self.Percentage_of_pass8_hod*0.01)*30)
                self.a7HOD_score = (p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8) / 8
                self.a7P_score = self.a7HOD_score
            return self.a7HOD_score,self.a7P_score

    def avg_of_passpercent_over60_hod(self):
            if self.Percent_over_602_hod == 0 and self.Percent_over_603_hod == 0 and self.Percent_over_604_hod == 0 and self.Percent_over_605_hod == 0 and self.Percent_over_606_hod == 0 and self.Percent_over_607_hod == 0 and self.Percent_over_608_hod == 0:
                p601 = ((self.Percent_over_601_hod/self.Percentage_of_pass1_hod)*40)
                self.b7HOD_score = p601
                self.b7P_score = self.b7HOD_score 
            elif self.Percent_over_603_hod == 0 and self.Percent_over_604_hod == 0 and self.Percent_over_605_hod == 0 and self.Percent_over_606_hod == 0 and self.Percent_over_607_hod == 0 and self.Percent_over_608_hod == 0:
                p601 = ((self.Percent_over_601_hod/self.Percentage_of_pass1_hod)*40)
                p602 = ((self.Percent_over_602_hod/self.Percentage_of_pass2_hod)*40)
                self.b7HOD_score = (p601 + p602) / 2
                self.b7P_score = self.b7HOD_score
            elif self.Percent_over_604_hod == 0 and self.Percent_over_605_hod == 0 and self.Percent_over_606_hod == 0 and self.Percent_over_607_hod == 0 and self.Percent_over_608_hod == 0:
                p601 = ((self.Percent_over_601_hod/self.Percentage_of_pass1_hod)*40)
                p602 = ((self.Percent_over_602_hod/self.Percentage_of_pass2_hod)*40) 
                p603 = ((self.Percent_over_603_hod/self.Percentage_of_pass3_hod)*40)
                self.b7HOD_score = (p601 + p602 + p603) / 3
                self.b7P_score = self.b7HOD_score
            elif self.Percent_over_605_hod == 0 and self.Percent_over_606_hod == 0 and self.Percent_over_607_hod == 0 and self.Percent_over_608_hod == 0:
                p601 = ((self.Percent_over_601_hod/self.Percentage_of_pass1_hod)*40)
                p602 = ((self.Percent_over_602_hod/self.Percentage_of_pass2_hod)*40) 
                p603 = ((self.Percent_over_603_hod/self.Percentage_of_pass3_hod)*40) 
                p604 = ((self.Percent_over_604_hod/self.Percentage_of_pass4_hod)*40)
                self.b7HOD_score = (p601 + p602 + p603 + p604) / 4
                self.b7P_score = self.b7HOD_score 
            elif self.Percent_over_606_hod == 0 and self.Percent_over_607_hod == 0 and self.Percent_over_608_hod == 0:
                p601 = ((self.Percent_over_601_hod/self.Percentage_of_pass1_hod)*40)
                p602 = ((self.Percent_over_602_hod/self.Percentage_of_pass2_hod)*40) 
                p603 = ((self.Percent_over_603_hod/self.Percentage_of_pass3_hod)*40) 
                p604 = ((self.Percent_over_604_hod/self.Percentage_of_pass4_hod)*40)
                p605 = ((self.Percent_over_605_hod/self.Percentage_of_pass5_hod)*40)
                self.b7HOD_score = (p601 + p602 + p603 + p604 + p605) / 5
                self.b7P_score = self.b7HOD_score
            elif self.Percent_over_607_hod == 0 and self.Percent_over_608_hod == 0:
                p601 = ((self.Percent_over_601_hod/self.Percentage_of_pass1_hod)*40)
                p602 = ((self.Percent_over_602_hod/self.Percentage_of_pass2_hod)*40) 
                p603 = ((self.Percent_over_603_hod/self.Percentage_of_pass3_hod)*40) 
                p604 = ((self.Percent_over_604_hod/self.Percentage_of_pass4_hod)*40)
                p605 = ((self.Percent_over_605_hod/self.Percentage_of_pass5_hod)*40)
                p606 = ((self.Percent_over_606_hod/self.Percentage_of_pass6_hod)*40)
                self.b7HOD_score = (p601 + p602 + p603 + p604 + p605  + p606) / 6
                self.b7P_score = self.b7HOD_score
            elif self.Percent_over_607_hod == 0:
                p601 = ((self.Percent_over_601_hod/self.Percentage_of_pass1_hod)*40)
                p602 = ((self.Percent_over_602_hod/self.Percentage_of_pass2_hod)*40) 
                p603 = ((self.Percent_over_603_hod/self.Percentage_of_pass3_hod)*40) 
                p604 = ((self.Percent_over_604_hod/self.Percentage_of_pass4_hod)*40)
                p605 = ((self.Percent_over_605_hod/self.Percentage_of_pass5_hod)*40)
                p606 = ((self.Percent_over_606_hod/self.Percentage_of_pass6_hod)*40)
                p607 = ((self.Percent_over_607_hod/self.Percentage_of_pass7_hod)*40)
                self.b7HOD_score = (p601 + p602 + p603 + p604 + p605  + p606 + p607) / 7
                self.b7P_score = self.b7HOD_score
            else:
                p601 = ((self.Percent_over_601_hod/self.Percentage_of_pass1_hod)*40)
                p602 = ((self.Percent_over_602_hod/self.Percentage_of_pass2_hod)*40) 
                p603 = ((self.Percent_over_603_hod/self.Percentage_of_pass3_hod)*40) 
                p604 = ((self.Percent_over_604_hod/self.Percentage_of_pass4_hod)*40)
                p605 = ((self.Percent_over_605_hod/self.Percentage_of_pass5_hod)*40)
                p606 = ((self.Percent_over_606_hod/self.Percentage_of_pass6_hod)*40)
                p607 = ((self.Percent_over_607_hod/self.Percentage_of_pass7_hod)*40)
                p608 = ((self.Percent_over_608_hod/self.Percentage_of_pass8_hod)*40)
                self.b7HOD_score = (p601 + p602 + p603 + p604 + p605  + p606 + p607 + p608) / 8
                self.b7P_score = self.b7HOD_score
            return self.b7HOD_score,self.b7P_score  

    def avg_of_passpercent(self):
            if self.Percentage_of_pass2 == 0 and self.Percentage_of_pass3 == 0 and self.Percentage_of_pass4 == 0 and self.Percentage_of_pass5 == 0 and self.Percentage_of_pass6 == 0 and self.Percentage_of_pass7 == 0 and self.Percentage_of_pass8 == 0:
                p1 = ((self.Percentage_of_pass1*0.01)*30)
                self.a7_Sub_Code_of_theory_Subjects_taught_and_No_of_Students_score = p1 
            elif self.Percentage_of_pass3 == 0 and self.Percentage_of_pass4 == 0 and self.Percentage_of_pass5 == 0 and self.Percentage_of_pass6 == 0 and self.Percentage_of_pass7 == 0 and self.Percentage_of_pass8 == 0:
                p1 = ((self.Percentage_of_pass1*0.01)*30)
                p2 = ((self.Percentage_of_pass2*0.01)*30)
                self.a7_Sub_Code_of_theory_Subjects_taught_and_No_of_Students_score = (p1 + p2) / 2
            elif self.Percentage_of_pass4 == 0 and self.Percentage_of_pass5 == 0 and self.Percentage_of_pass6 == 0 and self.Percentage_of_pass7 == 0 and self.Percentage_of_pass8 == 0:
                p1 = ((self.Percentage_of_pass1*0.01)*30)
                p2 = ((self.Percentage_of_pass2*0.01)*30) 
                p3 = ((self.Percentage_of_pass3*0.01)*30)
                self.a7_Sub_Code_of_theory_Subjects_taught_and_No_of_Students_score = (p1 + p2 + p3) / 3
            elif self.Percentage_of_pass5 == 0 and self.Percentage_of_pass6 == 0 and self.Percentage_of_pass7 == 0 and self.Percentage_of_pass8 == 0:
                p1 = ((self.Percentage_of_pass1*0.01)*30)
                p2 = ((self.Percentage_of_pass2*0.01)*30) 
                p3 = ((self.Percentage_of_pass3*0.01)*30) 
                p4 = ((self.Percentage_of_pass4*0.01)*30)
                self.a7_Sub_Code_of_theory_Subjects_taught_and_No_of_Students_score = (p1 + p2 + p3 + p4) / 4
            elif self.Percentage_of_pass6 == 0 and self.Percentage_of_pass7 == 0 and self.Percentage_of_pass8 == 0:
                p1 = ((self.Percentage_of_pass1*0.01)*30)
                p2 = ((self.Percentage_of_pass2*0.01)*30) 
                p3 = ((self.Percentage_of_pass3*0.01)*30) 
                p4 = ((self.Percentage_of_pass4*0.01)*30)
                p5 = ((self.Percentage_of_pass5*0.01)*30)
                self.a7_Sub_Code_of_theory_Subjects_taught_and_No_of_Students_score = (p1 + p2 + p3 + p4 + p5) / 5
            elif self.Percentage_of_pass7 == 0 and self.Percentage_of_pass8 == 0:
                p1 = ((self.Percentage_of_pass1*0.01)*30)
                p2 = ((self.Percentage_of_pass2*0.01)*30) 
                p3 = ((self.Percentage_of_pass3*0.01)*30) 
                p4 = ((self.Percentage_of_pass4*0.01)*30)
                p5 = ((self.Percentage_of_pass5*0.01)*30)
                p6 = ((self.Percentage_of_pass6*0.01)*30)
                self.a7_Sub_Code_of_theory_Subjects_taught_and_No_of_Students_score = (p1 + p2 + p3 + p4 + p5 + p6) / 6
            elif self.Percentage_of_pass8 == 0:
                p1 = ((self.Percentage_of_pass1*0.01)*30)
                p2 = ((self.Percentage_of_pass2*0.01)*30) 
                p3 = ((self.Percentage_of_pass3*0.01)*30) 
                p4 = ((self.Percentage_of_pass4*0.01)*30)
                p5 = ((self.Percentage_of_pass5*0.01)*30)
                p6 = ((self.Percentage_of_pass6*0.01)*30)
                p7 = ((self.Percentage_of_pass7*0.01)*30)
                self.a7_Sub_Code_of_theory_Subjects_taught_and_No_of_Students_score = (p1 + p2 + p3 + p4 + p5 + p6 + p7) / 7
            else:
                p1 = ((self.Percentage_of_pass1*0.01)*30)
                p2 = ((self.Percentage_of_pass2*0.01)*30) 
                p3 = ((self.Percentage_of_pass3*0.01)*30) 
                p4 = ((self.Percentage_of_pass4*0.01)*30)
                p5 = ((self.Percentage_of_pass5*0.01)*30)
                p6 = ((self.Percentage_of_pass6*0.01)*30)
                p7 = ((self.Percentage_of_pass7*0.01)*30)
                p8 = ((self.Percentage_of_pass8*0.01)*30)
                self.a7_Sub_Code_of_theory_Subjects_taught_and_No_of_Students_score = (p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8) / 8
            return self.a7_Sub_Code_of_theory_Subjects_taught_and_No_of_Students_score

    def avg_of_passpercent_over60(self):
            if self.Percent_over_602 == 0 and self.Percent_over_603 == 0 and self.Percent_over_604 == 0 and self.Percent_over_605 == 0 and self.Percent_over_606 == 0 and self.Percent_over_607 == 0 and self.Percent_over_608 == 0:
                p601 = ((self.Percent_over_601/self.Percentage_of_pass1)*40)
                self.b7_Percentage_of_Students_scoring_gt_60_score = p601 
            elif self.Percent_over_603 == 0 and self.Percent_over_604 == 0 and self.Percent_over_605 == 0 and self.Percent_over_606 == 0 and self.Percent_over_607 == 0 and self.Percent_over_608 == 0:
                p601 = ((self.Percent_over_601/self.Percentage_of_pass1)*40)
                p602 = ((self.Percent_over_602/self.Percentage_of_pass2)*40)
                self.b7_Percentage_of_Students_scoring_gt_60_score = (p601 + p602) / 2
            elif self.Percent_over_604 == 0 and self.Percent_over_605 == 0 and self.Percent_over_606 == 0 and self.Percent_over_607 == 0 and self.Percent_over_608 == 0:
                p601 = ((self.Percent_over_601/self.Percentage_of_pass1)*40)
                p602 = ((self.Percent_over_602/self.Percentage_of_pass2)*40) 
                p603 = ((self.Percent_over_603/self.Percentage_of_pass3)*40)
                self.b7_Percentage_of_Students_scoring_gt_60_score = (p601 + p602 + p603) / 3
            elif self.Percent_over_605 == 0 and self.Percent_over_606 == 0 and self.Percent_over_607 == 0 and self.Percent_over_608 == 0:
                p601 = ((self.Percent_over_601/self.Percentage_of_pass1)*40)
                p602 = ((self.Percent_over_602/self.Percentage_of_pass2)*40) 
                p603 = ((self.Percent_over_603/self.Percentage_of_pass3)*40) 
                p604 = ((self.Percent_over_604/self.Percentage_of_pass4)*40)
                self.b7_Percentage_of_Students_scoring_gt_60_score = (p601 + p602 + p603 + p604) / 4 
            elif self.Percent_over_606 == 0 and self.Percent_over_607 == 0 and self.Percent_over_608 == 0:
                p601 = ((self.Percent_over_601/self.Percentage_of_pass1)*40)
                p602 = ((self.Percent_over_602/self.Percentage_of_pass2)*40) 
                p603 = ((self.Percent_over_603/self.Percentage_of_pass3)*40) 
                p604 = ((self.Percent_over_604/self.Percentage_of_pass4)*40)
                p605 = ((self.Percent_over_605/self.Percentage_of_pass5)*40)
                self.b7_Percentage_of_Students_scoring_gt_60_score = (p601 + p602 + p603 + p604 + p605) / 5
            elif self.Percent_over_607 == 0 and self.Percent_over_608 == 0:
                p601 = ((self.Percent_over_601/self.Percentage_of_pass1)*40)
                p602 = ((self.Percent_over_602/self.Percentage_of_pass2)*40) 
                p603 = ((self.Percent_over_603/self.Percentage_of_pass3)*40) 
                p604 = ((self.Percent_over_604/self.Percentage_of_pass4)*40)
                p605 = ((self.Percent_over_605/self.Percentage_of_pass5)*40)
                p606 = ((self.Percent_over_606/self.Percentage_of_pass6)*40)
                self.b7_Percentage_of_Students_scoring_gt_60_score = (p601 + p602 + p603 + p604 + p605  + p606) / 6
            elif self.Percent_over_607 == 0:
                p601 = ((self.Percent_over_601/self.Percentage_of_pass1)*40)
                p602 = ((self.Percent_over_602/self.Percentage_of_pass2)*40) 
                p603 = ((self.Percent_over_603/self.Percentage_of_pass3)*40) 
                p604 = ((self.Percent_over_604/self.Percentage_of_pass4)*40)
                p605 = ((self.Percent_over_605/self.Percentage_of_pass5)*40)
                p606 = ((self.Percent_over_606/self.Percentage_of_pass6)*40)
                p607 = ((self.Percent_over_607/self.Percentage_of_pass7)*40)
                self.b7_Percentage_of_Students_scoring_gt_60_score = (p601 + p602 + p603 + p604 + p605  + p606 + p607) / 7
            else:
                p601 = ((self.Percent_over_601/self.Percentage_of_pass1)*40)
                p602 = ((self.Percent_over_602/self.Percentage_of_pass2)*40) 
                p603 = ((self.Percent_over_603/self.Percentage_of_pass3)*40) 
                p604 = ((self.Percent_over_604/self.Percentage_of_pass4)*40)
                p605 = ((self.Percent_over_605/self.Percentage_of_pass5)*40)
                p606 = ((self.Percent_over_606/self.Percentage_of_pass6)*40)
                p607 = ((self.Percent_over_607/self.Percentage_of_pass7)*40)
                p608 = ((self.Percent_over_608/self.Percentage_of_pass8)*40)
                self.b7_Percentage_of_Students_scoring_gt_60_score = (p601 + p602 + p603 + p604 + p605  + p606 + p607 + p608) / 8
            return self.b7_Percentage_of_Students_scoring_gt_60_score 
    #NO BSH

    a8_No_of_projects_guided_score = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(40), MinValueValidator(0)])  
    a8HOD_score = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(40), MinValueValidator(0)]) 
    a8P_score = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(40), MinValueValidator(0)]) 
    b8_No_of_Best_Projects_Awarded_OR_Student_Project_Exhibited_in_competitions_or_Symposiums_OR_Funded_by_external_agency_OR_Student_Project_Paper_Publication_s_score = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(60), MinValueValidator(0)])
    b8file = models.FileField(upload_to='nobsh', null=True)
    b8HOD_score = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(60), MinValueValidator(0)])
    b8P_score = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(60), MinValueValidator(0)])
    c8_No_of_students_achieved_vertical_progression_under_your_mentorship = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(30), MinValueValidator(0)])
    c8file = models.FileField(upload_to='nobsh', null=True)
    c8HOD_No_of_students_achieved_vertical_progression_under_your_mentorship = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(30), MinValueValidator(0)])
    c8P_No_of_students_achieved_vertical_progression_under_your_mentorship = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(30), MinValueValidator(0)])

    #ONLY BSH

    a8B_No_of_Topper_in_1st_year_of_study_under_your_mentorship_score = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(30), MinValueValidator(0)])
    a8bfile = models.FileField(upload_to='bsh', null=True)
    a8BHOD_score = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(30), MinValueValidator(0)])
    a8BP_score = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(30), MinValueValidator(0)])
    b8B_No_of_students_achieved_vertical_progression_to_2nd_Year_under_your_mentorship_score = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(40), MinValueValidator(0)])
    b8bfile = models.FileField(upload_to='bsh', null=True)
    b8BHOD_score = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(40), MinValueValidator(0)])
    b8BP_score = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(40), MinValueValidator(0)])
    c8B_No_of_FCD_in_1st_year_of_study_under_your_mentorship_score = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(50), MinValueValidator(0)])
    c8bfile = models.FileField(upload_to='bsh', null=True)
    c8BHOD_score = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(50), MinValueValidator(0)])
    c8BP_score = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(50), MinValueValidator(0)])
    d8B_No_of_UG_or_PG_projects_Co_guided_score = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(10), MinValueValidator(0)])
    d8bfile = models.FileField(upload_to='bsh', null=True)
    d8BHOD_score = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(10), MinValueValidator(0)])
    d8BP_score = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(10), MinValueValidator(0)])
    Part1APIscore = models.BigIntegerField(default=0,null=True)
    Part1HODAPIscore = models.BigIntegerField(default=0,null=True)
    Part1PAPIscore = models.BigIntegerField(default=0,null=True)

    def __str__(self):
        return self.user

    def save(self,*args, **kwargs):

        self.avg_of_passpercent()
        self.avg_of_passpercent_over60()
        self.avg_of_passpercent_hod()
        self.avg_of_passpercent_over60_hod()

        self.Part1APIscore = (int(self.a7_Sub_Code_of_theory_Subjects_taught_and_No_of_Students_score) + int(self.b7_Percentage_of_Students_scoring_gt_60_score) + int(self.c7_Student_Feedback) + 
                    int(self.a9_No_of_conferences_or_workshops_or_Seminars_or_training_programs_or_etc_FDPs_attended_score) + int(self.b9_Use_of_ICT_in_TLP_score) + 
                    int(self.c9_No_of_conferences_or_workshops_or_Seminars_or_training_or_programs_or_etc_or_FDPs_conducted_or_coordinated_score) + int(self.a8_No_of_projects_guided_score) + 
                    int(self.b8_No_of_Best_Projects_Awarded_OR_Student_Project_Exhibited_in_competitions_or_Symposiums_OR_Funded_by_external_agency_OR_Student_Project_Paper_Publication_s_score) + 
                    int(self.c8_No_of_students_achieved_vertical_progression_under_your_mentorship) + int(self.a8B_No_of_Topper_in_1st_year_of_study_under_your_mentorship_score) + 
                    int(self.b8B_No_of_students_achieved_vertical_progression_to_2nd_Year_under_your_mentorship_score) + 
                    int(self.c8B_No_of_FCD_in_1st_year_of_study_under_your_mentorship_score) + int(self.d8B_No_of_UG_or_PG_projects_Co_guided_score))

        self.Part1HODAPIscore = (int(self.a7HOD_score) + int(self.b7HOD_score) + int(self.c7HOD_Student_Feedback) + int(self.a9HOD_score) + int(self.b9HOD_score) + int(self.c9HOD_score) + 
                        int(self.a8HOD_score) + int(self.b8HOD_score) + int(self.c8HOD_No_of_students_achieved_vertical_progression_under_your_mentorship) +
                        int(self.a8BHOD_score) + int(self.b8BHOD_score) + int(self.c8BHOD_score) + int(self.d8BHOD_score)) 
        self.Part1PAPIscore = (int(self.a7P_score) + int(self.b7P_score) + int(self.c7P_Student_Feedback) + int(self.a9P_score) + int(self.b9P_score) + int(self.c9P_score) +
                       int(self.a8P_score) + int(self.b8P_score) + int(self.c8P_No_of_students_achieved_vertical_progression_under_your_mentorship) + 
                       int(self.a8BP_score) + int(self.b8BP_score) + int(self.c8BP_score) + int(self.d8BP_score))
        
        super(AppraisalForm, self).save(*args, **kwargs)

    #part2


class AppraisalForm2(models.Model):

    CATEGORY = (
			('Basic Science and Humanities', 'Basic Science and Humanities'),
			('Mechanical Engineering', 'Mechanical Engineering'),
            ('Civil Engineering', 'Civil Engineering'),
            ('Computer Science and Engineering', 'Computer Science and Engineering'),
            ('Information Science and Engineering', 'Information Science and Engineering'),
            ('Electronics and Communication Engineering', 'Electronics and Communication Engineering'),
            ('Master of Business Administration', 'Master of Business Administration'),
            ('Master of Computer Applications', 'Master of Computer Applications'),
			) 

    ROLES = (
            ('Assistant Professor', 'Assistant Professor'),
            ('Associate Professor', 'Associate Professor'),
            ('Professor', 'Professor'),
    )

    user = models.CharField(max_length=10, null=True)
    department = models.CharField(max_length=200, null=True, choices=CATEGORY)
    designation = models.CharField(max_length=200, null=True, choices=ROLES)
    name = models.CharField(max_length=200, null=True)
    whether_HOD = models.BooleanField(default=False)
    submitted_Faculty = models.BooleanField(default=False)
    submitted_HOD = models.BooleanField(default=False)
    submitted_Principal = models.BooleanField(default=False)
    academic_year = models.IntegerField(null=True)
    
    a10_No_of_papers_published_in_journals_score = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(20), MinValueValidator(0)])
    a10file = models.FileField(upload_to='part2', null=True)     
    a10HOD_score = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(20), MinValueValidator(0)])
    a10P_score = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(20), MinValueValidator(0)])   
    b10_No_of_papers_presented_in_conferences_score = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(20), MinValueValidator(0)])
    b10file = models.FileField(upload_to='part2', null=True) 
    b10HOD_score = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(20), MinValueValidator(0)])
    b10P_score = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(20), MinValueValidator(0)])   
    c10_No_of_papers_indexed_in_In_Scopus_or_Web_of_Science_or_UGC_care_list_OR_No_of_book_chapters_authored_OR_No_of_Books_Authored_score = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(40), MinValueValidator(0)])
    c10file = models.FileField(upload_to='part2', null=True) 
    c10HOD_score = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(40), MinValueValidator(0)])
    c10P_score = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(40), MinValueValidator(0)]) 
    a11_No_of_Research_Project_proposals_submitted_score = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(20), MinValueValidator(0)])
    a11file = models.FileField(upload_to='part2', null=True) 
    a11HOD_score = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(20), MinValueValidator(0)])
    a11P_score = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(20), MinValueValidator(0)])    
    b11_No_of_Research_projects_Received_and_Amount_score = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(30), MinValueValidator(0)])
    b11file = models.FileField(upload_to='part2', null=True) 
    b11HOD_score = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(30), MinValueValidator(0)])
    b11P_score = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(30), MinValueValidator(0)])
    a12_No_of_Consultancy_projects_received_OR_ongoing_score = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(20), MinValueValidator(0)])
    a12file = models.FileField(upload_to='part2', null=True) 
    a12HOD_score = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(20), MinValueValidator(0)])
    a12P_score = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(20), MinValueValidator(0)])
    b12_No_of_patents_applied_awarded_score = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(20), MinValueValidator(0)])
    b12file = models.FileField(upload_to='part2', null=True) 
    b12HOD_score = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(20), MinValueValidator(0)])
    b12P_score = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(20), MinValueValidator(0)])
    part2APIscore = models.BigIntegerField(null=True, default=0)
    part2HODAPIscore = models.BigIntegerField(null=True, default=0)
    part2PAPIscore = models.BigIntegerField(null=True, default=0)

    def __str__(self):
        return self.user

    def save(self,*args, **kwargs):
        
        self.part2APIscore = (int(self.a10_No_of_papers_published_in_journals_score) + int(self.b10_No_of_papers_presented_in_conferences_score) + int(self.c10_No_of_papers_indexed_in_In_Scopus_or_Web_of_Science_or_UGC_care_list_OR_No_of_book_chapters_authored_OR_No_of_Books_Authored_score) + 
                                int(self.a11_No_of_Research_Project_proposals_submitted_score) + int(self.b11_No_of_Research_projects_Received_and_Amount_score) + int(self.a12_No_of_Consultancy_projects_received_OR_ongoing_score) + int(self.b12_No_of_patents_applied_awarded_score))
        self.part2HODAPIscore = (int(self.a10HOD_score) + int(self. b10HOD_score) + int(self.c10HOD_score) + int(self.a11HOD_score) + int(self.b11HOD_score) + int(self.a12HOD_score) + int(self.b12HOD_score))
        self.part2PAPIscore = (int(self.a10P_score) + int(self.b10P_score) + int(self.c10P_score) + int(self.a11P_score) + int(self.b11P_score) + int(self.a12P_score) + int(self.b12P_score))

        super(AppraisalForm2, self).save(*args, **kwargs)

    #part3

class AppraisalForm3(models.Model):

    CATEGORY = (
			('Basic Science and Humanities', 'Basic Science and Humanities'),
			('Mechanical Engineering', 'Mechanical Engineering'),
            ('Civil Engineering', 'Civil Engineering'),
            ('Computer Science and Engineering', 'Computer Science and Engineering'),
            ('Information Science and Engineering', 'Information Science and Engineering'),
            ('Electronics and Communication Engineering', 'Electronics and Communication Engineering'),
            ('Master of Business Administration', 'Master of Business Administration'),
            ('Master of Computer Applications', 'Master of Computer Applications'),
			) 

    ROLES = (
            ('Assistant Professor', 'Assistant Professor'),
            ('Associate Professor', 'Associate Professor'),
            ('Professor', 'Professor'),
    )

    user = models.CharField(max_length=10, null=True)
    department = models.CharField(max_length=200, null=True, choices=CATEGORY)
    designation = models.CharField(max_length=200, null=True, choices=ROLES)
    name = models.CharField(max_length=200, null=True)
    whether_HOD = models.BooleanField(default=False)
    submitted_Faculty = models.BooleanField(default=False)
    submitted_HOD = models.BooleanField(default=False)
    submitted_Principal = models.BooleanField(default=False)
    academic_year = models.IntegerField(null=True)

    a13 = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(10), MinValueValidator(0)])
    HOD_a13 = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(10), MinValueValidator(0)])
    P_a13 = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(10), MinValueValidator(0)])
    b13 = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(15), MinValueValidator(0)]) 
    HOD_b13 = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(15), MinValueValidator(0)])
    P_b13 = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(15), MinValueValidator(0)])
    c13 = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(15), MinValueValidator(0)])
    HOD_c13 = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(15), MinValueValidator(0)])
    P_c13 = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(15), MinValueValidator(0)])
    d13 = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(15), MinValueValidator(0)])
    HOD_d13 = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(15), MinValueValidator(0)])
    P_d13 = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(15), MinValueValidator(0)])
    e13 = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(20), MinValueValidator(0)]) 
    HOD_e13 = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(20), MinValueValidator(0)])
    P_e13 = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(20), MinValueValidator(0)])
    f13 = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(15), MinValueValidator(0)])
    HOD_f13 = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(15), MinValueValidator(0)])
    P_f13 = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(15), MinValueValidator(0)])
    a14 = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(30), MinValueValidator(0)])
    HOD_a14 = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(30), MinValueValidator(0)])
    P_a14 = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(30), MinValueValidator(0)])
    b14 = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(20), MinValueValidator(0)])
    HOD_b14 = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(20), MinValueValidator(0)])
    P_b14 = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(20), MinValueValidator(0)])
    c14 = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(20), MinValueValidator(0)])
    c14file = models.FileField(upload_to='part3', null=True) 
    HOD_c14 = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(20), MinValueValidator(0)])
    P_c14 = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(20), MinValueValidator(0)])
    a15 = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(20), MinValueValidator(0)])
    a15file = models.FileField(upload_to='part3', null=True) 
    HOD_a15 = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(20), MinValueValidator(0)])
    P_a15 = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(20), MinValueValidator(0)])
    part3APIscore = models.BigIntegerField(default=0, null=True)
    part3HODAPIscore = models.BigIntegerField(default=0, null=True)
    part3PAPIscore = models.BigIntegerField(default=0, null=True)

   

    def __str__(self):
        return self.user
    

    def save(self, *args, **kwargs):
        
        #part3

        self.part3APIscore = (int(self.a13) + int(self.b13) + int(self.c13) + int(self.d13) + int(self.e13) + int(self.f13) + int(self.a14) + int(self.b14) + int(self.c14) + int(self.a15))
        self.part3HODAPIscore = (int(self.HOD_a13) + int(self.HOD_b13) + int(self.HOD_c13) + int(self.HOD_d13) + int(self.HOD_e13)
                                 + int(self.HOD_f13) + int(self.HOD_a14) + int(self.HOD_b14) + int(self.HOD_c14) + int(self.HOD_a15))
        self.part3PAPIscore = (int(self.P_a13) + int(self.P_b13) + int(self.P_c13) + int(self.P_d13) + int(self.P_e13) +
                                int(self.P_f13) + int(self.P_a14) + int(self.P_b14) + int(self.P_c14) + int(self.P_a15))

        super(AppraisalForm3, self).save(*args, **kwargs)

#finalScore

class GrandApiScores(models.Model):

    CATEGORY = (
			('Basic Science and Humanities', 'Basic Science and Humanities'),
			('Mechanical Engineering', 'Mechanical Engineering'),
            ('Civil Engineering', 'Civil Engineering'),
            ('Computer Science and Engineering', 'Computer Science and Engineering'),
            ('Information Science and Engineering', 'Information Science and Engineering'),
            ('Electronics and Communication Engineering', 'Electronics and Communication Engineering'),
            ('Master of Business Administration', 'Master of Business Administration'),
            ('Master of Computer Applications', 'Master of Computer Applications'),
			) 

    ROLES = (
            ('Assistant Professor', 'Assistant Professor'),
            ('Associate Professor', 'Associate Professor'),
            ('Professor', 'Professor'),
    )

    GRADES = (
            ('A','A'),
            ('B','B'),
            ('C','C'),
            ('D','D'),
            ('E','E'),
            ('F','F'),
    )

    user = models.CharField(max_length=10, null=True)
    department = models.CharField(max_length=200, null=True, choices=CATEGORY)
    designation = models.CharField(max_length=200, null=True, choices=ROLES)
    name = models.CharField(max_length=200, null=True)
    grade = models.CharField(max_length=2, null=True, choices=GRADES)
    whether_HOD = models.BooleanField(default=False)
    submitted_Faculty = models.BooleanField(default=False)
    submitted_HOD = models.BooleanField(default=False)
    submitted_Principal = models.BooleanField(default=False)
    academic_year = models.IntegerField(null=True)

    Part1APIscore = models.BigIntegerField(default=0,null=True)
    Part1HODAPIscore = models.BigIntegerField(default=0,null=True)
    Part1PAPIscore = models.BigIntegerField(default=0,null=True)

    part2APIscore = models.BigIntegerField(null=True, default=0)
    part2HODAPIscore = models.BigIntegerField(null=True, default=0)
    part2PAPIscore = models.BigIntegerField(null=True, default=0)

    part3APIscore = models.BigIntegerField(default=0, null=True)
    part3HODAPIscore = models.BigIntegerField(default=0, null=True)
    part3PAPIscore = models.BigIntegerField(default=0, null=True)

    GrandScore = models.BigIntegerField(default=0,null=True)
    GrandScoreHOD = models.BigIntegerField(default=0,null=True)
    GrandScoreP = models.BigIntegerField(default=0,null=True)

    def __str__(self):
        return self.user
   

class BackupApiScores(models.Model):

    CATEGORY = (
			('Basic Science and Humanities', 'Basic Science and Humanities'),
			('Mechanical Engineering', 'Mechanical Engineering'),
            ('Civil Engineering', 'Civil Engineering'),
            ('Computer Science and Engineering', 'Computer Science and Engineering'),
            ('Information Science and Engineering', 'Information Science and Engineering'),
            ('Electronics and Communication Engineering', 'Electronics and Communication Engineering'),
            ('Master of Business Administration', 'Master of Business Administration'),
            ('Master of Computer Applications', 'Master of Computer Applications'),
			) 

    ROLES = (
            ('Assistant Professor', 'Assistant Professor'),
            ('Associate Professor', 'Associate Professor'),
            ('Professor', 'Professor'),
    )

    GRADES = (
            ('A','A'),
            ('B','B'),
            ('C','C'),
            ('D','D'),
            ('E','E'),
            ('F','F'),
    )

    YEARS = (
            ('2021','2021'),
            ('2022','2022'),
            ('2023','2023'),
    )

    user = models.CharField(max_length=10, null=True)
    department = models.CharField(max_length=200, null=True, choices=CATEGORY)
    designation = models.CharField(max_length=200, null=True, choices=ROLES)
    name = models.CharField(max_length=200, null=True)
    grade = models.CharField(max_length=2, null=True, choices=GRADES)
    whether_HOD = models.BooleanField(default=False)
    submitted_Faculty = models.BooleanField(default=False)
    submitted_HOD = models.BooleanField(default=False)
    submitted_Principal = models.BooleanField(default=False)
    academic_year = models.IntegerField(null=True, choices=YEARS)

    Part1APIscore = models.BigIntegerField(default=0,null=True)
    Part1HODAPIscore = models.BigIntegerField(default=0,null=True)
    Part1PAPIscore = models.BigIntegerField(default=0,null=True)

    part2APIscore = models.BigIntegerField(null=True, default=0)
    part2HODAPIscore = models.BigIntegerField(null=True, default=0)
    part2PAPIscore = models.BigIntegerField(null=True, default=0)

    part3APIscore = models.BigIntegerField(default=0, null=True)
    part3HODAPIscore = models.BigIntegerField(default=0, null=True)
    part3PAPIscore = models.BigIntegerField(default=0, null=True)

    GrandScore = models.BigIntegerField(default=0,null=True)
    GrandScoreHOD = models.BigIntegerField(default=0,null=True)
    GrandScoreP = models.BigIntegerField(default=0,null=True)

    def __str__(self):
        return self.user

class DatesToTrack(models.Model):
    backupdate = models.DateField()
    
class EXPDate(models.Model):
    expdate = models.DateField()



