from pyramid_restful.routers import ViewSetRouter
from .views.stock import StockAPIView
from .views.portfolio import PortfolioAPIView
from .views.auth import AuthAPIView
from .views.company import CompanyAPIView


def includeme(config):
    """
    """
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')

    router = ViewSetRouter(config)
    router.register('api/v1/auth', AuthAPIView, 'auth')
    router.register('api/v1/portfolio', PortfolioAPIView, 'portfolio')
    router.register('api/v1/stock', StockAPIView, 'stock')
    router.register('api/v1/company', CompanyAPIView, 'company')
