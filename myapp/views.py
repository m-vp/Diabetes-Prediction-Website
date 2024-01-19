from django.shortcuts import render , HttpResponse ,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import os
import pandas as pd
from .models import Result
from .forms import FeedbackForm
from .models import Feedback

def signuppage(request):
    if request.method == 'POST':
        username = request.POST['username']#username = request.POST.get('username')
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password != cpassword:
            return HttpResponse('passwords do not match')
        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error_message': 'Username is not unique'})
        my_user = User.objects.create_user(username,email,password)
        my_user.save()

        print(username)
        return redirect('login') #name of url shud be written
    return render(request,'signup.html')



def loginpage(request):
    if request.method == 'POST':
        username = request.POST['username']#username = request.POST.get('username')
        password = request.POST['password']

        user = authenticate(request,username = username,password = password) #lhs is table col.
        if user is not None:
            login(request,user)
            return render(request,'home.html')
        else:
            return HttpResponse("username or password is incorrect")
    return render(request,'login.html')



def predict(request):
    return render(request, 'predict.html')



def result(request):
    if request.method == 'POST':  # Check if the form is submitted using POST
        print("Inside result view")  # Add this line
        # Rest of your code
        data = pd.read_csv(r'C:\Users\mvenk\useless\diaanalysis\diaanalysis\diabetes-dataset.csv')

        X = data.drop('Outcome', axis=1)
        Y = data['Outcome']
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.30)

        model = LogisticRegression()
        model.fit(X_train, Y_train)
        
        val1 = float(request.POST['n1'])  # Change request.GET to request.POST
        val2 = float(request.POST['n2'])
        val3 = float(request.POST['n3'])
        val4 = float(request.POST['n4'])
        val5 = float(request.POST['n5'])
        val6 = float(request.POST['n6'])
        val7 = float(request.POST['n7'])
        val8 = float(request.POST['n8'])

        pred = model.predict([[val1, val2, val3, val4, val5, val6, val7, val8]])

        result1 = "5"

        if pred == [1]:
            result1 = "positive"
        else:
            result1 = "negative"


        Result.objects.create(
            user=request.user,
            pregnancies=val1,
            glucose=val2,
            BP=val3,
            skin_thickness=val4,
            Insulin=val5,
            BMI=val6,
            DPF=val7,
            age=val8,
            result_value=result1
        )

        return render(request, "result.html", {"result2": result1})
    else:
        print('wooooooooooooooooooooooooooo')


def provide_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)

        if form.is_valid():
            feedback_text = form.cleaned_data['feedback_text']
            Feedback.objects.create(user=request.user, feedback_text=feedback_text)
            return redirect('thank_you')

    else:
        form = FeedbackForm()

    return render(request, 'feedback_form.html', {'form': form})

def thank_you(request):
    return render(request, 'thankyou.html')