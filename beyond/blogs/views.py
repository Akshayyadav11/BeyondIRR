from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.views import View
from .models import Post
from .forms import PostForm 
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
from django.db.models import Q
#@login_required(login_url='blog_list')

class PostCreate(View):
    def get(self, request):
        obj = PostForm()   
        
        return render(request, "create_post_form.html", {'post_list': obj})

    
    def post(self, request): 
        obj = PostForm(request.POST)    
       
        if obj.is_valid():           
           
            instance = obj.save(commit=False)
            instance.author = self.request.user
            instance.save()
            return redirect('blog:blog_list')
        else:           
            return render(request, "create_post_form.html", {'post_list': obj})
 
class PostList(View):      
    def get(self, request):
        obj = Post.objects.filter(status=1).order_by('-created_on')
        keys = {"post_list": obj}
        return render(request, "post_list.html", keys)


class PostDetail(View):    
    def get(self, request, id):
        context ={}   
      
        context["post"] = Post.objects.get(id = id)
        print(context)   
        return render(request, "post_detail.html", context)



class PostDelete(View):
   
    def get(self, request, id):
        pos = Post.objects.get(id = id)
        pos.delete()   
        return redirect('blog:blog_list')


class EditPost(View): 
   
    def get(self, request, id):
        obj = Post.objects.get(id=id)
       
        fm = PostForm(instance=obj)
        return render(request, "update_post_form.html", {'post_list': fm})

   
    def post(self, request, id):
        pos = Post.objects.get(id=id)
        fm = PostForm(request.POST, instance=pos)
        if fm.is_valid():           
            fm.save()
            return redirect('blog:blog_list')


class UserPosts(View):
    def get(self, request):
        logged_in_user = request.user.id
        logged_in_user_posts = Post.objects.filter(author=logged_in_user)

        return render(request, 'user_posts.html', {'user_posts': logged_in_user_posts})
    


class AllUserPosts(View):
   def get(self, request):
        obj = Post.objects.all().order_by('-created_on')
        # obj = Post.objects.filter(status=1).order_by('-created_on')
        keys = {"post_list": obj}
        return render(request, "post_list.html", keys)
    


class AllDraftPosts(View):
   def get(self, request):
        obj = Post.objects.filter(status=0).order_by('-created_on')
        keys = {"post_list": obj}
        return render(request, "post_list.html", keys)
    

class AllArchivePosts(View):
   def get(self, request):
        
        obj = Post.objects.filter(status=2).order_by('-created_on')
        keys = {"post_list": obj}
        return render(request, "post_list.html", keys)
    

class UserSpecificPosts(View):
   def get(self, request):
        obj = Post.objects.filter(author=request.user.id, status=1).order_by('-created_on')
        # obj = Post.objects.filter(status=1).order_by('-created_on')
        keys = {"post_list": obj}
        return render(request, "post_list.html", keys)
    


class UserSpecificDraftPosts(View):
   def get(self, request):
        obj = Post.objects.filter(status=0,author=request.user.id).order_by('-created_on')
        keys = {"post_list": obj}
        return render(request, "post_list.html", keys)
    

class UserSpecificArchivePosts(View):
   def get(self, request):
        
        obj = Post.objects.filter(status=2, author=request.user.id).order_by('-created_on')
        keys = {"post_list": obj}
        return render(request, "post_list.html", keys)