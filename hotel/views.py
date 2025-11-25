# hotel/views.py - Business logic और page rendering

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Room

# Home page का view
def home(request):
    """Home page को show करता है"""
    # सभी कमरों को database से निकालता है
    rooms = Room.objects.all()
    
    # Context में data भेजता है
    context = {
        'rooms': rooms,
        'page_title': 'होटल - स्वागत है'
    }
    
    return render(request, 'hotel/home.html', context)

# कमरों की list page का view
def rooms_list(request):
    """सभी कमरों की list दिखाता है"""
    # सभी कमरों को database से निकालता है
    rooms = Room.objects.all()
    
    # Context में data भेजता है
    context = {
        'rooms': rooms,
        'page_title': 'हमारे कमरे'
    }
    
    return render(request, 'hotel/rooms.html', context)

# एक specific कमरे की details का view
def room_detail(request, pk):
    """एक कमरे की पूरी जानकारी दिखाता है"""
    try:
        # ID से कमरा खोजता है
        room = Room.objects.get(pk=pk)
        context = {
            'room': room,
            'page_title': room.name
        }
        return render(request, 'hotel/room_detail.html', context)
    except Room.DoesNotExist:
        # अगर कमरा नहीं मिला
        return render(request, '404.html', {'message': 'कमरा नहीं मिला'}, status=404)

# संपर्क पेज
def contact(request):
    """संपर्क पेज दिखाता है"""
    if request.method == 'POST':
        # Form data को process करना
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # आप यहाँ email भेज सकते हैं या database में save कर सकते हैं
        # For now, हम सिर्फ success message दिखाते हैं
        messages.success(request, '✅ आपका संदेश सफलतापूर्वक भेज दिया गया है। हम जल्द ही संपर्क करेंगे।')
        return redirect('hotel:contact')
    
    context = {'page_title': 'संपर्क करें'}
    return render(request, 'hotel/contact.html', context)

# लॉगिन पेज
def login_view(request):
    """यूजर को लॉगिन कराता है"""
    if request.user.is_authenticated:
        # अगर already logged in है तो home पर भेज दो
        return redirect('hotel:home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # यूजर को authenticate करना
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # लॉगिन successful
            login(request, user)
            messages.success(request, f'✅ स्वागत है, {user.first_name}!')
            return redirect('hotel:home')
        else:
            # लॉगिन failed
            messages.error(request, '❌ गलत यूजरनेम या पासवर्ड')
    
    context = {'page_title': 'लॉगिन करें'}
    return render(request, 'hotel/login.html', context)

# साइन अप पेज
def signup_view(request):
    """नया यूजर account बनाता है"""
    if request.user.is_authenticated:
        # अगर already logged in है तो home पर भेज दो
        return redirect('hotel:home')
    
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        phone = request.POST.get('phone')
        
        # Validation
        if password != confirm_password:
            messages.error(request, '❌ पासवर्ड मेल नहीं खा रहे हैं')
            return redirect('hotel:signup')
        
        if len(password) < 8:
            messages.error(request, '❌ पासवर्ड कम से कम 8 अक्षर का होना चाहिए')
            return redirect('hotel:signup')
        
        # Check करना कि username already exist करता है या नहीं
        if User.objects.filter(username=username).exists():
            messages.error(request, '❌ यह यूजरनेम पहले से मौजूद है')
            return redirect('hotel:signup')
        
        # Check करना कि email already exist करता है या नहीं
        if User.objects.filter(email=email).exists():
            messages.error(request, '❌ यह ईमेल पहले से रजिस्टर है')
            return redirect('hotel:signup')
        
        # नया यूजर बनाना
        try:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name
            )
            
            # यूजर को automatically लॉगिन कर दो
            login(request, user)
            messages.success(request, '✅ खाता सफलतापूर्वक बन गया। स्वागत है!')
            return redirect('hotel:home')
        
        except Exception as e:
            messages.error(request, f'❌ कोई त्रुटि हुई: {str(e)}')
            return redirect('hotel:signup')
    
    context = {'page_title': 'साइन अप करें'}
    return render(request, 'hotel/signup.html', context)

# लॉगआउट
def logout_view(request):
    """यूजर को लॉगआउट करता है"""
    logout(request)
    messages.success(request, '✅ आप लॉगआउट हो गए हैं')
    return redirect('hotel:home')

# भूल गए पासवर्ड (भविष्य के लिए)
def forgot_password(request):
    """पासवर्ड reset करने के लिए"""
    context = {'page_title': 'पासवर्ड भूल गए'}
    return render(request, 'hotel/forgot_password.html', context)
