from django.shortcuts import render
from pytube import YouTube

def dnld(request):
    return render(request, 'index.html' ) 
    

def index(request):
    if request.method == "POST":
        l = request.POST.get("link")
        video = YouTube(l)
        stream = video.streams.get_highest_resolution()
        stream.download()
        print('donloded')
        return render(request, 'index.html' )

# from django.shortcuts import render
# from pytube import YouTube

# def index(request):

#     try:

#         # check request.method is post or not
#         if request.method == 'POST':
#             try:
#                 # get link from the html form
#                 link = request.POST['link']
#                 video = YouTube(link)

#                 # set video resolution
#                 stream = video.streams.get_lowest_resolution()

#                 # download the video 
#                 stream.download()

#                 # render HTML page
#                 return render(request, 'index.html', {'msg':'Video downloaded'})
#             except:
#                 return render(request, 'index.html', {'msg':'Video not downloaded'})
#         return render(request, 'index.html', {'msg':''})
#     except:
#         return render(request, "index.html", {"msg":"Sorry something went wrong!"})

        