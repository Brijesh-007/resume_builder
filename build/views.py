from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template

# Create your views here.
data = {}
no_of_firms: list
no_of_deg: list
no_of_skills: list


def home(request):
    return render(request, 'personal_details.html')


def features(request):
    return render(request, 'features.html')

def career_details(request):
    data['first_name'] = str(request.POST['first_name']).upper()
    data['last_name'] = str(request.POST['last_name']).upper()
    data['designation'] = str(request.POST['designation']).capitalize()
    global no_of_firms
    global no_of_deg
    no_of_firms = range(1, int(request.POST['no_of_firms']) + 1)
    no_of_deg = range(1, int(request.POST['no_of_deg']) + 1)
    return render(request, 'career_details.html', {'firms': no_of_firms})


def education(request):
    data['company1'] = request.POST['company1']
    data['desg_job1'] = request.POST['desg_job1']
    data['experience1'] = request.POST['experience1']

    if len(no_of_firms) == 2:
        data['company2'] = request.POST['company2']
        data['desg_job2'] = request.POST['desg_job2']
        data['experience2'] = request.POST['experience2']
    else:
        data['company2'] = ""
        data['desg_job2'] = ""
        data['experience2'] = ""

    return render(request, 'education.html', {'degrees': no_of_deg})


def skills(request):
    global no_of_skills
    data['name_degree1'] = request.POST['name_degree1']
    data['institute1'] = request.POST['institute1']
    data['achievements1'] = request.POST['achievements1']
    no_of_skills = range(1, int(request.POST['no_of_skills']) + 1)

    if len(no_of_deg) == 2:
        data['name_degree2'] = request.POST['name_degree2']
        data['institute2'] = request.POST['institute2']
        data['achievements2'] = request.POST['achievements2']
    else:
        data['name_degree2'] = ""
        data['institute2'] = ""
        data['achievements2'] = ""

    return render(request, 'skills.html', {'skills': no_of_skills})


def summary(request):
    data['field_of_skills1'] = request.POST['field_of_skills1']
    data['skills1'] = str(request.POST['skills1']).split(',')

    if len(no_of_skills) == 2:
        data['field_of_skills2'] = request.POST['field_of_skills2']
        data['skills2'] = str(request.POST['skills2']).split(',')
    else:
        data['field_of_skills2'] = ""
        data['skills2'] = ""

    return render(request, 'summary.html')


def contact(request):
    data['summary'] = request.POST['summary']
    return render(request, 'contact_details.html')


def design_select(request):
    data['mobile'] = request.POST['Mobile']
    data['email'] = request.POST['email']
    data['portfolio'] = request.POST['portfolio']
    return render(request, 'SelectPage.html')


def submit_details1(request):
    return render(request, 'result.html', {'first_name': data['first_name'],
                                           'last_name': data['last_name'],
                                           'desg': data['designation'],
                                           'short': str(data['first_name'][0] + data['last_name'][0]).upper(),
                                           'email': data['email'],
                                           'mobile': data['mobile'],
                                           'portfolio': data['portfolio'],
                                           'designation1': data['desg_job1'],
                                           'experience1': data['experience1'],
                                           'company1': data['company1'],
                                           'designation2': data['desg_job2'],
                                           'experience2': data['experience2'],
                                           'company2': data['company2'],
                                           'degree1': data['name_degree1'],
                                           'achievements1': data['achievements1'],
                                           'institute1': data['institute1'],
                                           'degree2': data['name_degree2'],
                                           'achievements2': data['achievements2'],
                                           'institute2': data['institute2'],
                                           'field_skill1': data['field_of_skills1'],
                                           'skills1': data['skills1'],
                                           'field_skill2': data['field_of_skills2'],
                                           'skills2': data['skills2'],
                                           'summary': data['summary'],
                                           'no_of_deg': len(no_of_deg),
                                           'no_of_firms': len(no_of_firms),
                                           'no_of_skills': len(no_of_skills)
                                           })


def submit_details2(request):
    return render(request, 'result2.html', {'first_name': data['first_name'],
                                            'last_name': data['last_name'],
                                            'desg': data['designation'],
                                            'short': str(data['first_name'][0] + data['last_name'][0]).upper(),
                                            'email': data['email'],
                                            'mobile': data['mobile'],
                                            'portfolio': data['portfolio'],
                                            'designation1': data['desg_job1'],
                                            'experience1': data['experience1'],
                                            'company1': data['company1'],
                                            'designation2': data['desg_job2'],
                                            'experience2': data['experience2'],
                                            'company2': data['company2'],
                                            'degree1': data['name_degree1'],
                                            'achievements1': data['achievements1'],
                                            'institute1': data['institute1'],
                                            'degree2': data['name_degree2'],
                                            'achievements2': data['achievements2'],
                                            'institute2': data['institute2'],
                                            'field_skill1': data['field_of_skills1'],
                                            'skills1': data['skills1'],
                                            'field_skill2': data['field_of_skills2'],
                                            'skills2': data['skills2'],
                                            'summary': data['summary'],
                                            'no_of_deg': len(no_of_deg),
                                            'no_of_firms': len(no_of_firms),
                                            'no_of_skills': len(no_of_skills)
                                            })
