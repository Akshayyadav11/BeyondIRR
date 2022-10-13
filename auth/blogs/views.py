from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.views import View
from .models import Post
from .forms import PostForm 
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
from django.contrib.auth.decorators import login_required

#@login_required(login_url='blog_list')
#@login_required()
class PostCreate(View):
    def get(self, request):
        obj = PostForm()        
        return render(request, "create_post_form.html", {'post_list': obj})

    def post(self, request): 
        obj = PostForm(request.POST)    
        breakpoint()    
        if obj.is_valid():
            #obj.author = request.user.id
            instance = obj.save()
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
    