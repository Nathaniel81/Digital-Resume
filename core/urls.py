from django.urls import path
from . import views

app_name='core'

urlpatterns = [
    path('', views.Index.as_view(), name="Index"),
    path('contact/', views.Contact.as_view(), name="contact"),
    path('portfolio/', views.Portfolio.as_view(), name="porfolio"),
    path('portfolio/<slug:slug>', views.PortfolioDetail.as_view(), name="portfolio-detail"),
    path('blog/', views.Blog.as_view(), name="blogs"),
    path('blog/<slug:slug>', views.BlogDetail.as_view(), name="blog-detail"),
]