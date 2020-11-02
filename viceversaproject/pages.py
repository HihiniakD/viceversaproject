from django.shortcuts import render


def form(request):
	return render(request, 'form.html')


def reverse(request):
	user_text = request.GET['usertext']
	number_of_words = len(user_text.split())
	reversed_text = user_text[::-1]
	return render(request, 'reverse.html', {'usertext':user_text, 'reversedtext':reversed_text, 'numberofwords': number_of_words})