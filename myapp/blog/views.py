import logging
from .models import Post, AboutUs
from django.shortcuts import redirect, render
from django.http import  HttpResponse
from django.urls import reverse
from django.core.paginator import Paginator
from django.contrib import messages
from google.cloud import firestore
from myapp.firebase_config import get_db
from .form import ContactForm

# Create your views here.
def index(request):
    blog_title = "My Blog"
    
    # Fetch posts from Firebase
    db = get_db()
    posts_ref = db.collection('posts').where('published', '==', True).stream()
    
    posts = []
    for doc in posts_ref:
        post_data = doc.to_dict()
        post_data['id'] = doc.id  # Add document ID
        posts.append(post_data)
    
    # Sort by created_at timestamp (newest first)
    posts.sort(key=lambda x: x.get('created_at', 0), reverse=True)
    
    # Paginate posts - 6 posts per page
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, "blog/index.html", {
        "blog_title": blog_title, 
        "page_obj": page_obj,
        "posts": page_obj.object_list
    })

def detail(request, slug):
    # Fetch single post from Firebase by slug
    db = get_db()
    
    # Query Firestore for post with matching slug
    posts_ref = db.collection('posts').where('slug', '==', slug).limit(1).stream()
    
    post = None
    for doc in posts_ref:
        post = doc.to_dict()
        post['id'] = doc.id
        break
    
    return render(request, "blog/detail.html", {"post": post})

def old_url_redirect(request):
    return redirect(reverse("blog:new_page_url"))

def new_url_view(request):
    return HttpResponse("This is the new URL view.")

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Get form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            # Save to Firebase
            db = get_db()
            db.collection('contacts').add({
                'name': name,
                'email': email,
                'message': message,
                'created_at': firestore.SERVER_TIMESTAMP
            })
            
            messages.success(request, 'Thank you for contacting us!')
            return redirect('blog:contact')
    else:
        form = ContactForm()
    
    return render(request, "blog/contact.html", {'form': form})

def about_view(request):
    about_us = AboutUs.objects.first()
    return render(request, "blog/about.html", {"about_content": about_us.content if about_us else ""})