from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Student, Student_Profile, Program, CohortGroup ,student_types
from django.views import View





# we want to learn about django template instead of using httpresponse we can return our html
# def home(request):
#   student_list = Student.objects.all()  # Retrieve all students
  
#   # Create a dictionary to store each student's cohort group(s)
#   student_cohort_groups = {student.cohort_groups.all() for student in student_list}
  
#   context = {
#       "students": student_list,
#       "student_cohort_groups": student_cohort_groups  # Pass the student-cohort mapping
#   }
#   print(student_cohort_groups)
#   return render(request, 'html/index.html', context)

def home(request):
  student_list = Student.objects.all()  # Retrieve all students

  paginator = Paginator(student_list, 2)  # 10 students per page

  page_number = request.GET.get('page')
  try:
    students_page = paginator.page(page_number)
  except PageNotAnInteger:
    students_page = paginator.page(1)
  except EmptyPage:
    students_page = paginator.page(paginator.num_pages)
  
  # Attach cohort groups to each student object as a custom attribute which can also be done on the template
  for student in students_page:
    student.cohort_groups_list = student.cohort_groups.all()
  
  context = {
    #"students": student_list, # Now, each student has an attribute 'cohort_groups_list'
    "students_page": students_page,
    "student_rank" : student_types
  }
  
  return render(request, 'html/index.html', context)



def school(request):
  return HttpResponse('we are going for studies')

# we learnt about dynamic routing in django here

# def dynamic(request, unique):
# #    return HttpResponse(f"<h1>This is {unique}'s profile page</h1>")
#    return render(request, 'html/profile.html', {'profile': unique})

def profile_view(request, slug):
  # profile = username  # or fetch profile from the database
  # if len(profile) < 6:
  #     profile_exists = False
  # else:
  #     profile_exists = True

  # context = {
  #     'profile': profile,
  #     'profile_exists': profile_exists,
  # }

 
    # Use prefetch_related for the reverse relationship, assuming `related_name='cohort_groups'`
  student = get_object_or_404(
    Student.objects.prefetch_related('cohort_groups'),  # Adjust based on the actual related_name
    slug=slug
  )

  # Retrieve the first cohort group if it exists
  cohort_group = student.cohort_groups.first()

  if cohort_group:
      # Filter students that are in the same cohort group
    cohort_members = Student.objects.filter(
        cohort_groups=cohort_group
    ).prefetch_related('cohort_groups')  # Adjust for reverse relationship if necessary
  else:
      cohort_members = Student.objects.none()

  # Pass the data to the template
  context = {
    "student": student,
    'cohort_group': cohort_group,
    "cohort_members": cohort_members,
  }
  return render(request, 'html/profile.html', context)

# View for deleting a student
def delete_student(request, slug):
    student = get_object_or_404(Student, slug=slug)
    student.delete()  # Delete the student

    return redirect('home')  # Redirect after deletion

class Add_students(View):
    def post(self, request):
        # Extract form data
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        role = request.POST.get('role')
        email = request.POST.get('email')

        print('Data received:', username, firstname, lastname, role)

        # Check if all fields are present
        if not (username and firstname and lastname and role):
            return HttpResponse(
                "Form data is incomplete. Please provide all required fields.",
                status=400
            )

        # Check if username already exists
        if Student.objects.filter(username=username).exists():
            return HttpResponse("Username already exists. Please choose another.", status=409)

        # Save the data to the database
        student = Student.objects.create(
            username=username,
            first_name=firstname,
            last_name=lastname,
            student_type=role,
            email =email,
        )
        # Debug confirmation
        print(f"Student created: {student}")

        return HttpResponse("Student added successfully!", status=201)

        
       


      










